<!-- TODO -->

# 🗄️📃 Disclose handler

> Part of the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>)

> Implements the [`Disclose@Vault` 🅰️ method](<🗄️ Disclose 🐌 msg.md>)

## Script

```yaml
📃 Disclose@Vault:

# Verify the signature
- VERIFY|$.Msg

# Get for the data
- ASYNC|Disclosure >> $hook:
    $.Msg

# Get the data
- WAIT|$hook >> $data

# Create the collect
- SAVE|VaultCollects >> $collect:
    Collect: .UUID
    Consumer: $.Msg.From
    Data: $data
    .Delete: 5 minutes # Temporary

# Send the Collect message
- SEND:
    Header:
        To: $collect.Consumer
        Subject: Collect@Consumer
    Body:
        Collect: $collect.Collect
```

|Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Command ⌘/⌘ Command.md>) | [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) [`WAIT`](<../../../../35 💬 Chats/Scripts 📃/📃 for control ▶️/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
|