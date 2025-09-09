
How to pay the seat bill at a restaurant?
---

| Service | Prompt | User
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) seat
| 🔎 [Finder](<../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍲 Restaurant | 😃 What do you need? <br/>- [ Pay bill ]  <br/>- [ Something else ] | > Pay bill
| 🍲 Restaurant | 😃 Which bill? <br> - [ Table $25.00 ] <br/> - [ Own $5.00 ] <br/> - [ Split table ] | > Own (...)
| 💳 [Payer](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 💳🫥 Payer role.md>) | 🫥 Pay $5.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free)  | > card ABC
| 💳 [Payer](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 💳🫥 Payer role.md>) | 🫥 Add tip? [No, 10%, +] | > 10%
| 🧢 [Persona](<../../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | 🫥 Share name? [No] <br/> - [ 🧑‍🦰 personal ] <br/> - [ 💼 work ]  <br/> - [ 🦋 private ]     | > 🧑‍🦰 personal
| 🍲 Restaurant | ✅ Own paid, thanks Alice! <br/>- Remaining bill: $20.00
| ⭐ [Reviewer](<../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | > ⭐⭐⭐⭐⭐
||

