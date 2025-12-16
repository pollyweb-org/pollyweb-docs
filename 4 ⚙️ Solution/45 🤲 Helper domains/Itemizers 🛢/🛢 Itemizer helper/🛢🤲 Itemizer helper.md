# 🛢 Itemizer helper


## FAQ

1. **What's an Itemizer?**

    An [Itemizer 🛢 helper domain](<🛢🤲 Itemizer helper.md>)
    * is a [Helper 🤲 domain](<../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>)
    * that manages [Itemized 🪣 datasets](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * on behalf of other [domains 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>).

    ---
    <br/>

1. **What are the inbound messages supported?**

    |Scope|[Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | Purpose
    |-|-|-
    |Item   | [🚀 `Delete`](<../🛢📨 Itemizer msgs/Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>)| Delete an item
    |       | [🚀 `Get`](<../🛢📨 Itemizer msgs/Item Read 👥🚀🛢/🛢 Read 🚀 call.md>) | Get an item
    |       | [🚀 `Save`](<../🛢📨 Itemizer msgs/Item Save 👥🚀🛢/🛢 Save 🚀 call.md>) | Save an item
    |Table  | [🐌 `Build`](<../🛢📨 Itemizer msgs/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>) | Build a table
    |       | [🐌 `Burn`](<../🛢📨 Itemizer msgs/Table Burn 👥🐌🛢/🛢 Burn 🐌 msg.md>) | Destroy a table
    |       | [🚀 `List`](<../🛢📨 Itemizer msgs/Table List 👥🚀🛢/🛢 List 🚀 call.md>) | List all tables

    ---
    <br/>

1. **What are the triggers supported?**
   
    |[Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | Purpose
    |-|-
    | [🔔 `Triggered`](<../../Alarms ⏰/⏰🔔 Alarm events/⏰🔔 Triggered.md>) | Informs on item changes

    ---
    <br/>

1. **How are they mapped to script commands?**

    [Command ⌘](<../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    |[🧲 `READ`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | Calls [`Read@Itemizer` 🅰️ ](<../🛢📨 Itemizer msgs/Item Read 👥🚀🛢/🛢 Read 🚀 call.md>)
    |[💾 `SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Calls [`Save@Itemizer` 🅰️ ](<../🛢📨 Itemizer msgs/Item Save 👥🚀🛢/🛢 Save 🚀 call.md>)
    |[🗑️ `DELETE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) | Calls [`Delete@Itemizer` 🅰️ ](<../🛢📨 Itemizer msgs/Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>)

    ---
    <br/>

1. **What architectural patterns do Itemizers support?**

    | Pattern ♒ | Purpose
    |-|-
    | [Event sourcing](<../🛢♒ Itemizer patterns/Event sourcing ♒/🛢 Event sourcing ♒ pattern.md>) | Enables tracking and storing all changes to items over time, allowing for historical data retrieval and auditing.
    | [Insert Idempotency](<../🛢♒ Itemizer patterns/Idempotency on insert ♒/🛢 Insert Idempotency ♒ pattern.md>) | Ensures that repeated {{SAVE}} insert operations with the same data do not trigger more than one event.
    | [Update Idempotency](<../🛢♒ Itemizer patterns/Idempotency on update ♒/🛢 Update Idempotency ♒ pattern.md>) | Ensures that repeated {{READ}} then {{SAVE}} update operations with the same data do not trigger more than one event.
    | [Optimistic concurrency](<../🛢♒ Itemizer patterns/Optimistic concurrency ♒/🛢 Optimistic concurrency ♒ pattern.md>) | Allows multiple {{SAVE}} commands to run in parallel without locking resources, assuming that conflicts are rare.
    | [Saga state machine](<../🛢♒ Itemizer patterns/Saga state machine ♒/🛢 Saga state machine ♒ pattern.md>) | Implements a Saga pattern to manage long-running transactions with multiple steps across several domains.
    | [Temporal persistence](<../🛢♒ Itemizer patterns/Temporal persistence ♒/🛢 Temporal persistence ♒ pattern.md>) | Provides temporal data storage capabilities, allowing items to expire after a period of time according to their state.

    ---
    <br/>