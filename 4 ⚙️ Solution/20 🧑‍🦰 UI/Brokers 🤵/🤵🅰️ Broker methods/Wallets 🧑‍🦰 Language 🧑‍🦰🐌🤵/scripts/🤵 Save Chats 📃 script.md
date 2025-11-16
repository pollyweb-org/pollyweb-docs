# 🤵📃 Save Chats

> Part of the [`Language` 📃 handler](<../🤵 Language 📃 handler.md>)

## Script

```yaml
📃 Save-Chats:

# Verify the required inputs
- ASSERT:
    AllOf: $wallet, $translated

# Save the Chats
- PARALLEL|$wallet.Chats|$chat:
    
    # Set the Host title
    - SELECT >> $chat.Host$:
        First: Translation
        From: $translated.Domains
        Where: Domain.Is($chat.Host)
    
    # Save the Chat
    - SAVE|$chat
```


|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PARALLEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SELECT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerChats` 🪣 table](<../../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Is`](<../../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/Is ⓕ any.md>)
|
