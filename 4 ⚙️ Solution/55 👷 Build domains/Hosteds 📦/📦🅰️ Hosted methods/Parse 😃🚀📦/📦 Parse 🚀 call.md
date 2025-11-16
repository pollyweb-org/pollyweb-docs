# 😃🚀📦 Parse @ Hosted

> Purpose
 
* Handles a custom [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)


## Synchronous Call 🚀

```yaml
Header:
    From: any-talker.dom
    To: any-hosted.dom

Body:
    Command:
        # Example command
        ALARM|$time:
            MyHandler: 
                A: 1
                B: 2
```

|Object|Property|Type|Description
|-|-|-|-
| Header    |`From`|text| [Talker 😃 domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)
|           |`To`|text| [Hosted 📦 domain](<../../📦👥 Hosted domain.md>)
| | `Subject`|text| `Parse@Hosted` |
| Body      | `Command`     | any    | [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) to parse
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
| Run       | `Script`      | string    | [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to run
|           | `Inputs`      | dict    | Inputs for the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
|