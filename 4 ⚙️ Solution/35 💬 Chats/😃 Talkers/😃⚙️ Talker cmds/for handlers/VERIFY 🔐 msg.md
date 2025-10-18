<!-- TODO: detail -->
# 🔐 Talker `VERIFY` command

> Part of [Talker 😃](<../../😃 Talker.md>)

<br/>

1. **What is a VERIFY message command?**

    A `VERIFY`
    * is a [Command ⌘](<../for control/⌘ Command.md>) 
    * that checks if a given content was signed by the sender.

    ---
    <br/>

1. **What type of content can be verified?**

    | Type | Sender | Verification
    |-|-|-
    | [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [Domain 👥](<../../../../40 👥 Domains/👥 Domain.md>) | Was a [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) signed by the [domain 👥](<../../../../40 👥 Domains/👥 Domain.md>)?
    |  | [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) | Was a [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) signed by the [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)?
    | [File 📄](<../../../../30 🧩 Data/Files 📄/📄 File.md>) |  [Domain 👥](<../../../../40 👥 Domains/👥 Domain.md>) | Was a [File 📄](<../../../../30 🧩 Data/Files 📄/📄 File.md>) signed by the [domain 👥](<../../../../40 👥 Domains/👥 Domain.md>)?
    |  | [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) | Was a [File 📄](<../../../../30 🧩 Data/Files 📄/📄 File.md>) signed by the [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)?

    ---
    <br/>

1. **How to verify a message from a domain?**

    Here's a [Talker 😃](<../../😃 Talker.md>) that verifies a [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) from a [domain 👥](<../../../../40 👥 Domains/👥 Domain.md>).
    
    ```yaml
    # Verify the Message.
    - VERIFY|$.Msg
    ```

    It calls [`PublicKey@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Public Key.md>) with the `From` in the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>).


    ---
    <br/>

1. **How to verify a message from a Wallet?**

    Here's a [Talker 😃](<../../😃 Talker.md>) excerpt from [Pop Vault @ Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🔆 Broker locators/🤵🔆 Pop Vault.md>).

    ```yaml
    # Get the WalletID from the message
    - EVAL|$.Msg.Header.From >> $wallet

    # Get the Wallet item 🧑‍🦰
    - GET|Wallets|$wallet >> $wallet

    # Verify the Message.
    - VERIFY|$.Msg|$wallet.PublicKey
    ```

    | [Command ⌘](<../for control/⌘ Command.md>) | Purpose
    |-|-
    | ⬇️ [`EVAL`](<../for data/EVAL ⬇️ flow.md>) | To get the Wallet ID from the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>).
    | 🗺️ [`GET`](<../for data/GET 🗺️ item.md>) | To get the Public Key of the Wallet item.

    ---
    <br/>
