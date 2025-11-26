# 🤵 OnChatActivated ⚙️ handler

> Part of the [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnChatActivated ⚙️ uml.png>)

<br/>

## Script


```yaml
📃 OnChatActivated:

# On Pop@Broker
- IF|$Chat.Host.Is($.Hosted.Domain):

    Then: # Pop the Chat 
        SAVE|Broker.Chatters:
            .State: POP
            Chat: $Chat.ID
            Domain: $.Hosted.Domain
            Role: VAULT

    Else: # Add the HOST participant
        SAVE|Broker.Chatters:
            .State: HOST
            Chat: $Chat.ID
            Domain: $Chat.Host
            Role: HOST
```