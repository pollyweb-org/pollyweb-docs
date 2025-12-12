# 😃1️⃣ Talker `.ONE` script

> Purpose
 
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`ONE`](<1️⃣ ONE ⌘ cmd.md>) command.

<br/>

## Flow

![alt text](<1️⃣ ONE ⚙️ uml.png>)

<br/>

## How to call

Here are the outputs of the [`Parse@Hosted` 🚀 call](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Parse 😃🚀📦/📦 Parse 🚀 call.md>)

```yaml
- RUN .ONE:
    {PROMPT inputs}
```

<br/>

## Script

Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

```yaml
📃 .ONE:

# Assert the inputs
- ASSERT $.Inputs:
    AllOf: Options

# Ask the user to answer
- RUN .PROMPT >> $reply:
    :$.Inputs:
    Format: ONE

# Return the reply.
- RETURN: $reply
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../../📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`PROMPT` 📃 script](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/PROMPT 🤔/🤔 PROMPT 📃 script.md>)

---
<br/>