# 😃🔢 Talker `.DIGITS` script

> Purpose
 
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`DIGITS`](<🔢 DIGITS ⌘ cmd.md>) command.

<br/>

## Flow

![alt text](<🔢 DIGITS ⚙️ uml.png>)

<br/>

## How to call

Here are the outputs of the [`Parse@Hosted` 🚀 call](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Parse 😃🚀📦/📦 Parse 🚀 call.md>)

```yaml
- RUN .DIGITS:
    {PROMPT inputs}
```

<br/>

## Script

Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)


```yaml
📃 .DIGITS:

# Ask the user to answer
- RUN .PROMPT >> $reply:
    :$.Inputs:
    Format: DIGITS

# Return the reply.
- RETURN: $reply
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../../📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`PROMPT` 📃 script](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/PROMPT 🤔/🤔 PROMPT 📃 script.md>)

---
<br/>