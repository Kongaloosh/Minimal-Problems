import random
x = 5
y = 5


class CustomMDP:
    """
        Available actions:
            0: move forwards
            1: turn left
            2: turn right

        States:
            x,y pair describing where in the grid the agent is

        observation:
            the real-valued observations the agent

    """

    def __init__(self):
        self.__x_length = 5
        self.__y_length = 5
        self.__state_x = 0
        self.__state_y = 0
        self.__facing = 0
        self.__current_goal = random.randint(0, 3)
        self.__queue_length = 0
        self.__queue_action = None
        self.__max_momentum = 2
        print(self.get_state())

    def step(self, a):
        """takes an action a, returns a state s."""
        # if the current action is the direction we are going, increase the momentum

        if self.__queue_action == a:
            self.__queue_length = min(self.__queue_length + 1, self.__max_momentum)

        # if the action is in the opposite direction, decrease the momentum
        elif self.__queue_action is not None and abs(self.__queue_action - a)%2 == 0:
            self.__queue_length -= 1

            # If the momentum is now 0, we are still, there is no action
            if self.__queue_length == 0:
                self.__queue_action = None

        # if there is no action on the queue, go for
        elif self.__queue_action is None:
            self.__queue_action = a
            self.__queue_length += 1

        if self.__queue_action == 0:  # forwards
            # we need to check whether we will be adding or subtracting to the location
            direction = 1
            # if the facing variable is 2 or 3, we are going down or to the left
            if self.__facing >= 2:
                direction *= -1

            #  we now update the location
            if self.__facing % 2 == 0:      # if facing north or south
                self.__state_y = max(min(self.__state_y+direction, self.__y_length), 0)
            else:
                self.__state_x = max(min((self.__state_x+direction),self.__x_length), 0)

        elif self.__queue_action == 3: # turn left
            self.__facing = int((self.__facing - 1) % 4)

        elif self.__queue_action == 1: # turn right
            self.__facing = int((self.__facing + 1) % 4)

        elif self.__queue_action == 2: # go back
            # we need to check whether we will be adding or subtracting to the location
            direction = 1
            # if the facing variable is 2 or 3, we are going down or to the left
            if self.__facing < 2:
                direction *= -1
                #  we now update the location
            if self.__facing % 2 == 0:  # if facing north or south

                self.__state_y = max(min(self.__state_y + direction, self.__y_length), 0)
            else:
                self.__state_x = max(min((self.__state_x + direction), self.__x_length), 0)

        return self.get_observations()

    def get_state(self):
        return self.__state_x, self.__state_y, self.__facing, self.__queue_length, self.__queue_action

    def check_action(self,queue_action):
        if queue_action == 0 or queue_action == 2 or queue_action is None:  # forwards, backwards, or nothing
            return self.__facing

        elif queue_action == 3:  # turn left
            return int((self.__facing - 1) % 4)

        elif queue_action == 1:  # turn right
            return int((self.__facing + 1) % 4)

    def get_ground_truth(self):
        "for each action, returns the ground_truth"
        ground_truth = []
        queue_action = self.__queue_action

        for a in range(0,4):
            # if the action is in the opposite direction, decrease the momentum
            if a == self.__queue_action:
                ground_truth.append(self.check_action(a))

            elif self.__queue_action is not None and abs(self.__queue_action - a) % 2 == 0:
                # If the momentum is now 0, we are still, there is no action
                if self.__queue_length - 1 == 0:
                    ground_truth.append(self.check_action(None))
                else:
                    ground_truth.append(self.check_action(self.__queue_action))

            # if there is no action on the queue, go for
            elif self.__queue_action is None:
                ground_truth.append(self.check_action(a))

            else:
                ground_truth.append(self.check_action(queue_action))
        return ground_truth

    def get_observations(self):
        """For a given state, returns what the agent's observations are."""
        reward = 0

        if self.__facing == 0:
            # if facing north, return 1 and iff y is 5 return 1 + return current goal
            a = self.__facing if self.__state_y == self.__y_length else 0

        elif self.__facing == 1:
            # if facing north, return 1 and iff y is 5 return 1 + return current goal
            a = self.__facing if self.__state_x == self.__x_length else 0

        elif self.__facing == 2:
            # if facing north, return 1 and iff y is 5 return 1 + return current goal
            a = self.__facing if self.__state_y == 0 else 0

        elif self.__facing == 3:
            # if facing north, return 1 and iff y is 5 return 1 + return current goal
            a = self.__facing if self.__state_x == 0 else 0

        if a == self.__current_goal:
            new_goal = random.randint(0, 3)
            while new_goal == self.__current_goal:
                new_goal = random.randint(0, 3)
            self.__current_goal = new_goal
            reward = 1

        return [self.__facing, a, self.__current_goal], reward



