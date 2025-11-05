# ⏰ Alarm Triggers 🪣 table

> Data access

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Table: AlarmDomains
Key: Domain
Children: 
    Triggers: # List of triggers
        AlarmTriggers.Domain: AlarmDomain.Domain
```

## Example

Here's the [`READ` command](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
Domain: any-domain.dom
```