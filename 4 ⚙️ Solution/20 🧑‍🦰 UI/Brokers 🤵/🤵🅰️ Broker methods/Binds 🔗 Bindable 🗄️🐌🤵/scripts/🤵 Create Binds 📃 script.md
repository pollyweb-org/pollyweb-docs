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
        Language: $:chat.Wallet.Language
        Schemas: $:bindable

# Ask the user to select
- MANY|Which to bind? >> $selected:
    Options: $translated.Schemas

# Process the selected schemas
- PARALLEL|$selected|$schema:
    
    # Save the bind
    - SAVE|BrokerBinds >> $bind:
        ID: .UUID
        Vault: $.Msg.Host
        Wallet: $:chat.Wallet.ID
        Schema: $schema.Schema

    # Add to the list of binds
    - EVAL +> $binds:
        Bind: $bind.ID
        Schema: $schema.Schema

# Return the new binds
- RETURN|$binds
```


Needs ||
|-|-
[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`EVAL`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`MANY`](<../../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/MANY 🔠/🔠 MANY ⌘ cmd.md>) [`PARALLEL`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SAVE`](<../../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Function 🐍.md>) | [`{.Diff}`](<../../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.Diff}.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Translate@Graph` 🅰️ method](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|