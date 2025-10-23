<!-- TODO -->

# 😃↩️ Talker `UNDO` command

> Part of [Talker 😃](<../../😃 Talker role.md>)

> Cancels a soft delete.

<br/>

1. **What is an UNDO command?**

    An `UNDO` ↩️
    * is a [Command ⌘](<../...commands/⌘ Command.md>) 
    * that revers the removal of item in an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * that occurred with a soft [`DELETE`](<DELETE 🗑️ item.md>).

    ---
    <br/>


1. **What's the UNDO syntax?**

    ```yaml
    UNDO|$deleted
    ```

    | Argument| Purpose 
    |-|-
    | `$deleted`| [Placeholder 🧠](<../...placeholders/$Placeholder 🧠.md>) returned by [`DELETE`](<DELETE 🗑️ item.md>)

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

    Commands: [`CASE`](<../for control/CASE ⏯️.md>) [`DELETE`](<DELETE 🗑️ item.md>) [`SUCCESS`](<../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>)

    ---
    <br/>


    ---
    <br/>

1. **What's a use case for soft deletes?**

    See [Pop Token 🔆](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📃 Broker scripts/...procedures/🤵📃 Pop Token 🎫.md>).

    ---
    <br/>