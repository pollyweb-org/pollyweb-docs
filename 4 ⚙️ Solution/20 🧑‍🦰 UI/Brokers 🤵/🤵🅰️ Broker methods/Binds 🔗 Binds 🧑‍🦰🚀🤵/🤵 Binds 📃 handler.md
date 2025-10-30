# 🤵📃 Binds 🔗

> [Script 📃](<🤵 Binds 🚀 request.md>) that handles the [`Binds@Broker` 🅰️ method](<🤵 Binds 🚀 request.md>)

<br/>

## Flow

![alt text](<🤵 Binds ⚙️ uml.png>)

## Script

```yaml
📃 Binds@Broker:

# Get the wallet item
- GET >> $wallet:
    Set: BrokerWallets
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Prepare the response
- EVAL|$wallet.Binds >> $binds:
    - Bind
    - Vault
    - Vault$
    - Schema
    - Schema$

# Respond
- RETURN:
    Binds: $binds
```

|Needs ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`EVAL`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`RETURN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>) <br/> [`Binds` 🪣 table](<../../🤵🪣 Broker tables/Binds 🔗 table/🤵 BrokerBinds 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>) 
|