# 🤵 OnChatOpened 📃 script

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the [`Opened@Broker` 🅰️ method](<../../../🤵🅰️ Broker methods/Chats 💬 Opened 🧑‍🦰🐌🤵/🤵 Opened 🐌 msg.md>).

<br/>

## Diagram

![alt text](<🤵 OnChatOpened ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnChatOpened:

# Assert the Chat
- ASSERT|$Chat:
    AllOf: Wallet, Host
    UUIDs: Wallet
    Texts: Host

# Verify if it's a Pop@Broker
- IF|$Chat.Host.Is($.Hosted.Domain):

    Then: # Add the Broker to the Chat
        SAVE|Broker.Chatters:
            .State: POP
            Domain: $.Hosted.Domain
            Role: VAULT
            Chat: $Chat.ID

    Else: # Add the Finder to the Chat
        SAVE|Broker.Chatters:
            .State: FINDER
            Domain: $Chat.Wallet.Finder
            Role: VAULT
            Chat: $Chat.ID
```


| Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Is`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|