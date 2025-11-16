# 🤵📃 Save Binds

> Part of the [`Language` 📃 handler](<../🤵 Language 📃 handler.md>)

## Script

```yaml
📃 Save-Binds:

# Verify the required inputs
- ASSERT:
    AllOf: $wallet, $translated

# Save the Binds
- PARALLEL|$wallet.Binds|$bind:

    # Set the Vault title
    - SELECT >> $bind.Vault$:
        First: Translation
        From: $translated.Domains
        Where: Domain.Is($bind.Vault)

    # Save the bind
    - SAVE|$bind
```


|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PARALLEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SELECT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerBinds` 🪣 table](<../../../🤵🪣 Broker tables/Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Is`](<../../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/Is ⓕ any.md>)
|
