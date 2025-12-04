# 🤗 OnChatBinds 🔔 handler

> About
* Part of the [`Host.Chats` 🪣 table](<../🪣 Chats/🤗 Host.Chats 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤗 OnChatBinds ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnChatBinds:

# Process each Bind in parallel
- PARALLEL|$Chat.Binds|$id:

    # Read the Bind from the table
    - READ >> $bind:
        Set: Chat.Binds
        Key: $id

    # Add the details to the chat
    - PUT +> $binds:
        ID: $bind.ID
        Schema: $bind.Schema

# Add to the Chat item
- SAVE|$Chat:
    
    # Progress the state
    .State: TOKENS

    # Add the Binds
    Binds: $binds
```