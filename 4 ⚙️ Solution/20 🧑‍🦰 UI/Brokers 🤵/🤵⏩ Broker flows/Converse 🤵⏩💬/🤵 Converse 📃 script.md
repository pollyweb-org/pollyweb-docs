# 🤵📃 Converse 💬

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/📃 Script.md>) that implements the [`Converse` ⏩ flow](<🤵 Converse ⏩ flow.md>)

<br/>

## Script

> Requires `$:Wallet` and `$:Locator` placeholders from the [`Assess` 📃 script](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 📃 handler.md>).

> Continues from the [`Assess` 📃 script](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 📃 handler.md>)


```yaml
📃 Converse:

- ASSERT|.Inputs:
    AllOf: Locator, Wallet

# Get the Host details from the Graph
- SEND >> $domain:
    Header:
        To: $.Hosted.Graph
        Subject: Identity@Graph
    Body:
        Domain: $:Locator.Host

# Save the Host info
- SAVE|BrokerDomains:
    Domain: $domain.Domain
    Domain$: $domain.Name
    SmallIcon: $domain.SmallIcon
    BigIcon: $domain.BigIcon

# Get the translation for the language
- SEND >> $translation:
    Header:
        To: $.Hosted.Graph
        Subject: Translate@Graph
    Body:
        Language: $:Wallet.Language
        Domain: $:Locator.Host

# Create a new key pair
- KEYS >> $keys

# Create a new Chat
- SAVE|BrokerChats >> $chat:
    Chat: .UUID()
    Wallet: $:Wallet.Wallet
    # Host info
    Host: $:Locator.Host
    Host$: $translation.Domain
    # Locator info
    Key: $:Locator.Key
    Parameters: $:Locator.Parameters
    # For Wallets to sign messages
    PrivateKey: $keys.PrivateKey
    # For domains to verify Wallet messages
    PublicKey: $keys.PublicKey     

# Open the Chat in the Wallet app
- SEND:
    Header:
        To: $:Wallet.Notifier
        Subject: Converse@Notifier
    Body:
        Wallet: $chat.Wallet
        Hook: $.Msg.Hook
        Chat: $chat.Chat
        PrivateKey: $keys.PrivateKey
        Host: $chat.Host
        Host$: $chat.Host$
        SmallIcon: $domain.SmallIcon
        BigIcon: $domain.BigIcon

# Update the Chats
- RUN|UpdateChats:
    wallet: $:Wallet.Wallet
```


> Continues on [`UpdateChats` 📃 script](<../Update Chats 🤵⏩💬/🤵 Update Chats 📃 script.md>)

|Needs | |
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/⌘ Command.md>) | [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`KEYS`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/KEYS 🔑/🔑 KEYS ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`RUN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Converse@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>) <br/>  [`Identity@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)  <br/> [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$Holder 🧠.md>) | [`$.Hosted`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/📃 Script.md>) |[`UpdateChats`](<../Update Chats 🤵⏩💬/🤵 Update Chats 📃 script.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerChats` 🪣](<../../🤵🪣 Broker tables/Chats 💬 table/🤵 BrokerChats 🪣 table.md>) [`BrokerDomains` 🪣](<../../🤵🪣 Broker tables/Domains 👥 table/🤵 BrokerDomains 🪣 table.md>)
|