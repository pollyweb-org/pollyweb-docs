<!-- TODO -->

# 🤵📃 Saved 🎫 handler

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
- GET >> $wallet:
    Set: BrokerWallets
    Key: $.Msg.Header.From 

# Verify the signature
- VERIFY|$.Msg|$wallet.PublicKey

# Get the Offer 
- GET >> $offer:
    Set: BrokerOffers
    Key: $.Msg.Token
# idempotent, don't delete
# it will timeout eventually

# Get the Token 
GET >> $token:
    Set: Tokens@Broker
    Key: $.Msg.Token
    Default: $offer
# idempotent

# Save the Token file path
- SAVE|$token:
    :$offer:
    Path: $.Msg.Path

# Inform the Issuer
- SEND:
    Header:
        To: $token.Issuer
        Subject: Accepted@Issuer
    Body:
        Token: $token.Token
        Hook: $token.Hook

# Updated the Tokens
- RUN|UpdateTokens:
    wallet: $wallet
```

|Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET ⏬/⏬ GET ⌘ cmd.md>) [`RUN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens table`](<../../🤵🪣 Broker tables/Tokens 🎫 table/🤵 Tokens 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Accepted@Issuer`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>)
| [Scripts 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) | [`UpdateTokens`](<../../🤵⏩ Broker flows/Update Tokens 🤵⏩🎫/🤵 Update Tokens 📃 script.md>)
|
