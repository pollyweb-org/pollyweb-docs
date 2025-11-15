# 👥🐌🪵 Stop @ Logger

> Implementation
* Implements the [Logger 🪵 helper domain](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>)
* Implemented by the [`Stop` 📃 handler](<🪵 Stop 📃 handler.md>)

> Purpose
* Stops a log thread.

## Async Message 🐌

```yaml
Header:
    From: any-domain.dom
    To: any-logger.dom
    Subject: Stop@Logger

Body:
    Thread: <uuid>
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header    |`From`|string| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 call.md>)
|           |`To`|string| [Logger 🪵](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>) | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 call.md>)|           | `Subject`     | string    | `Log@Logger`
| Body      | `Thread`     | uuid    | Log thread ID | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 call.md>) | [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|| `Group`    | string    | Optional log group | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 call.md>) | [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|| `Blame`     | string    | Optional sender || [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|| `Level`      | string    | `INFO` `WARNING` `ERROR` || [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|| `Text`| string | Optional log text ||[`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|| `Details`   | any       | Optional log content || [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|