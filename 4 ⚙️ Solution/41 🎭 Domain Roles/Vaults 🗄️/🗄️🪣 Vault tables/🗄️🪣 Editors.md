# 🪣 Editors

> [Editor 🧑‍💻 domains](<../../../50 🫥 Agent domains/Editors 🧑‍💻/🧑‍💻🫥 Editor agent.md>)

<br/>

## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets/GET ⏬ item.md>) result.

```yaml
# GET|Editors|any-editor.dom
Broker: any-broker.dom
Bind:  <bind-id>
Editor: any-editor.dom
```

| Property | Type | Details
|-|-|-
| `Broker` | string | From [`Bound@Broker`](<../🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)
| `Bind`| uuid | From [`Bound@Broker`](<../🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)


<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Editors.yaml
Key: Broker, Bind, Editor
Parents:
    Bind: Binds|Broker,Bind
```