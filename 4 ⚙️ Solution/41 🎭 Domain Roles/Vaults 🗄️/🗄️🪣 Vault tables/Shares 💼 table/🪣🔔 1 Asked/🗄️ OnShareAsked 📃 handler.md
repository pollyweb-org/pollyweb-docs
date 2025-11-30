# 🗄️ OnShareAsked 📃 handler

> About
* Part of the [Vault 🗄️ domain](<../../../🗄️ Vault/🗄️🎭 Vault role.md>) role
* Part of the [`Vault.Shares` 🪣 table](<../🪣 Shares/🗄️ Vault.Shares 🪣 table.md>)

<br/>

## Diagram

![alt text](<🗄️ OnShareAsked ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnShareAsked:

# Assert the Share
- ASSERT|$Share:
    AllOf: Bind, Bind.Schema, Consumer
    UUIDs: Bind
    Texts: Bind.Schema, Consumer
    
# Check if the Consumer is trusted
- TRUSTS >> $trusted:
    Trusted: $Share.Consumer
    Schema: $Share.Bind.Schema
    Role: CONSUMER

# Save the answer
- IF|$trusted:
    Then: 
        SAVE|$Share:
            .State: TRUSTED
    Else: 
        SAVE|$Share:
            .State: UNTRUSTED
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRUSTS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Binds`](<../../Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>) [`Vault.Shares`](<../🪣 Shares/🗄️ Vault.Shares 🪣 table.md>)
|