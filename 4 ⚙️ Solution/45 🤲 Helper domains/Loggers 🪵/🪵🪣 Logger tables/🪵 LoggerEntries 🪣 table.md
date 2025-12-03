# 🪵 Logger Entries 🪣 table

> Purpose
* Saves log entries from [`Log@Logger` 📨 msg](<../🪵📨 Logger msgs/Log 👥🐌🪵/🪵 Log 🐌 msg.md>).

## Schema

Here's the [Itemized 🪣 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema.

```yaml
Prefix: Logger
Table: Entries
Key: ID

Parents: 

    Thread: # pre-registered
        Threads.ID: Entries.Thread

    Blame: # propagated
        Blames.Thread: Entries.Thread
        Blames.Name: Entries.Blame
        Blames.Domain: Entries.Domain

    Group: # propagated
        Groups.Thread: Entries.Thread
        Groups.Name: Entries.Group
        Groups.Domain: Entries.Domain

    Level: # propagated
        Levels.Thread: Entries.Thread
        Levels.Name: Entries.Level
        Levels.Domain: Entries.Domain

Propagate:
    - Blame
    - Group
    - Level
```

Uses: [`Parents`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) [`Propagate`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Propagate.md>)

## Example

```yaml
# READ|LoggerEntries|<entry-uuid>
ID: <entry-uuid>
Sent: 2025-10-10T13:45:23.123Z
Domain: <any-domain.dom>
Thread: <thread-uuid>
Level: INFO
Group: my-group-1
Blame: my-script
Text: This is a log text.
Details: {...}
```