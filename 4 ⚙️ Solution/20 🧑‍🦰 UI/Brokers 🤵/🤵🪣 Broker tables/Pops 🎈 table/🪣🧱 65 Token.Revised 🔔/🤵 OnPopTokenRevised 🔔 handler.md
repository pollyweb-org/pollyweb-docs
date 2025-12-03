# 🤵 OnPopTokenRevised 📃 script

> About
* Part of the [`Broker.Pops` 🪣 table](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
* Part of the [`Broker.Tokens.Revise` ⏩ flow](<../../Tokens 🎫 table/🪣🧱 50 Revise ⏩ flow/🤵 Broker.Tokens.Revise ⏩ flow.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts 
    * to an [Issuer 🎴 domain](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) invocation 
    * of the [`Revise@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>).

<br/>

## Diagram

![alt text](<🤵 OnPopTokenRevised ⚙️ uml.png>)

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
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`INFO`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Pops`](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
|
