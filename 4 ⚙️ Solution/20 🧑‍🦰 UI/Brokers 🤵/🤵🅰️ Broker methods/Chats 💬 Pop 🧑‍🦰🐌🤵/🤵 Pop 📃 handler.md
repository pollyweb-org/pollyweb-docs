# 🤵📃 Pop handler

> [Script 📃](<🤵 Pop 🐌 msg.md>) that implements the [`Pop@Broker` 🅰️ method](<🤵 Pop 🐌 msg.md>)

<br/>

## Script

<!-- TODO: Finish the code -->

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
- READ >> $wallet:
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

Commands: [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`READ`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)

| Scripts | Details
|-|-
| [▶️ `PopToken`](<Pop Token 🎫/🤵 Pop Token 📃 handler.md>) | Implements [🧑‍🦰💬🤵 Remove Token 🎫](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/Remove 💬🎫🤵 /🧑‍🦰 Remove Token ⏩ flow.md>)
| [▶️ `PopVault`](<Pop Vault/🤵 Pop Vault 📃 handler.md>) | Implements [🧑‍🦰💬🤵 Unbind Vault](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/Unbind 💬🗄️🤵 /🧑‍🦰 Unbind Vault ⏩ flow.md>)
|