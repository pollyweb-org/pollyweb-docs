# 😃🧘 Talker `HOOK` flow 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

> Used by
* [`Async` ⏩ flow](<../../../../35 💬 Chats/Talkers 😃/😃⏩ Talker flows/Run Async Tasks 😃⏩📦/😃 Async ⏩ flow.md>)

<br/>

## FAQ

1. **What's a HOOK flow command?**

    A [`HOOK` 🪝](<🪝 HOOK ⌘ cmd.md>)
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that creates a rollback checkpoint
    * to be triggered by the [`REEL` 🎣 command](<../REEL 🎣/🎣 REEL ⌘ cmd.md>)
    * or by the [`Handled@Talker` 🅰️ method](<../../../../35 💬 Chats/Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>)
    * while allowing the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) flow to continue.

    ---
    <br/>


1. **What's the HOOK syntax?**

    
    ```yaml
    # One-line
    - HOOK|$hook

    # Comprehensive
    - HOOK >> $response:
        Hook: $hook
    ```

    | Input| Purpose
    |-|-
    | `Hook`   | For [`REEL` 🎣](<../REEL 🎣/🎣 REEL ⌘ cmd.md>) and [`Handled@Talker` 🅰️](<../../../../35 💬 Chats/Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>)
    | `$response` | Response from [`REEL` 🎣](<../REEL 🎣/🎣 REEL ⌘ cmd.md>) or [`Handled@Talker` 🅰️](<../../../../35 💬 Chats/Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>)

    
    ---
    <br/>
