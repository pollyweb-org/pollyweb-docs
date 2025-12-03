# 💼 OnQueryTrusted 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnQueryTrusted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryTrusted:

# Get the data
- SEND >> $data:
    Header: 
        To: $Query.Vault
        Subject: Collect@Vault
    Body:
        Collect: $Query.Collect.Require

# Save the data
- SAVE|$Query:
    .State: CONSUMED
    Data: $data
```