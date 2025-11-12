<!-- TODO -->

# 🤵📃 Saved@Broker 🎫 handler

> Purpose: 
* [Script 📃](<🤵 Saved 🐌 msg.md>) method.

## Script

```yaml
📃 Saved@Broker:

# Assert the message
- ASSERT|$.Msg:
    AllOf: Token, Path
    UUIDs: Token, From
    Texts: Path

# Get the Wallet 🧑‍🦰
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $.Msg.Header.From 

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Get the Offer 
- READ >> $offer:
    Set: Broker.Offers
    Key: $.Msg.Token
# idempotent, don't delete
# it will timeout eventually

# Get the Token 
- READ >> $token:
    Set: Broker.Tokens
    Key: $.Msg.Token
    Default: $offer
# idempotent

# Save the Token
- SAVE|$token:
    $offer

# Inform the Issuer
- SEND:
    Header:
        To: $token.Issuer
        Subject: Accepted@Issuer
    Body:
        Token: $token.Token
        Hook: $token.Hook

# Updated the Tokens
- RUN|Update-Notifier:
    $wallet:
    updates: TOKENS
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens table`](<../../🤵🪣 Broker tables/Tokens 🎫 table/🤵 BrokerTokens 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Accepted@Issuer`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`Update Notifier` 📃 script](<../../🤵⏩ Broker flows/Update Notifier 🤵⏩📣/🤵 Update Notifier 📃 script.md>)
|
