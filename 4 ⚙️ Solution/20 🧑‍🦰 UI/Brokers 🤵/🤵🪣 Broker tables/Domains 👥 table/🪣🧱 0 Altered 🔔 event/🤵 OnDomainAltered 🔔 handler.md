# 🤵 OnDomainAltered 📃 handler

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * that projects the [Domains 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
    * of a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    * into the [`Broker.Frontend` 🪣 table](<../../Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>).



<br/>

## Diagram

![alt text](<🤵 OnDomainAltered ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnDomainAltered:

# Assert the inputs
- ASSERT $Domain:
    AllOf: Wallet
    UUIDs: Wallet

# Get the Wallet 🧑‍🦰
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $Domain.Wallet

# Get the Wallet's Frontend
- READ >> $frontend:
    Set: Broker.Frontend
    Key: $wallet.ID

# Prepare the response:
- PUT $wallet.Domains >> $domains:
    Name, Title, Description, SmallIcon, BigIcon

# Replace only the Frontend Tokens.
- SAVE $frontend:
    Domains: $domains
```


|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Domains`](<../🪣 Domains/🤵 Broker.Domains 🪣 table.md>) [`Frontend`](<../../Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>)  [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) 
|