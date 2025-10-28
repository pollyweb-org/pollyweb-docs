<!-- TODO -->

# 🤵📃 Tokens handler

[Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Tokens@Broker` 🅰️ method](<🤵 Tokens 🚀 request.md>)


## Flow

![alt text](<🤵 Tokens ⚙️ uml.png>)

## Script

```yaml
📃 Tokens@Broker:

# The the wallet item
- GET >> $wallet:
    Set: BrokerWallets
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Prepare the response:
- EVAL|$wallet.Tokens >> $tokens:
    - Issuer
    - Issuer$
    - Key
    - Path
    - Schema
    - Schema$
    - Status
    - Token

# Respond
- RETURN:
    Tokens: $tokens
```

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | [`EVAL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`RETURN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>) <br/> [`Tokens` 🪣 table](<../../🤵🪣 Broker tables/Tokens 🎫 table/🤵 Tokens 🪣 table.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|