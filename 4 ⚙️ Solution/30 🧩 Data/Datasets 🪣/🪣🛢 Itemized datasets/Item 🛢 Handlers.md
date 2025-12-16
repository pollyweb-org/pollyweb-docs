# Item 🛢 Handlers

> About
* Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

<br/>

## FAQ

1. **What architecture patterns does it allow?**

    |Pattern|Description|
    |-|-|
    | `Saga`   | Distributed asynchronous transactions coordination |
    | `Outbox` | Reliable message delivery in distributed systems |
    | `CQRS`   | Separation of read and write operations |
    | `Projection` | Transforming data into different views |
    | `Event Sourcing` | Capturing all changes as a sequence of events |
    | `Eventual Consistency` | Data consistency over time in distributed systems |    

    ---
    <br/>

1. **How to work with event handlers?**

    Event handlers 
    * are set on the [`Build@Itemized` 🐌 msg](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢📨 Itemizer msgs/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
    * and are streamed as [`Raised@Itemizer` 🔔 event](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Raised.md>)

    ---
    <br/>


1. **What are the possible events?**
    
    |Value|Description|
    |-|-|
    | `INSERTED`   | Item inserted on the [Itemized 🛢 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>) on a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
    | `UPDATED` | The content of the item has changed on a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
    | `DELETED` | Item deleted on a [`DELETE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>), either soft or hard
    | `ALTERED` | Raised on `INSERTED` `UPDATED` or `DELETED`
    
    ---
    <br/>

1. **How to register an Event Handler?**

    ```yaml
    Handlers:
        <handler>: 
            Events: [events]
            Assert: {asserts}
    ```

    |Input|Details|Example
    |-|-|-
    | `<handler>` | Name of the [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to handle | `MyHandler`
    | `[events]` | Events to handle | `INSERTED, ALTERED`
    | `{asserts}` | Filter events with [`.Assert`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) |
    |           | on the latest version of the item | `Item.A`
    |           | on the new property versions | `New.A`
    |           | and on old property versions | `Old.A`
    |

    Here's an example.

    ```yaml
    # Example
    Handlers: 

        OnChange: 
            Events: ALTERED

        OnSomeStatus:
            Events: UPDATED
            Assert: 
                Item.AnyField.Is: AnyValue
                New.AnyField: AnyNewValue
                Old.AnyField: AnyOldValue
    ```
    Uses: [`.IsFuture`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>) [`.Now`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>)

    ---
    <br/>
