# 🤵🪣 Broker.Domains table

> About
* Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* Similar to the [`Broker.Schemas` 🪣 table](<../../Schemas 🧩 table/🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>), but for Domains 👥

<br/>

## Lifecycle

![alt text](<🤵 Broker.Domains ⚙️ uml.png>)

<br/>

## Data access

|Actor| [🛢 Propagate](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Propagate.md>) | [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
|-|:-:|:-:|:-:
|[`Broker.Binds` 🪣](<../../Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>) | X
|[`Broker.Chats` 🪣](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) | X
|[`Broker.Tokens` 🪣](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) | X
|[`OnWalletLocalized` 🔔](<../../Wallets 🧑‍🦰 table/🪣🧱 21 Localized 🔔/🤵 OnWalletLocalized 🔔 handler.md>) |  |X| X |

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Domains
Item: Domain
Key: Name, Wallet
```

Here's the [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) definition.    

```yaml
Handlers:
    UNBOUND  >> OnDomainUnbound:    # Sets Bind.STATE: REMOVED
    INSERTED >> OnDomainInserted:   # Calls About@Graph
    UPDATED  >> OnDomainLocalized:  # Calls TRANSLATE
        Assert: New.Language
```
Handlers: [`OnInserted`](<../🪣🧱 1 Inserted 🔔 event/🤵 OnDomainInserted 🔔 handler.md>) [`OnUnbound`](<../🪣🧱 3 Unbound 🔔 event/🤵 OnDomainUnbound 🔔 handler.md>) [`OnLocalized`](<../🪣🧱 2 Localized 🔔 event/🤵 OnDomainLocalized 🔔 handler.md>)

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