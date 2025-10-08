# 🧑‍🦰⏩🤝 Subscribe Wallets to Billers

![](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/00 📎 Assets/💳 Biller User.png>)

For a user to [sign](<../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/16 🆔🔏 Verify Signatures.md>) a subscription, the following preconditions must be met:
- 1/ the user has default [Payer 💳](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) and [Identity 🆔](<../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) domains;
- 2/ the [Seller 💵 domain](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) has a default [Collector 🏦 domain](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>).

The following steps describe a subscription workflow:
- 1/ the user initiates a chat with a [Seller 💵](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>);
- 2/ the user selects a subscription in the chat;
- 3/ the Seller's [Biller 🤝](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>) sends the PDF terms to the user;
- 4/ the user accepts the PDF terms;
- 5/ the user's [Identity 🆔 domain](<../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) authenticates the user;
- 6/ the user's [Payer 💳](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) asks the user for a payment method;
- 7/ the [Seller 💵](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) confirms the subscription;
- 8/ the  [Biller 🤝](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>)  initiates the monthly collection.

<br/>

## Chat

| Service | Prompt  | User 
| - | - | - 
| 🛠️ [Helper](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 😃 Hi! What do you need? <br/>- [ Register ]  | > Register
| 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Ready to register?](<../50 🤗⏩ Hosts/05 🤗⏩🧑‍🦰 Form 📝.md>)? [Yes, No]<br>- Your broker binds with us 🔗 <br/>- You choose a billing plan 🤝 <br/>- Your payer adds a method 💳 <br/>- Your identity signs the terms 🆔 | > Yes
| 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Bind?](<../../8 📜 Manifests/👥 nlweb.org/{codes}/HOST/🧩 HostPersonalize.md>) | > Yes 
| 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Allow guest domain?](<../50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite 🛠️.md>) <br/> - Any Biller 🤝<br/>- [ Always ] for Any Helper 🛠️ | > Always
| 🤝 [Biller](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>) | 😃 What plan to subscribe? <br/>- [ Simple ] pay-as-you-go  <br/>- [ Monthly ] commitment | > Simple
| 💳 [Payer](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Link to Any Biller? [Yes, No, +] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC 
| 🆔 [Identity](<../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 [Sign terms?](<../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/16 🆔🔏 Verify Signatures.md>) 📄 [Yes, No] | > Yes
| 🆔 [Identity](<../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/21 🆔😶 Face scan.md>)
| 🛠️ [Helper](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | ✅ Done!
|

<br/>

## Talker

The corresponding [Talker 😃](<../../33 😃 Talkers/01 😃 Talker.md>) is as follows.

```yaml
💬 Register:                # Entry menu
- FORM|Register             # Provide instructions
- BIND|@HOST/PROFILE        # Bind to Wallet

- INVITE >> $billed:        
    Invitee: any-biller.com # Invite the Biller
    Code: @BILLER/SUBSCRIBE # Run the subscription

- FREEZE >> $inputs:        # Freeze all inputs
    Billed: {$billed}       # Add billing info
    Chat: {.Chat}           # Add context

- EVAL|{Save($inputs)}      # Save the register

- SUCCESS|Done!             # Inform success
- GOODBYE                   # Show advertisement
```

| [Command ⌘](<../../9 😃 Talkers/20 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
|-|-
| 📝 [`FORM`](<../../9 😃 Talkers/60 ⏩ Msg Flows/41 📝 FORM msg.md>) | To provide instructions.
| 🔗 [`BIND`](<../../9 😃 Talkers/60 ⏩ Msg Flows/44 🔗 BIND msg.md>) | To create a user profile.
| 🛠️ [`INVITE`](<../../9 😃 Talkers/60 ⏩ Msg Flows/46 🛠️ INVITE msg.md>) | To subscribe the user to plan.
| ❄️ [`FREEZE`](<../../9 😃 Talkers/60 ⏩ Msg Flows/42 ❄️ FREEZE msg.md>) | To disable past inputs.
| ⬇️ [`EVAL`](<../../9 😃 Talkers/30 💾 Talker data/20 ⬇️ EVAL flow.md>) | To register on the database.
| ✅ [`SUCCESS`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/23 ✅ SUCCESS prompt.md>) | To say that it was successful.
| 👋 [`GOODBYE`](<../../9 😃 Talkers/60 ⏩ Msg Flows/50 👋 GOODBYE.md>) | To show advertising.
|
