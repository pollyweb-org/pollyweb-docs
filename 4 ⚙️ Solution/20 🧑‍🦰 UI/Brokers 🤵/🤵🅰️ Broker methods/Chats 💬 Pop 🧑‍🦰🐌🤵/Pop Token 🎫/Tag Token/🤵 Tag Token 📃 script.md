<!-- TODO: Add lists of commands. -->

# 🤵📃 Tag Token script

> Flow
* Called by the [`Pop Token` 📃 handler](<../🤵 Pop Token 📃 handler.md>)

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

# Update the Token 🎫 list
- RUN|Update-Notifier:
    wallet: $token.Wallet
    updates: TOKENS

# Inform the user 🤔
- SUCCESS|Changed.
```

Uses||
|-|-
|[Commands ⌘](<../../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CASE`](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`CONFIRM`](<../../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`DELETE`](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) [`SEND`](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`SUCCESS`](<../../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>) [`RUN`](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)
| [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | 
