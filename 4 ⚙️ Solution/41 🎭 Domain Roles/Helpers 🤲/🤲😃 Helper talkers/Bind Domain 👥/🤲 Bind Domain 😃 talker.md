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
| 🤲 Helper |  😃 Hi! What do you need? <br/>- [ Bind ] my Domain | > Bind
| 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ Flow: Bind Domain [+]
| 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 Share domain admin?  [No] <br/> - [ 👥 Any Domain ]<br/>- [ 👥 Another Domain ] | > 👥 Any Domain
| 🆔 [Identity](<../../../../50 🫥 Agent domains/Identities 🆔/🆔 Identity agent/🆔 Identity 🫥 agent.md>) | 🫥 Let me see if it's you.   | [📸 selfie](<../../../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>)
| 🤲 Helper     | ✅ Domain bound!


<br/>

## Script

```yaml
📃 Bind Domain:
- INFORM: Bind Domain    # Announce what's coming
- BIND: .HOST/ADMIN      # Ask to bind the domain
- DONE: Domain bound!    # Confirmation
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`BIND`](<../../../Vaults 🗄️/🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>) [`DONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`INFORM`](<../../../Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) 
| [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`.HOST/ADMIN`](<../../../Hosts 🤗/🤗🧩 Host schemas/🧩 HOST'ADMIN.md>)

<br/>

## Manifest 📜

```yaml
Forms: 
    Bind Domain: .HOST/ADMIN
```

