<!-- TODO: Add lists of commands. -->

# 🤵📃 Remove Token 🎫 

> Part of the [`Broker.Pops` 🪣 table](<../../../🤵🪣 Broker tables/Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements [`Remove Token` ⏩ flow](<../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/Remove 💬🎫🤵 /🧑‍🦰 Remove Token ⏩ flow.md>)

> Flow
* Called by the [`Pop Token` 📃 handler](<../Token/🤵 PopToken 🔆 handler.md>)

## Script

```yaml
📃 Remove-Token:

# Verify inputs
- ASSERT|$.Inputs:
    AllOf: token

# Ask for confirmation 🤔
- CONFIRM|Remove Token {$token.Title}?

# Remove the Token 🎫
- DELETE|$token >> $deleted:
    Undo: 30 days

# Inform the user 🤔
- DONE:
    Text: Token removed.
    Options: 
        - /Undo removal

# Undo the removal.
- CASE:
    Undo: 
      - RUN|Undo-Token-Removal:
          $deleted
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`DELETE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`DONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)
