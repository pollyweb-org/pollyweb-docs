
<!-- TODO: detail -->

# 😃🔄 Talker `WHILE` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ

1. **What is a 🔄 command?**

    `WHILE` 🔄
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  
    * that runs a list of [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * repeatedly while a given condition is true.
  
    ---
    <br/>


1. **What is the syntax of the FOR command?**

    ```yaml
    WHILE <assertion>:
        # List of commands
        - <command-1>|$item
        - <command-n>|$item
        - BREAK
    ```

    | Input | Purpose | Example
    |-|-|-
    | `<assertion>` | [`.Assert`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) to evaluate | `$x.Length.IsAbove(0)`
    | `<command>`   | [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) to execute | [`SAVE`](<../../⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
    | `BREAK`| Special command to stop

    ---
    <br/>

