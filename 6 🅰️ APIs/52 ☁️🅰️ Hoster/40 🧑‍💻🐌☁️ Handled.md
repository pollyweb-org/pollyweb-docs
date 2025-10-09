# 🧑‍💻🐌☁️ Handled @ Hoster

> Implements [Hoster ☁️ helper domain](<../../9 😃 Talkers/90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>)

> Part of [☁️⏩🧑‍💻 Handle @ Hoster](<../../5 ⏩ Flows/79 😃⏩ Talkers/20 😃⏩🧑‍💻 Handle.md>) flow

> Receives the response from [Handle@Hosted](<../51 🧑‍💻🅰️ Hosted/01 ☁️🐌🧑‍💻 Handle.md>)

<br/>

## Async Message 🐌



```yaml
Header:
    From: any-host.com
    To: any-hoster.com
    Subject: Handled@Hoster
    
Body:
    Callback: <callback-uuid>
    Response: {A:1, B:2}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) name
|           | `To`          | string    | [Hoster ☁️ domain](<../../9 😃 Talkers/90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>) name
|           | `Subject`     | string    | `Handled@Hoster`
| Body      | `Callback`    | uuid      | Call back from [`Handle@Hosted`](<../51 🧑‍💻🅰️ Hosted/01 ☁️🐌🧑‍💻 Handle.md>)
|           | `Response`    | any       | Response to [`Handle@Hosted`](<../51 🧑‍💻🅰️ Hosted/01 ☁️🐌🧑‍💻 Handle.md>)
|