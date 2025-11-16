# 👥🐌🪵 Log @ Logger

> Implementation
* Implements the [Logger 🪵 helper domain](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>).
* Implemented by the [`Log` 📃 handler](<🪵 Log 📃 handler.md>).

> Purpose
* Saves a log message.

## Async Message 🐌

```yaml
Header:
    From: any-domain.dom
    To: any-logger.dom
    Subject: Log@Logger

Body:
    Thread: <uuid>
    Group: my-group     # Optional
    Blame: my-script    # Optional
    Level: ERROR        # Optional, defaults to INFO
    Text: bla, bla...   # Optional, defaults to details
    Details: {...}      # Optional
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header    |`From`|text| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 call.md>)
|           |`To`|text| [Logger 🪵](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>) | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 call.md>)|           | `Subject`     | string    | `Log@Logger`
| Body      | `Thread`     | uuid    | Log thread ID | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 call.md>) | [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|| `Group`    | string    | Optional log group | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 call.md>) | [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|| `Blame`     | string    | Optional sender || [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|| `Level`      | string    | `INFO` `WARNING` `ERROR` || [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|| `Text`|text| Optional log text ||[`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|| `Details`   | any       | Optional log content || [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|