# 🤵 OnChatActivated 🔔 handler

> Part of the [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnChatActivated ⚙️ uml.png>)

<br/>

## Script


```yaml
📃 OnChatActivated:

# Add the HOST participant
SAVE|Broker.Chatters:
    .State: HOST
    Chat: $Chat.ID
    Domain: $Chat.Host
    Role: HOST
```