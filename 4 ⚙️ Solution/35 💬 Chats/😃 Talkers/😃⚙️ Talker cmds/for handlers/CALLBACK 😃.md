<!-- TODO: -->

# 🔐 Talker `CALLBACK` command

> Part of [Talker 😃](<../../😃 Talker.md>)


> Used in [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)

<br/>

1. **What's the syntax of CALLBACK?**

    ```yaml
    CALLBACK|$callback:
        {response}
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `$callback`|   | -
    | `{response}` |  | `{A:1, B:2}`
    
    
    ---
    <br/>

1. **What's an example of CALLBACK?**

    Consider the following flow.

    ![alt text](<../../.📎 Assets/Callback.png>)

    <br/>

    Here's the [Talker 😃](<../../😃 Talker.md>)

    ```yaml
    # Talker 😃
    - BIND|.BIND >> $bound
    - IF|$bound:
        Then: SUCCESS|Your wallet is bound.
        Else: FAILURE|Not bounded.
    ```


    | [Command ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
    |-|-
    | 🔗 [`BIND`](<../for flows/BIND 🔗 msg.md>) | To [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) a user. 
    | ⤵️ [`IF`](<../for control/IF ⤵️.md>) | To verify the result.
    | 
    
    <br/>

    Here's the handler of [`Bound@Broker`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)


    ```yaml
    # Handler
    - GET|Callbacks|$.Msg.Callback >> $callback
    - CALLBACK|$callback
    ```

    | [Command ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
    |-|-
    | 🗺️ [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET 🗺️ item.md>) | Get the [Callback 🪣](<../../😃🪣 Talker tables/😃🪣 Callbacks.md>) from [`Bindable@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)  
    

    ---
    <br/>
