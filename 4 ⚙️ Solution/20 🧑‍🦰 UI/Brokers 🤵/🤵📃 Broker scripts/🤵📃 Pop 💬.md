# 🤵📃 Pop 🐌

> [Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements [`Pop@Broker` 🅰️ method](<../🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Pop.md>)

<br/>

## Script

```yaml
📃 Pop: 

# Get the Wallet 🧑‍🦰
- GET >> $wallet:
    Pool: Wallets
    Key: $.Msg.Header.From 

# Verify the Message.
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Handle the context.
- CASE|$.Msg.Body.Context:
    TOKEN: TALK|PopToken
    VAULT: TALK|PopVault
    BIND : TALK|PopBind
```

Commands: [`CASE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/CASE ⏯️.md>) [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) [`VERIFY`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>)

| Scripts | Details
|-|-
| [▶️ `PopToken`](<🤵📃 Pop Token 🎫.md>) | Implements [🧑‍🦰💬🤵 Remove Token 🎫](<../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Tokens 🎫/💬🤵 Remove 🎫.md>)
| [▶️ `PopVault`](<🤵📃 Pop Vault 🗄️.md>) | Implements [🧑‍🦰💬🤵 Unbind Vault](<../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Vaults 🗄️/💬🤵 Unbind 🗄️.md>)
|