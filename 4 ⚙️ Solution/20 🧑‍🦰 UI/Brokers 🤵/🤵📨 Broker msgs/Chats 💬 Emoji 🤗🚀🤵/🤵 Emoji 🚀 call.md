# 🤗🚀🤵 Emoji @ Broker

> About
* Part of [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* Changes the default emoji of [Prompts 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>)
* Implemented by the [`Emoji 📃 handler`](<🤵 Emoji 📃 handler.md>)

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-host.dom
    To: any-broker.dom
    Subject: Emoji@Broker

Body:
    Chat: <chat-uuid>
    Emoji: 😃
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
|Header|`From`|text| [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)|[`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||To|text| [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)|[`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` |text| `Emoji@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) | 
||`Emoji`  | text    | New emoji 
|

<br/>

## FAQ

1. **Why not an asynchronous message 🐌?**
   
    To be resilient to concurrency with the async [`Prompt@Broker` 📨 msg](<../Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>).
    * If both were async, they could arrive in the wrong order,
    * causing the subsequent Prompt@ to ignore the previous Emoji@.
  
    ---
    <br/>

1. **What happens if an invalid emoji is sent?**

    The emoji sent is ignored, and [Prompts 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) start defaulting to 😃.

    ---
    <br/>