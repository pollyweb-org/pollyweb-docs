# 👥🚀🕸 Form @ Graph

> ⚠️ This method doesn’t look at the header nor the signature of the request.

* Used in:
    * [Broker Inform ⏩ flow](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/02 💼⏩🧑‍🦰 Inform 📝.md>)

<br/>

## Synchronous Request 🚀


```yaml
Header: 
    From: any-consumer.com
    To: any-broker.com
    Subject: Form@Graph

Body:
    Domain: any-consumer.com
    Form: AnyForm
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the sender [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>)
|       | `To`      | string | [Graph 🕸 domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/50 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Form@Graph`
| Body  | `Domain`  | string | The [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) name to lookup
|       | `Form`    | string   | The name of form to return
|

<br/>


## Synchronous Response 


```yaml
Verb: order
Details: > 
  Bla, bla...
Steps:
  - Code: .CURATOR/FILTER
    Purpose: your curator orders 🧚
  - Code: .PAYER/CHARGE
    Purpose: your payer pays the bill 💳  
```

|Property|Type|Description
|-|-|-
| `Verb`    | string | `Ready to {verb}?` [confirmation 👍](<../../9 😃 Talkers/20 🤔 Prompts/7 ✏️ Input prompts/31 👍 CONFIRM prompt.md>)
| `Details` | string | Text to show on [Prompt 🤔 details](<../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/03 ⊕ with Details.md>)
| `Steps`   | list   | List of `Step` objects
|

### Step object

|Property|Type|Description
|-|-|-
| `Code` | string | [Schema Code 🧩](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) for [`Query@Broker`](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>)
| `Purpose` | string | Explication listed on [Prompt 🤔 details](<../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/03 ⊕ with Details.md>)
|

<br/>