# 🤵📃 Introduced

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Introduced@Broker`](<🤵 Introduced 🐌 msg.md>) method.

## Diagram

![alt text](<🤵 Introduced ⚙️ uml.png>)

## Chat 

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🤵 [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ From another chat: <br/>- [Return] to original chat
| 🤵 [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ Tokens shared [+]


## Script

```yaml
📃 Introduced@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    OneOf: Chat
    UUIDs: Chat

# Verify the message
- VERIFY|$.Msg

# Read the chat
- READ >> $chat:
    Set: BrokerChats
    Key: $.Msg.Chat

# Load the chat
- CHAT|$chat

# If there's an origin, allow going back
- IF|$chat.Origin:
    INFO:
        Text: From another chat
        Options: 
          - /Return to original chat § .CHAT,{$chat.Origin}
    
# If tokens were shared, inform the user
- IF|$chat.Tokens:
    INFO:
        Text: Tokens shared
        Details: (($chat.Tokens.Title.Markdown))
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSESS`](<../../🤵⏩ Broker flows/Assess 🔆⏩🤵/🤵 Assess ⏩ flow.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`INFO`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerChats`](<../../🤵🪣 Broker tables/Chats 💬 table/🤵 BrokerChats 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Markdown`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Markdown}.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|