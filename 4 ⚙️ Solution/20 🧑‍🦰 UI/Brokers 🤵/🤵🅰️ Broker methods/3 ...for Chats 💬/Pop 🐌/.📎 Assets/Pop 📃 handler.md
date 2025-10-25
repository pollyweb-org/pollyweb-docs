# 🤵📃 Pop handler

> [Script 📃](<../🧑‍🦰🐌🤵 Pop.md>) that implements the [`Pop@Broker` 🅰️ method](<../🧑‍🦰🐌🤵 Pop.md>)

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
    Set: Wallets
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

Commands: [`ASSERT`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`CASE`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/CASE ⏯️/CASE ⏯️.md>) [`GET`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) [`VERIFY`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>)

| Scripts | Details
|-|-
| [▶️ `PopToken`](<Pop Token 🎫 script.md>) | Implements [🧑‍🦰💬🤵 Remove Token 🎫](<../../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/💬🤵 Remove 🎫 chat.md>)
| [▶️ `PopVault`](<Pop Vault 🗄️ script.md>) | Implements [🧑‍🦰💬🤵 Unbind Vault](<../../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/💬🤵 Unbind 🗄️ chat.md>)
|