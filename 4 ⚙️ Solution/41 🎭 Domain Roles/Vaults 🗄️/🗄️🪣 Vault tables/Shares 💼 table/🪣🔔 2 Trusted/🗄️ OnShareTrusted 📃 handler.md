# 🗄️ OnShareTrusted 📃 handler

> About
* Part of the [Vault 🗄️ domain](<../../../🗄️ Vault/🗄️🎭 Vault role.md>) role
* Part of the [`Vault.Shares` 🪣 table](<../🪣 Shares/🗄️ Vault.Shares 🪣 table.md>)

<br/>

## Diagram

![alt text](<🗄️ OnShareTrusted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnShareTrusted:

# Assert the Share
- ASSERT|$Share:
    AllOf: Chat, Consumer, Language, Bind.Schema, Bind.User
    Texts: Language, Consumer, Bind.Schema, Bind.User
    UUIDs: Chat

# Execute the handler
- CALL|OnDisclose >> $data:
    
    # Share data
    Share: $Share.ID
    Consumer: $Share.Consumer
    Language: $Share.Language

    # Bind data
    Bind: $Share.Bind
    Schema: $Share.Bind.Schema
    Reference: $Share.Bind.Reference
    Internals: $Share.Bind.Internals

# Save the data for collection
- SAVE|$Share:
    .State: READY
    Data: $data
    Expires: .Now.Add(5 minutes)
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`ASYNC`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`WAIT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Shares`](<../🪣 Shares/🗄️ Vault.Shares 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Now`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>) [`.Add`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ.md>)
|