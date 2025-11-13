# 🤵 Bindable 📃 Create Binds

> Part of the [`Bindable` 📃 handler](<../🤵 Bindable 📃 handler.md>)

## Script

```yaml
📃 Create-Binds:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: bindable, chat

# Translate the offered schemas
- SEND >> $translated:
    Header:
        To: $.Hosted.Graph
        Subject: Translate@Graph
    Body:
        Language: $chat.Wallet.Language
        Schemas: $bindable

# Ask the user to select
- MANY|Which to bind? >> $selected:
    Options: $translated.Schemas

# Process the selected schemas
- PARALLEL|$selected|$schema:
    
    # Save the bind
    - SAVE|Broker.Binds >> $bind:
        ID: .UUID
        Vault: $.Msg.Host
        Wallet: $chat.Wallet.ID
        Schema: $schema.Schema
        Schema$: $schema.Translation

    # Add to the list of binds
    - CALL +> $binds:
        Bind: $bind.ID
        Schema: $schema.Schema

# Return the new binds
- RETURN|$binds
```


Uses||
|-|-
[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CALL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`MANY`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/MANY 🔠/🔠 MANY ⌘ cmd.md>) [`PARALLEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`{.Diff}`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Translate@Graph` 🅰️ method](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|