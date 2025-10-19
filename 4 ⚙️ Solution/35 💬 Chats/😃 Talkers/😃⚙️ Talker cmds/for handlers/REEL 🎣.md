# 🎣 Talker `REEL` command

> Part of [Talker 😃](<../../😃 Talker.md>)

<!-- TODO: examples -->
> Used in [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)

<br/>

1. **What's the REEL command?**

    A `REEL`
    * is a handler [Command ⌘](<../for control/⌘ Command.md>) 
    * for [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) handlers to unblock a pending [Talker 😃](<../../😃 Talker.md>).
  
    ---
    <br/>

1. **What's the syntax of REEL for Synchronous Requests?**

    ```yaml
    REEL:
      {response}
    ```
    
    | Argument| Purpose |
    |-|-
    | `{response}` | Response for the [Synchronous Request 🚀](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Request Sync 🚀.md>)

    ---
    <br/>

1. **What's the syntax of REEL for Async Messages?**
   
    ```yaml
    REEL|$hook:
      {response}
    ```

    | Argument| Purpose |
    |-|-
    | `$hook`| [Hooks 🪣 item](<../../😃🪣 Talker tables/😃🪣 Hooks 🪝.md>) saved by the [Command ⌘](<../for control/⌘ Command.md>) | -
    | `{response}` | [Command ⌘](<../for control/⌘ Command.md>) output to a [Placeholder 🧠](<../for data/$Placeholder 🧠.md>)

    ---
    <br/>

1. **What's an example of REEL?**

    Consider the [`BIND` flow command](<../for flows/BIND 🔗 msg.md>).

    ![alt text](<../../.📎 Assets/Reel.png>)

    <br/>

    Here's the [Talker 😃](<../../😃 Talker.md>)

    ```yaml
    # Talker 😃
    - BIND|.BIND >> $bound
    - IF|$bound:
        Then: SUCCESS|Your wallet is bound.
        Else: FAILURE|Not bounded.
    ```


    | [Command ⌘](<../for control/⌘ Command.md>) | Purpose
    |-|-
    | 🔗 [`BIND`](<../for flows/BIND 🔗 msg.md>) | To [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) a user. 
    | ⤵️ [`IF`](<../for control/IF ⤵️.md>) | To verify the result.
    | 
    
    <br/>

    Here's the handler of [`Bound@Broker`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)


    ```yaml
    # Handler
    - GET|Hooks@Talker|$.Msg.Hook >> $hook
    - REEL|$hook
    ```

    | [Command ⌘](<../for control/⌘ Command.md>) | Purpose
    |-|-
    | ⏬ [`GET`](<../for data/GET ⏬ item.md>) | Get the [Hook 🪣](<../../😃🪣 Talker tables/😃🪣 Hooks 🪝.md>) from [`Bindable@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)  
    

    ---
    <br/>
