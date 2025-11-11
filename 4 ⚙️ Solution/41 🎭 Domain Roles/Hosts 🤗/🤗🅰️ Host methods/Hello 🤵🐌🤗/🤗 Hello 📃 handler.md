# 🤗 Hello 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Hello@Host` 🅰️ method](<🤗 Hello 🐌 msg.md>)

## Diagram

![alt text](<🤗 Hello ⚙️ uml.png>)

## Handler

```yaml
📃 Hello@Host:

# Verify the message
- VERIFY|$.Msg

# Check if the Broker is trustworthy
- TRUSTS|$.Msg.From:
    Schema: .HOST/HELLO

# Assert the message
- ASSERT|$.Msg:
    - AllOf: Chat, Language, PublicKey, Schema, Key
    - Texts: Language, PublicKey, Schema, Key
    - UUIDs: Chat
    - Lists: Binds, Tokens, Parameters

# Save the data
- CHAT:
    Broker: $.Msg.From
    | `Broker` | [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | `any-broker.dom`
    | `ID` | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | `<chat-uuid>`
    | `Key`| Chat [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) Key | `$.Chat.Key` → `ANY-KEY`
    | `Role` | What [emoji](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/😶 Input emojis.md>) to show | `HOST` `AGENT` `HELPER`
    | `PublicKey` | To verify [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>) `PublicKey`
    | `Timezone`| For the [`.Now`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Now}.md>) function | `UTC+1` `PST` 
    | `Language` | For the [`.Now`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Now}.md>) function | `en-us`
    :$.Msg.Body:  

# Start a Chat for the locator
- TALK:
    Chat: $.Msg.Chat
    Schema: $.Msg.Schema 
    Key: $.Msg.Key
```


Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CHAT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`TALK`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/TALK 😃/😃 TALK ⌘ cmd.md>) [`TRUSTS`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|