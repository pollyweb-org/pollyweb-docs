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
        Hook: $Share.Hook   # Consumer hook 
        Share: $Share.ID    # Vault share hook
        Schema: $Share.Bind.Schema
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Consume@Consumer` 🅰️ method](<../../../../Consumers 💼/💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>)
|