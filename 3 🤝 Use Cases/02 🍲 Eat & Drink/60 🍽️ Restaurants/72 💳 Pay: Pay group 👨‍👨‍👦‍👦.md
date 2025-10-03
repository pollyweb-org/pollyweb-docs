
How to pay the table bill at a restaurant?
---

> From [Eat at restaurants 🍽️](<01 🍽️ Index.md>)

## 💬 Chat

| Domain | Prompt | User
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) seat
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍽️ Restaurant | 😃 What do you need? <br/>- [ Pay bill ]  <br/>- [ Something else ] | > Pay bill
| 🍽️ Restaurant | 😃 Which bill? <br> - [ Table $25.00 ] <br/> - [ Seat $5.00 ] <br/> - [ Split table ] | > Table (...)
| 💳 [Payer](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $25.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) <br/> - [ ✂️ Split bill ] | > card ABC
| 💳 [Payer](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Add tip? [No, 10%, +] | > 10%
| 🍽️ Restaurant | ✅ Table bill paid, thanks!
| ⭐ [Reviewer](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | > ⭐⭐⭐⭐⭐
||

