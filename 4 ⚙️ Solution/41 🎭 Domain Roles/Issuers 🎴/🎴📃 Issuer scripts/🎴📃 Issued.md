# 🎴📃 Issued

[Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements the [`Issued@Issuer` 🅰️ method](<../🎴🅰️ Issuer methods/🧑‍🦰🚀🎴 Issued.md>).

<br/>

## Scripts

```yaml
# Get the Chat data
- GET|Hooks@Talker|$.Msg.Hook >> $hook

# Verify the Message
- VERIFY|$.Msg

# Continue the Talker
- REEL|$hook
```

Needs||
|-|-
| [Commands ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) [`REEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>) [`VERIFY`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>)
| [Datasets 🪣](<../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats@Host`](<../../Hosts 🤗/🤗🪣 Host tables/🤗🪣 Chats 💬.md>)
| [Placeholders 🧠](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/$Placeholder 🧠.md>) | [`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>)
|