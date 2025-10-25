# 🎣 Talker `REEL` command

> Part of [Talker 😃](<../../../😃 Talker role.md>)

<!-- TODO: examples -->
> Used in [`Bound@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)

<br/>

1. **What's the REEL command?**

    A `REEL`
    * is a handler [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) 
    * for [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) handlers to unblock a pending [Talker 😃](<../../../😃 Talker role.md>).
  
    ---
    <br/>

1. **What's the syntax of REEL for Synchronous Requests?**

    ```yaml
    REEL|<http-code>:
      {response}
    ```
    
    | Argument| Purpose |
    |-|-
    | `<http-code>`| Defaults to `200` if omitted
    | `{response}` | Response for the [Synchronous Request 🚀](<../../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Sync Requests 🚀.md>)

    ---
    <br/>

1. **What's the syntax of REEL for Async Messages?**
   
    ```yaml
    REEL|$hook:
      {response}
    ```

    | Argument| Purpose |
    |-|-
    | `$hook`| [Hooks 🪣 item](<../../../😃🪣 Talker tables/😃🪣 Hooks 🪝 table.md>) saved by the [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) | -
    | `{response}` | [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) output to a [Placeholder 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>)

    ---
    <br/>

1. **What's an example of REEL?**

    Consider the [`BIND` flow command](<../../...methods 🤵/BIND 🔗/BIND 🔗 msg.md>).

    ![alt text](<.📎 Assets/Reel.png>)

    <br/>

    Here's the [Talker 😃](<../../../😃 Talker role.md>)

    ```yaml
    # Talker 😃
    - BIND|.BIND >> $bound
    - IF|$bound:
        Then: SUCCESS|Your wallet is bound.
        Else: FAILURE|Not bounded.
    ```

    Commands: [`BIND`](<../../...methods 🤵/BIND 🔗/BIND 🔗 msg.md>) [`IF`](<../IF ⤵️/IF ⤵️.md>)
    
    <br/>

    Here's the handler of [`Bound@Broker`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)


    ```yaml
    # Handler
    - GET|Hooks@Talker|$.Msg.Hook >> $hook
    - REEL|$hook
    ```

    | [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) | Purpose
    |-|-
    | ⏬ [`GET`](<../../...datasets 🪣/GET/GET ⏬ item.md>) | Get the [`Hook` 🪣](<../../../😃🪣 Talker tables/😃🪣 Hooks 🪝 table.md>) from [`Bindable@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)  
    

    ---
    <br/>
