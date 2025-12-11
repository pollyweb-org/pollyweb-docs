# 🤵 Welcome 😃 handler

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) where the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * informs the user about the origin of the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>), 
    * as well as the [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) and [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) shared with the [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).

<br/>

## Diagram

![alt text](<🤵 Welcome ⚙️ uml.png>)


## Chat 

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🤵 [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ From another chat: <br/>- [Return] to original chat
| 🤵 [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ Tokens shared [-] <br/>- 🎟️ Any Token, by Any Issuer<br/>- 🪪 Another Token, by Another Issuer


## Script

```yaml
📃 Welcome:

# Assert the inputs
- ASSERT:
    $.Chat.ID:
    $.Chat.Inputs.Domain: 
    $.Chat.Inputs.Domain.IsDomain:

# Get the chatter info
- READ >> $chatter:
    Set: Broker.Chatter
    Key: 
        Chat: $.Chat.ID
        Domain: $.Chat.Inputs.Domain

# If there's an origin, allow going back
- IF $chatter.Chat.Origin:
    INFO:
        Text: From another chat
        Options: 
          - /Return to original chat § .CHAT,{$chatter.Chat.Origin}

# If Binds were shared, inform the user
- IF $chatter.Binds:
    INFO:
        Text: Binds shared
        Details: ´$chatter.Binds.Title´

# If Tokens were shared, inform the user
- IF $chatter.Tokens:
    INFO:
        Text: Tokens shared
        Details: ´$chatter.Tokens.Title´
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`INFO`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Broker.Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) |  [`.IsDomain`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) 