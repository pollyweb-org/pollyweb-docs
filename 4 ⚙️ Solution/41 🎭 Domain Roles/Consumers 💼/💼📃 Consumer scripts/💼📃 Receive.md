# 💼📃 Receive

[Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements [`Receive@Consumer`](<../💼🅰️ Consumer methods/🧑‍🦰🐌💼 Receive.md>)

<br/>

## Script

```yaml
# Resolve the callback
- GET|Hooks@Talker|$.Msg.Hook >> $hook

# Get the chat
- GET|Chats@Host|$hook.Chat >> $chat

# Verify the Wallet signature
- VERIFY|$.Msg|$chat.PublicKey

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
| [Commands ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | [`REEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>)
| {{}}
| [Placeholders 🧠](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/$Placeholder 🧠.md>) | [`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>)
|