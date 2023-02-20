import random

# Constants
NUM_EPISODES = 100
NUM_STEPS = 10
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.99
EPSILON = 0.1
MAX_NUMBER = 100

# Expert policy
def expert_policy(target):
    guesses = []
    for i in range(NUM_STEPS):
        guess = random.randint(1, MAX_NUMBER)
        if guess == target:
            return guesses + [guess]
        guesses.append(guess)
    return guesses

# Imitation learning algorithm
class ImitationLearning:
    def __init__(self, target):
        self.policy = expert_policy(target)

    def get_action(self, state):
        return self.policy[state]

    def update_policy(self, state, action):
        pass # Do not update policy in imitation learning

# Reinforcement learning algorithm
class ReinforcementLearning:
    def __init__(self):
        self.q_table = [0] * MAX_NUMBER

    def get_action(self, state):
        if random.random() < EPSILON:
            return random.randint(1, MAX_NUMBER)
        else:
            return self.q_table.index(max(self.q_table)) + 1

    def update_policy(self, state, action):
        reward = -1
        if action == state:
            reward = 10
        self.q_table[action-1] += LEARNING_RATE * (reward + DISCOUNT_FACTOR * max(self.q_table) - self.q_table[action-1])

# Main game loop
def run_game(algorithm, target):
    state = 0
    for i in range(NUM_STEPS):
        action = algorithm.get_action(state)
        algorithm.update_policy(state, action)
        if action == target:
            print("You win!")

            return action
        state += 1
    print("You lose!")
    return action

# generate a random number between 1 and 100
target = random.randint(1, MAX_NUMBER)
# or just you can set any wanted value for the taregt
# target = 55

# Run the game with imitation learning
print("Imitation Learning:")
algorithm = ImitationLearning(target)
Imitation_guessed = run_game(algorithm, target)
print("the Random target number is:", target, "Imitation_guessed number:", Imitation_guessed)



# Run the game with reinforcement learning
print("Reinforcement Learning:")
algorithm = ReinforcementLearning()
Reinforcement_guessed = run_game(algorithm, target)
print("the Random target number is:", target, "Reinforcement_guessed number:", Reinforcement_guessed)

