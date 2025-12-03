# 🗄️ Disclose@Vault 📃 handler

> About
* Part of the [Vault 🗄️ domain](<../../🗄️ Vault/🗄️🎭 Vault role.md>)
* Implements the [`Disclose@Vault` 📨 msg](<🗄️ Disclose 🐌 msg.md>)

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
    AllOf: Bind, Chat, Hook, Language, Consumer
    UUIDs: Bind, Chat, Hook
    Texts: Language, Consumer

# Read the referenced Bind
- READ >> $bind:
    Set: Vault.Binds
    Key: $.Msg.Bind
    Assert:
        Broker: $.Msg.From
        .State: BOUND

# Create the collect
- SAVE|Vault.Shares:
    .State: ASKED
    Broker: $.Msg.From
    Bind: $.Msg.Bind
    Chat: $.Msg.Chat
    Hook: $.Msg.Hook
    Language: $.Msg.Language
    Consumer: $.Msg.Consumer
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |[`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE 📃 script.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Binds`](<../../🗄️🪣 Vault tables/Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>) [`Vault.Shares`](<../../🗄️🪣 Vault tables/Shares 💼 table/🪣 Shares/🗄️ Vault.Shares 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|