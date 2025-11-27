# 🤵 OnPopTokenRevised 📃 script

> Part of the [`Broker.Pops` 🪣 table](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)

> Part of the [`Broker.Tokens.Revise` ⏩ flow](<../../Tokens 🎫 table/🪣⏩ Flows/🪣🧱 7 Revise ⏩ flow/🤵 Broker.Tokens.Revise ⏩ flow.md>)

<br/>

## Script

```yaml
📃 OnPopTokenRevised:

# Assert the Pop
- ASSERT|$Pop:
    AllOf: Chat, Inputs.Key.Token, Inputs.Key.Issuer
    UUIDs: Chat, Inputs.Key.Token
    Texts: Inputs.Key.Issuer

# Load the Chat settings
- CHAT|$Pop.Chat

# Inform the user
- INFO:
    # Don't translate the title
    Text: >
        Token revised:
        - Token: ´{$Pop.Token.Title}´ 
        - Status: {$Pop.Token.Status}
        - Starts: {$Pop.Token.Start}
        - Expires: {$Pop.Token.Expires}
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CHAT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`INFO`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Pops`](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
|
