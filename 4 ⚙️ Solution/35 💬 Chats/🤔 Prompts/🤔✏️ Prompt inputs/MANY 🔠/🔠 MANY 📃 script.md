# 😃🔠 `.MANY` 🔽 script

> Purpose
 
* [Script 📃](<../../../😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`MANY`](<🔠 MANY ⌘ cmd.md>) command.

## Flow

![alt text](<🔠 MANY ⚙️ uml.png>)

## How to call

Here are the outputs of the [`Parse@Hosted` 🅰️ method](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Parse 😃🚀📦/📦 Parse 🚀 request.md>)

```yaml
- RUN|.MANY:
    {PROMPT inputs}
```

## Script

Here's the [Script 📃](<../../../😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>)

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
| [Commands ⌘](<../../../😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../../😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../../😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../../😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Placeholders 🧠](<../../../😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Inputs`](<../../../😃 Talkers/😃⚙️ Talker cmds/...functions 🐍/🔩 {.Inputs}.md>)
| [Scripts 📃](<../../../😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) | [`Prompts` 📃 script](<../../../😃 Talkers/😃⏩ Talker flows/Prompts 😃⏩🧑‍🦰/😃 Prompts 📃 script.md>)

---
<br/>