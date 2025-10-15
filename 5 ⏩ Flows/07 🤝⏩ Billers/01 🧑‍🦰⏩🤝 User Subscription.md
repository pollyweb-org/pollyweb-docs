# 🧑‍🦰⏩🤝 Subscribe Wallets to Billers

![](<../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/. 📎 Assets/💳 Biller User.png>)

For a user to [sign](<../../4 ⚙️ Solution/50 🫥 Agents/45 🆔 Identities/16 🆔🔏 Verify Signatures.md>) a subscription, the following preconditions must be met:
- 1/ the user has default [Payer 💳](<../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) and [Identity 🆔](<../../../../../../4 ⚙️ Solution/50 🫥 Agents/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) domains;
- 2/ the [Seller 💵 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/70 💵 Sellers/$ 💵🎭 Seller role.md>) has a default [Collector 🏦 domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>).

The following steps describe a subscription workflow:
- 1/ the user initiates a chat with a [Seller 💵](<../../4 ⚙️ Solution/41 🎭 Domain Roles/70 💵 Sellers/$ 💵🎭 Seller role.md>);
- 2/ the user selects a subscription in the chat;
- 3/ the Seller's [Biller 🤝](<../../4 ⚙️ Solution/45 🛠️ Helper domains/20 🤝 Billers/$ 🤝🛠️ Biller helper.md>) sends the PDF terms to the user;
- 4/ the user accepts the PDF terms;
- 5/ the user's [Identity 🆔 domain](<../../../../../../4 ⚙️ Solution/50 🫥 Agents/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) authenticates the user;
- 6/ the user's [Payer 💳](<../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) asks the user for a payment method;
- 7/ the [Seller 💵](<../../4 ⚙️ Solution/41 🎭 Domain Roles/70 💵 Sellers/$ 💵🎭 Seller role.md>) confirms the subscription;
- 8/ the  [Biller 🤝](<../../4 ⚙️ Solution/45 🛠️ Helper domains/20 🤝 Billers/$ 🤝🛠️ Biller helper.md>)  initiates the monthly collection.

<br/>

## Chat

| [Domain](<../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| - | - | - 
| 🛠️ [Helper](<../../4 ⚙️ Solution/45 🛠️ Helper domains/$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>) | 😃 Hi! What do you need? <br/>- [ Register ]  | > Register
| 🤵 [Broker](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) | 🫥 [Ready to register](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/02 💼⏩🧑‍🦰 Inform 📝.md>)? [Yes, No]<br>- Your broker binds with us 🔗 <br/>- You choose a billing plan 🤝 <br/>- Your payer adds a method 💳 <br/>- Your identity signs the terms 🆔 | > Yes
| 🤵 [Broker](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) | 🫥 [Bind?](<../90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind 🔗.md>) [Yes, No, +] <br/>- [Vault 🧩](<../../7 🧩 Codes/$/🧩 VAULT code.md>) | > Yes 
| 🤵 [Broker](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) | 🫥 [Allow guest domain?](<../50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite 🛠️.md>) <br/> - Any Biller 🤝<br/>- [ Always ] for Any Helper 🛠️ | > Always
| 🤝 [Biller](<../../4 ⚙️ Solution/45 🛠️ Helper domains/20 🤝 Billers/$ 🤝🛠️ Biller helper.md>) | 😃 What plan to subscribe? <br/>- [ Simple ] pay-as-you-go  <br/>- [ Monthly ] commitment | > Simple
| 💳 [Payer](<../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Link to Any Biller? [Yes, No, +] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC 
| 🆔 [Identity](<../../../../../../4 ⚙️ Solution/50 🫥 Agents/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) | 🫥 [Sign terms?](<../../4 ⚙️ Solution/50 🫥 Agents/45 🆔 Identities/16 🆔🔏 Verify Signatures.md>) 📄 [Yes, No] | > Yes
| 🆔 [Identity](<../../../../../../4 ⚙️ Solution/50 🫥 Agents/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<../../4 ⚙️ Solution/50 🫥 Agents/45 🆔 Identities/21 🆔😶 Face scan.md>)
| 🛠️ [Helper](<../../4 ⚙️ Solution/45 🛠️ Helper domains/$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>) | ✅ Done!
|

<br/>

## Talker

The corresponding [Talker 😃](<../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) is as follows.

```yaml
💬 Register:                # Entry menu
- INFORM|Register           # Provide instructions
- BIND|.VAULT               # Bind to Wallet

- INVITE >> $billed:        
    Invitee: any-biller.com # Invite the Biller
    Code: .BILLER/SUBSCRIBE # Run the subscription

- FREEZE >> $inputs:        # Freeze all inputs
    Billed: $billed         # Add billing info
    Chat: $.Chat            # Add context

- EVAL|Save($inputs)        # Save the register

- SUCCESS|Done!             # Inform success
- GOODBYE                   # Show advertisement
```

| [Command ⌘](<../../9 😃 Talkers/40 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
|-|-
| 📝 [`INFORM`](<../../9 😃 Talkers/60 ⏩ Msg flows/41 📝 INFORM msg.md>) | To provide instructions.
| 🔗 [`BIND`](<../../9 😃 Talkers/60 ⏩ Msg flows/44 🔗 BIND msg.md>) | To create a user profile.
| 🛠️ [`INVITE`](<../../9 😃 Talkers/60 ⏩ Msg flows/46 🛠️ INVITE msg.md>) | To subscribe the user to plan.
| ❄️ [`FREEZE`](<../../9 😃 Talkers/60 ⏩ Msg flows/42 ❄️ FREEZE msg.md>) | To disable past inputs.
| ⬇️ [`EVAL`](<../../9 😃 Talkers/30 🗃️ Talker data/20 ⬇️ EVAL flow.md>) | To register on the database.
| ✅ [`SUCCESS`](<../../9 😃 Talkers/20 🤔 Prompts/4 ⚠️ Status prompts/23 ✅ SUCCESS prompt.md>) | To say that it was successful.
| 👋 [`GOODBYE`](<../../9 😃 Talkers/60 ⏩ Msg flows/50 👋 GOODBYE.md>) | To show advertising.
|
