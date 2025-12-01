# 🤵 OnQueryAbrupt 🔔 handler


> About
* Part of the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) role
* Part of the [`Broker.Queries` 🪣 table](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnQueryAbrupt ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryAbrupt:

# Load the Chat
- CHAT|$Query.Chat

# Fail the Chat due to ABRUPT Query
- FAIL:
