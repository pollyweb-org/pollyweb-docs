# 🤵 Bindable 📃 handler

> Purpose
* Implements the [`Bindable@Broker` 🅰️ method](<🤵 Bindable 🐌 msg.md>)

## Flow

![alt text](<🤵 Bindable ⚙️ uml.png>)

## Script

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
    Set: BrokerChats
    Key: Chat

# Check if it's the host
- ASSERT|$.Msg:
    From: $chat.Host

# Get the existing binds
- EVAL >> $bound:
    Bind, Schema
    FROM $chat.Wallet.Binds
    MATCH Vault, $.Msg.From

# Get the bindable schemas
- EVAL|.Diff >> $bindable:
    # list of bound schemas
    - $bound.Schema  
    # list of offered schemas
    - $.Msg.Schemas.Schema  

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
- RUN|UpdateBinds@Broker:
    Wallet: $chat.Wallet.Wallet
```

Needs ||
|-|-
[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/...commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`IF`](<../../../../35 💬 Chats/Scripts 📃/...control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/$Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/...functions 🐍/{Function} 🐍.md>) | [`{.Diff}`](<../../../../35 💬 Chats/Scripts 📃/...functions 🐍/🔩 {.Diff}.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Bound@Vault` 🅰️ method](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/...commands ⌘/Script 📃/📃 Script.md>) | [`CreateBinds` 📃](<🤵 Bindable 📃 part 2.md>)
|