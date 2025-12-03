# Item 🛢 NoUpdates

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ

1. **How to block updates?**

    Here's the table definition.

    ```yaml
    NoUpdates: True  # it's False by default
    ```

    Here's a [`Script`](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) excerpt from [`Grab@Printer`](<../../../45 🤲 Helper domains/Printers 🖨️/🖨️📨 Printer msgs/Grab 👥🚀🖨️/🖨️ Grab 🚀 call.md>)

    ```yaml
    # Give a holder name to avoid exceptions.
    - SAVE|AnyTable:
        .OnBlocked: onBlocked
    ```

    |Action|Condition|Behavior
    |-|-|-
    | 💾 [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Same value | Allows multiple  idempotent saves
    | |Different | Blocked, raises an error
    | 🗑️ [`DELETE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) | - | Allows multiple idempotent times

    ---
    <br/>
