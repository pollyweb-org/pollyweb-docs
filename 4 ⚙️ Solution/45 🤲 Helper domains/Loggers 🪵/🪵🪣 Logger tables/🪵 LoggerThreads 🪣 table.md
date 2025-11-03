# 🪵 Logger Threads 🪣 table

> Purpose
* Registers threads from the [`Start@Logger` 🅰️ method](<../🪵🅰️ Logger methods/👥🚀🪵 Start/🪵 Start 🚀 request.md>)

<br/>

# Schema

Here's the [Itemized 🪣 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema.

```yaml
Prefix: Logger
Table: Threads
Key: ID

Children: 
    Blames: {Blames.Thread: Thread.ID}
    Entries: {Entries.Thread: Thread.ID}
    Groups: {Groups.Thread: Thread.ID}
    Levels: {Levels.Thread: Thread.ID}
```

## Example

```yaml
ID: <thread-uuid>
Delete: 1 day
```