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
    - SET|$tokens:
        $token.ID:
            ID: $token.ID
            Issuer: $token.Issuer
            Schema: $token.Schema

# Add the Tokens
- SAVE|$Chat:
    Tokens: $tokens

# Progress the state
- RETURN: CACHE
```