# 😃⤵️ Talker `THEN` flow 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ


1. **What's an THEN flow?**

    `THEN` ⤵️
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  
    * that runs a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) or [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)
    * following the success of an [`IF`](<../IF ⤵️/⤵️ IF ⌘ cmd.md>) or [`CONFIRM`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>).

    ---
    <br/>

1. **What's the THEN syntax?**


    ```yaml
    THEN: [commands...]
    ```

    | Input| Purpose | Example
    |-|-|-
    | `commands...` | List of [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) if `True` | [`RETURN`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)` 123`
    

    ---
    <br/>

1. **What are alternative syntaxes?**
    
    ```yaml
    - THEN <command>
    ```

    ```yaml
    - THEN: <command>
    ```

    ```yaml
    - THEN:
        <command>
    ```

    ```yaml
    - THEN>:
        - <command-1>
        - <command-n>
    ```
    
    ---
    <br/>
