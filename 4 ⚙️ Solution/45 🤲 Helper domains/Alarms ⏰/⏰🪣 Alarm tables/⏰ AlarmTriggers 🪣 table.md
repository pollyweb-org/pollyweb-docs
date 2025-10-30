# ⏰ Alarm Triggers 🪣 table


## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Table: AlarmTriggers
Key: Domain, When

# Link to the domains
Parents:
   Domain: 
        AlarmDomains.Domain: 
            AlarmTriggers.Domain

# Automatically create missing domains
Propagate:
    Domain
```

## Example

Here's the [`GET` command](<../../../35 💬 Chats/Scripts 📃/📃 for datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) result.


```yaml
Domain: 
When: 2023-04-01T05:00:30.001000Z
Hook: {object}
```