# 🤵📃 Set Language 

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Language@Broker`](<🤵 Language 🐌 msg.md>) method.

## Flow

![alt text](<🤵 Language ⚙️ uml.png>)

## Script

```yaml
📃 Language@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    AllOf: Language
    Texts: Language

# Get the wallet
- READ >> $wallet:
    Set: BrokerWallets
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Exit if language not changed
- CASE|$wallet.Language:
    $.Msg.Language: RETURN

- RUN|Translate-All

- PARALLEL:
    - RUN|Save-Chats($wallet, $translated)
    - RUN|Save-Binds($wallet, $translated)
    - RUN|Save-Tokens($wallet, $translated)

# Change the Wallet
- SAVE|$wallet:
    Language: .Msg.Language

# Inform the Notifier
- RUN|Updated@Notifier:
    Wallet: $Wallet
    Updates: [CHATS, BINDS, TOKENS]
```


|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>)  [`RUN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)  [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Function 🐍.md>) | [`{.Distinct}`](<../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.Distinct}.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Translate@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) | [`Update Notifier` 📃 script](<../../🤵⏩ Broker flows/Update Notifier 🤵⏩📣/🤵 Update Notifier 📃 script.md>)
|
