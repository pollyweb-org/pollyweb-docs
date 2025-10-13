# 😃🐌🧑‍💻 Evaluate @ Hosted

> Handles a [{Function} 🐍](<../../9 😃 Talkers/30 🗃️ Talker data/12 🐍 {Function}.md>) evaluation.

> Implements [Hosted 🧑‍💻 domain](<../../9 😃 Talkers/90 ☁️ Hosters/10 🧑‍💻☁️ Hosted domain.md>)

> Part of [😃⏩🧑‍💻 Handle @ Talker](<../../5 ⏩ Flows/79 😃⏩ Talkers/20 😃⏩🧑‍💻 Handle 🐍.md>) flow

> Followed by [`Handled@Talker`](<../92 😃🅰️ Talker/40 🧑‍💻🐌😃 Handled.md>) message

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-hoster.com
    To: any-domain.com
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
|           | `To`          | string    | [Hosted 🧑‍💻 domain](<../../9 😃 Talkers/90 ☁️ Hosters/10 🧑‍💻☁️ Hosted domain.md>) name
|           | `Subject`     | string    | `Handle@Hosted`
| Body      | `Callback`    | uuid      | Call back for [`Handled@Talker`](<../92 😃🅰️ Talker/40 🧑‍💻🐌😃 Handled.md>)
|           | `Function`    | string    | Name of the function to evaluate
|           | `Arguments`   | array     | Array of function arguments 
|