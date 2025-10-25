# 🤵📃 Set Language 

[Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Language@Broker`](<🤵 Language 🐌 msg.md>) method.

## Script

```yaml
📃 Language@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    AllOf: Language
    Texts: Language

# Get the wallet
- GET >> $wallet:
    Set: Wallets@Broker
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Exit if language not changed
- CASE|$wallet.Language:
    $.Msg.Language: RETURN

# Group the domains
- GROUP >> $domains:
    - $wallet.Chats.Host
    - $wallet.Binds.Vault
    - $wallet.Tokens.Issuer

# Group the schemas
- GROUP >> $schemas:
    $wallet.Tokens.Schema

# Translate domains and schemas
- SEND >> $translated:
    Header:
        To: $.Settings.Graph
        Subject: Translate@Graph
    Body:
        Language: $.Msg.Language
        Domains: $domains
        Schemas: $schemas

# Save the Chats
- PARALLEL|$wallet.Chats|$chat:
    - SAVE|$chat:
        Host$: Translation
            FROM $translated.Domains
            MATCH Domain, $chat.Host

# Save the Binds
- PARALLEL|$wallet.Binds|$bind:
    - SAVE|$bind:
        Vault$: Translation
            FROM $translated.Domains
            MATCH Domain, $bind.Vault

# Save the Tokens
- PARALLEL|$wallet.Tokens|$token:
    - SAVE|$token:
        Issuer$: Translation
            FROM $translated.Domains
            MATCH Domain, $token.Issuer 
        Schema$: Translation
            FROM $translated.Schemas
            MATCH Schema, $token.Schema

# Change the Wallet
- SAVE|$wallet:
    Language: .Msg.Language

# Inform the Notifier
- RUN|Updated@Notifier:
    Wallet: $:Wallet
    Updates: [CHATS, BINDS, TOKENS]
```


|Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`CASE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/CASE ⏯️/CASE ⏯️.md>) [`GROUP`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/GROUP 🧬/GROUP 🧬 lists.md>) [`RUN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RUN ▶️/RUN ▶️.md>)  [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Translate@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Scripts 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) | [`Update Notifier` 📃 script](<../../.📎 Assets/Update Notifier 📃 script.md>)
|
