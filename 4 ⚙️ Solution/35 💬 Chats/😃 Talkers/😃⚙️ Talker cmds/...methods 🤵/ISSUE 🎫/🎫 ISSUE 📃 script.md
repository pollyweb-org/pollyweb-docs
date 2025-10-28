# 💼 SHARE 📃 script

[Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) that implements the [`ISSUE`](<🎫 ISSUE ⌘ cmd.md>) command.

## Flow

![alt text](<🎫 ISSUE ⚙️ uml.png>)

## How to call

```yaml
- RUN|.ISSUE:
    Schema: any-authority.dom/ANY-SCHEMA
    Starts: 2018-12-10T13:45:00.000Z
    Expires: 2018-12-10T13:45:00.000Z
```

## Script

```yaml
📃 .ISSUE:

# Assert inputs
- ASSERT|$.Inputs:
    AllOf: Schema
    Texts: Schema
    Times: Starts, Expires

# Save the hook
- SAVE|TalkerHooks >> $hook:
    Hook: .UUID
    Broker: $.Chat.Broker
    Chat: $.Chat.Chat
    PublicKey: $.Chat.PublicKey
    Internals: $Internals
    Offer:
        Schema: $:Schema
        Starts: $:Starts
        Expires: $:Expires
        Properties: $:Properties
    
# Query the Broker
- SEND:
    Header:
        To: $.Chat.Broker
        Subject: Offer@Broker
    Body: 
        Chat: $.Chat.Chat
        Hook: $hook.Hook
        Schema: $:Schema
        Starts: $:Starts
        Expires: $:Expires

# Wait for the shared data
- WAIT >> $token:
    Hook: $hook.Hook

# Return the data
- RETURN:
    $token
```

Needs||
|-|-
|[Commands ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>)| [`ASSERT`](<../../...placeholders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`WAIT`](<../../...control ▶️/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHooks`](<../../../😃🪣 Talker tables/😃🪣 TalkerHooks 🪝 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Offer@Broker` 🅰️ method](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
| [Placeholders 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) | [`.Chat`](<../../...placeholders 🧠/$.Chat 💬/💬 $.Chat 🧠 holder.md>)
|