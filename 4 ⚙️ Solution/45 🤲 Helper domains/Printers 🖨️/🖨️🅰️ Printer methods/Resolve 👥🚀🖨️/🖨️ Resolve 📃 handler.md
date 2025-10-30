# 🖨️ Resolve 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Resolve@Printer` 🅰️ method](<🖨️ Resolve 🚀 request.md>)

## Flow

![alt text](<🖨️ Resolve ⚙️ uml.png>)

## Script

```yaml
📃 Resolve@Printer:

# Verify the signature
- VERIFY|$.Msg

# Get the alias.
- GET >> $alias:
    Set: PrinterAliases
    Key: $.Msg.Alias

# Return the locator
- RETURN:
    $alias.Locator
```

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/...commands ⌘/Command ⌘/⌘ Command.md>) | [`GET`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`RETURN`](<../../../../35 💬 Chats/Scripts 📃/...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`PrinterAliases` 🪣 table](<../../🖨️🪣 Printer tables/PrinterAliases 🪣 table.md>)
|