# 🪵 Logger Threads 🪣 table

> Purpose
* Registers threads from the [`Start@Logger` 🚀 call](<../🪵📨 Logger msgs/Start 👥🚀🪵/🪵 Start 🚀 call.md>)

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
Started: 2018-12-10T13:45:21.123Z
Stopped: 2018-12-10T13:45:28.345Z
```

|Property| Type| Purpose|Origin
|-|-|-|-
| `ID` | uuid | Thread ID | [`Start@`](<../🪵📨 Logger msgs/Start 👥🚀🪵/🪵 Start 🚀 call.md>)
| `Domain` | domain | Owner [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [`Start@`](<../🪵📨 Logger msgs/Start 👥🚀🪵/🪵 Start 🚀 call.md>)
| `Started` | time | When it was started | [`Start@`](<../🪵📨 Logger msgs/Start 👥🚀🪵/🪵 Start 🚀 call.md>)
| `Stopped` | time | When it was stopped | [`Stop@`](<../🪵📨 Logger msgs/Stop 👥🐌🪵/🪵 Stop 🐌 msg.md>) |
|