# ==========================================
# DAY 31 - MARKOV MODEL
# ==========================================

import numpy as np


print("==========================================")
print("DAY 31 - MARKOV MODEL")
print("==========================================")


# ------------------------------------------
# 1. Define States
# ------------------------------------------

states = [
    "Sunny",
    "Cloudy",
    "Rainy"
]

print("\nStates:")
print(states)


# ------------------------------------------
# 2. Transition Probability Matrix
# ------------------------------------------

transition_matrix = np.array([
    [0.6, 0.3, 0.1],   # Sunny
    [0.2, 0.5, 0.3],   # Cloudy
    [0.1, 0.3, 0.6]    # Rainy
])


print("\nTransition Probability Matrix:")
print(transition_matrix)


# ------------------------------------------
# 3. Check Row Probabilities
# ------------------------------------------

print("\nRow Sums:")

for row in transition_matrix:

    print(np.sum(row))


# ------------------------------------------
# 4. Find Next State Probabilities
# ------------------------------------------

current_state = "Sunny"

current_index = states.index(current_state)

probabilities = transition_matrix[current_index]


print("\nCurrent State:")
print(current_state)

print("\nNext State Probabilities:")

for state, probability in zip(
    states,
    probabilities
):

    print(
        state,
        "->",
        probability
    )


# ------------------------------------------
# 5. Predict Most Likely Next State
# ------------------------------------------

next_index = np.argmax(probabilities)

next_state = states[next_index]


print("\nMost Likely Next State:")
print(next_state)


# ------------------------------------------
# 6. Simulate Several Steps
# ------------------------------------------

print("\n==========================================")
print("MARKOV CHAIN SIMULATION")
print("==========================================")


current_state = "Sunny"

print("\nStarting State:")
print(current_state)


for step in range(5):

    current_index = states.index(
        current_state
    )

    probabilities = transition_matrix[
        current_index
    ]

    next_index = np.random.choice(
        len(states),
        p=probabilities
    )

    current_state = states[next_index]

    print(
        "Step",
        step + 1,
        "->",
        current_state
    )


# ------------------------------------------
# 7. Calculate Probability Distribution
#    After Several Steps
# ------------------------------------------

initial_distribution = np.array([
    1.0,
    0.0,
    0.0
])


print("\n==========================================")
print("STATE DISTRIBUTION")
print("==========================================")


distribution = initial_distribution


for step in range(5):

    distribution = np.dot(
        distribution,
        transition_matrix
    )

    print(
        "After step",
        step + 1,
        ":",
        distribution
    )


print("\n==========================================")
print("DAY 31 COMPLETED")
print("==========================================")