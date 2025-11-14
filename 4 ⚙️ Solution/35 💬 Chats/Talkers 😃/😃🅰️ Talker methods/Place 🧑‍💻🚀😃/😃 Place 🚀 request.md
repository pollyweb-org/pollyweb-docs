# 🧑‍💻🚀😃 Write @ Hoster

> Implementation 
* Implements [Hoster ☁️ helper domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>)
* Implemented by the [`Place` 📃 handler](<😃 Place 📃 handler.md>)

> Flow
* Part of [`Async` ⏩ flow](<../../😃⏩ Talker flows/Run Async Tasks 😃⏩📦/😃 Async ⏩ flow.md>) flow
* Paired with the [`Placed@Talker` 🅰️ method](<../Placed 🧑‍💻🚀😃/😃 Placed 🚀 request.md>)

> Purpose 
* Writes a value to a [Holder 🧠](<../../../Scripts 📃/Holder 🧠.md>).


<br/>

## Synchronous Request 🚀


```yaml
Header:
    From: any-host.dom
    To: any-hoster.dom
    Subject: Place@Talker

Body:
    Hook: <hook-uuid>
    Holder: $p
    Value: {A:1, B:2}
    Reason: Any reason...
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header    |`From`|string| [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name
|           |`To`|string| [Hoster ☁️ domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) name
|           | `Subject`     | string    | `Place@Talker`
| Body      | `Hook`      | uuid      | Handling context | [`Handle@Hosted`](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Handle 😃🐌📦/📦 Handle 🐌 msg.md>)
|           | `Holder` | string    | [Holder 🧠](<../../../Scripts 📃/Holder 🧠.md>) name
|           | `Value`       | any    | Any value to write
|           | `Reason`      | string | For traceability
|