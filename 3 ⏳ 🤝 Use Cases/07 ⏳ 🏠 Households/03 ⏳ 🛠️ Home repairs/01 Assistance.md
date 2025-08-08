#TODO

#TODO 

1. **How to request immediate home assistance?**

    A user can scan/tap the NFC/QR of the maintenance company.

    | Service | Prompt | User
    | - | - | - |
    | 👷 Company | 😃 Hi! What do you need? <br/>- [ Help now ] <br/>- [ Something else ] | > Help now
    | 👷 Company | 😃 What sort of help? <br/>- cleaner <br/>- plumber <br/>- other | > plumber
    | 🧢 [Persona](<../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/02 ✅ 🧢 Personas/02 ✅ 🧢🫥 Persona agent.md>) | 🫥 Share delivery address? [No]  <br/>- [ home ] <br/>- [ Alice's ] | > Alice's
    | [🗓️ Scheduler](<../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/38 ⏳ 🕓 User Timeline/04 ⏳ 🗓️🗄️ Scheduler agent.md>) | 🫥 Confirm plumber? [Yes, No] <br/>📍 43, Soho, W1D 3QX  <br/> 🕑 today, 11:30 am <br/> - you have a work meeting at 12pm. | > Yes
    | 💳 [Payer](<../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/01 ✅ 💳🫥 Payer agent.md>) | 🫥 Pay $50.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
    | 👷 Company | 😃 Describe the issue.   | 🎙️ (speech)
    | 👷 Company | ℹ️ OK, I'll shared with the team.
    | 👷 Company | ⏳ Waiting for plumber... <br/>- [ Cancel service ] <br/>- [ Reschedule ]
    | 👷 Company | ℹ️ The plumber is on the way.
    | 👷 Company | ⏳ Arriving in 23 minutes... <br/>- [ Cancel service ]
    | 👷 Company | ℹ️ The plumber arrived.
    | 👷 Company | ⏳ Waiting for the code 9723...
    | 👷 Company | ℹ️ Code accepted, let's start!
    | 👷 Company | ⏳ Waiting for completion...
    | 👷 Company | 😃 Is the service finished? [Yes, No] | > Yes   
    | 🆔 [Identity](<../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/05 ✅ 🆔 Identities/03 ✅ 🆔🫥 Identity agent.md>) | 🫥 Sign report? 📄 [Yes, No] | > Yes
    | 🆔 [Identity](<../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/05 ✅ 🆔 Identities/03 ✅ 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. 📸 | 🙂 smile
    | 👷 Company | 😃 How was the service? | > ⭐⭐⭐⭐⭐
    | 👷 Company | 😃 Tip the plumber? [No, $5, $10, $20] | > $10
    | 💳 [Payer](<../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/01 ✅ 💳🫥 Payer agent.md>) | 🫥 Pay $10.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
    | 👷 Company | 😉 You're all set, bye!
    | ⭐ [Reviewer](<../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/10 ⏳ 🔎 Finders/01 ✅ ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | > ⭐⭐⭐⭐⭐

    ---