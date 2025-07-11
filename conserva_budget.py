import numpy as np
import matplotlib.pyplot as plt

species = [
    'Amur Leopard',            # Critically Endangered Big Cat
    'Javan Rhino',             # Critically Endangered Rhino
    'Mountain Gorilla',        # Endangered Primate
    'Green Sea Turtle',        # Endangered Marine Species
    'Monarch Butterfly'        # Declining Pollinator Species
]

# Conservation benefit of protecting each species (arbitrary units)
benefits = np.array([100, 80, 60, 40, 30])

# Cost required to conserve each species (arbitrary units)
costs = np.array([50, 40, 30, 20, 10])

# Uncertainty associated with conservation outcome
uncertainty = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

# Total conservation budget available
budget = 100

# Simple Allocation Strategy: Benefit-Cost Ratio
benefit_cost_ratio = benefits / costs
sorted_indices = np.argsort(-benefit_cost_ratio)  # Sort descending

sorted_species = [species[i] for i in sorted_indices]
sorted_benefits = benefits[sorted_indices]
sorted_costs = costs[sorted_indices]
sorted_uncertainty = uncertainty[sorted_indices]

allocated_species = []
spent_budget = 0

for i in range(len(sorted_species)):
    if spent_budget + sorted_costs[i] <= budget:
        allocated_species.append(sorted_species[i])
        spent_budget += sorted_costs[i]

print("Optimal Conservation Allocation based on Benefit-Cost Ratio:")
for sp in allocated_species:
    print(f" - {sp}")
print(f"Total Budget Spent: {spent_budget} (of {budget})")

# Value of Information (VOI) Calculation

def value_of_information(cost_of_learning, expected_benefit_gain, prob_correct):
    """
    Calculate the Value of Information (VOI) for conservation decision-making.
    """
    return (expected_benefit_gain * prob_correct) - cost_of_learning

# Hypothetical VOI example:
learning_cost = 10
expected_benefit_gain = 50
prob_correct = 0.75

voi = value_of_information(learning_cost, expected_benefit_gain, prob_correct)
print(f"\nEstimated Value of Information: {voi:.2f} benefit units")

plt.figure(figsize=(10, 6))
plt.bar(species, benefits, color='mediumseagreen', label='Conservation Benefit')
plt.plot(species, costs, color='orange', marker='o', label='Conservation Cost')
plt.xlabel('Species')
plt.ylabel('Value')
plt.title('Conservation Benefit vs Cost for Multiple Species')
plt.legend()
plt.grid(True)
plt.show()