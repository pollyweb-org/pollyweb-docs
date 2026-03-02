# 🗄️ Bind 😃 handler

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * for a [Vault 🗄️ domain](<../../🗄️ Vault/🗄️🎭 Vault role.md>) 
    * to identify a [Wallet 🧑‍🦰 app](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
    * on subsequent [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

<br/>


## 💬 Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🗄️ [Vault](<../../🗄️ Vault/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ] my Wallet | > Bind
| 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 [Bind?](<../../🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>) [Yes, No] <br/> - Vault Personalization 🧩 <br/> - By Any Vault 🗄️ <br/> - Description: Bla, bla | > Yes
| 🗄️ [Vault](<../../🗄️ Vault/🗄️🎭 Vault role.md>) | ✅ Wallet bound!


<br/>

## Script

```yaml
📃 Bind Wallet:
- BIND: .VAULT/SELF     # Ask to bind the wallet
- DONE: Wallet bound!   # Confirmation
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`BIND`](<../../🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>) [`DONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`INFORM`](<../../../Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) 
| [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`.VAULT/SELF`](<../../🗄️🧩 Vault schemas/🧩 VAULT'SELF.md>)

<br/>
