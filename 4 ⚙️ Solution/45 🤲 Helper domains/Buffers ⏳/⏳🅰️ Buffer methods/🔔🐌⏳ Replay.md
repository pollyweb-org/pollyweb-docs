# 🔔🐌⏳ Replay @ Buffer

> Replays historical successfully handled messages.

> Implements a [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>)

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-subscriber.dom
    To: any-buffer.dom
    Subject: Replay@Buffer
Body:
    Queue: <queue-uuid>
    Starting: 2025-10-10T13:45:00.000Z  # Optional
    Ending: 2025-12-31T00:00:00.000Z    # Optional
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string| [Subscriber 🔔 domain](<../../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>) name
||`To`|string| [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>) name
||`Subject`| string | `Replay@Buffer`
|Body| `Queue`| uuid | Queue from [`Queue@Buffer`](<🔔🐌⏳ Queue.md>) |
| |`Starting`| timestamp | Start date and time (optional)
| |`Ending` | timestamp | Finish date and time (optional)
|