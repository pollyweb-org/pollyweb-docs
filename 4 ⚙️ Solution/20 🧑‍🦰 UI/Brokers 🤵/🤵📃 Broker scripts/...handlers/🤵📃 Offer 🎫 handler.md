# 🤵📃 Offer

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements the [`Offer@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🎴🐌🤵 Offer.md>)

> Part of the [`Save Token` 👉 flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉🎴 Save token.md>).
> 
<br/>

## Script

```yaml
📃 Offer:

# Verify the Issuer's message
- VERIFY|$.Msg

# Assert the required inputs
- ASSERT|$.Msg:
    - AllOf: Chat, Hook, Schema
    - UUIDs: Chat, Hook
    - Texts: Schema
    - Times: Starts, Expires

# Verify the dates
- ASSERT:
    - $.Msg.Starts < $.Msg.Expires

# Get the Chat
- GET >> $chat:
    Set: Chats@Broker
    Key: $.Msg.Chat

# Only allow offers from the Host
- ASSERT:
    - $.Msg.From ~= $chat.Host

# Translate the Issuer and Schema
- SEND >> $translation:
    To: $.Settings.Graph
    Subject: Translate@Graph
    Domain: $.Msg.From
    Schema: $.Msg.Schema

# Save the Offer
- SAVE|Offers@Broker:
    .Timeout: 1 hour
    Hook: $.Msg.Hook
    Issuer: $.Msg.From
    Issuer$: $translation.Domain
    Schema: $.Msg.Schema
    Schema$: $translation.Schema
    Starts: $.Msg.Starts
    Expires: $.Msg.Expires

# Update the domain translation
- RUN|UpdateDomain:
    Domain: $.Msg.From
    Domain$: $translation.Domain
```

> Run [`Update Domain` 📃 script](<../...procedures/🤵📃 Update Domain 🪣.md>)

<!-- TODO: Finish the detail -->

```yaml
- CONFIRM|Save token? >> $saved:
    Details: 
```

<br/>

Needs||
-|-
[Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets/GET ⏬ item.md>) [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/SAVE 💾 item.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/$SEND 📬 msg.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Domain`](<../../🤵🪣 Broker tables/🤵🪣 Domains table.md>) [`Tokens`](<../../🤵🪣 Broker tables/🤵🪣 Tokens table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) [`$.Settings`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Settings 🎛️.md>)
| [Scripts 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) | [`Update Domain`](<../...procedures/🤵📃 Update Domain 🪣.md>)
|