# 🤵 Save Chat 📃 script

## Script 

```yaml
📃 Save Chat:

# Verify the required inputs
- ASSERT|$.Inputs:
    AllOf: locator, wallet

# Get the Host details from the Graph
- SEND >> $domain:
    Header:
        To: $.Hosted.Graph
        Subject: Identity@Graph
    Body:
        Domain: $:locator.Host

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
        Language: $:wallet.Language
        Domain: $:locator.Host

# Create a new key pair
- KEYS >> $keys

# Create a new Chat
- SAVE|BrokerChats >> $chat:
    Chat: .UUID()
    Wallet: $:wallet.Wallet
    # Host info
    Host: $:locator.Host
    Host$: $translation.Domain
    # Locator info
    Key: $:locator.Key
    Parameters: $:locator.Parameters
    # For Wallets to sign messages
    PrivateKey: $keys.PrivateKey
    # For domains to verify Wallet messages
    PublicKey: $keys.PublicKey     

# Add the HOST participant
- SAVE|BrokerChatters:
    Chat: $chat.Chat
    Domain: $:locator.Host
    Role: HOST

# Add the FINDER participant
- SAVE|BrokerChatters:
    Chat: $chat.Chat
    Domain: $:wallet.Finder
    Role: VAULT

# Return the created chat
- RETURN|$chat
```

Needs||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`KEYS`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/KEYS 🔑/🔑 KEYS ⌘ cmd.md>) [`RETURN`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../../🤵🪣 Broker tables/Chats 💬 table/🤵 BrokerChats 🪣 table.md>) [`Chatters`](<../../../🤵🪣 Broker tables/Chatters 👥 table/🤵 BrokerChatters 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Function 🐍.md>) | [`.UUID`](<../../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.UUID}.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Inputs`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Inputs ▶️/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Identity@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>) [`Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|