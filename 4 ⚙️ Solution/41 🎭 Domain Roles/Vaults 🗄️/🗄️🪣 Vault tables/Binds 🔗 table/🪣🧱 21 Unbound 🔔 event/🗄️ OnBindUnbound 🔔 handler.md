# 🗄️ OnBindUnbound 🔔 handler

> About
* Part of the [`Vault.Binds` 🪣 table](<../🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
* Part of the [🗄️ `Vault.Binds.Unbound` ⏩ flow](<../🪣🧱 20 Unbind ⏩ flow/🗄️ Vault.Binds.Unbound ⏩ flow.md>)
* Reacts to the [`Unbound@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Unbound 🤵🐌🗄️/🗄️ Unbound 🐌 msg.md>)

<br/>

## Diagram

![alt text](<🗄️ OnBindUnbound ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindUnbound:

# Inform the Hosted if there's a reference
- IF|$Bind.Reference:
    ASYNC|OnUnbound:
        Bind: $Bind.ID
        Reference: $Bind.Reference
        Internals: $Bind.Internals
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASYNC`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Binds`](<../🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
|