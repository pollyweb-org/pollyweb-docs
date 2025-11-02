How to withdraw money from a cash machine?
--

A user can tap/scan the NFC/QR tag of a cash machine to start.
- To dispense the money, users need to scan/tap the dynamic tag of the dispenser.
- The dispenser's [ephemeral 🦋](<../../../../4 ⚙️ Solution/60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>) tag rotates to force users to stand beside it.

| [Domain](<../../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 🔎 [Finder](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) | ⓘ Any ATM (4.4 ⭐) [+]
| 🏧 ATM        | 😃 Hi! What do you need? <br/>- [ Withdraw ] <br/>- [ Something else ] | > Withdraw
| 🤵 [Broker](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 Ready to withdraw? [Yes, No] <br/> - your curator informs the amount  <br/> - your payer provides the funds <br/> - we take 10% commission <br/> - your payer may check your ID <br/> - you tap the dispenser to cash out. | > Yes
| 🧚 [Curator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) | ⏳ Analyzing options...
| 🧚 [Curator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) | 💭 Take how much? [$10, $20, +] | > +
| 🧚 [Curator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) | 💭 Take exactly how much? | `4 20s` <br> `3 5s`
| 🧚 [Curator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) | ❌ Sorry, no 3x $5 bills available. 
| 🧚 [Curator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) | 💭 Take 2x $10s instead? [Yes, No] | > Yes
| 🧚 [Curator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) | 💭 Confirm $100? [Yes, No] <br/> - (4 x $20) + (2 x $10) | > Yes
| 🏧 ATM        | ℹ️ Withdraw $100: [Change] <br/> - 4 bills of $20 <br/> - 2 bills of $10 <br/> - plus $10 fee (10%)
| 💳 [Payer](<../../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | 🫥 Pay $110.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 🆔 [Identity](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/6 🆔⏩😶 Face scan.md>)
| 🏧 ATM        | 😃 Tap the dispenser to cash out | 🔆 [tap](<../../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 🏧 ATM        | ✅ Take your money. 
| ⭐ [Rate](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐🫥 Reviewer agent.md>) | 🫥 Experience feedback? | ⭐ 4
||