<!-- TODO -->

<!--
[`.CHAT` 📃 script](<../../../../35 💬 Chats/😃 Talkers/😃📃 Talker scripts/...for placeholders 🧠/😃📃 .CHAT 💬 script.md>)
-->

# 🤵📃 Tokens handler

[Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/📃 Script.md>) that implements the [`Tokens@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🧑‍🦰🚀🤵 Tokens.md>)


## Handler

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
    Header:
        To: $.Settings.Graph
        Subject: Translate@Graph
    Body:
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

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/⌘ Command.md>) | [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET ⏬ item.md>) [`MERGE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/MERGE 🧬 lists.md>) [`REEL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/REEL 🎣.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>) 
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣](<../../🤵🪣 Broker tables/🤵🪣 Wallets table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Translate@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>) [`$.Settings`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Settings 🎛️.md>)
|