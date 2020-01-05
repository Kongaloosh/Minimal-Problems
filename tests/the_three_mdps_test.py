import unittest
from problems.the_three_mdps import ColliderProblem, ConfounderProblem


class TestCollider(unittest.TestCase):

    def test_init(self):
        mdp = ColliderProblem()
        agent_state, reward = mdp.get_observations()
        world_state = mdp.get_state()

        # What is returned as an observation to the agent is the current mass
        # the reward is also the mass
        self.assertEqual(agent_state[0], reward)
        self.assertEqual(len(agent_state), 1)
        self.assertEqual(world_state[0], 0)
        self.assertEqual(world_state[1], 0)

        # if we take an action, it should move the cycle forwards one step
        # here we check that if don't water in the sunny season, we get no reward for the whole season
        for i in range(mdp.get_cycle_len()):
            agent_state, reward = mdp.get_observations()
            world_state = mdp.get_state()
            self.assertEqual(world_state[1], i)
            self.assertEqual(world_state[0], 0)
            self.assertEqual(agent_state[0], 0)
            self.assertEqual(reward, 0)
            mdp.step(0)

        for i in range(mdp.get_cycle_len()):
            agent_state, reward = mdp.get_observations()
            world_state = mdp.get_state()
            self.assertEqual(agent_state[0], 1)
            self.assertEqual(reward, 1)
            self.assertEqual(world_state[0], 1)
            self.assertEqual(world_state[1], i)
            mdp.step(0)

        mdp.step(1)
        for i in range(mdp.get_cycle_len()-1):
            agent_state, reward = mdp.get_observations()
            world_state = mdp.get_state()
            self.assertEqual(agent_state[0], 1)
            self.assertEqual(reward, 1)
            self.assertEqual(world_state[0], 0)
            self.assertEqual(world_state[1], i+1)
            mdp.step(1)

        mdp.step(1)
        for i in range(mdp.get_cycle_len()-1):
            agent_state, reward = mdp.get_observations()
            world_state = mdp.get_state()
            self.assertEqual(world_state[1], i+1)
            self.assertEqual(world_state[0], 1)
            self.assertEqual(agent_state[0], 0)
            self.assertEqual(reward, 0)
            mdp.step(1)


class TestConfounder(unittest.TestCase):

    def test_init(self):
        mdp = ConfounderProblem()
        world_state = mdp.get_state()
        self.assertEqual(world_state[0], 0)
        self.assertEqual(world_state[1], 0)

        mdp.step(0)
        # we rest for a step to recover; no rewards, but restoration of nutrients
        agent_state, reward = mdp.get_observations()
        world_state = mdp.get_state()
        self.assertEqual(world_state[0], 0)     # biomass
        self.assertEqual(world_state[1], 1)     # nutrients
        self.assertEqual(agent_state[0], 0)     # reward
        self.assertEqual(reward, 0)             # reward

        mdp.step(1)
        # water to get biomass
        agent_state, reward = mdp.get_observations()
        world_state = mdp.get_state()
        self.assertEqual(world_state[0], 1)     # biomass
        self.assertEqual(world_state[1], 0)     # nutrients
        self.assertEqual(agent_state[0], 1)     # reward
        self.assertEqual(reward, 1)             # reward

        mdp.step(0)
        # Don't water to restore nutrients
        agent_state, reward = mdp.get_observations()
        world_state = mdp.get_state()
        self.assertEqual(world_state[0], 0)     # biomass
        self.assertEqual(world_state[1], 1)     # nutrients
        self.assertEqual(agent_state[0], 1)     # reward
        self.assertEqual(reward, 1)             # reward

        mdp.step(1)
        # Water to get biomass
        agent_state, reward = mdp.get_observations()
        world_state = mdp.get_state()
        self.assertEqual(world_state[0], 1)     # biomass
        self.assertEqual(world_state[1], 0)     # nutrients
        self.assertEqual(agent_state[0], 1)     # reward
        self.assertEqual(reward, 1)             # reward

        mdp.step(1)
        # Overwater one step; nutrients gone but biomass persists for one more step
        agent_state, reward = mdp.get_observations()
        world_state = mdp.get_state()
        self.assertEqual(world_state[0], 0)     # biomass
        self.assertEqual(world_state[1], 0)     # nutrients
        self.assertEqual(agent_state[0], 1)     # reward
        self.assertEqual(reward, 1)             # reward

        mdp.step(1)
        # Overwater one step; nutrients gone but biomass persists for one more step
        agent_state, reward = mdp.get_observations()
        world_state = mdp.get_state()
        self.assertEqual(world_state[0], 0)
        self.assertEqual(world_state[1], 0)
        self.assertEqual(agent_state[0], 0)
        self.assertEqual(reward, 0)

class TestChain(unittest.TestCase):

    def test_init(self):
        mdp = ColliderProblem()

if __name__ == '__main__':
    unittest.main()

