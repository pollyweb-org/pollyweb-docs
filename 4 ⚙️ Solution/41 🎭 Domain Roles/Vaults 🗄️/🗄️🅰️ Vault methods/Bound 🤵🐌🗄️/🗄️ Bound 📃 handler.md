# 🗄️📃 Bound script

> Part of the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>)

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Script 📃/📃 Script.md>) that implements the [`Bound@Vault` 🅰️ method](<🗄️ Bound 🐌 msg.md>).

> Called by 

* Called by the [`BIND` 🔗 command](<../../../../35 💬 Chats/Scripts 📃/📃 for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>)
* which then calls the [`Bindable@Broker` 🅰️ method](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>) 


<br/>

## Flow

![alt text](<🗄️ Bound ⚙️ uml.png>)

## Handler


```yaml
# Verify the domain signature
- VERIFY|$.Msg

# Resolve the callback
- GET >> $hook:
    Set: TalkerHooks
    Key: $.Msg.Hook

# Confirm it's the same Broker
- ASSERT|$.Msg:
    From: $hook.Broker

# Process each Bind
- PARALLEL|$.Msg.Binds|$bind:

    # Save each Bind
    - SAVE|VaultBinds:
        Broker: $.Msg.From
        Bind: $bind.Bind
        Schema: $bind.Schema
        User: $hook.User

# Continue the Chat
- REEL|$hook:
    $.Msg.Binds
```



Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Command ⌘/⌘ Command.md>) |  [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/...holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 for datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`PARALLEL`](<../../../../35 💬 Chats/Scripts 📃/📃 for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`REEL`](<../../../../35 💬 Chats/Scripts 📃/📃 for control ▶️/REEL 🎣/🎣 REEL ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Hooks@Table`](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃🪣 TalkerHooks 🪝 table.md>) [`Binds@Broker`](<../../🗄️🪣 Vault tables/Binds 🔗 table/🗄️ VaultBinds 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/...holders 🧠/$Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/...holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|


<br/>
