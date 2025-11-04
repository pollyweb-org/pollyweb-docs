# 🖨️ Resolve 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Resolve@Printer` 🅰️ method](<🖨️ Resolve 🚀 request.md>)

## Flow

![alt text](<🖨️ Resolve ⚙️ uml.png>)

## Script

```yaml
📃 Resolve@Printer:

# Verify the signature
- VERIFY|$.Msg

# Get the alias.
- READ >> $alias:
    Set: PrinterAliases
    Key: $.Msg.Alias

# Return the locator
- RETURN:
    $alias.Locator
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`READ`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`PrinterAliases` 🪣 table](<../../🖨️🪣 Printer tables/PrinterAliases 🪣 table.md>)
|