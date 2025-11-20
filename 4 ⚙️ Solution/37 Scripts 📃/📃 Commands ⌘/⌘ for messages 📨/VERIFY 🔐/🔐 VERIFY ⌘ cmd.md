# 🔐 Talker `VERIFY` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

<br/>

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

    ---
    <br/>

1. **What's the syntax of VERIFY?**

    ```yaml
    # For messages from domains
    VERIFY|$.Msg
    ```

    | Input| Purpose |
    |-|-
    | `$.Msg`| Built-in [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>).

    ```yaml
    # For messages from Wallets
    VERIFY|$.Msg:
        Key: $publicKey

    # One-liner version
    VERIFY|$.Msg|$publicKey
    ```

    | Input| Purpose |
    |-|-
    | `$publicKey`| [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the Public Key.


    ---
    <br/>

1. **How to verify a message from a domain?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that verifies a [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) from a [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>).
    
    ```yaml
    📃 Verify the Message:
    - VERIFY|$.Msg
    ```

    It calls [`PublicKey@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Public Key/🕸 Public Key 🚀 call.md>) with the `From` in the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>).


    ---
    <br/>



1. **How do Brokers verify a message from a Wallet?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) excerpt from [Pop Vault @ Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Pops 🍿 table/🪣🔔 3 Remove Bind/🤵 Remove Bind 📃 script.md>).

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

    | [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | 🧲 [`READ`](<../../⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | Get the Public Key of the [Wallet 🪣](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) in the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>).

    ---
    <br/>



1. **How do Hosts verify a message from a Wallet?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    
    # Get the Chat item 
    - READ >> $chat
        Set: Host.Chats
        Key: $.Msg.Body.Chat

    # Verify the Message.
    - VERIFY|$.Msg:
        Key: $chat.PublicKey
    ```

    | [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | 🧲 [`READ`](<../../⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | To get the Public Key of [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>).

    ---
    <br/>

