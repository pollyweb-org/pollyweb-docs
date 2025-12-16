# 😃⤵️ Talker `IFNOT` flow command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ


1. **What's an IFNOT flow command?**

    `IFNOT` ⤵️
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  
    * that represents the `Else` part of an [`IF`](<../IF ⤵️/⤵️ IF ⌘ cmd.md>).

    ---
    <br/>

1. **What's the IFNOT syntax?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

    ```yaml
    IFNOT|<assert>: 
        [cmds...]
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<assert>` | Input for [`.Assert`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>)  | `$h` `.f(*)`
    | `<cmds...>` | List of [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) if `True` | [`RETURN`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)` 123`
    

    ---
    <br/>
