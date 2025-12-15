# 😃🧪 Talker `TRY` command 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

<br/>


1. **What's the `TRY` command?**

    `TRY` 🧪
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that catches errors on a block of commands.


    ---
    <br/>


1. **What's the `TRY` syntax?**

    ```yaml
    TRY >> $error:
        {block of commands}
    ```

    | Input| Purpose | Example
    |-|-|-
    | `$error`| Error message | `Invalid data`
    
    ---
    <br/>


1. **What's an example of a `TRY` for [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)?**

    The [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) below displays `Caught dummy error`.

    ```yaml
    📃 Example:

    # Catch an error from ASSERT
    - TRY >> $error:
        - ASSERT $data:
            Error: dummy error
            1.Equals: 2

    # Handle the error
    - IF $error:
        - INFO: Caught {$error}
    - ELSE:
        - INFO: No errors
    ```
    Uses: [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`.Equals`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Equals ⓕ.md>)

    ---
    <br/>