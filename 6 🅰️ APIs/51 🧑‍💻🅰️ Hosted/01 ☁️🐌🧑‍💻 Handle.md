# ☁️🐌🧑‍💻 Evaluate @ Hosted

> Implements [👥 Hosted 🧑‍💻 domain](<../../9 😃 Talkers/90 ☁️ Hosters/10 🧑‍💻☁️ Hosted domain.md>)

> Part of [☁️⏩🧑‍💻 Handle @ Hoster](<../../5 ⏩ Flows/79 😃⏩ Talkers/20 😃⏩🧑‍💻 Handle.md>) flow

> Followed by [`Handled@Hoster`](<../52 ☁️🅰️ Hoster/40 🧑‍💻🐌☁️ Handled.md>) method

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-hoster.com
    To: <uuid>.any-proxy.com
    Subject: Handle@Hosted
Body:
    Request: <request-uuid>
    Function: my-function
    Arguments: 
        - {A:1, B:2}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Hoster ☁️ domain](<../../9 😃 Talkers/90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>) name
|           | `To`          | string    | URL of the [Hosted 🧑‍💻](<../../9 😃 Talkers/90 ☁️ Hosters/10 🧑‍💻☁️ Hosted domain.md>) API
|           | `Subject`     | string    | `Handle@Hosted`
| Body      | `Callback`    | uuid      | Call back for [`Handled@Host`](<../52 ☁️🅰️ Hoster/40 🧑‍💻🐌☁️ Handled.md>)
|           | `Function`    | string    | Name of the function to evaluate
|           | `Arguments`   | array     | Array of function arguments 
|