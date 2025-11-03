# 🪵 Logger Levels 🪣 table

> Flow
* Part of the [Logger 🪵 helper domain](<../🪵 Logger helper/🪵 Logger 🤲 helper.md>)
* Automatically inserted by the [`LoggerEntries` 🪣 table](<🪵 LoggerEntries 🪣 table.md>).
* Automatically deleted by the [`LoggerThreads` 🪣 table](<🪵 LoggerThreads 🪣 table.md>).

## Schema
Here's the [Itemized 🪣 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema.

```yaml 
Prefix: Logger
Table: Levels
Key: Name

Parents: 
    Domain: { Domains.Name: Levels.Domain }
    Thread: { Threads.ID: Levels.Thread }

Children:
    Entries: 
        Entries.Domain: Levels.Domain
        Entries.Level: Levels.Name

Distincts:
    Blames: Entries.Blame
    Groups: Entries.Group
```

Uses: [`Parents`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) [`Children`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) [`Distincts`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Distincts.md>)


## Example

```yaml
Name: ERROR
Domain: any-domain.dom
Thread: <thread-uuid>
```