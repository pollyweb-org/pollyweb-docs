# 🖨️ Resolve 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Resolve@Printer` 🅰️ method](<🖨️ Resolve 🚀 call.md>)

## Flow

![alt text](<🖨️ Resolve ⚙️ uml.png>)

## Script

```yaml
📃 Resolve@Printer:

# Verify the signature
- VERIFY|$.Msg

# Get the alias.
- READ >> $alias:
    Set: Printer.Aliases
    Key: $.Msg.Alias

# Return the locator
- RETURN:
    $alias.Locator
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`PrinterAliases` 🪣 table](<../../🖨️🪣 Printer tables/PrinterAliases 🪣 table.md>)
|