<!-- TODO -->


```yaml
📃 CreateBinds:

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
    
    # Create the bind
    - EVAL|.UUID >> $bind
    
    # Save the bind
    - SAVE|BrokerBinds >> $item:
        Bind: $bind
        Vault: $.Msg.Host
        Wallet: $chat.Wallet.Wallet
        Schema: $schema.Schema

    # Add to the list of binds
    - EVAL +> $binds:
        Bind: $bind
        Schema: $schema.Schema

# Return the new binds
- RETURN|$binds
```


Needs ||
|-|-
[Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | [`EVAL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>) | [`{.Diff}`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...functions 🐍/🔩 {.Diff}.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Translate@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|