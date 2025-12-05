# 🗄️ Disclose@Vault 📃 handler

> About
* Part of the [Vault 🗄️ domain](<../../🗄️ Vault/🗄️🎭 Vault role.md>)
* Implements the [`Disclose@Vault` 🐌 msg](<🗄️ Disclose 🐌 msg.md>)

<br/>

## Diagram

![alt text](<🗄️ Disclose ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Disclose@Vault:

# Verify the signature
- VERIFY|$.Msg

# Assert the message
- ASSERT|$.Msg:
    AllOf: Bind, Chat, Query, Language, Consumer
    UUIDs: Bind, Chat, Query
    Consumer.IsDomain:
    Language.IsLanguage:

# Read the referenced Bind
- READ >> $bind:
    Set: Vault.Binds
    Key: $.Msg.Bind
    Assert:
        Broker: $.Msg.From
        .State: BOUND

# Create the collect
- SAVE|Vault.Discloses:
    .State: ASKED
    Bind: $.Msg.Bind
    Chat: $.Msg.Chat
    Query: $.Msg.Query
    Broker: $.Msg.From
    Language: $.Msg.Language
    Consumer: $.Msg.Consumer
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |[`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE 📃 script.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Binds`](<../../🗄️🪣 Vault tables/Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>) [`Vault.Discloses`](<../../🗄️🪣 Vault tables/Discloses 💼 table/🪣 Discloses/🗄️ Vault.Discloses 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsDomain`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsLanguage`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsLanguage ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|