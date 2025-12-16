# 🛢 Saga state machine ♒ pattern

> Part of [Itemizer 🛢 helper domains](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)

The Saga state machine ♒ pattern enables the management of long-running transactions by breaking them into a series of smaller, manageable steps, each represented by a state in the Itemizer 🛢.
* Each step can be independently committed or rolled back, allowing for greater flexibility and fault tolerance.
* The state machine tracks the progress of the transaction, ensuring that each step is completed in order.
* If a step fails, compensating actions can be triggered to undo the effects of previous steps, maintaining data consistency.

## Diagram

![alt text](<🛢 Saga state machine ⚙️ uml.png>)