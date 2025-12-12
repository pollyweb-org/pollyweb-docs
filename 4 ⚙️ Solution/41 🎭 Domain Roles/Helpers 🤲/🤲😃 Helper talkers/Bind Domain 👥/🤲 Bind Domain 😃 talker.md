# 🤲 Bind Domain 😃 handler

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * for a [Helper 🤲 domain](<../../🤲 Helper/🤲🎭 Helper role.md>) 
    * to identify a [Wallet 🧑‍🦰 app](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
    * as an admin of a [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>).

<br/>


## 💬 Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🗄️ [Vault](<../../../Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ] my Domain | > Bind

## 💬 Chat 

Consider the following excerpt from the [Flight check in 🤝 use case](<../../../../../3 🤝 Use Cases/03 🧳 Travel/09 🧳 Travel by air 💺/14 💺 Ticket/05 Flight check in.md>) as an example.

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🗄️ [Vault](<../../../Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ] my Wallet | > Bind
| 🤲 Helper     | ℹ️ I need Alice's passport.
| 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 Share passport?  [No] <br/> - [ 🇬🇧 UK Alice ]<br/>- [ 🇬🇧 UK Teresa ]<br/>- [ 🇺🇸 US Teresa ] | > 🇬🇧 UK Alice 
| 🛩️ Airline     | ✅ Thanks!
| 🗄️ [Vault](<../../../Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) | ✅ [Bound!](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)


<br/>

## Script

```yaml
📃 BindWallet:
- INFORM Bind       # Announce what's coming
- BIND .VAULT/SELF  # Ask to bind the wallet
- DONE|Bound!       # Confirmation
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`BIND`](<../../../Vaults 🗄️/🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>) [`DONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`INFORM`](<../../../Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) 
| [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`VAULT/SELF`](<../../../Vaults 🗄️/🗄️🧩 Vault schemas/🧩 VAULT'SELF code.md>)

<br/>

## Manifest 📜

```yaml
Forms: 
    Bind: .VAULT/SELF
```

