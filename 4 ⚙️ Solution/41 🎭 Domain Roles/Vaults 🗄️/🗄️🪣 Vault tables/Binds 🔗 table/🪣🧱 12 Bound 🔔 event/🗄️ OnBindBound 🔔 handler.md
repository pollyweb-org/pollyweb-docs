# 🗄️ OnBindBound 📃 handler

> About
* Part of the [`Vault.Binds` 🪣 table](<../🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
* Part of the [🗄️ `Vault.Binds.Bind` ⏩ flow](<../🪣🧱 10 Bind ⏩ flow/🗄️ Vault.Binds.Bind ⏩ flow.md>)
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the [`Bound@Vault` 🐌 msg](<../../../🗄️📨 Vault msgs/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>).
* Returns a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) item to the [`BIND`](<../../../🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>) command.
 
<br/>

## Diagram

![alt text](<🗄️ OnBindBound ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindBound:

# Inform the Hosted if there's a reference
- IF $Bind.Reference:
    ASYNC|OnBound:
        Bind: $Bind.ID
        Reference: $Bind.Reference
        Internals: $Bind.Internals

# Return the bind
- REEL $Bind.ID:
    $Bind
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASYNC`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`REEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>)
|