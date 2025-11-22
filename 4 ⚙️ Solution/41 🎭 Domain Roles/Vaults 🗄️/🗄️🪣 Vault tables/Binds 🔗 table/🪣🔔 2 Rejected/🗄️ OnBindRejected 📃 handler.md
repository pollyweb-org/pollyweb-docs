# 🗄️ OnBindRejected 📃 handler

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the [`Rejected@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Rejected 🤵🐌🗄️/🗄️ Rejected 🐌 msg.md>).
 
<br/>

## Diagram

![alt text](<🗄️ OnBindRejected ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindRejected:

# Assert the Bind
- ASSERT|$Bind:
    - AllOf: Hook
    - UUIDs: Hook

# Return the call
- REEL|$Bind.Hook
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`REEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>)
|