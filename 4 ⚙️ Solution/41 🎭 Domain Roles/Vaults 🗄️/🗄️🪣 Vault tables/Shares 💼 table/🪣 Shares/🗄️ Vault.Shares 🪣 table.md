# 🪣 Shares

> Purpose
* Manages the lifecycle of requests to the [`Disclose@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>).

<br/>

## Lifecycle

![alt text](<🗄️ Vault.Shares ⚙️ uml.png>)

<br/>

## Data Access

* Inserted by [`Disclose@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>)
* Read by [`Collect@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
Prefix: Vault
Table: Shares
Item: Share
```

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Vault.Binds`](<../../Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>).

```yaml
Parents: Bind
```

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) are: [`OnAsked`](<../🪣🔔 1 Asked/🗄️ OnShareAsked 📃 handler.md>) [`OnTrusted`](<../🪣🔔 2 Trusted/🗄️ OnShareTrusted 📃 handler.md>) [`OnReady`](<../🪣🔔 3 Ready/🗄️ OnShareReady 📃 handler.md>).

```yaml
Handlers:
    ASKED   >> OnShareAsked
    TRUSTED >> OnShareTrusted
    READY   >> OnShareReady
```

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# From Disclose@Vault
ID: <share-uuid>
Bind: <bind-uuid>   # Vault bind
Chat: <chat-uuid>   # Broker chat
Hook: <hook-uuid>   # Consumer hook
Language: en-us     # Data language
Consumer: any-consumer.dom

# From OnSharedAsked
Data: {...}
```

