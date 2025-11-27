# 🤵 OnPopToken 🔔 handler

> Part of the [`Broker.Pops` 🪣 table](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)

<br/>

## Script

<!-- TODO: Finish the code -->

```yaml
📃 Pop-Token: 

# Assert $.Msg
- ASSERT|$.Msg:
    AllOf: Hook, Token
    UUIDs: Hook, Token

# Get the Token 🎫
- READ >> $token:
    Set: Broker.Tokens
    Key: $Token

# Verify the Message
- VERIFY|$.Msg:
    Key: $token.Wallet.PublicKey

# Ask for an action.
- ONE|What do you need?:
    - /Tag Token
    - /Remove Token

# Execute the action.
- CASE:
    Set:
        RUN|Tag-Token:
            $token
    Remove: 
        RUN|Remove-Token:
            $token
```

Uses: [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
