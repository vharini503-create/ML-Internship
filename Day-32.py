# ==========================================
# DAY 32 - HIDDEN MARKOV MODEL
# ==========================================

import numpy as np


print("==========================================")
print("DAY 32 - HIDDEN MARKOV MODEL")
print("==========================================")


# ------------------------------------------
# 1. Define Hidden States
# ------------------------------------------

states = [
    "Sunny",
    "Rainy"
]

print("\nHidden States:")
print(states)


# ------------------------------------------
# 2. Define Observations
# ------------------------------------------

observations = [
    "Walk",
    "Shop",
    "Clean"
]

print("\nObservations:")
print(observations)


# ------------------------------------------
# 3. Initial State Probabilities
# ------------------------------------------

initial_probability = {
    "Sunny": 0.6,
    "Rainy": 0.4
}

print("\nInitial State Probabilities:")
print(initial_probability)


# ------------------------------------------
# 4. Transition Probabilities
# ------------------------------------------

transition_probability = {

    "Sunny": {
        "Sunny": 0.7,
        "Rainy": 0.3
    },

    "Rainy": {
        "Sunny": 0.4,
        "Rainy": 0.6
    }
}

print("\nTransition Probabilities:")

for state in states:

    print(
        state,
        "->",
        transition_probability[state]
    )


# ------------------------------------------
# 5. Emission Probabilities
# ------------------------------------------

emission_probability = {

    "Sunny": {
        "Walk": 0.6,
        "Shop": 0.3,
        "Clean": 0.1
    },

    "Rainy": {
        "Walk": 0.1,
        "Shop": 0.4,
        "Clean": 0.5
    }
}

print("\nEmission Probabilities:")

for state in states:

    print(
        state,
        "->",
        emission_probability[state]
    )


# ------------------------------------------
# 6. Given Observation
# ------------------------------------------

observation_sequence = [
    "Walk",
    "Shop",
    "Clean"
]

print("\nObservation Sequence:")
print(observation_sequence)


# ------------------------------------------
# 7. Find Most Likely State
#    For Each Observation
# ------------------------------------------

print("\n==========================================")
print("MOST LIKELY HIDDEN STATES")
print("==========================================")


predicted_states = []


for observation in observation_sequence:

    probabilities = {}

    for state in states:

        probability = (
            initial_probability[state]
            *
            emission_probability[state][observation]
        )

        probabilities[state] = probability


    most_likely_state = max(
        probabilities,
        key=probabilities.get
    )

    predicted_states.append(
        most_likely_state
    )

    print(
        "Observation:",
        observation
    )

    print(
        "Probabilities:",
        probabilities
    )

    print(
        "Most Likely State:",
        most_likely_state
    )

    print()


# ------------------------------------------
# 8. Final Prediction
# ------------------------------------------

print("==========================================")
print("FINAL PREDICTION")
print("==========================================")

print("\nObservations:")
print(observation_sequence)

print("\nPredicted Hidden States:")
print(predicted_states)


# ------------------------------------------
# 9. Explain HMM Components
# ------------------------------------------

print("\n==========================================")
print("HMM COMPONENTS")
print("==========================================")

print("\nHidden States:")
print(states)

print("\nObservations:")
print(observations)

print("\nTransition Probability:")
print("Probability of moving from one state to another.")

print("\nEmission Probability:")
print("Probability of an observation being produced by a state.")

print("\nInitial Probability:")
print("Probability of starting in each hidden state.")


print("\n==========================================")
print("DAY 32 COMPLETED")
print("==========================================")# ==========================================
# DAY 32 - HIDDEN MARKOV MODEL
# ==========================================

import numpy as np


print("==========================================")
print("DAY 32 - HIDDEN MARKOV MODEL")
print("==========================================")


# ------------------------------------------
# 1. Define Hidden States
# ------------------------------------------

states = [
    "Sunny",
    "Rainy"
]

print("\nHidden States:")
print(states)


# ------------------------------------------
# 2. Define Observations
# ------------------------------------------

observations = [
    "Walk",
    "Shop",
    "Clean"
]

print("\nObservations:")
print(observations)


# ------------------------------------------
# 3. Initial State Probabilities
# ------------------------------------------

initial_probability = {
    "Sunny": 0.6,
    "Rainy": 0.4
}

print("\nInitial State Probabilities:")
print(initial_probability)


# ------------------------------------------
# 4. Transition Probabilities
# ------------------------------------------

transition_probability = {

    "Sunny": {
        "Sunny": 0.7,
        "Rainy": 0.3
    },

    "Rainy": {
        "Sunny": 0.4,
        "Rainy": 0.6
    }
}

print("\nTransition Probabilities:")

for state in states:

    print(
        state,
        "->",
        transition_probability[state]
    )


# ------------------------------------------
# 5. Emission Probabilities
# ------------------------------------------

emission_probability = {

    "Sunny": {
        "Walk": 0.6,
        "Shop": 0.3,
        "Clean": 0.1
    },

    "Rainy": {
        "Walk": 0.1,
        "Shop": 0.4,
        "Clean": 0.5
    }
}

print("\nEmission Probabilities:")

for state in states:

    print(
        state,
        "->",
        emission_probability[state]
    )


# ------------------------------------------
# 6. Given Observation
# ------------------------------------------

observation_sequence = [
    "Walk",
    "Shop",
    "Clean"
]

print("\nObservation Sequence:")
print(observation_sequence)


# ------------------------------------------
# 7. Find Most Likely State
#    For Each Observation
# ------------------------------------------

print("\n==========================================")
print("MOST LIKELY HIDDEN STATES")
print("==========================================")


predicted_states = []


for observation in observation_sequence:

    probabilities = {}

    for state in states:

        probability = (
            initial_probability[state]
            *
            emission_probability[state][observation]
        )

        probabilities[state] = probability


    most_likely_state = max(
        probabilities,
        key=probabilities.get
    )

    predicted_states.append(
        most_likely_state
    )

    print(
        "Observation:",
        observation
    )

    print(
        "Probabilities:",
        probabilities
    )

    print(
        "Most Likely State:",
        most_likely_state
    )

    print()


# ------------------------------------------
# 8. Final Prediction
# ------------------------------------------

print("==========================================")
print("FINAL PREDICTION")
print("==========================================")

print("\nObservations:")
print(observation_sequence)

print("\nPredicted Hidden States:")
print(predicted_states)


# ------------------------------------------
# 9. Explain HMM Components
# ------------------------------------------

print("\n==========================================")
print("HMM COMPONENTS")
print("==========================================")

print("\nHidden States:")
print(states)

print("\nObservations:")
print(observations)

print("\nTransition Probability:")
print("Probability of moving from one state to another.")

print("\nEmission Probability:")
print("Probability of an observation being produced by a state.")

print("\nInitial Probability:")
print("Probability of starting in each hidden state.")


print("\n==========================================")
print("DAY 32 COMPLETED")
print("==========================================")