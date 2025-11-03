# 🪵 Logger Threads 🪣 table

> Purpose
* Registers threads from the [`Start@Logger` 🅰️ method](<../🪵🅰️ Logger methods/Start 👥🚀🪵/🪵 Start 🚀 request.md>)

<br/>

# Schema

Here's the [Itemized 🪣 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema.

```yaml
Prefix: Logger
Table: Threads
Key: ID

Parents:
    Domain: {Domains.Name: Thread.Domain}

Children: 
    Blames: {Blames.Thread: Thread.ID}
    Entries: {Entries.Thread: Thread.ID}
    Groups: {Groups.Thread: Thread.ID}
    Levels: {Levels.Thread: Thread.ID}

Cascade:
    - Blames
    - Entries
    - Groups
    - Levels
```
Uses: [`Parents`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) [`Children`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) [`Cascade`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Cascade.md>) 

## Example

```yaml
ID: <thread-uuid>
Domain: any-domain.dom
Delete: 1 day
```