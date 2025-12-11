# 💼 SHARE 📃 script

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`SHARE`](<💼 SHARE ⌘ cmd.md>) command.

## Flow

![alt text](<💼 SHARE ⚙️ uml.png>)

## How to call

```yaml
- RUN .SHARE:
    Schemas: 
      - any-authority.dom/ANY-SCHEMA
    Context: {...}
    Domain: any-domain.dom
```

## Script

```yaml
📃 .SHARE:

# Assert the inputs
- ASSERT $.Inputs:
    AllOf: Schemas
    Lists: Schemas
    Domain.IsDomain:
    Schemas.Each.IsSchema:

# Save the hook
- SAVE Consumer.Queries >> $query:
    Broker: $.Chat.Broker
    Chat: $.Chat.Chat
    Schemas: $Schemas
    Context: $Context
    Domain: $Domain 

# Wait for the shared data
- WAIT >> $data:
    Hook: $query.ID

# Return the data
- RETURN:
    $data
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`WAIT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Consumer.Queries`](<../../💼🪣 Consumer tables/Queries 🗄️ table/🪣 Queries/💼 Consumer.Queries 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsDomain`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>) [`.Each`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Each ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Inputs`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
|