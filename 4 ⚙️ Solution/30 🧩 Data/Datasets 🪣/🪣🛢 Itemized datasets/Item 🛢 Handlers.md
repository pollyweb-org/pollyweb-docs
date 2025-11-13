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
    | `ADDED`   | Item inserted on the [Itemized 🛢 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>) on a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
    | `CHANGED` | The content of the item has changed on a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
    | `EXPIRED` | Item removed automatically due to a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) expiration
    | `DELETED` | Item deleted on a [`DELETE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>), either soft or hard
    | `PURGED`  | Item removed automatically due to an [`UNDO`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) timeout
    |

1. **How to register an Event Handler?**

    ```yaml
    Table: <name>

    Handlers:
        <handler>: 
            Events: [events]
            Asserts: {asserts}
    ```

    |Input|Details|Example
    |-|-|-
    | `<handler>` | Name of the [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to handle | `MyHandler`
    | `[events]` | Events to handle | `ADDED, PURGED`
    | `{asserts}` | Filter events with [`.Assert`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Assert}.md>) |
    |           | on the new version of the item | `Item.A`
    |           | and on old versions of changes | `Changes.A`
    |

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS

    Handlers: 

        OnTimeout: 
            Events: EXPIRED, PURGED

        OnChange: 
            Events: ADDED, CHANGED, DELETED

        OnSomeStatus:
            Events: CHANGED
            Asserts: 
                Item.Expires.IsAbove(.Now):
                Item.Status: NEW_STATUS
                Changes.Status: OLD_STATUS
    ```
    Uses: [`.IsAbove`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsAbove}.md>) [`.Now`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Now}.md>)

    ---
    <br/>