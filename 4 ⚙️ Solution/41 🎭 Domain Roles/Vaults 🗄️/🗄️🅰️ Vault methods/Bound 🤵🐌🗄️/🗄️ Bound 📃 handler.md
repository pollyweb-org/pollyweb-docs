# 🗄️📃 Bound script

> Flow
* Part of the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>)

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Bound@Vault` 🅰️ method](<🗄️ Bound 🐌 msg.md>).

> Called by 

* Called by the [`BIND` 🔗 command](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>)
* which then calls the [`Bindable@Broker` 🅰️ method](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>) 



## Flow

![alt text](<🗄️ Bound ⚙️ uml.png>)

## Handler


```yaml
# Verify the domain signature
- VERIFY|$.Msg

# Resolve the callback
- READ >> $hook:
    Set: Talker.Hooks
    Key: $.Msg.Hook

# Confirm it's the same Broker
- ASSERT|$.Msg:
    From: $hook.Broker

# Save the Bind
- SAVE|Vault.Binds:
    Bind: $.Msg.Bind
    Broker: $hook.Broker
    Schema: $hook.Schema
    User: $hook.User

# Continue the Chat
- REEL|$hook:
    $.Msg.Bind
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)  [`REEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Talker.Hooks`](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Hooks 🪣 table.md>) [`Vault.Binds`](<../../🗄️🪣 Vault tables/Binds 🔗 table/🗄️ VaultBinds 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|


<br/>
