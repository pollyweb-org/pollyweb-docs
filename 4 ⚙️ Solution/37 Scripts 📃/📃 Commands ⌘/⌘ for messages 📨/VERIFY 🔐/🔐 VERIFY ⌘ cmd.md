# 🔐 Talker `VERIFY` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ

1. **What is a VERIFY message command?**

    A [`VERIFY`](<🔐 VERIFY ⌘ cmd.md>)
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that checks if a given content was signed by the sender.

    ---
    <br/>

1. **What type of content can be verified?**

    | Type | Sender | Verification
    |-|-|-
    | [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [Domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | Was a [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) signed by the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)?
    |  | [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | Was a [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) signed by the [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)?
    | [File 📄](<../../../../30 🧩 Data/Files 📄/📄 File.md>) |  [Domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | Was a [File 📄](<../../../../30 🧩 Data/Files 📄/📄 File.md>) signed by the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)?
    |  | [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | Was a [File 📄](<../../../../30 🧩 Data/Files 📄/📄 File.md>) signed by the [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)?
    |[Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) | [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | Was a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) signed by the [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)?
    ||| and does it comply with the [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)

    ---
    <br/>

1. **What's the syntax for messages from domains?**

    ```yaml
    VERIFY|$.Msg
    ```

    | Input| Purpose |
    |-|-
    | `$.Msg`| Built-in [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>).

    ---
    <br/>


1. **How to verify a message from a domain?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that verifies a [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) from a [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>).
    
    ```yaml
    📃 Verify the Message:
    - VERIFY|$.Msg
    ```

    It calls [`PublicKey@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Public Key/🕸 Public Key 🚀 call.md>) with the `From` in the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>).


    ---
    <br/>


1. **What's the syntax for messages from [Wallet 🧑‍🦰 apps](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)?**

    ```yaml
    - VERIFY|$.Msg:
        Key: $publicKey

    # One-liner version
    - VERIFY|$.Msg|$publicKey
    ```

    | Input| Purpose |
    |-|-
    | `$publicKey`| [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the Public Key.


    ---
    <br/>

1. **How do [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) verify a message from a [Wallet 🧑‍🦰 app](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) excerpt from [Pop Vault @ Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Pops 🎈 table/🪣🧱 52 Bind » Remove 🔔/🤵 OnPopRemoveBind 🔔 handler.md>).

    ```yaml
    📃 Example:

    # Get the WalletID from the message 
    - READ >> $wallet:
        Set: Broker.Wallets
        Key: $.Msg.Header.From

    # Verify the Message.
    - VERIFY|$.Msg:
        Key: $wallet.PublicKey
    ```
    Uses: [`$.Msg`](<../../../📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`READ`](<../../⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<🔐 VERIFY ⌘ cmd.md>)

    ---
    <br/>



1. **How do [Host 🤗 domains](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) verify a message from a [Wallet 🧑‍🦰 app](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    
    # Get the Chat item 
    - READ >> $chat:
        Set: Host.Chats
        Key: 
            Broker: $.Msg.Broker
            Chat: $.Msg.Chat

    # Verify the Message.
    - VERIFY|$.Msg:
        Key: $chat.PublicKey
    ```
    Uses: [`$.Msg`](<../../../📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`READ`](<../../⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<🔐 VERIFY ⌘ cmd.md>)


    ---
    <br/>


1. **What's the syntax for [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)?**

    ```yaml
    # Blocker version (raises error if invalid)
    - VERIFY|$token 
    
    # Safe version (stores result in $isValid)
    - VERIFY|$token >> $isValid
    ```

    | Input| Purpose |
    |-|-
    | `$token`| [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
    | `$isValid`| [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) that will store `true`/`false`.


    ---
    <br/>