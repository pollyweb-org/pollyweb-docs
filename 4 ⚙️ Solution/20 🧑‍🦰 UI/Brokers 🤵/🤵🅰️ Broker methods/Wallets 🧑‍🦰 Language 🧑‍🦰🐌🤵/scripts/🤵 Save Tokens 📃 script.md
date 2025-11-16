# 🤵📃 Save Tokens

> Part of the [`Language` 📃 handler](<../🤵 Language 📃 handler.md>)

## Script

```yaml
📃 Save-Tokens:

# Verify the required inputs
- ASSERT:
    AllOf: $wallet, $translated

# Save the Tokens
- PARALLEL|$wallet.Tokens|$token:

    # Set the Issuer
    - SELECT >> $token.Issuer$: 
        First: Translation
        From: $translated.Domains
        Where: Domain.Is($token.Issuer)

    # Set the Schema
    - SELECT >> $token.Schema$: 
        First: Translation
        From: $translated.Schemas
        Where: Schema.Is($token.Schema)
    
    # Save the Token
    - SAVE|$token
```


|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PARALLEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SELECT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerTokens` 🪣 table](<../../../🤵🪣 Broker tables/Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Is`](<../../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/Is ⓕ any.md>)
|
