<!-- TODO: detail -->
# 🔐 Talker `VERIFY` command

> Part of [Talker 😃](<../../../😃 Talker role.md>)

<br/>

1. **What is a VERIFY message command?**

    A [`VERIFY`](<🔐 VERIFY ⌘ cmd.md>)
    * is a [Command ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) 
    * that checks if a given content was signed by the sender.

    ---
    <br/>

1. **What type of content can be verified?**

    | Type | Sender | Verification
    |-|-|-
    | [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [Domain 👥](<../../../../../40 👥 Domains/👥 Domain.md>) | Was a [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) signed by the [domain 👥](<../../../../../40 👥 Domains/👥 Domain.md>)?
    |  | [Wallet 🧑‍🦰](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) | Was a [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) signed by the [Wallet 🧑‍🦰](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)?
    | [File 📄](<../../../../../30 🧩 Data/Files 📄/📄 File.md>) |  [Domain 👥](<../../../../../40 👥 Domains/👥 Domain.md>) | Was a [File 📄](<../../../../../30 🧩 Data/Files 📄/📄 File.md>) signed by the [domain 👥](<../../../../../40 👥 Domains/👥 Domain.md>)?
    |  | [Wallet 🧑‍🦰](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) | Was a [File 📄](<../../../../../30 🧩 Data/Files 📄/📄 File.md>) signed by the [Wallet 🧑‍🦰](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)?

    ---
    <br/>

1. **What's the syntax of VERIFY?**

    ```yaml
    # For messages from domains
    VERIFY|$.Msg
    ```

    | Argument| Purpose |
    |-|-
    | `$.Msg`| Built-in [Placeholder 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) with the [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>).

    ```yaml
    # For messages from Wallets
    VERIFY|$.Msg:
        Key: $publicKey

    # One-liner version
    VERIFY|$.Msg|$publicKey
    ```

    | Argument| Purpose |
    |-|-
    | `$publicKey`| [Placeholder 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) with the Public Key.


    ---
    <br/>

1. **How to verify a message from a domain?**

    Here's a [Talker 😃](<../../../😃 Talker role.md>) that verifies a [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) from a [domain 👥](<../../../../../40 👥 Domains/👥 Domain.md>).
    
    ```yaml
    # Verify the Message.
    - VERIFY|$.Msg
    ```

    It calls [`PublicKey@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Public Key.md>) with the `From` in the [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>).


    ---
    <br/>



1. **How do Brokers verify a message from a Wallet?**

    Here's a [Talker 😃](<../../../😃 Talker role.md>) excerpt from [Pop Vault @ Broker](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Pop 🧑‍🦰🐌🤵/🤵 Pop Vault 📃 script.md>).

    ```yaml
    # Get the WalletID from the message 
    - GET >> $wallet:
        Set: BrokerWallets
        Key: $.Msg.Header.From

    # Verify the Message.
    - VERIFY|$.Msg:
        Key: $wallet.PublicKey
    ```

    | [Command ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) | Purpose
    |-|-
    | ⏬ [`GET`](<../../...datasets 🪣/GET ⏬/⏬ GET ⌘ cmd.md>) | Get the Public Key of the [Wallet 🪣](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>) in the [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>).

    ---
    <br/>



1. **How do Hosts verify a message from a Wallet?**

    Here's a [Talker 😃](<../../../😃 Talker role.md>).

    ```yaml
    # Get the Chat item 
    - GET >> $chat
        Set: HostChats
        Key: $.Msg.Body.Chat

    # Verify the Message.
    - VERIFY|$.Msg:
        Key: $chat.PublicKey
    ```

    | [Command ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) | Purpose
    |-|-
    | ⏬ [`GET`](<../../...datasets 🪣/GET ⏬/⏬ GET ⌘ cmd.md>) | To get the Public Key of [`Hello@Host`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>).

    ---
    <br/>

