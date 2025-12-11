# 🤵 OnChatOpened 🔔 handler

> Part of the [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the [`Opened@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Chats 💬 Opened 🧑‍🦰🐌🤵/🤵 Opened 🐌 msg.md>).

<br/>

## Diagram

![alt text](<🤵 OnChatOpened ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnChatOpened:

# Assert the Chat
- ASSERT $Chat:
    AllOf: Host
    Texts: Host

# Activate the Chat on Pop@Broker
- IF $Chat.Host.Is($.Hosted.Domain):
    RETURN ACTIVE

# Otherwise, add the Finder to the Chat
- INVITE:
    Chat: $Chat.ID
    Broker: $.Hosted.Domain
    Helper: $Chat.Wallet.Finder
    Schema: .CHAT/INTRO/FINDER
    Context:
        Host: $Chat.Host
        Language: $Chatter.Chat.Language.Require
        Reviewer: $Chatter.Chat.Wallet.Reviewer.Require

# Then invite the Broker itself to the Chat
- INVITE:
    Chat: $Chat.ID
    Broker: $.Hosted.Domain
    Helper: $.Hosted.Domain
    Schema: .CHAT/INTRO/BROKER

# Return presented
- RETURN ACTIVE
```


| Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`INVITE`](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/INVITE 🤲/🤲 INVITE ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Is`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|