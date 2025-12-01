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