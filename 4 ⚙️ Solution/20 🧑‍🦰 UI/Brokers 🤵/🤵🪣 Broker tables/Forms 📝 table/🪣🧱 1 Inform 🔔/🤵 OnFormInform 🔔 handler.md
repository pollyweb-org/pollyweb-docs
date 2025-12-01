# 🤵 OnFormInform 🔔 handler

> About
* Part of the [`Broker.Forms` 🪣 table](<../🪣 Forms/🤵 Broker.Forms 🪣 table.md>)
* Part of the [`Inform` ⏩ flow](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)
* Reacts to [`Inform@Broker` 📃 handler](<../../../🤵🅰️ Broker methods/Share 💼 Inform 💼🐌🤵/🤵 Inform 📃 handler.md>)

<br/>

## Chat

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🤵 [Broker](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 [Continue?](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/INFORM 📝/📝 INFORM ⌘ cmd.md>) [Yes, No] <br/> **Order a meal**<br/>- your curator orders 🧚<br/> - your payer pays 💳  | > Yes

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
        Form: $Form.Name
        Domain: $From.Consumer
        Language: $Form.Chat.Language

# Set the chat language and context
- CHAT|$Form.Chat 

# Ask for confirmation to proceed
- CONFIRM: 
    Text: >
        Continue?
        **´{$form.Title}´**
        ´{$form.Steps.Purpose}´
    Details: ´$form.Details´

# Set the form on the Chat
- SAVE|$Form.Chat:
    Form: $Form.ID
    FormSchemas: $form.Steps.Schema

# Progress the state
- SAVE|$Form:
    Schemas: $form.Steps.Schema
    .State: INFORMED
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | {{CHAT}} [`INFO`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)  [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Forms`](<../🪣 Forms/🤵 Broker.Forms 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Form@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Form/🕸 Form 🚀 call.md>)
|