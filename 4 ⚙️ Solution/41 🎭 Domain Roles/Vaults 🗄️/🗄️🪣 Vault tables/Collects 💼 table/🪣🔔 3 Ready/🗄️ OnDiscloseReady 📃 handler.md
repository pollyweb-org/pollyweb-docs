# 🗄️ OnDiscloseReady 📃 handler

> About
* Part of the [Vault 🗄️ domain](<../../../🗄️ Vault/🗄️🎭 Vault role.md>) role
* Part of the [`Vault.Discloses` 🪣 table](<../🪣 Collects/🗄️ Vault.Discloses 🪣 table.md>)

<br/>

## Diagram

![alt text](<🗄️ OnDiscloseReady ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnDiscloseReady:

# Send the Collect message
- SEND:
    Header:
        To: $Disclose.Consumer
        Subject: Consume@Consumer
    Body:
        Query: $Disclose.Hook.Require   # Consumer hook 
        Schema: $Disclose.Bind.Schema.Require
        Collect: $Disclose.ID    # Vault share hook
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Consume@Consumer` 🐌 msg](<../../../../Consumers 💼/💼📨 Consumer msgs/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>)
|