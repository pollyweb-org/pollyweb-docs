# 🪵 Logger Groups 🪣 table

> Flow
* Part of the [Logger 🪵 helper domain](<../🪵 Logger helper/🪵 Logger 🤲 helper.md>)
* Automatically inserted by the [`LoggerEntries` 🪣 table](<🪵 LoggerEntries 🪣 table.md>).
* Automatically deleted by the [`LoggerThreads` 🪣 table](<🪵 LoggerThreads 🪣 table.md>).

## Schema
Here's the [Itemized 🪣 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema.

```yaml 
Prefix: Logger
Table: Groups
Key: Name

Parents: 
    Domain: { Domains.Name: Groups.Domain }
    Thread: { Threads.ID: Groups.Thread }

Children:
    Entries: 
        Entries.Domain: Groups.Domain
        Entries.Group: Groups.Name

Distincts:
    Blames: Entries.Blame
    Levels: Entries.Levels
```

Uses: [`Parents`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) [`Children`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) [`Distincts`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Distincts.md>)


## Example

```yaml
Name: my-group
Domain: any-domain.dom
Thread: <thread-uuid>
```