<!-- TODO -->

![alt text](<🤵 Bindable ⚙️ uml.png>)

```yaml
📃 Bindable@Broker:

# Verify the signature
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Chat, Hook, Schemas
    UUIDs: Chat, Hook
    Lists: Schemas

# Get the chat
- GET >> $chat:
    Set: Chats@Broker
    Key: Chat

# Check if it's the host
- ASSERT:
    $chat.Host: $.Msg.From

# Get the existing binds
- EVAL >> $bound:
    Bind, Schema
    FROM $chat.Wallet.Binds
    MATCH Vault, $.Msg.From

# Get the bindable schemas
-EVAL|.Diff >> $bindable:
    - $bound.Schema  # list of bound schemas
    - $.Msg.Schemas  # list of offered schemas

# Translate the bindable schemas
- IF|$bindable:
    RUN|CreateBinds >> $binds

# Merge existing with new
- EVAL >> $send:
    :$bound: # already bound
    :$binds: # just created

# Send the created binds
- SEND:
    Header: 
        To: $.Msg.From
        Subject: Bound@Vault
    Body:
        Hook: $.Msg.Hook
        Binds: $send
    
# Update the binds    
RUN|UpdateBinds@Broker:
    Wallet: $chat.Wallet.Wallet
```

```yaml
📃 CreateBinds:

# Translate the offered schemas
- SEND >> $translated:
    Header:
        To: $.Settings.Graph
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
    - SAVE|Binds@Broker >> $item:
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
[Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`EVAL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/EVAL ⬇️ flow.md>) [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>) | [`{.Diff}`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...functions 🐍/🔩 {.Diff}.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Bound@Vault` 🅰️ method](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|