<!-- TODO -->

# 🤵📃 Tokens handler

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Tokens@Broker` 🅰️ method](<🤵 Tokens 🚀 request.md>)


## Flow

![alt text](<🤵 Tokens ⚙️ uml.png>)

## Script

```yaml
📃 Tokens@Broker:

# The the wallet item
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Prepare the response:
- PUT|$wallet.Tokens >> $tokens:
    - Issuer
    - Issuer$
    - Key
    - Schema
    - Schema$
    - Status
    - Token

# Respond
- RETURN:
    Tokens: $tokens
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`EVAL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 BrokerWallets 🪣 table.md>) <br/> [`Tokens` 🪣 table](<../../🤵🪣 Broker tables/Tokens 🎫 table/🤵 BrokerTokens 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|