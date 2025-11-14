# 👥🚀🕸 Form @ Graph

> Part of [Graph 🕸 domain](<../🕸🤲 Graph helper.md>)

> ⚠️ This method doesn’t look at the header nor the signature of the request.

* Used in:
    * [Broker Inform ⏩ flow](<../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)

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
| Header|`From`|string| The name of the sender [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|       |`To`|string| [Graph 🕸 domain](<../🕸🤲 Graph helper.md>) name
|       | `Subject` | string | `Form@Graph`
| Body  | `Domain`  | string | The [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name to lookup
|       | `Form`    | string   | The name of form to return
|

<br/>


## Synchronous Response 


```yaml
Verb: order
Details: > 
  Bla, bla...
Steps:
  - Schema: .CURATOR/CURATE
    Purpose: your curator orders 🧚
  - Schema: .PAYER/CHARGE
    Purpose: your payer pays the bill 💳  
```

|Property|Type|Description
|-|-|-
| `Verb`    | string | `Ready to {verb}?` [confirmation 👍](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>)
| `Details` | string | Text to show on [Prompt 🤔 details](<../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>)
| `Steps`   | list   | List of `Step` objects
|

### Step object

|Property|Type|Description
|-|-|-
| `Schema` | string | [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) for [`Query@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Purpose` | string | Explication listed on [Prompt 🤔 details](<../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>)
|

<br/>