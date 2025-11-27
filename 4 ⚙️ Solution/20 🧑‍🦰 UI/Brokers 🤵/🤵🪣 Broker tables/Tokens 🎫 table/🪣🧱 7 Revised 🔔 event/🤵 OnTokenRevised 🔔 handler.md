# 🤵 OnTokenRevised 🔔 handler

> Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

> Part of the [`Broker.Tokens.Revise` ⏩ flow](<../🪣🧱 7 Revise ⏩ flow/🤵 Broker.Tokens.Revise ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnTokenRevised ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenRevised:

# Assert the inputs
- ASSERT|$Token:
    AllOf: Token, Issuer, Status, Starts, Wallet
    UUIDs: Token, Wallet
    Texts: Status, Issuer
    Times: Starts, Expires

# Open a Pop to inform the user
- SAVE|Broker.Pops:
    Wallet: $Token.Wallet
    Context: TOKEN.REVISED
    Key: 
        Token: $Token.Token
        Issuer: $Token.Issuer
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Pops`](<../../Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>) [`Broker.Tokens`](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) 
|