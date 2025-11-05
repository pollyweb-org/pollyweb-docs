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
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PARALLEL`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SAVE`](<../../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SELECT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerTokens` 🪣 table](<../../../🤵🪣 Broker tables/Tokens 🎫 table/🤵 BrokerTokens 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Function 🐍.md>) | [`.Is`](<../../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.Is}.md>)
|
