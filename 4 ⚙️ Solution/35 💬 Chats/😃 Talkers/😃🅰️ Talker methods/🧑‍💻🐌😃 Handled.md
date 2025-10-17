# 🧑‍💻🐌☁️ Handled @ Hoster

> Returns a [{Function} 🐍](<../😃⚙️ Talker cmds/for data/{Function} 🐍.md>) evaluation.

> Implements [Hoster ☁️ helper domain](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>)

> Part of [😃⏩🧑‍💻 Handle @ Talker](<../😃⏩ Talker flows/😃⏩🧑‍💻 Handle 🐍.md>) flow

> Receives the response from [Handle@Hosted](<../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/😃🐌📦 Handle.md>)

<br/>

## Async Message 🐌



```yaml
Header:
    From: any-host.dom
    To: any-hoster.dom
    Subject: Handled@Talker
    
Body:
    Callback: <callback-uuid>
    Response: {A:1, B:2}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) name
|           | `To`          | string    | [Hoster ☁️ domain](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) name
|           | `Subject`     | string    | `Handled@Talker`
| Body      | `Callback`    | uuid      | Call back from [`Handle@Hosted`](<../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/😃🐌📦 Handle.md>)
|           | `Response`    | any       | Response to [`Handle@Hosted`](<../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/😃🐌📦 Handle.md>)
|