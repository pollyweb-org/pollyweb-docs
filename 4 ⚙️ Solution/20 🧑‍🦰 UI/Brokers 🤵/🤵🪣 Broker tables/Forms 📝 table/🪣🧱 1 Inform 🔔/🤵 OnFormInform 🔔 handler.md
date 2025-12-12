# 🤵 OnFormInform 🔔 handler

> About
* Part of the [`Broker.Forms` 🪣 table](<../🪣 Forms/🤵 Broker.Forms 🪣 table.md>)
* Part of the [`Inform` ⏩ flow](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)
* Reacts to [`Inform@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 📃 handler.md>)

<br/>

## Chat

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🤵 [Broker](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 [Continue?](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) [Yes, No] <br/> **Order a meal**<br/>- your curator orders 🧚<br/> - your payer pays 💳  | > Yes

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
        Form: $Form.Name.Require
        Domain: $Form.Consumer.Require
        Language: $Form.Chat.Language.Require

# Set the chat language and context
- CHAT $Form.Chat 

# If there are many steps...
- IF form.Steps.AreMany:

    Then: # ...ask for confirmation to proceed 
        - CONFIRM: 
            Text: >
                Ready to continue?
                **´{$form.Title.Require}´**
                ´{$form.Steps.Purpose.Require}´
            Details: ´$form.Details´

    Else: # ...otherwise, just inform
        - INFO:
            Text: Flow: ´{$form.Title.Require}´
            Details: > 
                Steps: 
                ´{$form.Steps.Purpose.Require}´
                ´$form.Details´

# Set the form on the Chat
- SAVE $Form.Chat:
    Form: $Form.ID
    FormSchemas: $form.Steps.Schema

# Progress the state
- SAVE $Form:
    Schemas: $form.Steps.Schema
    .State: INFORMED
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`INFO`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)  [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Forms`](<../🪣 Forms/🤵 Broker.Forms 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.AreMany`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/AreMany ⓕ.md>) [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Form@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Form/🕸 Form 🚀 call.md>)
|