<!-- TODO -->

# 🤵📃 Saved 🎫 handler

> Purpose: 
* [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/📃 Script.md>) that implements the [`Saved@Broker`](<../../🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🧑‍🦰🐌🤵 Saved.md>) method.

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
    Set: Wallets@Broker
    Key: $.Msg.Header.From 

# Verify the signature
- VERIFY|$.Msg|$wallet.PublicKey

# Get the Offer 
- GET >> $offer:
    Set: Offers@Broker
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
    To: $token.Issuer
    Subject: Accepted@Issuer
    Token: $token.Token
    Hook: $token.Hook

# Updated the Tokens
- RUN|UpdateTokens:
    wallet: $wallet
```

|Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/GET ⏬ item.md>) [`RUN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/RUN ▶️.md>) [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/SAVE 💾 item.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/SEND 📬 msg.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens table`](<../../🤵🪣 Broker tables/🤵🪣 Tokens table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Accepted@Issuer`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🤵🐌🎴 Accepted.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>)
| [Scripts 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/📃 Script.md>) | [`UpdateTokens`](<../...procedures/🤵📃 Update Tokens.md>)
|
