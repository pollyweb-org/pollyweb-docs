# 🗄️ OnBindDeclined 🔔 handler

> Purpose
* Part of the [`Vault.Binds` 🪣 table](<../🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
* Part of the [🗄️ `Vault.Binds.Bind` ⏩ flow](<../🪣🧱 10 Bind ⏩ flow/🗄️ Vault.Binds.Bind ⏩ flow.md>)
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the [`Bound@Vault` 📨 msg](<../../../🗄️📨 Vault msgs/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>).
 
<br/>

## Diagram

![alt text](<🗄️ OnBindDeclined ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindDeclined:

# Return empty if declined
- REEL|$Bind.ID
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`REEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>)
|