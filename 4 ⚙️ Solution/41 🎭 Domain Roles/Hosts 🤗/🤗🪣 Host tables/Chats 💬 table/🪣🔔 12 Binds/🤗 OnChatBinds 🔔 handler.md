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
- PARALLEL $Chat.Binds >> $id:

    # Read the Bind from the table
    - READ >> $bind:
        Set: Chat.Binds
        Key: $id

    # Add the details to the chat
    - SET $binds:
        $bind.ID:
            ID: $bind.ID
            Schema: $bind.Schema
            Reference: $bind.Reference

# Set the Wallet to the first .BIND, if any
- SELECT >> $wallet:
    First: ID
    From: $binds
    Where: 
        Schema: .BIND

# Add to the Chat item
- SAVE $Chat:
    Binds: $binds
    Wallet: $wallet

# Progress the state
- RETURN: TOKEN
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`PARALLEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) |