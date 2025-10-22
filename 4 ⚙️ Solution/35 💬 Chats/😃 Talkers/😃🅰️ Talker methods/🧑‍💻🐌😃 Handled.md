# 🧑‍💻🐌😃 Handled @ Talker


> Implements [Hoster ☁️ helper domain](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>)


> Flow: 

* Part of the [`Handle` ⏩ flow](<../😃⏩ Talker flows/😃⏩🧑‍💻 Handle 🐍.md>) flow
*  Receives async responses from the [`Handle@Hosted`](<../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/😃🐌📦 Handle.md>) method.


> Purpose: 

* Returns a [{Function} 🐍](<../😃⚙️ Talker cmds/for data/{Function} 🐍.md>) evaluation.


<br/>

## Async Message 🐌



```yaml
Header:
    From: any-host.dom
    To: any-hoster.dom
    Subject: Handled@Talker
    
Body:
    Hook: <Hook-uuid>
    Response: {A:1, B:2}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Hosted 📦](<../📦👥 Hosted domain.md>) from [`Handle@Hosted`](<../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/😃🐌📦 Handle.md>)
|           | `To`          | string    | [Hoster ☁️](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) from [`Handle@Hosted`](<../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/😃🐌📦 Handle.md>)
|           | `Subject`     | string    | `Handled@Talker`
| Body      | `Hook`    | uuid      | `Hook` from [`Handle@Hosted`](<../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/😃🐌📦 Handle.md>)
|           | `Response`    | any       | Response to [`Handle@Hosted`](<../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/😃🐌📦 Handle.md>)
|