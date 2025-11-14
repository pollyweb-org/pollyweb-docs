# 🤵 Save Chat 📃 script

> Part of the [`Assess@Broker` 📃 script](<../🤵 Locate 📃 handler.md>)

## Diagram

![alt text](<🤵 Save Chat ⚙️ uml.png>)

## Script 

```yaml
📃 Save-Chat:

# Verify the required inputs
- ASSERT|$.Inputs:
    AllOf: locator, wallet

# Get the translation for the language
- TRANSLATE >> $translation:
    Domain: $locator.Host
    To: $wallet.Language

# Create a new key pair
- KEYS >> $keys

# Create a new Chat
- SAVE|Broker.Chats >> $chat:
    Chat: .UUID()
    Wallet: $wallet.ID
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
- SAVE|Broker.Chatters:
    Chat: $chat.ID
    Domain: $locator.Host
    Role: HOST

# Add the FINDER participant
- SAVE|Broker.Chatters:
    Chat: $chat.ID
    Domain: $wallet.Finder
    Role: VAULT

# Add the BROKER participant
- SAVE|Broker.Chatters:
    Chat: $chat.ID
    Domain: $.Hosted.Domain
    Role: VAULT

# Return the created chat
- RETURN|$chat
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`KEYS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/KEYS 🔑/🔑 KEYS ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../../../🤵🪣 Broker tables/Chatters 👥 table/🤵 Broker.Chatters 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.UUID`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.UUID}.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Identity@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>) [`Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|