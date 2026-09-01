# ==========================================
# DAY 34 - PROBABILISTIC INFERENCE
# ==========================================

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


print("==========================================")
print("DAY 34 - PROBABILISTIC INFERENCE")
print("==========================================")


# ------------------------------------------
# 1. Create Bayesian Network
# ------------------------------------------

model = DiscreteBayesianNetwork([
    ("Rain", "WetGround"),
    ("Sprinkler", "WetGround")
])


# ------------------------------------------
# 2. Prior Probability of Rain
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
# 3. Prior Probability of Sprinkler
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
# 4. Conditional Probability of Wet Ground
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
# 5. Add Probability Distributions
# ------------------------------------------

model.add_cpds(
    cpd_rain,
    cpd_sprinkler,
    cpd_wetground
)


# ------------------------------------------
# 6. Check Model
# ------------------------------------------

print("\nModel Check:")

print(model.check_model())


# ------------------------------------------
# 7. Create Inference Object
# ------------------------------------------

inference = VariableElimination(model)


# ==========================================
# 8. PRIOR PROBABILITY
# ==========================================

print("\n==========================================")
print("PRIOR PROBABILITY")
print("==========================================")

prior = inference.query(
    variables=["Rain"]
)

print(prior)


# ==========================================
# 9. POSTERIOR PROBABILITY
# ==========================================

print("\n==========================================")
print("POSTERIOR PROBABILITY")
print("==========================================")


posterior = inference.query(
    variables=["Rain"],
    evidence={
        "WetGround": "Yes"
    }
)

print(
    "\nP(Rain | WetGround = Yes):"
)

print(posterior)


# ==========================================
# 10. MULTIPLE EVIDENCE
# ==========================================

print("\n==========================================")
print("MULTIPLE EVIDENCE")
print("==========================================")


result = inference.query(
    variables=["Rain"],
    evidence={
        "WetGround": "Yes",
        "Sprinkler": "Off"
    }
)

print(
    "\nP(Rain | WetGround = Yes, "
    "Sprinkler = Off):"
)

print(result)


# ==========================================
# 11. QUERY WET GROUND
# ==========================================

print("\n==========================================")
print("QUERY: WET GROUND")
print("==========================================")


result = inference.query(
    variables=["WetGround"],
    evidence={
        "Rain": "Yes"
    }
)

print(
    "\nP(WetGround | Rain = Yes):"
)

print(result)


# ==========================================
# 12. Query Sprinkler
# ==========================================

print("\n==========================================")
print("QUERY: SPRINKLER")
print("==========================================")


result = inference.query(
    variables=["Sprinkler"],
    evidence={
        "WetGround": "Yes"
    }
)

print(
    "\nP(Sprinkler | WetGround = Yes):"
)

print(result)


# ==========================================
# 13. Summary
# ==========================================

print("\n==========================================")
print("INFERENCE SUMMARY")
print("==========================================")

print("""
Prior:
Probability before observing evidence.

Evidence:
Information that we already know.

Posterior:
Updated probability after considering evidence.

Inference:
Using known information to calculate
unknown probabilities.
""")


print("\n==========================================")
print("DAY 34 COMPLETED")
print("==========================================")