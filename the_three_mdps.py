"""
Niko Yasui and I had a conversation about what the most minimal problems are which require knowledge of some external
factors not contained within the agent's observations. We settled on three cases dependent on Judea Perl's causal model
problems.


Note on the distinction between confounder and chain:
It may not be immediately clear what the difference is between the chain and the confounder. The key is to look at how
the mass variable is updated on each time-step. For the confounder, mass is a function of the action and the hidden
variable. For the chain, the mass is a function of the previous mass and the hidden variable; the hidden variable,
is influenced by the action, but the action does not influence the mass directly.
"""
from mdp import MDP


class ColliderProblem(MDP):

    def __init__(self):
        self.__cycle_len = 2
        self.__current_cycle_step = 0
        self.__current_cycle = 0
        self.__result = None
        self.__action = None

    def step(self, a):
        """Given an action, updates and returns the observations available."""
        self.__result = self.__current_cycle != self.__action
        self.__current_cycle_step += 1
        if self.__current_cycle_step == self.__cycle_len:
            self.__current_cycle = not self.__current_cycle
        self.__current_cycle_step = self.__current_cycle_step % self.__cycle_len
        self.__action = a
        return self.get_observations()

    def get_state(self):
        """Gets the information needed to define the world state."""
        return [self.__current_cycle, self.__current_cycle_step]

    # def get_ground_truth(self):
    #     truth = [0,0]
    #     if 0 != bool(self.__current_cycle):
    #         truth[0] = 0
    #     else:
    #         truth[0] = self.__cycle_len - self.__current_cycle_step
    #     if 1 != bool(self.__current_cycle):
    #         truth[1] = 0
    #     else:
    #         truth[1] = self.__cycle_len -  self.__current_cycle_step
    #     print(self.__current_cycle, self.__current_cycle_step)
    #     return truth

    def get_observations(self):
        """Gets the current observation available to the agent given the world state."""
        return [self.__result], self.__result

    def get_cycle_len(self):
        return self.__cycle_len

    def get_ground_truth(self):
        # if I do nothing, how many steps to growth, if I do nothing, how many steps until death
        return [
            int(self.__current_cycle == 0) * (self.__cycle_len - self.__current_cycle_step),
            int(self.__current_cycle == 1) * (self.__cycle_len - self.__current_cycle_step),
                ]


class ConfounderProblem(MDP):
    """
    This is a problem where the actions taken by the agent impact not only the observable variable, but some hidden
    variable. The observable variable seen by the agent after taking an action is influenced by both the action taken
    and the hidden variable.


    An Analogy: resource drain.
    """

    def __init__(self):
        self.__nutrient_level = False
        self.__mass = False
        self.__current_reward = False

    def step(self, a):
        """Given an action taken, updates and returns the observations available."""
        self.__nutrient_level = self.__nutrient_level != a
        self.__mass = self.__mass != self.__nutrient_level
        self.__current_reward = self.__mass

        return self.get_observations()

    def get_state(self):
        """Gets the information needed to define the world state."""
        return [self.__mass, self.__nutrient_level]

    def get_observations(self):
        """Gets the current observation available to the agent given the world state."""
        return [self.__current_reward], self.__current_reward



class ChainProblem(MDP):

    def __init__(self):
        self.__nutrient_level = False
        self.__mass = False
        self.__current_reward = False

    def step(self, a):
        """Given an action taken, updates and returns the observations available."""
        self.__current_reward = (self.__mass or self.__nutrient_level)

        if self.__mass != self.__nutrient_level:
            self.__mass = self.__nutrient_level

        if bool(self.__nutrient_level) == bool(a):
            # the hidden state is flipped
            self.__nutrient_level = not self.__nutrient_level

        return self.get_observations()

    def get_state(self):
        """Gets the information needed to define the world state."""
        return [self.__mass, self.__nutrient_level]

    def get_observations(self):
        """Gets the current observation available to the agent given the world state."""
        return [self.__current_reward], self.__current_reward

