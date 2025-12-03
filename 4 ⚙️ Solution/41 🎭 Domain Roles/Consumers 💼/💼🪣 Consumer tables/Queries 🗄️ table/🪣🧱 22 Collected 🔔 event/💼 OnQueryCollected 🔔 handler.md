# 💼 OnQueryCollected 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnQueryCollected ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryCollected:

# Continue the talker 
- RACE|$Query.ID:
    $Query.Collected
```