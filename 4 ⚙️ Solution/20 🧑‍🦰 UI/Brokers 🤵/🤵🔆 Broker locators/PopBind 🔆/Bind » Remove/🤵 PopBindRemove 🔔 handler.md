# 🤵 OnPopRemoveBind 🔔 handler

> About
* Part of the [`Broker.Pops` 🪣 table](<../../../🤵🪣 Broker tables/Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
* Called by the [`Pop@Broker` 📃 script](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 handler.md>)
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Unbind Vault` 💬 flow](<../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/Unbind 💬🗄️🤵 /🧑‍🦰 Unbind Vault ⏩ flow.md>) 


<br/>


## Script


```yaml
📃 PopBind.RemoveBind:

# Verify the inputs
- ASSERT|$bind

# Ask for confirmation 🤔
- CONFIRM: Unbind ´{$bind.Title}´? This action cannot be undone.

# Remove the bind
- SAVE|$bind:
    .State: REMOVED

# Inform the user 🤔
- DONE|Done.
- GOODBYE
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>)  [`DONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`GOODBYE`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds`](<../../../🤵🪣 Broker tables/Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>)