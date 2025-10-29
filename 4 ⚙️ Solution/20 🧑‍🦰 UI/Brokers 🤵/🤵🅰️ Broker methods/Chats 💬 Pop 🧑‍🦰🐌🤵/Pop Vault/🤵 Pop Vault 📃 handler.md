<!-- TODO: Add lists of commands. -->
<!-- TODO: Add initial parser. -->

# 🤵📃 Pop Vault 🗄️

> [Script 📃](<../../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Unbind Vault` 💬 flow](<../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/Unbind 💬🗄️🤵 /🧑‍🦰 Unbind Vault ⏩ flow.md>) 

> Called by the [`Pop@Broker` 📃 script](<../🤵 Pop 📃 handler.md>)


<br/>

<!-- TODO: separate the Unbind Vault script -->

## Script

> Requires a `$:Wallet` holder from the [`Pop@Broker` 📃 script](<../🤵 Pop 📃 handler.md>)

<!-- TODO: change the ASSERT -->
```yaml
📃 PopVault:

# Verify the inputs
- ASSERT|.Inputs
    AllOf: Wallet

# Get the Vault 
- GET >> $vault:
    Set: $:Wallet.Vaults
    Key: $.Msg.Body.Key

# Ask for confirmation 🤔
- CONFIRM|Unbind vault {$vault.Title}?

# Filter the binds.
- FILTER|Which ones? >> $binds:
    Options: $vault.Binds
    ID: Bind
    Title: Schema$

# Remove each bind
- PARALLEL|$vault.Binds|$bind:

    # Delete the Bind
    - DELETE|$bind
    
    # Inform the Vault
    - SEND:
        Header:
            To: $bind.Vault
            Subject: Unbound@Vault
        Body:
            Bind: $bind.ID

# Update the bind list
- SEND:
    Header:
        To: $:Wallet.Notifier
        Subject: Updated@Notifier
    Body:
        Wallet: $:Wallet.ID
        Updates: [ BINDS ]

# Inform the user 🤔
- SUCCESS|Done.
```

Needs||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CONFIRM`](<../../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`FILTER`](<../../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...methods 🤵/FILTER 🔽/🔽 FILTER ⌘ cmd.md>) [`GET`](<../../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>)  [`PARALLEL`](<../../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SEND`](<../../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`SUCCESS`](<../../../../../35 💬 Chats/Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Hook` 🪣](<../../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃🪣 TalkerHooks 🪝 table.md>) from [`Bindable@Broker`](<../../Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)  
| [Holders 🧠](<../../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/$Holder 🧠.md>) | [`$.Msg`](<../../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>) 
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Update@Notifier` 🅰️ method](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|
