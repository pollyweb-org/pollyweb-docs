# 🤵 Translate All 📃 script

> Part of the [`Language` 📃 handler](<../🤵 Language 📃 handler.md>)

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that translates 
    * all [domains 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) 
    * and [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) 
    * used by the [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).

## Script

```yaml
📃 Translate-All:

- ASSERT:
    $wallet

# Group the domains
- DISTINCT >> $domains:
    $wallet.Chats.Host
    $wallet.Binds.Vault
    $wallet.Tokens.Issuer

# Group the schemas
- DISTINCT >> $schemas:
    $wallet.Tokens.Schema

# Translate domains and schemas
- SEND >> $translated:
    Header:
        To: $.Hosted.Graph
        Subject: Translate@Graph
    Body:
        Language: $.Msg.Language
        Domains: $domains
        Schemas: $schemas

# Return the translations
- RETURN:
    $translated
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DISTINCT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/DISTINCT 🌪️/🌪️ DISTINCT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)   | [`$.Hosted`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>) [`$.Msg`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Translate@Graph` 🅰️ method](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>)
|