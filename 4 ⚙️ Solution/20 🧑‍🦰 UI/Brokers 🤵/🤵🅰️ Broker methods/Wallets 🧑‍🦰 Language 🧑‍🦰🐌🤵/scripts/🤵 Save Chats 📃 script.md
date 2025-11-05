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
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PARALLEL`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SAVE`](<../../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SELECT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerChats` 🪣 table](<../../../🤵🪣 Broker tables/Chats 💬 table/🤵 BrokerChats 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Function 🐍.md>) | [`.Is`](<../../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.Is}.md>)
|
