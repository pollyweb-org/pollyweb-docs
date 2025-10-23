# 🤵📃 Binds 🔗

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements the [`Binds@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🧑‍🦰🚀🤵 Binds.md>)

<br/>

## Script

```yaml
# The the wallet item
- GET >> $wallet:
    Set: Wallets@Broker
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Translate the vaults and the schemas
- SEND >> $translations:
    Subject: Translate@Graph
    Language: $wallet.Language
    Domains: $wallet.Vaults
    Schemas: $wallet.BindSchemas

# Add the vault titles
- MERGE >> $binds:
    Lists: 
        BINDS: $wallet.Binds
        DOMAINS: $translations.Domains
    Match: 
        BINDS.Vault: DOMAINS.Domain
    Output: 
        Bind: BINDS.Bind
        Vault: BINDS.Vault
        Vault$: DOMAINS.Translation
        Schema: BINDS.Schema
        
# Add the schema titles
- MERGE >> $binds:
    Lists: 
        BINDS: $binds
        SCHEMAS: $translations.Schemas
    Match: 
        BINDS.Schema: SCHEMAS.Schema
    Output: 
        :BINDS:
        Schema$: SCHEMAS.Translation

# Respond
- REEL:
    Binds: $binds
```

|Needs ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) [`REEL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>)

| [Command ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| ⏬ [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets/GET ⏬ item.md>) | Get the [Wallet 🪣 item](<../../🤵🪣 Broker tables/🤵🪣 Wallets table.md>)
| 🔐 [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>) | Verify the  [Signature 🔏](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Signatures 🔏.md>) of the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| 📬 [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/$SEND 📬 msg.md>) | Call [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| 🧬 [`MERGE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/MERGE 🧬 lists.md>) | Add the translations to the dataset
| 🎣 [`REEL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>) | Respond to the [Synchronous Request 🚀](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Request Sync 🚀.md>)
|
