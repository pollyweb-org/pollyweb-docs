# Item 🛢 Triggers

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ

1. **How to work with triggers?**

    Triggers 
    * are set on the [`Build@Itemized` 🅰️ method](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
    * and are consumed by the [`Triggered@Talker` 🅰️ method](<../../../45 🤲 Helper domains/Alarms ⏰/⏰🔔 Alarm events/⏰🔔 Triggered.md>)

    ---
    <br/>



1. **What are the possible triggers?**
    
    |Value|Description|
    |-|-|
    | `ADDED`   | Item inserted on the [Itemized 🛢 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) on a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
    | `CHANGED` | The content of the item has changed on a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
    | `EXPIRED` | Item removed automatically due to a [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) expiration
    | `DELETED` | Item deleted on a [`DELETE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>), either soft or hard
    | `PURGED`  | Item removed automatically due to an [`UNDO`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) timeout
    |

1. **How to register a Trigger?**

    ```yaml
    Table: <name>
    Triggers:
        <handler>: <trigger-list>
    ```

    |Input|Details|Example
    |-|-|-
    | `<handler>` | Name of the [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to handle | `MyHandler`
    | `<trigger-list>` | Triggers to handle | `ADDED,PURGED`
    |

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS
    Triggers: 
        OnTimeout: EXPIRED, PURGED
        OnChange: ADDED, CHANGED, DELETED
    ```

    ---
    <br/>