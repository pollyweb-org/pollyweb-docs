<!-- TODO: Add lists of commands. -->

# 🔆 Locator: Pop Token

> [Script ▶️](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/▶️ Script.md>) that implements [`Remove Token` 🎫 flow](<../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Tokens 🎫/💬🤵 Remove 🎫.md>)

> Called by [`Pop@Broker` 🅰️ method](<../🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Pop.md>)


<br/>

## Script

```yaml
▶️ PopToken:

# Get the Token 🎫
- GET|$wallet.Tokens|$.Msg.Body.Key >> $token

# Ask for an action.
- ONE|What do you need?:
    - /Remove token

# Execute the action.
- CASE:
    Remove: RUN|RemoveToken
```

Commands: [`CASE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/CASE ⏯️.md>) [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) [`ONE`](<../../../35 💬 Chats/🤔 Prompts/🤔✏️ Prompt inputs/53 1️⃣ ONE prompt.md>)  [`RUN`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/RUN ▶️.md>)

```yaml
▶️ RemoveToken:

# Ask for confirmation 🤔
- CONFIRM|Remove token {$token.Title}?

# Remove the Token 🎫
- DELETE|$token >> $delete:
    Soft: 30 days

    OnSoft: 
        # Update the Token 🎫 list
        - SEND:
            To: $wallet.Notifier
            Subject: Updated@Notifier
            Wallet: $wallet.ID
            Updates: [ TOKENS ]

    OnHard:
        # Remove from Wallet
        - SEND:
            To: $wallet.Notifier
            Subject: Remove@Notifier
            Wallet: $wallet.ID
            Path: $token.Path

# Inform the user 🤔
- SUCCESS|Token removed.:
    Options: 
        - /Undo removal

# Undo the removal.
- CASE:
    Undo: RUN|UndoRemoval
```

Commands: [`CASE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/CASE ⏯️.md>) [`CONFIRM`](<../../../35 💬 Chats/🤔 Prompts/🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>) [`DELETE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/DELETE 🗑️ item.md>) [`SEND`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) [`SUCCESS`](<../../../35 💬 Chats/🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>) [`RUN`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/RUN ▶️.md>)


```yaml
▶️ UndoRemoval:

# Cancel the soft delete.
- UNDO|$delete

# Inform the user 🤔
- SUCCESS|Token restored.
```

| Command | Details
|-|-
| {{UNDO}}
| ✅ [`SUCCESS`](<../../../35 💬 Chats/🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>)