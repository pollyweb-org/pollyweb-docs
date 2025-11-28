# 🤵 Emoji 📃 handler

> About
* Part of [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Emoji@Broker` 🅰️ method](<🤵 Emoji 📃 handler.md>)
* Only for active [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
* Only for [Host 🤗 domains](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) and [Helper 🤲 domains](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>)

<br/>

## Diagram

![alt text](<🤵 Emoji ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Emoji@Broker

# Verify the message
- VERIFY|$.Msg

# Assert the message
- ASSERT|$.Msg:
    AllOf: Chat, Emoji
    UUIDs: Chat
    Texts: Emoji
    Emoji.Length.IsAtMost: 1

# Get the Chatter
- READ:
    Set: Broker.Chatters
    Key:
        Chat: $.Msg.Chat
        Domain: $.Msg.From
    Assert:
        Role.IsIn: HOST, HELPER
        Chat.State: ACTIVE   

# Update the Chat emoji
- SAVE|$chatter.Chat:
    Emoji: $.Msg.Emoji
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)  | [`Broker.Chatters`](<../../🤵🪣 Broker tables/Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Broker.Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) |
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsAtMost`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsAtMost ⓕ.md>) [`.IsIn`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.Length`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Length ⓕ.md>) |
|

<br>

## FAQ

1. **Why aren't invalid emojis raising an error?**

    For the following reasons:
    1. avoids raising unnecessary errors that break flows;
    2. emojis will be filtered in the [`OnPromptInserted` 🔔 handler](<../../🤵🪣 Broker tables/Prompts 🤔 table/🪣🧱 1 Inserted 🔔/🤵 OnPromptInserted 🔔 handler.md>);
    3. avoids duplicating logic, simplifying maintenance;
    4. keeps the record of the change in the chat history.

    ---
    <br/>