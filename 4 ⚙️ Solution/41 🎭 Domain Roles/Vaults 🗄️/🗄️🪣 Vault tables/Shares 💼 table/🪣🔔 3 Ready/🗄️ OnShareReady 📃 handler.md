# 🗄️ OnShareReady 📃 handler

> About
* Part of the [Vault 🗄️ domain](<../../../🗄️ Vault/🗄️🎭 Vault role.md>) role
* Part of the [`Vault.Shares` 🪣 table](<../🪣 Shares/🗄️ Vault.Shares 🪣 table.md>)

<br/>

## Diagram

![alt text](<🗄️ OnShareReady ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnShareReady:

# Send the Collect message
- SEND:
    Header:
        To: $Share.Consumer
        Subject: Collect@Consumer
    Body:
        Hook: $Share.Hook.Require   # Consumer hook 
        Share: $Share.ID.Require    # Vault share hook
        Schema: $Share.Bind.Schema.Require
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Consume@Consumer` 🐌 msg](<../../../../Consumers 💼/💼📨 Consumer msgs/SHARE Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>)
|