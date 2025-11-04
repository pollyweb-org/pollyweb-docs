# 🪣 Binds

> Stores the content of [`Bound@Broker`](<../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)

<br/>

## Example

Here's the [`READ` command](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Binds|<broker>,<bind-id>
Broker: any-broker.dom
Bind: <bind-id>
Schema: .BIND
User: <user-reference>
```

| Property | Type | Details
|-|-|-
| `Broker` | string | From [`Bound@Broker`](<../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
| `Bind`| uuid | From [`Bound@Broker`](<../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
| `Schema` | string | From [`Bound@Broker`](<../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
| `User` | any | Internal anchor
| 

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Binds.yaml
Key: Broker, Bind
```
