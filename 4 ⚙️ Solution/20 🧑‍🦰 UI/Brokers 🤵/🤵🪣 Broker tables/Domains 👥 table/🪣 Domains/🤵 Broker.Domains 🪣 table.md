# 🤵🪣 Domains @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores details on [Host 🤗 domains](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).



## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Domains.yaml
Prefix: Broker
Table: Domains
Key: Name

Triggers:
    OnDomainAdded: ADDED # CHANGED
```


## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Hosts|<host>

Name: any-domain.dom
Title: Any Domain
Description: bla, bla...
SmallIcon: <base64>
BigIcon: <base64>
```