# 🤵📃 Pop handler

> [Script 📃](<🤵 Pop 🐌 msg.md>) that implements the [`Pop@Broker` 🅰️ method](<🤵 Pop 🐌 msg.md>)

<br/>

## Script

```yaml
📃 Pop: 

# Assert $.Msg
- ASSERT|$.Msg:
    AllOf: Hook, Key, Context
    UUIDs: Hook, Key

# Assert $.Msg.Context
- ASSERT|$.Msg.Context:
    Enum: TOKEN, HOST, ISSUER, VAULT, BIND, TOKEN

# Get the Wallet 🧑‍🦰
- GET >> $wallet:
    Set: BrokerWallets
    Key: $.Msg.Header.From 

# Verify the Message
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Handle the context
- CASE|$.Msg.Body.Context:

    TOKEN: 
        RUN|PopToken:
            Wallet: $wallet
            Token: 
    VAULT:  
        RUN|PopVault:
            Wallet: 
            Vault: 

    BIND : TALK|PopBind
```

Commands: [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)

| Scripts | Details
|-|-
| [▶️ `PopToken`](<🤵 Pop Token 📃 script.md>) | Implements [🧑‍🦰💬🤵 Remove Token 🎫](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/Remove 💬🎫🤵 /🧑‍🦰 Remove Token ⏩ flow.md>)
| [▶️ `PopVault`](<🤵 Pop Vault 📃 script.md>) | Implements [🧑‍🦰💬🤵 Unbind Vault](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/Unbind 💬🗄️🤵 /🧑‍🦰 Unbind vault ⏩ flow.md>)
|