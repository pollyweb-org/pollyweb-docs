# 🗄️ OnDiscloseTrusted 📃 handler

> About
* Part of the [Vault 🗄️ domain](<../../../🗄️ Vault/🗄️🎭 Vault role.md>) role
* Part of the [`Vault.Discloses` 🪣 table](<../🪣 Discloses/🗄️ Vault.Discloses 🪣 table.md>)
<br/>

## Diagram

![alt text](<🗄️ OnDetailed ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnDiscloseTrusted:

# Assert the Disclose
- ASSERT $Disclose:
    AllOf: Chat, Consumer, Language, Bind.Schema, Bind.User
    Texts: Language, Consumer, Bind.Schema, Bind.User
    UUIDs: Chat

# Read the Vault.Schemas table
- READ >> $schema:
    Set: Vault.Schemas
    Key: $Disclose.Bind.Schema

# Load the chat
- CHAT:
    Broker: $Disclose.Broker
    Chat: $Disclose.Chat

# Execute the handler
- RUN $schema.Script >> $data:
    $Disclose

# Save the data for collection
- SAVE $Disclose:
    STATE: READY
    Data: $data
    Expires: .Now.Add(5 minutes)
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CHAT`](<../../../../Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Discloses`](<../🪣 Discloses/🗄️ Vault.Discloses 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Now`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>) [`.Add`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ.md>)
|