# 🤵📃 Translate 

[Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Translate@Broker`](<../../🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/Translate/🧑‍🦰🐌🤵 Translate.md>) method.

## Script

```yaml
# Verify the required inputs
- ASSERT:
    - $.Msg.Language

- SEND:
    To: $.Settings.Graph
    Subject: Translate@Graph
    Language: $.Msg.
```

|Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|