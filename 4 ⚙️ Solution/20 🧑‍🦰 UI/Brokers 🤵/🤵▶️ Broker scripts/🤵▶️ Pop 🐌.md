# 🤵😃 Pop 🐌 Broker

> [Script ▶️](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/▶️ Script.md>) that implements [`Pop@Broker` 🅰️ method](<../🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Pop.md>)

<br/>

## Script

```yaml
# Get the Wallet 🧑‍🦰
- GET|Wallets|$.Msg.Header.From >> $wallet

# Verify the Message.
- VERIFY|$.Msg|$wallet.PublicKey

# Handle the context.
- CASE|$.Msg.Body.Context:
    TOKEN: TALK|PopToken
    VAULT: TALK|PopVault
    BIND : TALK|PopBind
```

|Talkers | Details
|-|-
| [`PopToken 🔆`](<🤵▶️ Pop Token 🎫.md>) | Implements [🧑‍🦰💬🤵 Remove Token 🎫](<../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Tokens 🎫/💬🤵 Remove 🎫.md>)
| [`PopVault 🔆`](<🤵▶️ Pop Vault 🗄️.md>) | Implements [🧑‍🦰💬🤵 Unbind Vault](<../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Vaults 🗄️/💬🤵 Unbind 🗄️.md>)
|