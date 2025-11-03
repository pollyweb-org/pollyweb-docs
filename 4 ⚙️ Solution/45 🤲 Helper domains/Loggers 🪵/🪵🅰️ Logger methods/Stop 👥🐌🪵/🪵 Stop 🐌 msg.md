# 👥🐌🪵 Log @ Logger

> Implementation
* Implements the [Logger 🪵 helper domain](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>)

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
| Header    |`From`|domain| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 request.md>)
|           |`To`|domain| [Logger 🪵](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>) | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 request.md>)|           | `Subject`     | string    | `Log@Logger`
| Body      | `Thread`     | uuid    | Log thread ID | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 request.md>) | [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 request.md>)
|| `Group`    | string    | Optional log group | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 request.md>) | [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 request.md>)
|| `Blame`     | string    | Optional sender || [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 request.md>)
|| `Level`      | string    | `INFO` `WARNING` `ERROR` || [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 request.md>)
|| `Text`| string | Optional log text ||[`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 request.md>)
|| `Details`   | any       | Optional log content || [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 request.md>)
|