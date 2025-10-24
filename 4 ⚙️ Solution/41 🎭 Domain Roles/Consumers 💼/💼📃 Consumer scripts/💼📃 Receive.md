# 💼📃 Receive

[Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... ⌘ commands/📃 Script.md>) that implements [`Receive@Consumer`](<../💼🅰️ Consumer methods/🧑‍🦰🐌💼 Receive.md>)

<br/>

## Script

```yaml
# Resolve the callback
- GET >> $hook
    Set: Hooks@Talker
    Key: $.Msg.Hook

# Get the chat
- GET >> $chat:
    Set: Chats@Host
    Key: $hook.Chat

# Verify the Wallet signature
- VERIFY|$.Msg:
    Key: $chat.PublicKey

# Process each Bind
- PARALLEL|$.Msg.Binds|$bind:

    # Save each Bind
    - SAVE|Binds@Vault:
        Broker: $.Msg.From
        Bind: $bind.Bind
        Schema: $bind.Schema
        User: $chat.User

# Continue the Chat
- REEL|$hook:
    $.Msg.Binds
```

Needs||
|-|-
| [Commands ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... ⌘ commands/⌘ Command.md>) | [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/GET ⏬ item.md>) [`PARALLEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... control ▶️/PARALLEL *️⃣.md>) [`REEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... control ▶️/REEL 🎣.md>) [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/SAVE 💾 item.md>) [`VERIFY`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages/VERIFY 🔐 msg.md>)
| [Messages 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Bound@Vault`](<../../Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)
| [Placeholders 🧠](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages/$.Msg 📨.md>)
|