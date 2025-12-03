# 💼 OnQueryConsume 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../🪣 Queries/💼 Consumer.Queries 🪣 table.md>)
* Reacts to the [`Consume@Consumer` 🅰️ method](<../../../💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>)

<br/>

## Diagram

![alt text](<💼 OnQueryConsume ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryConsume:

# Verify if the Vault is trusted
- TRUSTS:
    Trusted: $Query.Vault
    Schema: $Query.Schema
    Role: VAULT

# Get the data
- SEND >> $data:
    Header: 
        To: $.Msg.From
        Subject: Collect@Vault
    Body:
        Collect: $.Msg.Collect

# Assert the schema
- ASSERT|$data:
    Schema: $.Msg.Schema
```