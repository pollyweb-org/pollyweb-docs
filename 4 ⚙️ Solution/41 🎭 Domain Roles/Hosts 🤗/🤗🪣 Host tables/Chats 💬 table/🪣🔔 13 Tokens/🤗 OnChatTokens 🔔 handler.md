# 🤗 OnChatTokens 🔔 handler

> About
* Part of the [`Host.Chats` 🪣 table](<../🪣 Chats/🤗 Host.Chats 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤗 OnChatTokens ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnChatTokens:

# Process each Token in parallel
- PARALLEL|$Chat.Tokens|$id:

    # Read the Token from the table
    - READ >> $token:
        Set: Chat.Tokens
        Key: $id
    
    # Add the details to the chat
    - PUT +> $tokens:
        ID: $token.ID
        Schema: $token.Schema

# Add to the Chat item
- SAVE|$Chat:
    
    # Progress the state
    .State: CACHE

    # Add the Tokens
    Tokens: $tokens
```