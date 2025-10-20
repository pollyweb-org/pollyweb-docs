> [Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements the [`Offer@Broker` 🅰️ method](<../🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🎴🐌🤵 Offer.md>)


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

# Translate the Issuer and the Schema
- SEND >> $translations:
    To: $.Settings.Graph
    Subject: Translate@Graph
    Domain: $.Msg.From
    Schema: $.Msg.Schema

# Save the Offer
- SAVE|Tokens:
    Hook: $.Msg
    Schema: any-authority.dom/ANY-SCHEMA:1.0
    Starts: 2018-12-10T13:45:00.000Z
    Expires: 2018-12-10T13:45:00.000Z

```

Needs||
-|-
Commands | [`ASSERT`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/SAVE 💾 item.md>) {{SEND}} [`VERIFY`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>)
