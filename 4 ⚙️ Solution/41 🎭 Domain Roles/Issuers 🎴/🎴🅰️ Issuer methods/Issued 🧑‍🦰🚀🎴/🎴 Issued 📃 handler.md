# 🎴📃 Issued

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃⌘ commands/Script 📃/📃 Script.md>) that implements the [`Issued@Issuer` 🅰️ method](<🎴 Issued 🚀 request.md>).

<br/>

## Scripts

```yaml
📃 Issued@Issuer:

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Hook
    UUIDs: Hook

# Get the hook
- GET >> $hook:
    Set: TalkerHooks
    Key: $.Msg.Hook

# Verify the Message
- VERIFY|$.Msg:
    Key: $hook.PublicKey

# Return the token
- RETURN:
    $hook.Issued
```

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃⌘ commands/Command ⌘/⌘ Command.md>) | [`GET`](<../../../../35 💬 Chats/Scripts 📃/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`REEL`](<../../../../35 💬 Chats/Scripts 📃/...control ▶️/REEL 🎣/🎣 REEL ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats@Host`](<../../../Hosts 🤗/🤗🪣 Host tables/Chats 💬 table/🤗 HostChats 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/...holders 🧠/$Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/...holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|