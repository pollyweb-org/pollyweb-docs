# 🗄️📃 Bound script

> Part of the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>)

> Purpose

* [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Bound@Vault` 🅰️ method](<🤵🐌🗄️ Bound.md>).

> Called by 

* Called by the [`BIND` 🔗 command](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...methods 🤵/BIND 🔗/BIND 🔗 msg.md>)
* which then calls the [`Bindable@Broker` 🅰️ method](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>) 


<br/>

## Handler


```yaml
# Verify the domain signature
- VERIFY|$.Msg

# Resolve the callback
- GET|Hooks@Talker|$.Msg.Hook >> $hook

# Confirm it's the same Broker
- ASSERT:
    $.Msg.From: $hook.Broker

# Process each Bind
- PARALLEL|$.Msg.Binds|$bind:

    # Save each Bind
    - SAVE|Binds@Vault:
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
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) |  [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) [`PARALLEL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/PARALLEL *️⃣/PARALLEL *️⃣.md>) [`REEL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/REEL 🎣/REEL 🎣.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Hooks@Table`](<../../../../35 💬 Chats/😃 Talkers/😃🪣 Talker tables/😃🪣 Hooks 🪝 table.md>) [`Binds@Broker`](<../../🗄️🪣 Vault tables/🗄️🪣 Binds.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>)
|


<br/>
