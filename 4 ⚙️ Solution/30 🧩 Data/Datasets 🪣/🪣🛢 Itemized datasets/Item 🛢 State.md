# Item 🛢 .State

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ

1. **What's the .State field for?**

    The `.State` field
    * allows to track the state of an item in a workflow
    * and trigger actions on state changes
    * such as sending notifications, or triggering other processes.

    <br/>

1. **What architecture patterns does it follow?**

    * [Event Sourcing pattern](<https://martinfowler.com/eaaDev/EventSourcing.html>)
    * [Observer pattern](<https://martinfowler.com/eaaDev/Observer.html>)
    * [State Transition pattern](<https://docs.microsoft.com/en-us/azure/architecture/patterns/state-transition>)
    * [Saga pattern](<https://docs.microsoft.com/en-us/azure/architecture/patterns/saga>)
    * [Workflow pattern](<https://docs.microsoft.com/en-us/azure/architecture/patterns/workflow>)
    <!-- Outbox Pattern — specifically "Transactional Outbox" -->
    * [Outbox pattern](<https://microservices.io/patterns/data/transactional-outbox.html>)
    <!-- CQRS Pattern -->
    * [CQRS pattern](<https://martinfowler.com/bliki/CQRS.html>)
    * [Event-Driven Architecture pattern](<https://martinfowler.com/articles/201701-event-driven.html>)
    * [Domain-Driven Design pattern](<https://martinfowler.com/bliki/DomainDrivenDesign.html>)
    <!-- Projections -->
    * [Projection pattern](<https://docs.microsoft.com/en-us/azure/architecture/patterns/projection>)
    <!-- Eventual consistency pattern -->
    * [Eventual Consistency pattern](<https://docs.microsoft.com/en-us/azure/architecture/patterns/eventual-consistency>)
    

    ---
    <br/>

1. **How to work with .State changes?**

    `.State` changes
    * are set on the [`Build@Itemized` 🅰️ method](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
    * and processed by [Item 🛢 Handlers](<Item 🛢 Handlers.md>)
    * with the new state in the `New.State` property
    * and the old state in the `Old.State` property.


    ---
    <br/>

1. **How does it behave in idempotent scenarios?**

    `.State` is supposed to be changed.
    * Meaning that setting a `.State` in an item with the same state fails.
    * Meaning that duplicate events fail to be processed.
    * To mitigate error logs, stale `.State` changes raise a special `REPEATED` event.

    ---
    <br/>