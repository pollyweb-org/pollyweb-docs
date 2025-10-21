# 🤵📃 Offer

> [Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements the [`Offer@Broker` 🅰️ method](<../🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🎴🐌🤵 Offer.md>)

<br/>

## Script

```yaml
📃 Offer:

# Verify the Issuer's message
- VERIFY|$.Msg

# Get the Chat
- GET >> $chat:
    Pool: Chats@Broker
    Key: $.Msg.Chat

# Only allow offers from the Host
- ASSERT:
    $.Msg.From: $chat.Host

# Translate the Issuer and Schema
- SEND >> $translation:
    To: $.Settings.Graph
    Subject: Translate@Graph
    Domain: $.Msg.From
    Schema: $.Msg.Schema

# Save the Offer
- SAVE|Tokens@Broker:
    Hook: $.Msg.Hook
    Issuer: $.Msg.From
    Issuer$: $translation.Domain
    Schema: $.Msg.Schema
    Schema$: $translation.Schema
    Starts: $.Msg.Starts
    Expires: $.Msg.Expires

# Update the domain translation
- GET >> $domain:
    OnMissing:
- SAVE|$domain
```

Needs||
-|-
[Commands ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | [`ASSERT`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/SAVE 💾 item.md>) [`SEND`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) [`VERIFY`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>)
| [Messages 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Translate@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Placeholders 🧠](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/$Placeholder 🧠.md>) | [`$.Settings`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Settings 🎛️.md>)
| [Datasets 🪣](<../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Domain`](<../🤵🪣 Broker tables/🤵🪣 Domains.md>) [`Tokens`](<../🤵🪣 Broker tables/🤵🪣 Tokens.md>)
|