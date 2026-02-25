# 🪣 Editors

> [Editor 🧑‍💻 domains](<../../../../../50 🫥 Agent domains/Editors 🧑‍💻/$/🧑‍💻🫥 Editor agent.md>)

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Editors|any-editor.dom
Broker: any-broker.dom
Bind:  <bind-id>
Editor: any-editor.dom
```

| Property | Type | Details
|-|-|-
| `Broker` |text| From [`Bound@Broker`](<../../../🗄️📨 Vault msgs/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
| `Bind`| uuid | From [`Bound@Broker`](<../../../🗄️📨 Vault msgs/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)


<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Editors.yaml
Key: Broker, Bind, Editor
Parents:
    Bind: Binds|Broker,Bind
```