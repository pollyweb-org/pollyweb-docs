# 🤗📃 Prompt  script

> Implements [`Prompted@Hosted`](<../../🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted/🧑‍🦰🚀🤗 Prompted.md>)

## Script

```yaml
📃 Prompt@Host:

# Assert inputs:
- ASSERT:
    AllOf: $:Statement, $:Format
    Texts: $:Statement, $:Details
    Lists: $:Options
    UUIDs: $:Appendix  

# Stage the prompt.
- SAVE|Prompts@Host >> $prompt:
    Metadata:
        Prompt: .UUID
        PublicKey: $.Chat.PublicKey
    Prompted:
        Format: $:Format
        Statement: $:Statement
        Options: $:Options
        Details: $:Details
        Appendix: $:Appendix    

# Send it to the Broker.
- SEND:
    Header:
        To: $.Chat.Broker
        Subject: Prompt@Broker
    Body:
        Chat: $.Chat.Chat
        Prompt: $saved.Metadata.Prompt
        Expires: .Add(.Now, 5 minute)

# TODO: Wait for what?
- WAIT
```


Needs ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>) [`WAIT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/WAIT ⏸️/WAIT ⏸️.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Chat`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$.Chat 💬.md>)
|