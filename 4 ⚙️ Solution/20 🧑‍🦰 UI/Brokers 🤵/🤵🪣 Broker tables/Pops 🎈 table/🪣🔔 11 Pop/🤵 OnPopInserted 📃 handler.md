# 🤵📃 OnPopped handler


## Diagram

![alt text](<🤵 OnPopInserted ⚙️ uml.png>)


## Script


```yaml
📃 OnPopped: 

# Assert the Pop
- ASSERT|$Pop:
    AllOf: Wallet, Hook

# Add the Chat
- SAVE|Broker.Chats:
    Hook: $Pop.Hook
    Wallet: $Pop.Wallet
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) {{SAVE}}
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | {{Broker.Pops table}}
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | {{$.Hosted}}
|