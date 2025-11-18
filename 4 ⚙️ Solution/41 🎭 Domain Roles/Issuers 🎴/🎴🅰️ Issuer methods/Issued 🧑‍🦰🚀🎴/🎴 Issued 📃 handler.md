# 🎴📃 Issued

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Issued@Issuer` 🅰️ method](<🎴 Issued 🚀 call.md>).

<br/>

## Scripts

```yaml
📃 Issued@Issuer:

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Hook
    UUIDs: Hook

# Get the hook
- READ >> $hook:
    Set: Talker.Hooks
    Key: $.Msg.Hook

# Verify the Message
- VERIFY|$.Msg:
    Key: $hook.PublicKey

# Return the token
- RETURN:
    $hook.Issued
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`REEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats@Host`](<../../../Hosts 🤗/🤗🪣 Host tables/Chats 💬 table/🪣 Chats/🤗 Host.Chats 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|