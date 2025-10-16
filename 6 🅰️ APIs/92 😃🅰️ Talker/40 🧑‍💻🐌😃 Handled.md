# 🧑‍💻🐌☁️ Handled @ Hoster

> Returns a [{Function} 🐍](<../../9 😃 Talkers/30 🗃️ Talker data/12 🐍 {Function}.md>) evaluation.

> Implements [Hoster ☁️ helper domain](<../../4 ⚙️ Solution/45 🤲 Helper domains/55 ☁️ Hosters/☁️🤲 Hoster helper.md>)

> Part of [😃⏩🧑‍💻 Handle @ Talker](<../../5 ⏩ Flows/79 😃⏩ Talkers/20 😃⏩🧑‍💻 Handle 🐍.md>) flow

> Receives the response from [Handle@Hosted](<../../4 ⚙️ Solution/90 👷 Build/91 📦 Hosteds/📦🅰️ Hosted methods/😃🐌📦 Handle.md>)

<br/>

## Async Message 🐌



```yaml
Header:
    From: any-host.com
    To: any-hoster.com
    Subject: Handled@Talker
    
Body:
    Callback: <callback-uuid>
    Response: {A:1, B:2}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) name
|           | `To`          | string    | [Hoster ☁️ domain](<../../4 ⚙️ Solution/45 🤲 Helper domains/55 ☁️ Hosters/☁️🤲 Hoster helper.md>) name
|           | `Subject`     | string    | `Handled@Talker`
| Body      | `Callback`    | uuid      | Call back from [`Handle@Hosted`](<../../4 ⚙️ Solution/90 👷 Build/91 📦 Hosteds/📦🅰️ Hosted methods/😃🐌📦 Handle.md>)
|           | `Response`    | any       | Response to [`Handle@Hosted`](<../../4 ⚙️ Solution/90 👷 Build/91 📦 Hosteds/📦🅰️ Hosted methods/😃🐌📦 Handle.md>)
|