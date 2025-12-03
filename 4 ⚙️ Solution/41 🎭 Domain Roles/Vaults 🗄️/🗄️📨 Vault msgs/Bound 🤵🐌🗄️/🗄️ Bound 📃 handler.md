# 🗄️📃 Bound script

> Part of the [Vault 🗄️ domain](<../../🗄️ Vault/🗄️🎭 Vault role.md>)

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Bound@Vault` 📨 msg](<🗄️ Bound 🐌 msg.md>).
* Returns a confirmation to the [`BIND` 📃 script](<../../🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND 📃 script.md>).


<br/>

## Flow

![alt text](<🗄️ Bound ⚙️ uml.png>)

<br/>

## Handler

```yaml
📃 Bound@Vault:

# Verify the domain signature
- VERIFY|$.Msg

# Assert the message
- ASSERT|$.Msg:
    AllOf: Bind, Answer
    Answer.IsIn: ACCEPTED, DECLINED

# Get the Bind
- READ >> $bind:
    Set: Vault.Binds
    Key: $.Msg.Bind
    Assert: 
        Broker: $.Msg.From
        .State: OFFERED

# Save the Bind
- CASE|$.Msg.Answer:
    ACCEPTED: 
        SAVE|$bind:
            .State: BOUND
    DECLINED:
        SAVE|$bind:
            .State: DECLINED
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)  [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Binds`](<../../🗄️🪣 Vault tables/Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|


<br/>
