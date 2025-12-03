# 🤗 OnHostPromptAsserted 🔔 handler

> About
* Part of the [Host 🤗 domain](<../../../🤗 Host role/🤗🎭 Host role.md>) role
* Part of the [`Host.Prompts` 🪣 table](<../🪣 Prompts/🤗 Host.Prompts 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤗 OnHostPromptAsserted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnPromptAsserted:

# Assert readiness for Prompt@Broker
- ASSERT|$Prompt:
    AllOf: ID, Chat, Format, Expires, Broker
    Texts: Emoji, Format, Broker
    Times: Expires
    UUIDs: ID, Chat
    Expires.IsFuture:
    Emoji.Length: 1

# Call the Prompt@Broker
- SEND|$Prompt:
    Header:
        To: Broker
        Subject: Prompt@Broker
    Body:
        Prompt: ID
        Chat: Chat
        Emoji: Emoji
        Format: Format
        Expires: Expires
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Prompts`](<../🪣 Prompts/🤗 Host.Prompts 🪣 table.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsFuture`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>) [`.Length`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Length ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Prompt@Broker` 📨 msg](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)