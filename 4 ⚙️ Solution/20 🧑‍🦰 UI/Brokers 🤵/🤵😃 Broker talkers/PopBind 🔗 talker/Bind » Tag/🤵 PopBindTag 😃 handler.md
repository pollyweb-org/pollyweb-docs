# 🤵 PopBindTag 🔆 handler


## Diagram

![alt text](<🤵 PopBindTag ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 PopBindTag:

# Verify inputs
- ASSERT $bind

# Ask for the tag
- TEXT What to tag? >> $tag:
    Details: Provide an alias that you recognize.
    Default: $bind.Tag
    Nullable: True

# Update the Bind
- SAVE $bind:
    Tag: $tag
    Title: $tag

# Inform the user
- DONE Changed.
- GOODBYE
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`GOODBYE`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)  [`TEXT`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 💭/💭 TEXT ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds`](<../../../🤵🪣 Broker tables/Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
|
