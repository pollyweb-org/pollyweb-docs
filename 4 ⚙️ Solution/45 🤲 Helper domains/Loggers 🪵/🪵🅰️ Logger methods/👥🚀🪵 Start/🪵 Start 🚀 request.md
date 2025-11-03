<!-- TODO -->


# 👥🚀🪵 Start @ Logger

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
    Types: 
        - my-type-1
        - my-type-2
```


|Object|Property|Type|Description
|-|-|-|-
| Header    |`From`|domain| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|           |`To`|domain| [Logger 🪵 helper domain](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>)
|           | `Subject`     | string    | `Start@Logger`
| Body    | `Delete`     | string    | [`.Add`](<../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.Add}.md>) log retention
|         | `Types`    | string[]  | Only save these log types

<br/>

## Synchronous Response

```yaml
Thread: <thread-uuid>
```

||Property|Type|Description|Purpose
|-|-|-|-|-
|  | `Thread`     | uuid    | Created log thread | [`Log@Logger`](<../👥🐌🪵 Log/🪵 Log 🐌 msg.md>)