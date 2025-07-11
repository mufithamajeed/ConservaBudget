# Theoretical Background: ConservaBudget

## 1. Introduction

Conservation resources are often limited, requiring difficult choices about **which species or habitats to prioritize**. This project models this challenge mathematically and explores how tools from **decision science** can support more informed conservation planning.

---

## 2. The Conservation Budgeting Problem

Given:
- A finite **budget** for conservation actions.
- Multiple species, each with:
  - An **estimated conservation benefit**.
  - A **cost of intervention**.
  - A level of **uncertainty** in outcomes.

The goal is to select the combination of actions that **maximizes total benefit without exceeding the budget**.

---

## 3. Simple Decision Rule: Benefit-Cost Ratio

One commonly used approach is to prioritize species based on the **Benefit-Cost Ratio (BCR)**:

$$
\text{BCR} = \frac{\text{Conservation Benefit}}{\text{Cost of Intervention}}
$$

Species with the highest BCRs are selected until the available budget is exhausted.

While simple, this method:
- Ignores uncertainty.
- Assumes linear and independent benefits.

---

## 4. Value of Information (VOI) in Conservation

Decisions often have to be made **under uncertainty** about outcomes, species viability, or intervention effectiveness. Sometimes, it's better to:
- Spend resources on **learning** (e.g., field studies, surveys).
- Then act once better data reduces uncertainty.

### VOI Formula:
$$
\text{VOI} = (\text{Expected Benefit Gain} \times \text{Probability of Correct Decision}) - \text{Cost of Learning}
$$

A **positive VOI** suggests that additional information could improve decisions and outcomes.

VOI is widely used in:
- **Biodiversity conservation**
- **Invasive species management**
- **Endangered species recovery planning**

---

## 5. Example Species in This Simulation

Species chosen for this model:
1. **Amur Leopard** *(Panthera pardus orientalis)*
2. **Javan Rhino** *(Rhinoceros sondaicus)*
3. **Mountain Gorilla** *(Gorilla beringei beringei)*
4. **Green Sea Turtle** *(Chelonia mydas)*
5. **Monarch Butterfly** *(Danaus plexippus)*

These species illustrate a diversity of conservation contexts—mammals, reptiles, invertebrates—each with different benefits, costs, and uncertainties.

---

## 6. Future Directions

- Apply **stochastic dynamic programming** for sequential decisions.
- Incorporate **ecosystem-level interactions** (not just species-level).
- Use **Bayesian updating** to model the actual learning process over time.

---

*This theoretical note was created as part of a research portfolio for PhD applications in mathematical ecology, conservation optimization, and decision science.*
````