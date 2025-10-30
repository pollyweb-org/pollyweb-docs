# 😃🧘 Talker `HOOK` flow 

> Part of [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>)

> Used by
* [`Async` ⏩ flow](<../../../Talkers 😃/😃⏩ Talker flows/Async Tasks 😃⏩📦/😃 Async ⏩ flow.md>)

<br/>

## FAQ

1. **What's a HOOK flow command?**

    A [`HOOK` 🪝](<🪝 HOOK ⌘ cmd.md>)
    * is a flow [Command ⌘](<../../📃 basics/⌘ Command.md>) 
    * that creates a rollback checkpoint
    * to be triggered by the [`REEL` 🎣 command](<../REEL 🎣/🎣 REEL ⌘ cmd.md>)
    * or by the [`Handled@Talker` 🅰️ method](<../../../Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>)
    * while allowing the [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>) flow to continue.

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
    | `Hook`   | For [`REEL` 🎣](<../REEL 🎣/🎣 REEL ⌘ cmd.md>) and [`Handled@Talker` 🅰️](<../../../Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>)
    | `$response` | Response from [`REEL` 🎣](<../REEL 🎣/🎣 REEL ⌘ cmd.md>) or [`Handled@Talker` 🅰️](<../../../Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>)

    
    ---
    <br/>
