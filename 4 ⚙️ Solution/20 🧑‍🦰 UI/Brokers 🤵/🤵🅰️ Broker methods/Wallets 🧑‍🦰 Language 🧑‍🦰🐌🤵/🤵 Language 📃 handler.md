# 🤵📃 Set Language 

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Language@Broker`](<🤵 Language 🐌 msg.md>) method.

## Flow

![alt text](<🤵 Language ⚙️ uml.png>)

## Script

```yaml
📃 Language@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    AllOf: Language
    Texts: Language

# Get the wallet
- READ >> $wallet:
    Set: BrokerWallets
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Exit if language not changed
- CASE|$wallet.Language:
    $.Msg.Language: RETURN

# Group the domains
- EVAL|.Distinct >> $domains:
    :$wallet.Chats.Host:
    :$wallet.Binds.Vault:
    :$wallet.Tokens.Issuer:

# Group the schemas
- EVAL|.Distinct >> $schemas:
    :$wallet.Tokens.Schema:

# Translate domains and schemas
- SEND >> $translated:
    Header:
        To: $.Hosted.Graph
        Subject: Translate@Graph
    Body:
        Language: $.Msg.Language
        Domains: $domains
        Schemas: $schemas

# Save the Chats
- PARALLEL|$wallet.Chats|$chat:
    # Set the Host title
    - SELECT >> $chat.Host$:
        First: Translation
        From: $translated.Domains
        Where: Domain.Is($chat.Host)
    # Save the Chat
    - SAVE|$chat

# Save the Binds
- PARALLEL|$wallet.Binds|$bind:
    # Set the Vault title
    - SELECT >> $bind.Vault$:
        First: Translation
        From: $translated.Domains
        Where: Domain.Is($bind.Vault)
    # Save the bind
    - SAVE|$bind

# Save the Tokens
- PARALLEL|$wallet.Tokens|$token:
    # Set the Issuer
    SELECT >> $token.Issuer$: 
        First: Translation
        From: $translated.Domains
        Where: Domain.Is($token.Issuer)
    # Set the Schema
    SELECT >> $token.Schema$: 
        First: Translation
        From: $translated.Schemas
        Where: Schema.Is($token.Schema)
    # Save the Token
    - SAVE|$token

# Change the Wallet
- SAVE|$wallet:
    Language: .Msg.Language

# Inform the Notifier
- RUN|Updated@Notifier:
    Wallet: $Wallet
    Updates: [CHATS, BINDS, TOKENS]
```


|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>)  [`RUN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)  [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Function 🐍.md>) | [`{.Distinct}`](<../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.Distinct}.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Translate@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) | [`Update Notifier` 📃 script](<../../🤵⏩ Broker flows/Update Notifier 🤵⏩📣/🤵 Update Notifier 📃 script.md>)
|
