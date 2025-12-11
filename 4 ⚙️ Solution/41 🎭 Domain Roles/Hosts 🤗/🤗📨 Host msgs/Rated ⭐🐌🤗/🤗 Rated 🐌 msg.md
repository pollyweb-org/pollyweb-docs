# ⭐🐌🤗 Rated@Host

> About
* Part of [Host 🤗 domain](<../../🤗 Host role/🤗🎭 Host role.md>)

<br/>

## Asynchronous Message ⭐🐌

```yaml
Header:
    From: any-reviewer.dom
    To: any-host.dom
    Subject: Rated@Host

Body:
    Rate: <rate-uuid>   # for replying
    Form: AnyForm       # last Inform@Broker, if any
    Stars: 4            # from 1 to 5
    Feedback: Could be faster and cheaper.
```

|Object|Property|Type|Description | Origin
|-|-|-|-|-
| Header    |`From`|text| {{Reviewer}} name
| |`To`|text| {{Host}} name | 
| | `Subject`     | string    | `Rated@Host`
| Body      | `Rate`    | uuid      | Reply to {{}}