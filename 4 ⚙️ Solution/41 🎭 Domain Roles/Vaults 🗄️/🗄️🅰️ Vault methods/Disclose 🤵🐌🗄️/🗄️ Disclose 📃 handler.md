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
- SAVE|Vault.Collects >> $collect:
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

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) [`WAIT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
|