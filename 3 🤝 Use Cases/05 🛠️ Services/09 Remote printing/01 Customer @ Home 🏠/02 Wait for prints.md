Wait for printing delivery
---

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
|-|-|-|
|...|...
| 🖨️ Printer   | ⏳ Preparing your order... <br/>- [ Cancel order ] <br/> - [ Change order ] <br/> - [ Change delivery ] |
| 🖨️ Printer   | ℹ️ Order ready for pick-up.
| 🛎️ [Concierge](<../../../../4 ⚙️ Solution/30 🫥 Agents/06 🛎️ Concierges/01 🛎️🫥 Concierge agent.md>) | ⏳ Picking up... <br/>- [ Cancel pick-up ] |
| 🛎️ [Concierge](<../../../../4 ⚙️ Solution/30 🫥 Agents/06 🛎️ Concierges/01 🛎️🫥 Concierge agent.md>) | ⏳ Picked up! Delivery in 12 min... <br/>- [ Cancel delivery ] |
| 🛎️ [Concierge](<../../../../4 ⚙️ Solution/30 🫥 Agents/06 🛎️ Concierges/01 🛎️🫥 Concierge agent.md>) | 📣 Delivery arrived! [ Quiet, 5... 4... ] | > Quiet
| 🛎️ [Concierge](<../../../../4 ⚙️ Solution/30 🫥 Agents/06 🛎️ Concierges/01 🛎️🫥 Concierge agent.md>) | ✅ Order delivered.
| 🛎️ [Concierge](<../../../../4 ⚙️ Solution/30 🫥 Agents/06 🛎️ Concierges/01 🛎️🫥 Concierge agent.md>) | 🫥 Tip the courier? [No] <br/>- [ $2 ] <br/>- [ $5 ] <br/>- [ Another value ] | > $5 |
| 💳 [Payer](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $5.00 tip? 📄 [No] <br/>- [ Card ABC ] + $0.10 <br/>- [ Card DEF ] (free) <br/> - [ ✂️ Split bill ] | > Card ABC |
| ⭐ [Rate](<../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | ⭐ 5 |
||