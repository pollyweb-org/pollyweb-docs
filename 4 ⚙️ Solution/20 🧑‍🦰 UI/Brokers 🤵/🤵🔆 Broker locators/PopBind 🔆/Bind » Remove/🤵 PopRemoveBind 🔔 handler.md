# 🤵 OnPopRemoveBind 🔔 handler

> About
* Part of the [`Broker.Pops` 🪣 table](<../../../🤵🪣 Broker tables/Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
* Called by the [`Pop@Broker` 📃 script](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 handler.md>)
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Unbind Vault` 💬 flow](<../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/Unbind 💬🗄️🤵 /🧑‍🦰 Unbind Vault ⏩ flow.md>) 


<br/>

<!-- TODO: separate the Unbind Vault script -->

## Script


```yaml
📃 PopBind.RemoveBind:

# Verify the inputs
- ASSERT|$.Inputs:
    AllOf: Wallet

# Get the Vault 
- SELECT >> $vault:
    From: $Wallet.Vaults
    Where: Domain.Is($.Msg.Body.Key)

# Ask for confirmation 🤔
- CONFIRM: Unbind ´{$bind.Title}´?

# Remove the bind
- DELETE|$bind

# Inform the user 🤔
- DONE|Done.
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`ASK`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/ASK 🙋/🙋 ASK ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)  [`PARALLEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`DONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) 
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Update@Notifier`](<../../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|
