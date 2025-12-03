# 🤵📃 Tag Token script

> Part of the [`Broker.Pops` 🪣 table](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)

> Flow
* Called by the [`OnPopToken` 🔔 handler](<../🪣🧱 61 Token 🔔/🤵 OnPopToken 🔔 handler.md>)

## Script

```yaml
📃 Tag-Token:

# Verify inputs
- ASSERT|$.Inputs:
    AllOf: token

# Ask for the tag 🤔
- TEXT|What to tag? >> $tag
    Details: Provide an alias that you recognize.
    Default: $token.Tag
    Nullable: True

# Update the Token 🎫
- SAVE|$token:
    Tag: $tag
    Title: $tag

# Inform the user 🤔
- DONE|Changed.
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`DONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`TEXT`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens` 🪣 table](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
|
