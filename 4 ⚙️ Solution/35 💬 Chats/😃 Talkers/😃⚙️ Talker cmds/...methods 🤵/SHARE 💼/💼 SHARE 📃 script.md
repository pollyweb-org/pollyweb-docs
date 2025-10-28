# 💼 SHARE 📃 script

[Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) that implements [`SHARE`](<💼 SHARE ⌘ cmd.md>)

## Flow

![alt text](<💼 SHARE ⚙️ uml.png>)

## How to call

```yaml
- RUN|.SHARE:
    Schemas: 
      - any-authority.dom/ANY-SCHEMA
```

## Script

```yaml
📃 .SHARE:

# Assert inputs
- ASSERT|.Inputs:
    AllOf: Schemas
    Lists: Schemas

# Save the hook
- SAVE|TalkerHooks >> $hook:
    Hook: .UUID
    Broker: $.Chat.Broker
    Chat: $.Chat.Chat
    PublicKey: $.Chat.PublicKey
    Schemas: $:Schemas

# Query the Broker
- SEND:
    Header:
        To: $.Chat.Broker
        Subject: Query@Broker
    Body: 
        Chat: $.Chat.Chat
        Hook: $hook.Hook
        Schemas: $:Schemas

# Wait for the shared data
- WAIT >> $shared:
    Signal: $hook.Hook

# Return the data
- RETURN:
    $shared
```

Needs||
|-|-
|[Commands ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>)| [`ASSERT`](<../../...placeholders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`WAIT`](<../../...control ▶️/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHooks`](<../../../😃🪣 Talker tables/😃🪣 TalkerHooks 🪝 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Query@Broker` 🅰️ method](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| [Placeholders 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) | [`.Chat`](<../../...placeholders 🧠/$.Chat 💬/💬 $.Chat ⌘ cmd.md>)
|