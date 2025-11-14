<!-- TODO:
In the internal .REEL implementation, 
clarify that the REEL always exists the script where the $.Script was invoked.
If the are 10 lines in the script and the $.Script is in the 7th, 
then the last 3 will never be executed because REEL will exit the script.
-->

# 🎣 Talker `REEL` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

<!-- TODO: examples -->
> Used in [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)

<br/>

1. **What's the REEL command?**

    A `REEL`
    * is a handler [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * for [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) handlers to unblock a pending [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
  
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
    | `$hook`| [Hooks 🪣 item](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Hooks 🪣 table.md>) saved by the [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | -
    | `{response}` | [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) output to a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

    ---
    <br/>

1. **What's an example of REEL?**

    Consider the [`BIND` flow command](<../../⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>).

    ![alt text](<🎣 REEL ⚙️ uml.png>)

    <br/>

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

    ```yaml
    📃 Example:
    - BIND|.BIND >> $bound
    - IF|$bound:
        Then: SUCCESS|Your wallet is bound.
        Else: FAILURE|Not bounded.
    ```

    Uses: [`BIND`](<../../⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) [`IF`](<../../⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>)
    
    <br/>

    Here's the handler of [`Bound@Broker`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)


    ```yaml
    # Handler
    - READ >> $hook:
        Set: Talker.Hooks
        Key: $.Msg.Hook
    - REEL|$hook
    ```

    | [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | 🧲 [`READ`](<../../⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | Get the [`Hook` 🪣](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Hooks 🪣 table.md>) from [`Bindable@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)  
    

    ---
    <br/>
