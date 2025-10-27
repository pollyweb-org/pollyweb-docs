# 🖨️ Resolve 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Resolve@Printer` 🅰️ method](<🖨️ Resolve 🚀 request.md>)

## Script

```yaml
📃 Resolve@Printer:

# Verify the signature
- VERIFY|$.Msg

# Get from the table.
- GET >> $alias:
    Set: PrinterAliases
    Key: $.Msg.Alias


```
<!-- TODO: finish the code and add a sequence diagram -->