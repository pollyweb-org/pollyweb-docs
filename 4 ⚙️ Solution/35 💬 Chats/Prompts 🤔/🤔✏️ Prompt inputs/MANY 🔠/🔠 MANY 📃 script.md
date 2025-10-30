# 😃🔠 `.MANY` 🔽 script

> Purpose
 
* [Script 📃](<../../../Scripts 📃/📃⌘ commands/Script 📃/📃 Script.md>) that implements the [`MANY`](<🔠 MANY ⌘ cmd.md>) command.

## Flow

![alt text](<🔠 MANY ⚙️ uml.png>)

## How to call

Here are the outputs of the [`Parse@Hosted` 🅰️ method](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Parse 😃🚀📦/📦 Parse 🚀 request.md>)

```yaml
- RUN|.MANY:
    {PROMPT inputs}
```

## Script

Here's the [Script 📃](<../../../Scripts 📃/📃⌘ commands/Script 📃/📃 Script.md>)

<!-- TODO -->

```yaml
📃 .FILTER:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: Options

# Ask the user to answer
- RUN|.PROMPT >> $reply:
    :$.Inputs:

# Return the reply.
- RETURN|$reply
```

Needs||
|-|-
| [Commands ⌘](<../../../Scripts 📃/📃⌘ commands/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../../Scripts 📃/...holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../../Scripts 📃/...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../../Scripts 📃/...control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Holders 🧠](<../../../Scripts 📃/...holders 🧠/$Holder 🧠.md>) | [`$.Inputs`](<../../../Scripts 📃/...holders 🧠/$.Inputs ▶️/▶️ $.Inputs 🧠 holder.md>)
| [Scripts 📃](<../../../Scripts 📃/📃⌘ commands/Script 📃/📃 Script.md>) | [`Prompts` 📃 script](<../../../Talkers 😃/😃⏩ Talker flows/Prompts 😃⏩🧑‍🦰/😃 Prompts 📃 script.md>)

---
<br/>