<!-- TODO -->

# 🗄️📃 Collect handler

> Part of the [Vault 🗄️ domain](<../🗄️🎭 Vault role.md>)


## Script


```yaml
# Verify the signature
- VERIFY|$.Msg

# Get the collect
- GET >> $collect:
    Set: Collects@Vault
    Key: $.Msg.Collect

# Assert the Consumer
- ASSERT:
    $.Msg.From: $collect.Consumer

# Return the response
- REEL:
    $collect.Data
```

| [Command ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/⌘ Command.md>) | Purpose
|-|-
| 🚦 [`ASSERT`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦.md>) | Assert if it's the right [Consumer 💼](<../../Consumers 💼/💼🎭 Consumer role.md>)
| ⏬ [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) | Get the [Collect 🪣](<../🗄️🪣 Vault tables/🗄️🪣 Collects.md>) from [`Consume@Consumer`](<../../Consumers 💼/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>)
| 🎣 [`REEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/REEL/REEL 🎣.md>) | Respond to the [Synchronous Request 🚀](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Sync Requests 🚀.md>)
| 🔐 [`VERIFY`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>) | Verify the domain [Signature 🔏](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Signatures 🔏.md>) of the [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>)
|

<br/>

|Needs||
|-|-
|