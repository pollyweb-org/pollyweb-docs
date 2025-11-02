# 💼 SHARE 📃 script

[Script 📃](<../../📃 basics/Script 📃.md>) that implements the [`SHARE`](<💼 SHARE ⌘ cmd.md>) command.

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

# Assert inputs
- ASSERT|$.Inputs:
    AllOf: Schemas
    Lists: Schemas

# Save the hook
- SAVE|TalkerHooks >> $hook:
    Hook: .UUID
    Broker: $.Chat.Broker
    Chat: $.Chat.ID
    PublicKey: $.Chat.PublicKey
    Schemas: $:Schemas
    Context: $:Context

# Query the Broker
- SEND|$hook:
    Header:
        To: Broker
        Subject: Query@Broker
    Body: 
        Chat: Chat
        Hook: Hook
        Schemas: Schemas

# Wait for the shared data
- WAIT >> $shared:
    Hook: $hook.Hook

# Return the data
- RETURN:
    $shared
```

Needs||
|-|-
|[Commands ⌘](<../../📃 basics/Command ⌘.md>)| [`ASSERT`](<../../📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`WAIT`](<../../📃 control ▶️/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHooks`](<../../../Talkers 😃/😃🪣 Talker tables/😃 TalkerHooks 🪣 table.md>)
| [Holders 🧠](<../../📃 basics/Holder 🧠.md>) | [`.Chat`](<../../📃 holders 🧠/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Inputs`](<../../📃 holders 🧠/$.Inputs ▶️/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Query@Broker` 🅰️ method](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) <br/> [`Disclose@Vault` 🅰️ method](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>) <br/> [`Context@Consumer` 🅰️ method](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Context 🗄️🚀💼/💼 Context 🚀 request.md>) <br/> [`Consume@Consumer` 🅰️ method](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>) <br/> [`Collect@Vault` 🅰️ method](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Collect 💼🚀🗄️/🗄️ Collect 🚀 request.md>)
|