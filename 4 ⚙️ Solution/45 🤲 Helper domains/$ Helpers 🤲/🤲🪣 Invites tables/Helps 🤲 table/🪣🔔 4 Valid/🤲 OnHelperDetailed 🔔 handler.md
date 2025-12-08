# 🤲 OnHelperDetailed 🔔 handler

> About
* Part of the [`Helper.Helps` 🪣 table](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) 


## Diagram

![alt text](<🤲 OnHelperDetailed ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnHelperDetailed:

# Read the schema scripts
- READ >> $script:
    Set: Helper.Schemas
    Key: $Invite.Schema

# Run the schema script
- RUN|$script >> $result:
    Invite: $Invite

# Save the Help details
- SAVE|$Invite:
    .State: HELPED
    Details: $result
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Helper.Helps`](<../🪣 Helps/🤲 Helper.Helps 🪣 table.md>) [`Helper.Schemas`](<../../Schemas 🧩 table/🪣 Schemas/🤲 Helper.Schemas 🪣 table.md>)
