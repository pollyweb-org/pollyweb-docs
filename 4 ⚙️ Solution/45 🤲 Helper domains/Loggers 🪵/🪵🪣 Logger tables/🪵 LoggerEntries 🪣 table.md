# 🪵 Logger Entries 🪣 table

> Purpose
* Saves log entries from [`Log@Logger` 🅰️ method](<../🪵🅰️ Logger methods/Log 👥🐌🪵/🪵 Log 🐌 msg.md>).

## Schema

Here's the [Itemized 🪣 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema.

```yaml
Prefix: Logger
Table: Entries
Key: ID

Parents: 

    Thread: 
        Threads.ID: Entries.Thread

    Group: 
        Groups.Thread: Entries.Thread
        Groups.Name: Entries.Group

    Type:
        Types.Thread: Entries.Thread
        Types.Name: Entries.Type

    Blame:
        Blames.Thread: Entries.Thread
        Blames.Name: Entries.Blame

Propagate:
    - Group
    - Type
    - Blame
```

Uses: [`Parents`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) [`Propagate`](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Propagate.md>)

## Example

```yaml
# GET|LoggerEntries|<entry-uuid>
ID: <entry-uuid>
Sent: 2025-10-10T13:45:23.123Z
Thread: <thread-uuid>
Level: INFO
Group: my-group-1
Blame: my-script
Text: This is a log text.
Details: {...}
```