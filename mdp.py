
class MDP(object):
    """
    A framework for describing Markov Decision Processes.
    """

    def __init__(self):
        raise NotImplementedError()

    def step(self, a):
        """Given an action, updates and returns the observations available."""
        raise NotImplementedError()

    def get_state(self):
        """Gets the information needed to define the world state."""
        raise NotImplementedError()

    def get_ground_truth(self):
        raise NotImplementedError()

    def get_observations(self):
        """Gets the current observation given the world-state for the agent."""
        raise NotImplementedError()
