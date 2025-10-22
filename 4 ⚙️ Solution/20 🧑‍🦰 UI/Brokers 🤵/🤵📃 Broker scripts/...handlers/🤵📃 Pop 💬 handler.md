# 🤵📃 Pop 🐌

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements the [`Pop@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Pop.md>)

<br/>

## Script

```yaml
📃 Pop: 

# Assert $.Msg
- ASSERT|$.Msg:
    Must: Hook, Key, Context
    Uuid: Hook, Key

# Assert $.Msg.Context
- ASSERT|$.Msg.Context:
    Enum: TOKEN, HOST, ISSUER, VAULT, BIND, TOKEN

# Get the Wallet 🧑‍🦰
- GET >> $wallet:
    Pool: Wallets
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

Commands: [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) [`CASE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/CASE ⏯️.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>)

| Scripts | Details
|-|-
| [▶️ `PopToken`](<../...procedures/🤵📃 Pop Token 🎫.md>) | Implements [🧑‍🦰💬🤵 Remove Token 🎫](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/💬🤵 Remove 🎫.md>)
| [▶️ `PopVault`](<../...procedures/🤵📃 Pop Vault 🗄️.md>) | Implements [🧑‍🦰💬🤵 Unbind Vault](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/💬🤵 Unbind 🗄️.md>)
|