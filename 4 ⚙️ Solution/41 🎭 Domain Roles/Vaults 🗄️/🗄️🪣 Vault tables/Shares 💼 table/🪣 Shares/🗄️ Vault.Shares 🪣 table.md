# 🪣 Collects

> Purpose
* Stores the hooks for [`Collect@Vault`](<../../../🗄️🅰️ Vault methods/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>)

> Data Access

* Inserted by [`Disclose@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>)
* Read by [`Collect@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
Prefix: Vault
Table: Shares
Item: Share

Parents:
    Bind: { Binds.ID, Share.ID }
```

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# From Disclose@Vault
ID: <share-uuid>
Chat: <chat-uuid>
Bind: <bind-uuid>
Consumer: any-broker.dom
Language: en-us

# From OnSharedAsked
Data: {...}
```

