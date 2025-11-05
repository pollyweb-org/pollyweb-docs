# 🪵 Logger Domains 🪣 table

> Purpose
* Stores the [domains 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) helped by the [Logger 🪵 helper domain](<../🪵 Logger helper/🪵 Logger 🤲 helper.md>).

## Schema
Here's the [Itemized 🪣 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema.

```yaml 
Prefix: Logger
Table: Domains
Key: Name

Children: 
    Entries: { Entries.Domain: Domains.Name }
    Threads: { Threads.Domain: Domains.Name }

Cascade:
    - Entries
    - Threads

Distincts:
    Blames: Entries.Domain
    Groups: Entries.Group
    Levels: Entries.Level
```

Uses: [`Children`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) [`Cascade`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Cascade.md>) [`Distincts`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Distincts.md>)

<br/>

## Example

```yaml
# READ|LoggerDomains|any-domain.dom
Name: any-domain.dom
```
Uses: [`READ`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)