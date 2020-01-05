import unittest
from problems.compass_world_mdp import CustomMDP


class TestSum(unittest.TestCase):

    def test_init(self):
        mdp = CustomMDP()
        x, y, facing, momentum, m_action = mdp.get_state()

        self.assertTrue(x == 0)
        self.assertTrue(y == 0)
        self.assertTrue(facing == 0)
        self.assertTrue(momentum == 0)
        self.assertTrue(m_action is None)

    def test_movement(self):
        mdp = CustomMDP()
        mdp.step(0)
        # if I step forwards, what happens?
        x, y, facing, momentum, m_action = mdp.get_state()
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)
        self.assertEqual(facing, 0)
        self.assertEqual(m_action, 0)
        self.assertEqual(momentum, 1)

        # c
        mdp.step(4)
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)
        self.assertEqual(facing, 0)

        mdp.step(0)
        mdp.step(0)
        mdp.step(0)
        mdp.step(0)

        x, y, facing, momentum, m_action = mdp.get_state()
        self.assertEqual(x, 0)
        self.assertEqual(y, 5)
        self.assertEqual(facing, 0)
        self.assertEqual(momentum, 2)
        self.assertEqual(m_action,0)

        mdp.step(4)
        x, y, facing, momentum, m_action = mdp.get_state()
        self.assertEqual(x, 0)
        self.assertEqual(y, 5)
        self.assertEqual(facing, 0)
        self.assertEqual(momentum, 1)
        self.assertEqual(m_action, 0)

        mdp.step(4)
        x, y, facing, momentum, m_action = mdp.get_state()
        self.assertEqual(x, 0)
        self.assertEqual(y, 5)
        self.assertEqual(facing, 0)
        self.assertEqual(momentum, 0)
        self.assertEqual(m_action, None)

        mdp.step(1)
        mdp.step(1)
        x, y, facing, momentum, m_action = mdp.get_state()
        self.assertTrue(x == 0)
        self.assertTrue(y == 5)
        self.assertTrue(facing == 2)
        self.assertEqual(momentum,2)
        self.assertEqual(m_action,1)

        mdp.step(1)
        x, y, facing, momentum, m_action = mdp.get_state()
        self.assertTrue(x == 0)
        self.assertTrue(y == 5)
        self.assertEqual(facing, 3)
        self.assertEqual(momentum, 2)
        self.assertEqual(m_action, 1)

        mdp.step(4)
        x, y, facing, momentum, m_action = mdp.get_state()
        self.assertTrue(x == 0)
        self.assertTrue(y == 5)
        self.assertEqual(facing, 0)
        self.assertEqual(momentum, 2)
        self.assertEqual(m_action, 1)

        mdp.step(3)
        x, y, facing, momentum, m_action = mdp.get_state()
        self.assertTrue(x == 0)
        self.assertTrue(y == 5)
        self.assertEqual(facing, 1)
        self.assertEqual(momentum, 1)
        self.assertEqual(m_action, 1)


        mdp.step(3)
        x, y, facing, momentum, m_action = mdp.get_state()
        self.assertTrue(x == 0)
        self.assertTrue(y == 5)
        self.assertEqual(facing, 1)
        self.assertEqual(momentum, 0)
        self.assertEqual(m_action, None)


if __name__ == '__main__':
    unittest.main()
