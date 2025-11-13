<!-- TODO: Add lists of commands. -->

# 🤵📃 Undo Token Removal 🎫 

> Purpose
* [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements [`Remove Token` 🎫 flow](<../../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/Remove 💬🎫🤵 /🧑‍🦰 Remove Token ⏩ flow.md>)

> Flow
* Called by the [`Remove Token` 📃 script](<🤵 Remove Token 📃 script.md>)

## Script

```yaml
📃 Undo-Token-Removal:

# Verify inputs
- ASSERT|$.Inputs:
    AllOf: deleted

# Cancel the soft delete.
- UNDO|$deleted

# Inform the user 🤔
- SUCCESS|Token restored.
```

Uses: [`UNDO`](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) [`SUCCESS`](<../../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)