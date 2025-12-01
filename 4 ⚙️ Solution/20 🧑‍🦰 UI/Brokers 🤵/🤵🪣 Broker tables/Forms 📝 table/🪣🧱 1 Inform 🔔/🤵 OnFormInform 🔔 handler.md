# 🤵 OnFormInform 🔔 handler

> About
* Part of the [`Broker.Forms` 🪣 table](<../🪣 Forms/🤵 Broker.Forms 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnFormInform ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnFormInform:


# Call Form@Graph
- SEND >> $form:
    Header: 
        To: $.Hosted.Graph
        Subject: Form@Graph
    Body:
        Form: $.Msg.Form
        Domain: $.Msg.From
        Language: $chatter.Chat.Language

# Inform the user
- INFO: 
    Text: ...

# Ask for confirmation to proceed
- CONFIRM|Ready to continue?

# Progress the state
- SAVE|$Form:
    .State: INFORMED
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats` 🪣 table](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
|