# 😃🚀📦 Parse @ Hosted

> Purpose
 
* Handles a custom [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>)


## Synchronous Request 🚀

```yaml
Header:
    From: any-talker.dom
    To: any-hosted.dom

Body:
    Command:
        # Example command
        ALARM|$time$:
            MyHandler: 
                A: 1
                B: 2
```

|Object|Property|Type|Description
|-|-|-|-
| Header    |`From`|domain| [Talker 😃 domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)
|           |`To`|domain| [Hosted 📦 domain](<../../📦👥 Hosted domain.md>)
| | `Subject`| string | `Parse@Hosted` |
| Body      | `Command`     | any    | [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) to parse
|

## Synchronous Response

```yaml
Run:
    Script: .ALARM
    Inputs:
        When: $time
        Call: MyHandler
        With: {A:, B:2}
```

|Object|Property|Type|Description
|-|-|-|-
| Run       | `Script`      | string    | [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) to run
|           | `Inputs`      | map    | Inputs for the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>)
|