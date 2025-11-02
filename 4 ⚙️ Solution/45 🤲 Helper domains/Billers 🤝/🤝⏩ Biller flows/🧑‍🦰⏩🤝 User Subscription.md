# 🧑‍🦰⏩🤝 Subscribe Wallets to Billers

![](<../.📎 Assets/💳 Biller User.png>)

For a user to [sign](<../../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/5 🆔⏩🔏 Verify Signatures.md>) a subscription, the following preconditions must be met:
- 1/ the user has default [Payer 💳](<../../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) and [Identity 🆔](<../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) domains;
- 2/ the [Seller 💵 domain](<../../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) has a default [Collector 🏦 domain](<../../Collectors 🏦/🏦🤲 Collector helper.md>).

The following steps describe a subscription workflow:
- 1/ the user initiates a chat with a [Seller 💵](<../../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>);
- 2/ the user selects a subscription in the chat;
- 3/ the Seller's [Biller 🤝](<../🤝🤲 Biller helper.md>) sends the PDF terms to the user;
- 4/ the user accepts the PDF terms;
- 5/ the user's [Identity 🆔 domain](<../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) authenticates the user;
- 6/ the user's [Payer 💳](<../../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) asks the user for a payment method;
- 7/ the [Seller 💵](<../../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) confirms the subscription;
- 8/ the  [Biller 🤝](<../🤝🤲 Biller helper.md>)  initiates the monthly collection.

<br/>

## Chat

| [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| - | - | - 
| 🛠️ [Helper](<../../$ Helpers 🤲/🤲👥 Helper domain.md>) | 😃 Hi! What do you need? <br/>- [ Register ]  | > Register
| 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵🤲 Broker helper.md>) | 🫥 [Ready to register](<../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)? [Yes, No]<br>- Your broker binds with us 🔗 <br/>- You choose a billing plan 🤝 <br/>- Your payer adds a method 💳 <br/>- Your identity signs the terms 🆔 | > Yes
| 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵🤲 Broker helper.md>) | 🫥 [Bind?](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind vault ⏩ flow.md>) [Yes, No, +] <br/>- [Vault 🧩](<../../../../7 🧩 Codes/$/🧩 VAULT code.md>) | > Yes 
| 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵🤲 Broker helper.md>) | 🫥 [Allow guest domain?](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>) <br/> - Any Biller 🤝<br/>- [ Always ] for Any Helper 🤲 | > Always
| 🤝 [Biller](<../🤝🤲 Biller helper.md>) | 😃 What plan to subscribe? <br/>- [ Simple ] pay-as-you-go  <br/>- [ Monthly ] commitment | > Simple
| 💳 [Payer](<../../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | 🫥 Link to Any Biller? [Yes, No, +] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC 
| 🆔 [Identity](<../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) | 🫥 [Sign terms?](<../../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/5 🆔⏩🔏 Verify Signatures.md>) 📄 [Yes, No] | > Yes
| 🆔 [Identity](<../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<../../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/6 🆔⏩😶 Face scan.md>)
| 🛠️ [Helper](<../../$ Helpers 🤲/🤲👥 Helper domain.md>) | ✅ Done!
|

<br/>

## Talker

The corresponding [Script 📃](<../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) is as follows.

```yaml
💬 Register:                # Entry menu
- INFORM|Register           # Provide instructions
- BIND|.VAULT               # Bind to Wallet

- INVITE >> $billed:        
    Invitee: any-biller.com # Invite the Biller
    Schema: .BILLER/SUBSCRIBE # Run the subscription

- FREEZE >> $inputs:        # Freeze all inputs
    Billed: $billed         # Add billing info
    Chat: $.Chat            # Add context

- EVAL|Save($inputs)        # Save the register

- SUCCESS|Done!             # Inform success
- GOODBYE                   # Show advertisement
```

| [Command ⌘](<../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | Purpose
|-|-
| 📝 [`INFORM`](<../../../35 💬 Chats/Scripts 📃/📃 methods 🤵/INFORM 📝/📝 INFORM ⌘ cmd.md>) | To provide instructions.
| 🔗 [`BIND`](<../../../35 💬 Chats/Scripts 📃/📃 methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) | To create a user profile.
| 🛠️ [`INVITE`](<../../../35 💬 Chats/Scripts 📃/📃 methods 🤵/INVITE 🤲/🤲 INVITE ⌘ cmd.md>) | To subscribe the user to plan.
| ❄️ [`FREEZE`](<../../../35 💬 Chats/Scripts 📃/📃 methods 🤵/FREEZE ❄️/❄️ FREEZE ⌘ cmd.md>) | To disable past inputs.
| ⬇️ [`EVAL`](<../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) | To register on the database.
| ✅ [`SUCCESS`](<../../../35 💬 Chats/Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>) | To say that it was successful.
| 👋 [`GOODBYE`](<../../../35 💬 Chats/Scripts 📃/📃 methods 🤵/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) | To show advertising.
|
