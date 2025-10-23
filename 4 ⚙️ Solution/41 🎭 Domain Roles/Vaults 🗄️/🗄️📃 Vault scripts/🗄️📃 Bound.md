# 🗄️📃 Bound script

> [Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements the [`Bound@Vault` 🅰️ method](<../🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>).

<br/>

## Handler

> Called by the [`BIND` 🔗 command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/BIND 🔗 msg.md>)

> Then called by the [`Bindable@Broker` 🅰️ method](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>) 

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
| [Commands ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) |  [`ASSERT`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets/GET ⏬ item.md>) [`PARALLEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/PARALLEL *️⃣.md>) [`REEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>) [`VERIFY`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>)
| [Datasets 🪣](<../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Hooks@Table`](<../../../35 💬 Chats/😃 Talkers/😃🪣 Talker tables/😃🪣 Hooks 🪝.md>) [`Binds@Broker`](<../🗄️🪣 Vault tables/🗄️🪣 Binds.md>)
| [Placeholders 🧠](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders/$Placeholder 🧠.md>) | [`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>)
|


<br/>
