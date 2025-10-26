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
- ASYNC|Disclosure >> $data:
    $.Msg

# Get the data
- WAIT|$data

# Create the collect
- SAVE|Collects@Vault >> $collect:
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
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>) [`WAIT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/WAIT ⏸️/WAIT ⏸️.md>)
|