<!-- TODO: Add lists of commands. -->

# 🤵📃 Pop Token 🎫 

> [Script 📃](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements [`Remove Token` 🎫 flow](<../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/💬🤵 Remove 🎫 chat.md>)

> Called by [`Pop@Broker` 🅰️ method](<Pop 🅰️ method.md>)


<br/>

## Script

```yaml
📃 PopToken:

# Verify inputs
- ASSERT:
    AllOf: !Token, !Wallet
    UUIDs: !Token

# Get the Token 🎫
- GET >> $token:
    Set: !Wallet.Tokens
    Key: !Token

# Ask for an action.
- ONE|What do you need?:
    - /Remove token

# Execute the action.
- CASE:
    Remove: 
      - RUN|RemoveToken:
          Token: $token
          Wallet: !Wallet
```

Commands: [`ASSERT`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`CASE`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/CASE ⏯️/CASE ⏯️.md>) [`GET`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) [`ONE`](<../../../../../35 💬 Chats/🤔 Prompts/🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>)  [`RUN`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RUN ▶️/RUN ▶️.md>)

```yaml
📃 RemoveToken:

# Verify inputs
- ASSERT:
    AllOf: !Token, !Wallet

# Ask for confirmation 🤔
- CONFIRM|Remove token {$token.Title}?

# Remove the Token 🎫
- DELETE|$token >> $delete:
    Undo: 30 days

# Update the Token 🎫 list
- RUN|UpdateTokens:
    wallet: $wallet

# Inform the user 🤔
- SUCCESS|Token removed.:
    Options: 
        - /Undo removal

# Undo the removal.
- CASE:
    Undo: RUN|UndoRemoval
```

Commands: [`CASE`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/CASE ⏯️/CASE ⏯️.md>) [`CONFIRM`](<../../../../../35 💬 Chats/🤔 Prompts/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`DELETE`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/DELETE/DELETE 🗑️ item.md>) [`SEND`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>) [`SUCCESS`](<../../../../../35 💬 Chats/🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>) [`RUN`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RUN ▶️/RUN ▶️.md>)


```yaml
📃 UndoRemoval:

# Cancel the soft delete.
- UNDO|$delete

# Inform the user 🤔
- SUCCESS|Token restored.
```

Commands: [`UNDO`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/UNDO/UNDO ↩️.md>) [`SUCCESS`](<../../../../../35 💬 Chats/🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)