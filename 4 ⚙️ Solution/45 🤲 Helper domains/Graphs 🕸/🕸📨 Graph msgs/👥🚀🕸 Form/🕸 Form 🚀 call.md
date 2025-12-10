# 👥🚀🕸 Form @ Graph

> About
* Part of [Graph 🕸 domain](<../../🕸 Graph helper/🕸🤲 Graph helper.md>)
* Part of the [`Inform` ⏩ flow](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)

<br/>

## Synchronous Call 🚀


```yaml
Header: 
    From: any-consumer.dom
    To: any-broker.dom
    Subject: Form@Graph

Body:
    Form: AnyForm
    Domain: any-consumer.dom
    Language: en-us
```

|Object|Property|Type|Description
|-|-|-|-
| Header|`From`|text| The name of the sender [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|       |`To`|text| [Graph 🕸 domain](<../../🕸 Graph helper/🕸🤲 Graph helper.md>) name
|       | `Subject` |text| `Form@Graph`
| Body  | `Domain`  |text| The [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name to lookup
|       | `Form`    | string   | The name of form to return
|       | `Language`| text     | The language code for the form
|

<br/>

## Synchronous Response 


```yaml
Title: Order a meal
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
| `Title`    |text| Form title to display to users
| `Details` |text| Text to show on [Prompt 🤔 details](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>)
| `Steps`   | list   | List of `Step` objects
|

### Step object

|Property|Type|Description
|-|-|-
| `Schema` |text| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) for [`Query@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Purpose` |text| Explication listed on [Prompt 🤔 details](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>)
|

<br/>

## FAQ

1. **How to define a Form on a domain [Manifest 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>)?**

    See the [`INFORM`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) command.

    ---
    <br/>

