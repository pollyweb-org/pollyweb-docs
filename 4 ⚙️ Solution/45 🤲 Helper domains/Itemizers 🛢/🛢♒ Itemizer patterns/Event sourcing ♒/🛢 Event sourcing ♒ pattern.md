# 🛢 Event sourcing ♒ pattern

> Part of [Itemizer 🛢 helper domains](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)

The Event sourcing ♒ pattern involves storing the state changes of an Itemizer 🛢 as a sequence of events rather than just the current state.
* This allows for a complete history of changes, enabling features like auditing, replaying events to reconstruct past states, and easier debugging.
* It is particularly useful in systems where tracking changes over time is crucial.
* Events in the log are immutable and represent a fact that has occurred in the system.
* The current state of the Itemizer 🛢 item can be derived by replaying these events in order.
* Event sourcing can be combined with Command Query Responsibility Segregation (CQRS) to separate read and write operations, further enhancing performance and scalability.

## Diagram

![alt text](<🛢 Event sourcing ⚙️ uml.png>)