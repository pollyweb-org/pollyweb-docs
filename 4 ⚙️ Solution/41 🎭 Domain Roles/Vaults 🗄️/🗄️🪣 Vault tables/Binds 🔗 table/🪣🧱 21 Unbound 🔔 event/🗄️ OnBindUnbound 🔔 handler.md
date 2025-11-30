# 🗄️ OnBindUnbound 🔔 handler

> About
* Part of the [`Vault.Binds` 🪣 table](<../🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
* Reacts to the [`Unbound@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Unbound 🤵🐌🗄️/🗄️ Unbound 🐌 msg.md>)

<br/>

## Diagram

![alt text](<🗄️ OnBindUnbound ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindUnbound:

# Assert the Bind
- ASSERT|$Bind:
    AllOf: ID, Vault, VaultRole, VaultID, Chat, Schema, Created
    UUIDs: ID, VaultID, Chat
    Texts: Vault, VaultRole, Schema
    Times: Created

# Return empty to the REEL call
- REEL|$Bind.ID
```