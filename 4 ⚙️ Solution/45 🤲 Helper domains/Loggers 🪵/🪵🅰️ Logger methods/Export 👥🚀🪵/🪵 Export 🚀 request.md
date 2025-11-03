# 👥🚀🪵 Export

> Implementation
* Implements the [Logger 🪵 helper domain](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>)

> Purpose
* Exports previously sent logs.

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-logger.dom
    Subject: Export@Logger

Body:
    Thread: <thread-uuid>       # Optional
    Groups:                     # Optional
        - my-group-1
        - my-group-2
    Blame: my-script            # Optional
    Level: ERROR                # Optional

    # Time filters
    Period: 5 minutes           # Optional
    Interval:                   # Optional
        - 2025-10-10T13:00:00Z
        - 2025-10-10T14:00:00Z
```
|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header    |`From`|domain| [`domain`](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 request.md>)
|           |`To`|domain| [Logger 🪵](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>) | [`Start@`](<../Start 👥🚀🪵/🪵 Start 🚀 request.md>)
|           | `Subject`     | string    | `Export@Logger`
| Body      | `Thread`     | uuid    | Optional Thread ID | [`Log@`](<../Log 👥🐌🪵/🪵 Log 🐌 msg.md>)
|         | `Groups`    | string[]  | Optional groups | [`Log@`](<../Log 👥🐌🪵/🪵 Log 🐌 msg.md>)
|         | `Blame`     | string    | Optional script name | [`Log@`](<../Log 👥🐌🪵/🪵 Log 🐌 msg.md>)
|         | `Period`    | string    | [`.Minus`](<../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.Minus}.md>) time period | [`Log@`](<../Log 👥🐌🪵/🪵 Log 🐌 msg.md>)
|         | `Interval`  | string[]  | Start and end times | [`Log@`](<../Log 👥🐌🪵/🪵 Log 🐌 msg.md>)
|

## Synchronous Response

```yaml
Threads:
    - Thread: <thread-uuid>
      Logs: 

Entries: 
    - Sent: 2025-10-10T13:45:23.123Z
      Details: {...}
```