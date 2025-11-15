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
    Texts: Schema

# Get the chat
- READ >> $chat:
    Set: Broker.Chats
    Key: $.Msg.Chat

# Check if it's the host
- ASSERT|$.Msg:
    From: $chat.Host
    
# Set the Chat context
- CHAT:
    Broker: $.Msg.To
    Chat: $.Msg.Chat

# Translate 
- TRANSLATE >> $translation:
    Domain: $.Msg.From
    Schema: $.Msg.Schema

# Ask for confirmation
- CONFIRM: |
    Accept bind? 
    - Vault: ´$translation.Domain´ 
    - Schema: ´$translation.Schema´

# Save the bind
- SAVE|Broker.Binds >> $bind:
    Wallet: $chat.Wallet.ID
    Hook: $.Msg.Hook
    Vault: $.Msg.Host
    Vault$: $translation.Domain
    Schema: $.Msg.Schema
    Schema$: $translation.Schema
```

Uses||
|-|-
[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CHAT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`CONFIRM`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|

