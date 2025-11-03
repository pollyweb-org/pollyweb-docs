<!-- TODO -->

# Async Message 🐌

```yaml
Header:
    From: any-domain.dom
    To: any-logger.dom
    Subject: Log@Logger

Body:
    Thread: <uuid>
    Group: my-group
    Blame: my-script
    Type: ERROR
    Log: {...}
```

|Object|Property|Type|Description|Origin
|-|-|-|-
| Header    |`From`|domain| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|           |`To`|domain| [Logger 🪵 helper domain](<../../🪵 Logger helper/🪵 Logger 🤲 helper.md>)
|           | `Subject`     | string    | `Log@Logger`