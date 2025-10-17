<!-- TODO: detail -->
# 🔐 Talker `VERIFY` command

> Part of [Talker 😃](<../😃 Talker.md>)

<br/>

1. **What is a VERIFY message command?**

    A `VERIFY`
    * is a [Command ⌘](<../😃⚙️ Talker cmds/⌘ Command.md>) 
    * that checks if a given content was signed by the sender.

    ---
    <br/>

1. **What type of content can be verified?**

    | Type | Sender | Verification
    |-|-|-
    | [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [Domain 👥](<../../../40 👥 Domains/👥 Domain.md>) | Was a [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) signed by the [domain 👥](<../../../40 👥 Domains/👥 Domain.md>)?
    |  | [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) | Was a [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) signed by the [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)?
    | [File 📄](<../../../30 🧩 Data/Files 📄/📄 File.md>) |  [Domain 👥](<../../../40 👥 Domains/👥 Domain.md>) | Was a [File 📄](<../../../30 🧩 Data/Files 📄/📄 File.md>) signed by the [domain 👥](<../../../40 👥 Domains/👥 Domain.md>)?
    |  | [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) | Was a [File 📄](<../../../30 🧩 Data/Files 📄/📄 File.md>) signed by the [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)?

    ---
    <br/>

1. **How to verify a message from a domain?**

    Here's a [Talker 😃](<../😃 Talker.md>) that verifies a [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) from a [domain 👥](<../../../40 👥 Domains/👥 Domain.md>).
    
    ```yaml
    # Verify the Message.
    - VERIFY|$.Msg
    ```

    It calls [`PublicKey@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Public Key.md>) with the `From` in the [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>).


    ---
    <br/>

1. **How to verify a message from a Wallet?**

    Here's a [Talker 😃](<../😃 Talker.md>) excerpt from [Pop Vault @ Broker](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🔆 Broker locators/🤵🔆 Pop Vault.md>).

    ```yaml
    # Get the WalletID from the message
    - EVAL|$.Msg.Header.From >> $walletID

    # Get the Wallet item 🧑‍🦰
    - MAP|Wallets|$walletID >> $wallet

    # Verify the Message.
    - VERIFY|$.Msg|$wallet.PublicKey
    ```

    | [Command ⌘](<../😃⚙️ Talker cmds/⌘ Command.md>) | Purpose
    |-|-
    | ⬇️ [`EVAL`](<../😃💾 Talker data/EVAL ⬇️ flow.md>) | To get the Wallet ID from the [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>).
    | 🪣 [`MAP`](<../😃💾 Talker data/MAP 🪣 item.md>) | To get the Public Key of the Wallet item.

    ---
    <br/>
