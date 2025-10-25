# 🤵📃 Translate 

[Script 📃](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Language@Broker`](<../🧑‍🦰🐌🤵 Language.md>) method.

## Script

```yaml
# Verify the required inputs
- ASSERT:
    - $.Msg.Language

- SEND:
    To: $.Settings.Graph
    Subject: Translate@Graph
    Language: $.Msg.Language

- RUN:
    - UpdateChats
    - UpdateBinds
    - UpdateTokens
```

|Needs||
|-|-
| [Commands ⌘](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`SEND`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>) [`RUN`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RUN ▶️/RUN ▶️.md>)
| [Messages 📨](<../../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Translate@Graph`](<../../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Scripts 📃](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) | - [`Update Chats` 📃 script](<../../../../🤵⏩ Broker flows/Update Chats 💬/.📎 Assets/Update Chats 📃 script.md>) <br/> - [`Update Binds` 📃 script](<../../../../🤵⏩ Broker flows/Update Binds 🔗/.📎 Assets/Update Binds 📃 script.md>) <br/> - [`Update Tokens` 📃 script](<../../../../🤵⏩ Broker flows/Update Tokens 🎫/.📎 Assets/Update Tokens 📃 script.md>)
|