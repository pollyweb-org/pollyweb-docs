# 🤵 PopToken 🔆 handler

<br/>

## Diagram

![alt text](<🤵 PopToken ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 PopToken: 

# Assert the inputs
- ASSERT:
    $.Chat.Wallet: 
    $.Chat.Inputs.Token:
    $.Chat.Inputs.Issuer:

# Get the Token 🎫
- SELECT >> $token:
    From: Broker.Tokens
    Where: 
        Token: $.Chat.Inputs.Token
        Issuer: $.Chat.Inputs.Issuer
        Wallet: $.Chat.Wallet

# Show info about the Token
- INFO|Token: ´{$token.Title}´

# Add general options
- IF|$token.State.IsIn(ACTIVE, REMOVED):
    - PUT +> $options: /Tag Token

# Add options of active tokens
- IF|$token.State.Is(ACTIVE):
    - PUT +> $options: /Remove Token

# Ask for an action.
- ONE|What do you need?:
    Options: $options

# Execute the action.
- CASE >> $handler:
    Tag: PopTokenTag
    Remove: PopTokenRemove

# Handle the selection
- RUN|$handler: $token
```

Uses ||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`IFNOT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IFNOT ⤵️/⤵️ IFNOT ⌘ cmd.md>) [`INFO`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/1️⃣ ONE ⌘ cmd.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SELECT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens`](<../../../🤵🪣 Broker tables/Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Is`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) 