# 😃🔩 Talker `{.Default}` function

> About
* Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
* Used by the [`DEFAULT` ⌘ command](<../../📃 Commands ⌘/⌘ for holders 🧠/DEFAULT 📭/📭 DEFAULT ⌘ cmd.md>)

## FAQ


1. **What's the .Default syntax?**

    ```yaml
    $holder.Default: [defaults...]
    ```

    | Inputs | Purpose 
    |-|-
    | `$holder` | [Holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) to assess 
    | `defaults...` | List of potential defaults


    ---
    <br/>

1. **How does it work?**

    Holder | Defaults | Output | 
    |-|-|-
    | A | ... | A
    | empty | A, B | A
    | empty | empty, B | B
    | empty | empty | empty

    ---
    <br/>


1. **How to use the .Default function?**

    Implicitly, via the [`DEFAULT`](<../../📃 Commands ⌘/⌘ for holders 🧠/DEFAULT 📭/📭 DEFAULT ⌘ cmd.md>) command.

    ```yaml
    - DEFAULT $in:
        A: 123
        B: 456
    ```

    With the [`SET`](<../../📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>) command.

    ```yaml
    - SET $in:
        A.Default: 123
        B.Default: 456
    ```
    
    Using interpolation with commands like [`INFO`](<../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>).

    ```yaml
    - INFO: The value is {$in.A.Default(123)}
    ```

    ---
    <br/>