# 👥🚀🪵 Start @ Logger

> Implementation
* Implements the [Logger 🪵 helper domain](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>)
* Implemented by the [`Start` 📃 handler](<🪵 Start 📃 handler.md>)

> Purpose
* Initiates a log thread.

## Synchronous Call 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-logger.dom
    Subject: Start@Logger

Body:
    Delete: 1 day
    Groups: 
        - my-type-1
        - my-type-2
```


|Object|Property|Type|Description|Destination
|-|-|-|-|-
| Header    |`From`|text| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|           |`To`|text| [Logger 🪵](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>)
|           | `Subject`     | string    | `Start@Logger`
| Body    | `Delete`     | string    | [`.Minus`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Minus}.md>) log retention
|         | `Group`    | string[]  | Only save these log groups | [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|

<br/>

## Synchronous Response

```yaml
Thread: <thread-uuid>
```

||Property|Type|Description|Purpose
|-|-|-|-|-
|  | `Thread`     | uuid    | Created log thread | [`Log@`](<../Log 👥🐌🪵/🪵 Log 🐌 msg.md>) [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 call.md>)
|