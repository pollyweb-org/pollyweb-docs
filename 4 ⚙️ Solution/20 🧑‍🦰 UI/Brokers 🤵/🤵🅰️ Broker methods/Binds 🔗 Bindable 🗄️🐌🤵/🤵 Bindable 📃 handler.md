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
- READ >> $chat:
    Set: BrokerChats
    Key: Chat

# Check if it's the host
- ASSERT|$.Msg:
    From: $chat.Host

# Get the existing binds
- SQL >> $bound:
    Select: Bind, Schema
    From: $chat.Wallet.Binds
    Where: Vault.Is($.Msg.From)

# Get the bindable schemas
- EVAL|.Diff >> $bindable:
    # list of bound schemas
    - $bound.Schema  
    # list of offered schemas
    - $.Msg.Schemas.Schema  

# Translate the bindable schemas
- IF|$bindable:
    RUN|Create-Binds >> $binds:
        bindable: $bindable
        chat: $chat

# Send the binds to the Vault
- RUN|Send-Binds:
    $bound, $binds
    
# Update the binds    
- RUN|Update-Binds:
    wallet: $chat.Wallet
```

Uses||
|-|-
[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`{.Diff}`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Bound@Vault` 🅰️ method](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`CreateBinds` 📃](<scripts/🤵 Create Binds 📃 script.md>) <br/> [`Update Notifier` 📃 script](<../../🤵⏩ Broker flows/Update Notifier 🤵⏩📣/🤵 Update Notifier 📃 script.md>)
|