# 🤵📃 Offer

> [Script 📃](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Offer@Broker` 🅰️ method](<../🎴🐌🤵 Offer.md>)

> Part of the [`Save Token` 👉 flow](<../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉🎴 Save token.md>).
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
    Header:
        To: $.Settings.Graph
        Subject: Translate@Graph
    Body:
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

> Run [`Update Domain` 📃 script](<../../../🤵📃 Broker scripts/...procedures/🤵📃 Update Domain 🪣.md>)

<!-- TODO: Finish the detail -->

```yaml
- CONFIRM|Save token? >> $saved:
    Details: 
```

<br/>

Needs||
-|-
[Commands ⌘](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`GET`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) [`SAVE`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>) [`SEND`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>) [`VERIFY`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Domain`](<../../../🤵🪣 Broker tables/🤵🪣 Domains table.md>) [`Tokens`](<../../../🤵🪣 Broker tables/🤵🪣 Tokens table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Placeholders 🧠](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>) [`$.Settings`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Settings 🎛️.md>)
| [Scripts 📃](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) | [`Update Domain`](<../../../🤵📃 Broker scripts/...procedures/🤵📃 Update Domain 🪣.md>)
|