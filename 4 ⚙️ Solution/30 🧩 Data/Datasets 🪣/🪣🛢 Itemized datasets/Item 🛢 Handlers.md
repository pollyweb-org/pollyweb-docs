# Item 🛢 Handlers

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ

1. **How to work with events?**

    Events 
    * are set on the [`Build@Itemized` 🅰️ method](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
    * and are streamed as [`Raised@Itemizer` 🔔 event](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Raised.md>)

    ---
    <br/>



1. **What are the possible events?**
    
    |Value|Description|
    |-|-|
    | `ADDED`   | Item inserted on the [Itemized 🛢 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>) on a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
    | `CHANGED` | The content of the item has changed on a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
    | `EXPIRED` | Item removed automatically due to a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) expiration
    | `DELETED` | Item deleted on a [`DELETE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>), either soft or hard
    | `PURGED`  | Item removed automatically due to an [`UNDO`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) timeout
    |

1. **How to register an Event?**

    ```yaml
    Table: <name>
    Handlers:
        <handler>: 
            <trigger-list>
    ```

    |Input|Details|Example
    |-|-|-
    | `<handler>` | Name of the [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to handle | `MyHandler`
    | `<trigger-list>` | Events to handle | `ADDED,PURGED`
    |

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS
    Events: 
        OnTimeout: EXPIRED, PURGED
        OnChange: ADDED, CHANGED, DELETED
    ```

    ---
    <br/>