How to withdraw money from a cash machine?
--

A user can tap/scan the NFC/QR tag of a cash machine to start.
- To dispense the money, users need to scan/tap the dynamic tag of the dispenser.
- The dispenser's [ephemeral 🦋](<../../../../4 ⏳ ⚙️ Solution/60 ⏳ 🧰 Edge/62 ⏳ 🦋 Ephemerals/03 ⏳ 🦋🔌 Ephemeral device.md>) tag rotates to force users to stand beside it.

| Service | Prompt | User
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>)
| 🔎 [Finder](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/10 ⏳ 🔎 Finders/02 ⏳ 🔎🫥 Finder vault.md>) | ⓘ Any ATM (4.4 ⭐) [+]
| 🏧 ATM        | 😃 Hi! What do you need? <br/>- [ Withdraw ] <br/>- [ Something else ] | > Withdraw
| 🏧 ATM        | 😃 Ready to withdraw? [Yes, No] <br/> - your curator informs the amount  <br/> - your payer provides the funds <br/> - we take 10% commission <br/> - your payer may check your ID <br/> - you tap the dispenser to cash out. | > Yes
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | ⏳ Analyzing options...
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | 💭 Take how much? [$10, $20, +] | > +
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | 💭 Take exactly how much? | `4 20s` <br> `3 5s`
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | ❌ Sorry, no 3x $5 bills available. 
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | 💭 Take 2x $10s instead? [Yes, No] | > Yes
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | 💭 Confirm $100? [Yes, No] <br/> - (4 x $20) + (2 x $10) | > Yes
| 🏧 ATM        | ℹ️ Withdraw $100: [Change] <br/> - 4 bills of $20 <br/> - 2 bills of $10 <br/> - plus $10 fee (10%)
| 💳 [Payer](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/01 ✅ 💳🫥 Payer agent.md>) | 🫥 Pay $110.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 🆔 [Identity](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/05 ✅ 🆔 Identities/03 ✅ 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. 📸 | 🙂 smile
| 🏧 ATM        | 😃 Tap the dispenser to cash out | 🔆 [tap](<../../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>)
| 🏧 ATM        | ✅ Take your money. 
| ⭐ [Reviewer](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/10 ⏳ 🔎 Finders/01 ✅ ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | > ⭐⭐⭐⭐
||