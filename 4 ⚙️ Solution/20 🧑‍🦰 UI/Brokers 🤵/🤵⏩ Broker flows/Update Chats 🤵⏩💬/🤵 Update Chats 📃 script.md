# 🤵📃 Update chats @ Broker

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that 
    * updates the translated [domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
    * for [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) in the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    * and notifies the [Notifier 📣 domain](<../../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) about the changes.

> Continues from the [`Converse` 📃 script](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/scripts/🤵 Call Converse 📃 script.md>)


<br/>

## How to call
```yaml
RUN|Update-Chats:
    wallet: $wallet
```

## Script

```yaml
📃 Update-Chats:

# Verify required inputs
- ASSERT|$.Inputs:
    AllOf: wallet

# Notify Wallets to update Binds
- RUN|Updated@Notifier:
    Wallet: $:wallet.ID
    Updates: [CHATS]
```


Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) | [`Update Notifier` 📃 script](<../Update Notifier 🤵⏩📣/🤵 Update Notifier 📃 script.md>)
|