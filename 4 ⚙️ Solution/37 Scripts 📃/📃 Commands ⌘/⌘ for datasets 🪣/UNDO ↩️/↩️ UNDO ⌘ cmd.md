<!-- TODO -->

# 😃↩️ Talker `UNDO` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

> Implemented by the [`.UNDO` 📃 script](<↩️ UNDO 📃 script.md>)

> Cancels a soft [`DELETE` 🗑️ command](<../DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>)

<br/>

1. **What is an UNDO command?**

    An `UNDO` ↩️
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that revers the removal of item in an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * that occurred with a soft [`DELETE`](<../DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>).

    ---
    <br/>


1. **What's the UNDO syntax?**

    ```yaml
    UNDO|$deleted
    ```

    | Input| Purpose 
    |-|-
    | `$deleted`| [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) returned by [`DELETE`](<../DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>)

    ---
    <br/>

1. **How to use an UNDO?**

    ```yaml 
    # Delete an item
    - DELETE|$item >> $deleted:
        Undo: 30 days

    # Inform the user 
    - SUCCESS|Removed:
        # Non-blocking undo option
        Options: Undo 

    # Undo the delete later, eventually
    - CASE:
        Undo: 
        - UNDO|$deleted
    ```

    Uses: [`CASE`](<../../⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`DELETE`](<../DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) [`SUCCESS`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>


    ---
    <br/>

1. **What's a use case for soft deletes?**

    See [Pop Token 🔆](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Pops 🍿 table/🪣🔔 61 Token/🤵 Pop Token 📃 handler.md>).

    ---
    <br/>