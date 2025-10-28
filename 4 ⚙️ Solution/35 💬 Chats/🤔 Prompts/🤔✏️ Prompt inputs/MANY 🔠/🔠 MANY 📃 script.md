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

# Ask the user to answer
- PROMPT >> $reply:
    Statement: $:Statement
    Options: $:Options$

# Return the reply.
- RETURN|$reply
```

Commands: {{PROMPT}} [`RETURN`](<../../../😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) 

---
<br/>