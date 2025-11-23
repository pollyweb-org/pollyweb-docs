# Item 🛢 Handlers

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ

1. **How to work with event handlers?**

    Event handlers 
    * are set on the [`Build@Itemized` 🅰️ method](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
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
    | `EXPIRED` | Item removed automatically due to a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) expiration
    | `PURGED`  | Item removed automatically due to an [`UNDO`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) timeout
    |

1. **How to register an Event Handler?**

    ```yaml
    Table: <table-name>
    Item: <item-name>

    Handlers:
        <handler>: 
            Events: [events]
            Assert: {asserts}
    ```

    |Input|Details|Example
    |-|-|-
    | `<handler>` | Name of the [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to handle | `MyHandler`
    | `[events]` | Events to handle | `INSERTED, PURGED`
    | `{asserts}` | Filter events with [`.Assert`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) |
    |           | on the latest version of the item | `Item.A`
    |           | on the new property versions | `New.A`
    |           | and on old property versions | `Old.A`
    |

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS
    Item: ORDER

    Handlers: 

        OnTimeout: 
            Events: EXPIRED, PURGED

        OnChange: 
            Events: ALTERED

        OnSomeStatus:
            Events: UPDATED
            Assert: 
                Item.Expires.IsAbove(.Now):
                New.State: NEW_STATE
                Old.State: OLD_STATE
    ```
    Uses: [`.IsAbove`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsAbove ⓕ any.md>) [`.Now`](<../../../37 Scripts 📃/📃 Holders 🧠/Time 📚 holders/Now ⓕ.md>)

    ---
    <br/>