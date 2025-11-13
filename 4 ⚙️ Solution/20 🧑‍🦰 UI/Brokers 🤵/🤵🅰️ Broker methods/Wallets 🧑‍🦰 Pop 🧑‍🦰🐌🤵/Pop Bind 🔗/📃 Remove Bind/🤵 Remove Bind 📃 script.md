<!-- TODO: Add lists of commands. -->
<!-- TODO: Add initial parser. -->

# 🤵📃 Pop Vault 🗄️

> [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Unbind Vault` 💬 flow](<../../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/Unbind 💬🗄️🤵 /🧑‍🦰 Unbind Vault ⏩ flow.md>) 

> Called by the [`Pop@Broker` 📃 script](<../../🤵 Pop 📃 handler.md>)


<br/>

<!-- TODO: separate the Unbind Vault script -->

## Script

> Requires a `$:Wallet` holder from the [`Pop@Broker` 📃 script](<../../🤵 Pop 📃 handler.md>)

<!-- TODO: change the ASSERT -->
```yaml
📃 PopVault:

# Verify the inputs
- ASSERT|.Inputs
    AllOf: Wallet

# Get the Vault 
- SELECT >> $vault:
    From: $Wallet.Vaults
    Where: Domain.Is($.Msg.Body.Key)

# Ask for confirmation 🤔
- CONFIRM|Unbind vault {$vault.Title}?

# Filter the binds.
- ASK|Which ones? >> $binds:
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
        To: $Wallet.Notifier
        Subject: Updated@Notifier
    Body:
        Wallet: $Wallet.ID
        Updates: [ BINDS ]

# Inform the user 🤔
- SUCCESS|Done.
```

Uses||
|-|-
| [Commands ⌘](<../../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CONFIRM`](<../../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`ASK`](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/ASK 🙋/🙋 ASK ⌘ cmd.md>) [`READ`](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)  [`PARALLEL`](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SEND`](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`SUCCESS`](<../../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)
| [Holders 🧠](<../../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>) 
| [Messages 📨](<../../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Update@Notifier`](<../../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|
