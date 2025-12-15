# 🌐 WEB 📃 script

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`WEB`](<🌐 WEB ⌘ cmd.md>).

<br/>

## Flow
![alt text](<🌐 WEB ⚙️ uml.png>)

<br/>

## How to call
Here are the outputs of the [`Parse@Hosted` 🚀 call](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Parse 😃🚀📦/📦 Parse 🚀 call.md>)

```yaml
- RUN .WEB:
    {PROMPT inputs}
```

<br/>

## Script

Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

```yaml
📃 .WEB:

# Assert the inputs
- ASSERT $.Inputs:
    AllOf: URL, Hook
    UUIDs: Hook
    URL.IsURL:

# Send it as a non-blocking prompt
- RUN .PROMPT:
    :$.Inputs:
    Format: WEB

# Wait for the hook to be called
- WAIT: $Hook >> $result

# Return the result
- RETURN: $result
```

Uses ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../../📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../../📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`WAIT`](<../../../📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>) |
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsURL`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/IsURL ⓕ.md>) 
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`PROMPT` 📃 script](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/PROMPT 🤔/🤔 PROMPT 📃 script.md>)