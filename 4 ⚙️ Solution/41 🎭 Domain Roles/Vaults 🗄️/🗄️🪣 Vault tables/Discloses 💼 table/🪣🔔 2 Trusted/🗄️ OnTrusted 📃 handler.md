# 🗄️ Disclose.OnTrusted 📃 handler

> About
* Part of the [Vault 🗄️ domain](<../../../🗄️ Vault/🗄️🎭 Vault role.md>) role
* Part of the [`Vault.Discloses` 🪣 table](<../🪣 Discloses/🗄️ Vault.Discloses 🪣 table.md>)
<br/>

## Diagram

![alt text](<🗄️ OnTrusted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTrusted:

# Assert the Disclose
- ASSERT $Disclose:
    AllOf: Consumer, Query, Bind.Schema
    Texts: Consumer, Bind.Schema
    UUIDs: Query

# Get the query context
- SEND >> $context:
    Header:
        To: $Disclose.Consumer
        Subject: Queried@Consumer
    Body:
        Query: $Disclose.Query
        Schema: $Disclose.Bind.Schema

# Save the data for collection
- SAVE $Disclose:
    .State: DETAILED
    Context: $context
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`ASYNC`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`WAIT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Discloses`](<../🪣 Discloses/🗄️ Vault.Discloses 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Now`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>) [`.Add`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Queried@Consumer` 🚀 call](<../../../../Consumers 💼/💼📨 Consumer msgs/Queried 🗄️🚀💼/💼 Queried 🚀 call.md>)