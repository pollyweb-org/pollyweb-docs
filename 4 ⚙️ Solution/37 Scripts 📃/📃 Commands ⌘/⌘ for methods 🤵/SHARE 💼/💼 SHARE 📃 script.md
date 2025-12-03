# 💼 SHARE 📃 script

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`SHARE`](<💼 SHARE ⌘ cmd.md>) command.

## Flow

![alt text](<💼 SHARE ⚙️ uml.png>)

## How to call

```yaml
- RUN|.SHARE:
    Schemas: 
      - any-authority.dom/ANY-SCHEMA
    Context: {...}
```

## Script

```yaml
📃 .SHARE:

# Save the hook
- SAVE|Consumer.Queries >> $query:
    Broker: $.Chat.Broker
    Chat: $.Chat.ID
    Schemas: $Schemas
    Context: $Context

# Wait for the shared data
- WAIT >> $shared:
    Hook: $hook.Hook

# Return the data
- RETURN:
    $shared
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`WAIT`](<../../⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHooks`](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Hooks 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`.Chat`](<../../../📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Query@Broker` 🅰️ method](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) <br/> [`Disclose@Vault` 🅰️ method](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>) <br/> [`Context@Consumer` 🅰️ method](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Context 🗄️🚀💼/💼 Context 🚀 call.md>) <br/> [`Consume@Consumer` 🅰️ method](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>) <br/> [`Collect@Vault` 🅰️ method](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>)
|