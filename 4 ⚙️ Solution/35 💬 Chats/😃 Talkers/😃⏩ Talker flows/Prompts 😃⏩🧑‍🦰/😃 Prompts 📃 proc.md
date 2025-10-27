# 🤗📃 Prompt  script

> Implements [`Prompted@Hosted`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>)

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
- SAVE|HostPrompts >> $prompt:
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

# Block and wait for an answer
- IF|In($:Format, [INFO,FAILURE,SUCCESS,TEMP]):
    Then: HOOK|$saved.Metadata.Prompt
    Else: WAIT|$saved.Metadata.Prompt
```


Needs ||
|-|-
| [Commands ⌘](<../../😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`SAVE`](<../../😃⚙️ Talker cmds/...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg ⌘ cmd.md>) [`WAIT`](<../../😃⚙️ Talker cmds/...control ▶️/WAIT ⏸️/WAIT ⏸️ ⌘ cmd.md>)
| [{Functions} 🐍](<../../😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>) | [`{.In}`](<../../😃⚙️ Talker cmds/...functions 🐍/🔩 {.In}.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Prompt@Broker` 🅰️ method](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
| [Placeholders 🧠](<../../😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Chat`](<../../😃⚙️ Talker cmds/...placeholders 🧠/$.Chat 💬.md>)
|