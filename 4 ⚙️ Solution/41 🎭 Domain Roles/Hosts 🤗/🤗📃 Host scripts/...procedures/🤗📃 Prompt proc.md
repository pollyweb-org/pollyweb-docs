# 🤗📃 Prompt  script

> Implements [`Prompted@Hosted`](<../../🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>)

## Script

```yaml
📃 Prompt@Host:

# Save the prompt.
- SAVE|Prompts@Host >> $prompt:
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
    To: $.Chat.Broker
    Subject: Prompt@Broker
    Chat: $.Chat.Chat
    Prompt: $saved.Prompt
    Expires: .Add(.Now, 1 minute)

# TODO: Wait for what?
- WAIT
```


Needs ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... ⌘ commands/⌘ Command.md>) | [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/SAVE 💾 item.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages/SEND 📬 msg.md>) [`WAIT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... control ▶️/WAIT ⏸️.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... placeholders 🧠/$Placeholder 🧠.md>) | [`$.Chat`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... placeholders 🧠/$.Chat 💬.md>)
|