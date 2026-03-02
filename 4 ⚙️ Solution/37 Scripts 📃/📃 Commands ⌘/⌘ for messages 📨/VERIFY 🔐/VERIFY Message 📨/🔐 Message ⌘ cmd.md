# 🔐 Talker `VERIFY` Message 📨

> About
* Part of the [`VERIFY` ⌘ command](<../VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
* Implemented by the [`VERIFY-Message` 📃 script](<🔐 Message 📃 script.md>)

## FAQ


1. **What's the syntax for messages from domains?**

    ```yaml
    VERIFY $.Msg
    ```

    | Input| Purpose |
    |-|-
    | `$.Msg`| Built-in [Holder 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>).

    ---
    <br/>


1. **How to verify a message from a domain?**

    Here's a [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that verifies a [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) from a [domain 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>).
    
    ```yaml
    📃 Verify the Message:
    - VERIFY $.Msg
    ```

    It calls [`PublicKey@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Public Key/🕸 Public Key 🚀 call.md>) with the `From` in the [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>).


    ---
    <br/>


1. **What's the syntax for messages from [Wallet 🧑‍🦰 apps](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)?**

    ```yaml
    - VERIFY $.Msg:
        Key: $publicKey
    ```

    | Input| Purpose |
    |-|-
    | `$publicKey`| [Holder 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the Public Key.


    ---
    <br/>

1. **How do [Broker 🤵 domain](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) verify a message from a [Wallet 🧑‍🦰 app](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)?**

    Here's a [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) excerpt from [Pop Vault @ Broker](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵😃 Broker talkers/PopBind 🔗 talker/Bind » Remove/🤵 PopBindRemove 😃 handler.md>).

    ```yaml
    📃 Example:

    # Get the WalletID from the message 
    - READ >> $wallet:
        Set: Broker.Wallets
        Key: $.Msg.Header.From

    # Verify the Message.
    - VERIFY $.Msg:
        Key: $wallet.PublicKey
    ```
    Uses: [`$.Msg`](<../../../../📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`READ`](<../../../⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<🔐 Message ⌘ cmd.md>)

    ---
    <br/>



1. **How do [Host 🤗 domains](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) verify a message from a [Wallet 🧑‍🦰 app](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)?**

    Here's a [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    
    # Get the Chat item 
    - READ >> $chat:
        Set: Host.Chats
        Key: 
            Broker: $.Msg.Broker
            Chat: $.Msg.Chat

    # Verify the Message.
    - VERIFY $.Msg:
        Key: $chat.PublicKey
    ```
    Uses: [`$.Msg`](<../../../../📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`READ`](<../../../⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<🔐 Message ⌘ cmd.md>)


    ---
    <br/>

