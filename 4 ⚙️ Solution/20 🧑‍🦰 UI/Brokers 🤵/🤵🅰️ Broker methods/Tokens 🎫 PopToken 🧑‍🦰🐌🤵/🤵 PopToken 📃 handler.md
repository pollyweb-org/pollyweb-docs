# 🤵📃 Pop handler

> [Script 📃](<🤵 PopToken 🐌 msg.md>) that implements the [`Pop@Broker` 🅰️ method](<🤵 PopToken 🐌 msg.md>)

<br/>

## Script

<!-- TODO: Finish the code -->

```yaml
📃 Pop: 

# Assert $.Msg
- ASSERT|$.Msg:
    - AllOf: Hook, Token
    - UUIDs: Hook, Token

# Get the Token 🎫
- READ >> $token:
    Set: BrokerTokens
    Key: $Token

# Verify the Message
- VERIFY|$.Msg:
    Key: $token.Wallet.PublicKey

# Ask for an action.
- ONE|What do you need?:
    - /Set token title
    - /Remove token

# Execute the action.
- CASE:
    Set:
        RUN|Set-tag:
            $token
    Remove: 
        RUN|Remove-Token:
            $token
```

Uses: [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
