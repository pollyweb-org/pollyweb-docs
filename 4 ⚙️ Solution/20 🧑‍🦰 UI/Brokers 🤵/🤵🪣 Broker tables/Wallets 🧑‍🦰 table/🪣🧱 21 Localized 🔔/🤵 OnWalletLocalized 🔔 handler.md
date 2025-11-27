# 🤵 OnWalletLocalized 📃 handler

> About
* Part of the [🤵 `Broker.Wallets.Localize` ⏩ flow](<../🪣🧱 20 Localize ⏩ flow/🤵 Broker.Wallets.Localize ⏩ flow.md>)


<br/>

## Diagram

![alt text](<🤵 OnWalletLocalized ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnWalletLocalized:

# Assert the Wallet
- ASSERT|$Wallet:
    AllOf: Language
    Texts: Language

# Update all related entities in this Wallet
- PARALLEL:

    # Update all Binds in this Wallet
    - PARALLEL|$Wallet.Binds|$bind:
        SAVE|$bind:
            Language: $Wallet.Language

    # Update all Chats in this Wallet
    - PARALLEL|$Wallet.Chats|$chat:
        SAVE|$chat:
            Language: $Wallet.Language

    # Update all Domains in this Wallet
    - PARALLEL|$Wallet.Domains|$domain:
        SAVE|$domain:
            Language: $Wallet.Language

    # Update all Schemas in this Wallet
    - PARALLEL|$Wallet.Schemas|$schema:
        SAVE|$schema:
            Language: $Wallet.Language

    # Update all Tokens in this Wallet
    - PARALLEL|$Wallet.Tokens|$token:
        SAVE|$token:
            Language: $Wallet.Language
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PARALLEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Binds`](<../../Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>) [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Domains`](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) [`Tokens`](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) [`Wallets`](<../🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) |
|