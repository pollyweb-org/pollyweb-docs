# 🤵📃 Tag Token script

> Flow
* Called by the [`Pop Token` 📃 handler](<../🪣🔔 4 Token/🤵 Pop Token 📃 handler.md>)

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
- SUCCESS|Changed.
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SUCCESS`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>) [`TEXT`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Bro../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.mdker.Tokens 🪣 table.md>)
|
