# 🗄️ Vault.Binds 🪣 table

> About
* Stores the content of the {{Bound@Vault}}

<br/>

## Data Access

| Action | [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | [`DELETE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) |
|-|-|-|-|
| [`Bound` 📃 handler](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 📃 handler.md>) |  | X |  |



<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Binds.yaml
Key: Broker, Bind
```


<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
Broker: any-broker.dom
Bind: <bind-id>
Schema: .BIND
Reference: <user-reference>
```

| Property | Type | Details
|-|-|-
| `Broker` |text| From [`Bound@Broker`](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
| `Bind`| uuid | From [`Bound@Broker`](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
| `Schema` |text| From [`Bound@Broker`](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
| `Reference` | any | Internal anchor
| 