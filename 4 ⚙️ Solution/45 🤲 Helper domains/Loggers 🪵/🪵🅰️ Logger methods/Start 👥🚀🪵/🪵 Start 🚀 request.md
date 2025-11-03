# 👥🚀🪵 Start @ Logger

> Implementation
* Implements the [Logger 🪵 helper domain](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>)


> Purpose
* Initiates a log thread.

## Synchronous Request

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
| Header    |`From`|domain| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|           |`To`|domain| [Logger 🪵](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>)
|           | `Subject`     | string    | `Start@Logger`
| Body    | `Delete`     | string    | [`.Minus`](<../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.Minus}.md>) log retention
|         | `Group`    | string[]  | Only save these log groups | [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 request.md>)
|

<br/>

## Synchronous Response

```yaml
Thread: <thread-uuid>
```

||Property|Type|Description|Purpose
|-|-|-|-|-
|  | `Thread`     | uuid    | Created log thread | [`Log@`](<../Log 👥🐌🪵/🪵 Log 🐌 msg.md>) [`Export@`](<../Export 👥🚀🪵/🪵 Export 🚀 request.md>)
|