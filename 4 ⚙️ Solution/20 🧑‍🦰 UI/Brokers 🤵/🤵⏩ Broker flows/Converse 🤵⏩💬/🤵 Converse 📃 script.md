# 🤵📃 Converse 💬

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) tha🤵 Converse ⏩ flow.mds/Converse 🤵⏩💬/🤵 Converse ⏩ flow.md>)

<br/>

## Script

> Requires `$:Wallet` and `$:Locator` placeholders from the [`Assess` 📃 script](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 📃 handler.md>).

> Continues from the [`Assess@Broker` 📃 script](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 📃 handler.md>)


```yaml
📃 Converse@Broker:

# Assert the inputs
- ASSERT|.Inputs:
    AllOf: Locator, Wallet

# Set local variables for readability
- EVAL|$:Wallet >> $wallet
- EVAL|$:Locator >> $locator

# Get the Host details from the Graph
- SEND >> $domain:
    Header:
        To: $.Hosted.Graph
        Subject: Identity@Graph
    Body:
        Domain: $locator.Host

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
        Language: $wallet.Language
        Domain: $locator.Host

# Create a new key pair
- KEYS >> $keys

# Create a new Chat
- SAVE|BrokerChats >> $chat:
    Chat: .UUID()
    Wallet: $wallet.Wallet
    # Host info
    Host: $locator.Host
    Host$: $translation.Domain
    # Locator info
    Key: $locator.Key
    Parameters: $locator.Parameters
    # For Wallets to sign messages
    PrivateKey: $keys.PrivateKey
    # For domains to verify Wallet messages
    PublicKey: $keys.PublicKey     

# Add the HOST participant
- SAVE|BrokerChatters:
    Chat: $chat.Chat
    Domain: $chat.Host
    Role: HOST

# Add the FINDER participant
- SAVE|BrokerChatters:
    Chat: $chat.Chat
    Domain: $wallet.Finder
    Role: VAULT

# Open the Chat in the Wallet app
- SEND:
    Header:
        To: $wallet.Notifier
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
- RUN|UpdateChats@Broker:
    wallet: $wallet.Wallet

# Return the new Chat
- RETURN:
    Chat: $chat
```


> Continues on [`UpdateChats@Broker` 📃 script](<../Update Chats 🤵⏩💬/🤵 Update Chats 📃 script.md>)

|Needs | |
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`KEYS`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/KEYS 🔑/🔑 KEYS ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`RUN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Converse@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>) <br/>  [`Identity@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)  <br/> [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Hosted`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) | [`Updat../Update Chats 🤵⏩💬/🤵 Update Chats 📃 script.mde Chats 📃 script.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerChats` 🪣](<../../🤵🪣 Broker tables/Chats 💬 table/🤵 BrokerChats 🪣 table.md>) [`BrokerDomains` 🪣](<../../🤵🪣 Broker tables/Domains 👥 table/🤵 BrokerDomains 🪣 table.md>)
|