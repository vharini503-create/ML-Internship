# ==========================================
# DAY 33 - BAYESIAN NETWORK
# ==========================================

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


print("==========================================")
print("DAY 33 - BAYESIAN NETWORK")
print("==========================================")


# ------------------------------------------
# 1. Create Bayesian Network Structure
# ------------------------------------------

model = DiscreteBayesianNetwork([
    ("Rain", "WetGround"),
    ("Sprinkler", "WetGround")
])


print("\nBayesian Network Structure:")
print(model.edges())


# ------------------------------------------
# 2. Define Probability of Rain
# ------------------------------------------

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


# ------------------------------------------
# 3. Define Probability of Sprinkler
# ------------------------------------------

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


# ------------------------------------------
# 4. Define Wet Ground Probability
# ------------------------------------------

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


# ------------------------------------------
# 5. Add CPDs to Model
# ------------------------------------------

model.add_cpds(
    cpd_rain,
    cpd_sprinkler,
    cpd_wetground
)


# ------------------------------------------
# 6. Check Model
# ------------------------------------------

print("\nChecking Bayesian Network:")

print(model.check_model())


# ------------------------------------------
# 7. Display CPDs
# ------------------------------------------

print("\n==========================================")
print("PROBABILITY DISTRIBUTIONS")
print("==========================================")


print("\nRain Probability:")
print(cpd_rain)


print("\nSprinkler Probability:")
print(cpd_sprinkler)


print("\nWet Ground Probability:")
print(cpd_wetground)


# ------------------------------------------
# 8. Perform Inference
# ------------------------------------------

inference = VariableElimination(model)


# ------------------------------------------
# 9. Probability of Wet Ground
# ------------------------------------------

result = inference.query(
    variables=["WetGround"]
)

print("\n==========================================")
print("PROBABILITY OF WET GROUND")
print("==========================================")

print(result)


# ------------------------------------------
# 10. Probability of Wet Ground
#     When it is Raining
# ------------------------------------------

result_rain = inference.query(
    variables=["WetGround"],
    evidence={
        "Rain": "Yes"
    }
)

print("\n==========================================")
print("WET GROUND GIVEN RAIN")
print("==========================================")

print(result_rain)


# ------------------------------------------
# 11. Probability of Wet Ground
#     When Sprinkler is On
# ------------------------------------------

result_sprinkler = inference.query(
    variables=["WetGround"],
    evidence={
        "Sprinkler": "On"
    }
)

print("\n==========================================")
print("WET GROUND GIVEN SPRINKLER ON")
print("==========================================")

print(result_sprinkler)


# ------------------------------------------
# 12. Probability of Rain Given Wet Ground
# ------------------------------------------

result_reverse = inference.query(
    variables=["Rain"],
    evidence={
        "WetGround": "Yes"
    }
)

print("\n==========================================")
print("PROBABILITY OF RAIN GIVEN WET GROUND")
print("==========================================")

print(result_reverse)


print("\n==========================================")
print("DAY 33 COMPLETED")
print("==========================================")