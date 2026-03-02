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
| 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ⓘ Flow: Bind Domain [+]
| 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 Share domain admin?  [No] <br/> - [ 👥 Any Domain ]<br/>- [ 👥 Another Domain ] | > 👥 Any Domain
| 🆔 [Identifier](<../../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) | 🫥 Let me see if it's you.   | [📸 selfie](<../../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>)
| 🤲 Helper     | ✅ Domain bound!


<br/>

## Script

```yaml
📃 Bind Domain:
- ASSERT: $.Chat.Wallet     # Ensure there's a wallet

- INFORM: Bind Domain       # Open the form
- SHARE: .DOMAIN >> $token  # Get a domain Token
- VERIFY: $token            # Verify the Token
- IDENTIFY: $token          # Verify the Token's user

- SAVE Helper.Domains:      # Save the binding
    Domain: $token.Issuer
    Wallet: $.Chat.Wallet
- GOODBYE: Domain bound!    # Show confirmation
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`BIND`](<../../../Vaults 🗄️/🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>) [`DONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`IDENTIFY`](<../../../Consumers 💼/💼⌘ Consumer cmds/IDENTIFY 🆔/🆔 IDENTIFY ⌘ cmd.md>) [`INFORM`](<../../../Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) 
| [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`.DOMAIN`](<../../../../40 👥 Domains/👥🧩 Domain schemas/🧩 DOMAIN.md>)

<br/>

## Manifest 📜

```yaml
Forms: 
    Bind Domain: .DOMAIN
```

