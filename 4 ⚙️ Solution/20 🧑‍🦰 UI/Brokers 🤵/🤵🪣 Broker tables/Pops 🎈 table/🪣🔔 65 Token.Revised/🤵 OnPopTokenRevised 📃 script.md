# 🤵 OnPopTokenRevised 📃 script

## Script

```yaml
📃 OnPopTokenRevised:

# Load the Chat settings
- CHAT|$Pop.Chat

# Read the token
- READ >> $token:
    Set: Broker.Tokens
    Key:
        Token: $Pop.Inputs.Key.Token
        Token: $Pop.Inputs.Key.Issuer

# Inform the user
- INFO:
    Text: >
        Token revised:
        - Token: 
    Token: 

# Update the Token 🎫
- SAVE|$token:
    Tag: $tag
    Title: $tag

# Inform the user 🤔
- SUCCESS|Changed.
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SUCCESS`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>) [`TEXT`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens` 🪣 table](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
|
