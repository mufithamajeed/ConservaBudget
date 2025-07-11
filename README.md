# ConservaBudget

**ConservaBudget** is a simple simulation tool that models the allocation of limited conservation resources across multiple species or habitats. It demonstrates how decision-makers can use quantitative tools such as **Benefit-Cost analysis** and **Value of Information (VOI)** to prioritize conservation actions under uncertainty.

This project is part of a research portfolio at the intersection of **mathematical ecology, optimization, and decision theory**.

---

## Features

- Models conservation allocation under **budget constraints** for multiple threatened species.
- Prioritizes species using **Benefit-Cost Ratio** as a simple decision rule.
- Calculates a **Value of Information (VOI)** to explore when it may be beneficial to gather better data before acting.
- Visualizes conservation **benefits vs costs** across species.

---

## Example Species

This simulation uses the following endangered species as illustrative examples:
- **Amur Leopard**
- **Javan Rhino**
- **Mountain Gorilla**
- **Green Sea Turtle**
- **Monarch Butterfly**

Each species is assigned:
- An estimated **conservation benefit** (ecological, social, or cultural value).
- An associated **cost of intervention**.
- An **uncertainty level** representing outcome risk.

---

## Value of Information (VOI)

The VOI calculation helps decide whether limited conservation budgets should be spent on:
1. **Immediate action**, or
2. **Collecting more information** before making decisions.

The formula used is:
```

VOI = (Benefit of Better Decision × Probability of Correct Decision) - Cost of Learning

````

---

## Usage

The code is implemented in **Python** using `numpy` and `matplotlib`. To run the simulation and view the visualization:

```bash
python conserva_budget.py
````

---

## Future Work

* Implement advanced allocation models (e.g., **stochastic knapsack**, **multi-objective optimization**).
* Simulate dynamic conservation strategies with real-time learning.
* Integrate actual species population data for real-world applications.

---

*This project was developed as part of a research portfolio for PhD applications in mathematical ecology, conservation management, and decision science.*
