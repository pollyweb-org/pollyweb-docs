<!-- TODO: Add lists of commands. -->

# 🤵📃 Pop Token 🎫 

> [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements [`Remove Token` 🎫 flow](<../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/Remove 💬🎫🤵 /🧑‍🦰 Remove Token ⏩ flow.md>)

> Called by [`Pop@Broker` 🅰️ method](<../🤵 Pop 🐌 msg.md>)


<br/>

## Script

```yaml
📃 Pop-Token:

# Verify inputs
- ASSERT|$.Inputs:
    AllOf: Token, Wallet
    UUIDs: Token

# Get the Token 🎫
- READ >> $token:
    Set: $Wallet.Tokens
    Key: $Token

# Ask for an action.
- ONE|What do you need?:
    - /Remove token

# Execute the action.
- CASE:
    Remove: 
      - RUN|RemoveToken:
          Token: $token
          Wallet: $Wallet
```

Uses: [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>)  [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
