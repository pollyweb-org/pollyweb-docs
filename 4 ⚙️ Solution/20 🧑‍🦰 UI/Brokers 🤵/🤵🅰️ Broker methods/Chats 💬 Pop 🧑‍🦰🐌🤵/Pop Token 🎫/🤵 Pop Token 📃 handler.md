<!-- TODO: Add lists of commands. -->

# 🤵📃 Pop Token 🎫 

> [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/📃 Script.md>) that implements [`Remove Token` 🎫 flow](<../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/Remove 💬🎫🤵 /🧑‍🦰 Remove Token ⏩ flow.md>)

> Called by [`Pop@Broker` 🅰️ method](<../🤵 Pop 🐌 msg.md>)


<br/>

## Script

```yaml
📃 PopToken:

# Verify inputs
- ASSERT|$.Inputs:
    AllOf: Token, Wallet
    UUIDs: Token

# Get the Token 🎫
- GET >> $token:
    Set: $:Wallet.Tokens
    Key: $:Token

# Ask for an action.
- ONE|What do you need?:
    - /Remove token

# Execute the action.
- CASE:
    Remove: 
      - RUN|RemoveToken:
          Token: $token
          Wallet: $:Wallet
```

Commands: [`ASSERT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`GET`](<../../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`ONE`](<../../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>)  [`RUN`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)

```yaml
📃 RemoveToken:

# Verify inputs
- ASSERT|$.Inputs:
    AllOf: Token, Wallet

# Get the token
- GET >> $token:
    Set: BrokerTokens
    Key: $:Token

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

Commands: [`CASE`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`CONFIRM`](<../../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`DELETE`](<../../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) [`SEND`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`SUCCESS`](<../../../../../35 💬 Chats/Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>) [`RUN`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)


```yaml
📃 UndoRemoval:

# Cancel the soft delete.
- UNDO|$delete

# Inform the user 🤔
- SUCCESS|Token restored.
```

Commands: [`UNDO`](<../../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) [`SUCCESS`](<../../../../../35 💬 Chats/Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)