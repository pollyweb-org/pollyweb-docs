# 🤗 OnChatTokens 🔔 handler

> About
* Part of the [`Host.Chats` 🪣 table](<../🪣 Chats/🤗 Host.Chats 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤗 OnChatCache ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnChatCache:

# Put the Chat item into the holder
- PUT >> $.Chat:
    $Chat

# Progress the Chat state
- SAVE $Chat:
    .State: ACTIVE

# Return to the CHAT command
- RACE $Chat.ID:
```