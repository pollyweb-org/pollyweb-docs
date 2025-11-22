# 😃🐌🧑‍💻 Handle @ Hosted

> Implements [Hosted 📦 domain](<../../📦👥 Hosted domain.md>)

> Flow: 

* Part of the [`Handle` ⏩ flow](<../../../../35 💬 Chats/Talkers 😃/😃⏩ Talker flows/Run Sync Functions 😃⏩📦/😃 Call ⏩ flow.md>) 
* Followed by the [`Handled@Talker` 🅰️ method](<../../../../35 💬 Chats/Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>) 

> Purpose: 

* Handles a [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) evaluation.


<br/>

## Async Message 🐌

```yaml
Header:
    From: any-hoster.dom
    To: any-domain.dom
    Subject: Handle@Hosted
    
Body:
    Hook: <hook-uuid>
    Function: my-function
    Inputs: 
        - {A:1, B:2}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    |`From`|text| [Hoster ☁️ domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️ Hoster helper/☁️🤲 Hoster helper.md>) name
|           |`To`|text| [Hosted 📦 domain](<../../📦👥 Hosted domain.md>) name
|           | `Subject`     | string    | `Handle@Hosted`
| Body      | `Hook`    | uuid      | Hook for [`Handled@Talker`](<../../../../35 💬 Chats/Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>)
|           | `Function`    | string    | Name of the [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) to evaluate
|           | `Arguments`   | array     | Array of [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) arguments 
|