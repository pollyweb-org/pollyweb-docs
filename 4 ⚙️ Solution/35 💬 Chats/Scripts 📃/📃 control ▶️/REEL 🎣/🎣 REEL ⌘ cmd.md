<!-- TODO:
In the internal .REEL implementation, 
clarify that the REEL always exists the script where the $.Script was invoked.
If the are 10 lines in the script and the $.Script is in the 7th, 
then the last 3 will never be executed because REEL will exit the script.
-->

# 🎣 Talker `REEL` command

> Part of [Script 📃](<../../📃 basics/Script 📃.md>)

<!-- TODO: examples -->
> Used in [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)

<br/>

1. **What's the REEL command?**

    A `REEL`
    * is a handler [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * for [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) handlers to unblock a pending [Script 📃](<../../📃 basics/Script 📃.md>).
  
    ---
    <br/>

1. **What's the syntax of REEL for Synchronous Requests?**

    ```yaml
    REEL|<http-code>:
      {response}
    ```
    
    | Input| Purpose |
    |-|-
    | `<http-code>`| Defaults to `200` if omitted
    | `{response}` | Response for the [Synchronous Request 🚀](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Sync Requests 🚀.md>)

    ---
    <br/>

1. **What's the syntax of REEL for Async Messages?**
   
    ```yaml
    REEL|$hook:
      {response}
    ```

    | Input| Purpose |
    |-|-
    | `$hook`| [Hooks 🪣 item](<../../../Talkers 😃/😃🪣 Talker tables/😃🪣 TalkerHooks 🪝 table.md>) saved by the [Command ⌘](<../../📃 basics/Command ⌘.md>) | -
    | `{response}` | [Command ⌘](<../../📃 basics/Command ⌘.md>) output to a [Holder 🧠](<../../📃 basics/Holder 🧠.md>)

    ---
    <br/>

1. **What's an example of REEL?**

    Consider the [`BIND` flow command](<../../📃 methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>).

    ![alt text](<🎣 REEL ⚙️ uml.png>)

    <br/>

    Here's the [Script 📃](<../../📃 basics/Script 📃.md>)

    ```yaml
    📃 Example:
    - BIND|.BIND >> $bound
    - IF|$bound:
        Then: SUCCESS|Your wallet is bound.
        Else: FAILURE|Not bounded.
    ```

    Commands: [`BIND`](<../../📃 methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) [`IF`](<../IF ⤵️/⤵️ IF ⌘ cmd.md>)
    
    <br/>

    Here's the handler of [`Bound@Broker`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)


    ```yaml
    # Handler
    - GET >> $hook:
        Set: TalkerHooks
        Key: $.Msg.Hook
    - REEL|$hook
    ```

    | [Command ⌘](<../../📃 basics/Command ⌘.md>) | Purpose
    |-|-
    | 🧲 [`GET`](<../../📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) | Get the [`Hook` 🪣](<../../../Talkers 😃/😃🪣 Talker tables/😃🪣 TalkerHooks 🪝 table.md>) from [`Bindable@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)  
    

    ---
    <br/>
