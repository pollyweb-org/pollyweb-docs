# 🤲 Help.OnValid 🔔 handler

> About
* Part of the [`Helper.Helps` 🪣 table](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 


## Diagram

![alt text](<🤲 Help.OnValid ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Help.OnValid:

# Read the schema scripts
- READ >> $script:
    Set: Helper.Schemas
    Key: $Help.Schema

# Run the schema script
- RUN $script >> $helped:
    Schema: $Help.Schema
    Context: $Help.Context
    Consumer: $Help.Consumer

# Verify the helped data
- VERIFY $helped:
    Schema: $Help.Schema

# Save the Help details
- SAVE $Help:
    STATE: HELPED
    Helped: $helped
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFIED`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Invites 🤲 table/🪣🔔 3 Verified/🤵 OnInviteVerified 🔔 handler.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Helper.Helps`](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) [`Helper.Schemas`](<../../Schemas 🧩 table/🪣 Schemas/🤲 Helper.Schemas 🪣 table.md>)
