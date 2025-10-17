<!-- TODO: Add lists of commands. -->

# 🔆 Pop Token

> Implements [🧑‍🦰💬🤵 Remove Token 🎫](<../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Tokens 🎫/💬🤵 Remove 🎫.md>)

<br/>

```yaml
💬 Handler:

# Get the Wallet 🧑‍🦰
- MAP|Wallets|$.Msg.Header.From >> $wallet

# Verify the Message.
- VERIFY|$.Msg|$wallet.PublicKey

# Get the Token 🎫
- MAP|$wallet.Tokens|$.Msg.Body.Key >> $token

# Ask for an action.
- ONE|What do you need?:
    - /Remove token

# Execute the action.
- CASE:
    Remove: RUN|RemoveToken
```

```yaml
RemoveToken:

# Ask for confirmation 🤔
- CONFIRM|Remove token {$token.Title}?

# Remove the Token 🎫
- DELETE|$token >> $delete:
    Soft: 30 days

    OnSoft: 
        # Update the Token 🎫 list
        - MSG|Updated@Notifier|$wallet.Notifier:
            WalletID: $wallet.ID
            Updates: [ TOKENS ]

    OnHard:
        # Remove from Wallet
        - MSG|Remove@Notifier|$wallet.Notifier:
            WalletID: $wallet.ID
            Path: $token.Path

# Inform the user 🤔
- SUCCESS|Token removed.:
    Options: 
        - /Undo removal

# Undo the removal.
- CASE:
    Undo: RUN|UndoRemoval
```

```yaml
UndoRemoval:

# Cancel the soft delete.
- UNDO|$delete

# Inform the user 🤔
- SUCCESS|Token restored.
```
