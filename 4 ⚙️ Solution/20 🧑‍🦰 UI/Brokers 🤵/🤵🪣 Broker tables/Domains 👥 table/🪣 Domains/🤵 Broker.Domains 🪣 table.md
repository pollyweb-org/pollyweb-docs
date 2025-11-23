# 🤵🪣 Domains @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores details on [Host 🤗 domains](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Domains
Item: Domain
Key: Name

Handlers:
    OnDomainInserted: 
        Events: INSERTED 
    OnDomainLocalized: 
        Events: UPDATED
        Assert: New.Language
```

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# From Chat,Bind,Token propagation
Name: any-domain.dom
Wallet: <wallet-uuid>

# From OnDomainAdded, OnPopLocalize
Language: en-US
Title: Any Domain
Description: bla, bla...
SmallIcon: <base64>
BigIcon: <base64>

# From Pop@Broker
Blocked: false
Muted: false
```