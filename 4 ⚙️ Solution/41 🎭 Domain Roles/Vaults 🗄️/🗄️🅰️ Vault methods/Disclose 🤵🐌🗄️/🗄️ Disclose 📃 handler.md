<!-- TODO -->

# 🗄️📃 Disclose handler

> Part of the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>)

> Implements the [`Disclose@Vault` 🅰️ method](<🗄️ Disclose 🐌 msg.md>)

## Script

```yaml
📃 Disclose@Vault:

# Verify the signature
- VERIFY|$.Msg

# Create the collect
- SAVE|Vault.Shares:
    .State: ASKED
    Consumer: $.Msg.From
    Data: $data
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASYNC`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) [`WAIT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|