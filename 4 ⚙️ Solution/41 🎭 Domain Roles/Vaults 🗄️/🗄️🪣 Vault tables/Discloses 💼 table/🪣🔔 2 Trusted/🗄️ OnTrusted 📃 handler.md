# 🗄️ OnDiscloseTrusted 📃 handler

> About
* Part of the [Vault 🗄️ domain](<../../../🗄️ Vault/🗄️🎭 Vault role.md>) role
* Part of the [`Vault.Discloses` 🪣 table](<../🪣 Discloses/🗄️ Vault.Discloses 🪣 table.md>)
<br/>

## Diagram

![alt text](<🗄️ OnTrusted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnDiscloseTrusted:

# Assert the Disclose
- ASSERT|$Disclose:
    AllOf: Chat, Consumer, Language, Bind.Schema, Bind.User
    Texts: Language, Consumer, Bind.Schema, Bind.User
    UUIDs: Chat

# Execute the handler
- CALL|OnDisclose >> $data:
    
    # Share data
    Disclose: $Disclose.ID
    Consumer: $Disclose.Consumer
    Language: $Disclose.Language

    # Bind data
    Bind: $Disclose.Bind
    Schema: $Disclose.Bind.Schema
    Reference: $Disclose.Bind.Reference
    Internals: $Disclose.Bind.Internals

# Save the data for collection
- SAVE|$Disclose:
    .State: READY
    Data: $data
    Expires: .Now.Add(5 minutes)
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`ASYNC`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`WAIT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Discloses`](<../🪣 Discloses/🗄️ Vault.Discloses 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Now`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>) [`.Add`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ.md>)
|