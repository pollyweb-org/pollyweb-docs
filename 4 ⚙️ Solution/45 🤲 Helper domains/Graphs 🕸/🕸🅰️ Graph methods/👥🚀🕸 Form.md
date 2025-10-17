# 👥🚀🕸 Form @ Graph

> ⚠️ This method doesn’t look at the header nor the signature of the request.

* Used in:
    * [Broker Inform ⏩ flow](<../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/💼⏩🧑‍🦰 Inform 📝.md>)

<br/>

## Synchronous Request 🚀


```yaml
Header: 
    From: any-consumer.dom
    To: any-broker.dom
    Subject: Form@Graph

Body:
    Domain: any-consumer.dom
    Form: AnyForm
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the sender [domain 👥](<../../../40 👥 Domains/👥 Domain.md>)
|       | `To`      | string | [Graph 🕸 domain](<../🕸🤲 Graph helper.md>) name
|       | `Subject` | string | `Form@Graph`
| Body  | `Domain`  | string | The [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) name to lookup
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
| `Verb`    | string | `Ready to {verb}?` [confirmation 👍](<../../../35 💬 Chats/🤔 Prompts/🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>)
| `Details` | string | Text to show on [Prompt 🤔 details](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/3 ⊕ with Details.md>)
| `Steps`   | list   | List of `Step` objects
|

### Step object

|Property|Type|Description
|-|-|-
| `Code` | string | [Schema Code 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) for [`Query@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Query.md>)
| `Purpose` | string | Explication listed on [Prompt 🤔 details](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/3 ⊕ with Details.md>)
|

<br/>