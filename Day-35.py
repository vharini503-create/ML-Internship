# ==========================================
# DAY 35 - PROBABILISTIC ML REVIEW
# ==========================================

import numpy as np

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


print("==========================================")
print("DAY 35 - PROBABILISTIC ML REVIEW")
print("==========================================")


# ==========================================
# PART 1 - MARKOV MODEL
# ==========================================

print("\n==========================================")
print("PART 1 - MARKOV MODEL")
print("==========================================")


states = [
    "Sunny",
    "Cloudy",
    "Rainy"
]


transition_matrix = np.array([

    [0.6, 0.3, 0.1],

    [0.2, 0.5, 0.3],

    [0.1, 0.3, 0.6]

])


print("\nStates:")
print(states)


print("\nTransition Matrix:")
print(transition_matrix)


current_state = "Sunny"

current_index = states.index(
    current_state
)


probabilities = transition_matrix[
    current_index
]


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


next_index = np.argmax(
    probabilities
)

next_state = states[next_index]


print("\nMost Likely Next State:")
print(next_state)


# ==========================================
# PART 2 - HIDDEN MARKOV MODEL
# ==========================================

print("\n==========================================")
print("PART 2 - HIDDEN MARKOV MODEL")
print("==========================================")


hidden_states = [
    "Sunny",
    "Rainy"
]


observations = [
    "Walk",
    "Shop",
    "Clean"
]


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


observation_sequence = [
    "Walk",
    "Shop",
    "Clean"
]


print("\nObservation Sequence:")
print(observation_sequence)


print("\nMost Likely Hidden States:")


predicted_states = []


for observation in observation_sequence:

    probabilities = {}

    for state in hidden_states:

        probabilities[state] = (
            emission_probability[state][observation]
        )

    best_state = max(
        probabilities,
        key=probabilities.get
    )

    predicted_states.append(
        best_state
    )

    print(
        observation,
        "->",
        best_state
    )


print("\nPredicted Hidden States:")
print(predicted_states)


# ==========================================
# PART 3 - BAYESIAN NETWORK
# ==========================================

print("\n==========================================")
print("PART 3 - BAYESIAN NETWORK")
print("==========================================")


model = DiscreteBayesianNetwork([
    ("Rain", "WetGround"),
    ("Sprinkler", "WetGround")
])


# Rain probability

cpd_rain = TabularCPD(
    variable="Rain",
    variable_card=2,
    values=[
        [0.7],
        [0.3]
    ],
    state_names={
        "Rain": ["No", "Yes"]
    }
)


# Sprinkler probability

cpd_sprinkler = TabularCPD(
    variable="Sprinkler",
    variable_card=2,
    values=[
        [0.6],
        [0.4]
    ],
    state_names={
        "Sprinkler": ["Off", "On"]
    }
)


# Wet ground probability

cpd_wetground = TabularCPD(
    variable="WetGround",
    variable_card=2,

    values=[
        [0.99, 0.90, 0.80, 0.01],
        [0.01, 0.10, 0.20, 0.99]
    ],

    evidence=[
        "Rain",
        "Sprinkler"
    ],

    evidence_card=[
        2,
        2
    ],

    state_names={
        "WetGround": ["No", "Yes"],
        "Rain": ["No", "Yes"],
        "Sprinkler": ["Off", "On"]
    }
)


model.add_cpds(
    cpd_rain,
    cpd_sprinkler,
    cpd_wetground
)


print("\nBayesian Network:")
print(model.edges())


print("\nModel Check:")
print(model.check_model())


# ==========================================
# PART 4 - PROBABILISTIC INFERENCE
# ==========================================

print("\n==========================================")
print("PART 4 - PROBABILISTIC INFERENCE")
print("==========================================")


inference = VariableElimination(
    model
)


# Prior probability

prior = inference.query(
    variables=["Rain"]
)


print("\nPrior Probability of Rain:")
print(prior)


# Posterior probability

posterior = inference.query(
    variables=["Rain"],
    evidence={
        "WetGround": "Yes"
    }
)


print("\nProbability of Rain")
print("given Wet Ground = Yes:")

print(posterior)


# Multiple evidence

posterior_2 = inference.query(
    variables=["Rain"],
    evidence={
        "WetGround": "Yes",
        "Sprinkler": "Off"
    }
)


print("\nProbability of Rain")
print("given Wet Ground = Yes")
print("and Sprinkler = Off:")

print(posterior_2)


# ==========================================
# FINAL SUMMARY
# ==========================================

print("\n==========================================")
print("PROBABILISTIC ML SUMMARY")
print("==========================================")


print("""
Markov Model:
Models transitions between observable states.

Hidden Markov Model:
Models hidden states using observations.

Bayesian Network:
Represents probabilistic relationships
between variables.

Probabilistic Inference:
Uses evidence to calculate or update
unknown probabilities.

Prior:
Probability before evidence.

Posterior:
Updated probability after evidence.
""")


print("\n==========================================")
print("PROBABILISTIC ML STAGE COMPLETED")
print("==========================================")