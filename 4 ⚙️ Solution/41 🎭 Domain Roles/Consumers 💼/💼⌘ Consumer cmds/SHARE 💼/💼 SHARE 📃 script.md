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
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`WAIT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHooks`](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Hooks 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Inputs`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Query@Broker` 📨 msg](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) <br/> [`Disclose@Vault` 📨 msg](<../../../Vaults 🗄️/🗄️📨 Vault msgs/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>) <br/> [`Context@Consumer` 📨 msg](<../../💼📨 Consumer msgs/Context 🗄️🚀💼/💼 Context 🚀 call.md>) <br/> [`Consume@Consumer` 📨 msg](<../../💼📨 Consumer msgs/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>) <br/> [`Collect@Vault` 📨 msg](<../../../Vaults 🗄️/🗄️📨 Vault msgs/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>)
|