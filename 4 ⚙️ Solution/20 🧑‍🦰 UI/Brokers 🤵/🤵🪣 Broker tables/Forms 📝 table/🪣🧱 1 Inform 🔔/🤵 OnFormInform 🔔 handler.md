# 🤵 OnFormInform 🔔 handler

> About
* Part of the [`Broker.Forms` 🪣 table](<../🪣 Forms/🤵 Broker.Forms 🪣 table.md>)
* Part of the [`Inform` ⏩ flow](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)
* Reacts to [`Inform@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 📃 handler.md>)

<br/>

## Chat

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🤵 [Broker](<../../../🤵/🤵 Broker 🤲 helper.md>) | 🫥 [Continue?](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) [Yes, No] <br/> **Order a meal**<br/>- your curator orders 🧚<br/> - your payer pays 💳  | > Yes

<br/>

## Diagram

![alt text](<🤵 OnFormInform ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnFormInform:

# Call Form@Graph
- GRAPH Form >> $form:
    Form: $Form.Name.Require
    Domain: $Form.Consumer.Require
    Language: $Form.Chat.Language.Require

# Set the chat language and context
- CHAT $Form.Chat 

# If there are many steps
- IF: form.Steps.AreMany

- THEN: # ask for confirmation
    - CONFIRM: 
        Text: >
            Ready to continue?
            **´{$form.Title.Require}´**
            ´{$form.Steps.Purpose.Require}´
        Details: ´$form.Details´

- ELSE: # otherwise, just inform
    - INFO:
        Text: 
            Flow: ´{$form.Title.Require}´
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
    STATE: INFORMED
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>)  [`GRAPH`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/GRAPH 🕸/🕸 GRAPH ⌘ cmd.md>) [`INFO`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Forms`](<../🪣 Forms/🤵 Broker.Forms 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.AreMany`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/AreMany ⓕ.md>) [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Form@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Form/🕸 Form 🚀 call.md>)
|