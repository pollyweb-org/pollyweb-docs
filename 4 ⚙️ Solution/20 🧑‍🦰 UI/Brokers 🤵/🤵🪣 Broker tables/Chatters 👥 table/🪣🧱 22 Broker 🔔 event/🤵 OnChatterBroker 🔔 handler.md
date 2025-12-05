# 🤵 OnChatterBroker 🔔 handler

> Part of the [`Broker.Chatters` 🪣 table](<../🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)


> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) where the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * informs the user about the origin of the [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>), 
    * as well as the [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) and [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) shared with the [Host 🤗 domain](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).

<br/>

## Diagram

![alt text](<🤵 OnChatterBroker ⚙️ uml.png>)


## Chat 

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🤵 [Broker](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ From another chat: <br/>- [Return] to original chat
| 🤵 [Broker](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ Tokens shared [-] <br/>- 🎟️ Any Token, by Any Issuer<br/>- 🪪 Another Token, by Another Issuer


## Script

```yaml
📃 OnChatterBroker:

# Get the chat
- PUT|$Chatter.Chat >> $chat

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
        Details: ´$chat.Tokens.Title.Markdown´
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`INFO`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Markdown`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Markdown ⓕ.md>)
|