
How to split the table bill at a restaurant?
---

| Service | Prompt | User
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>) seat
| 🔎 [Finder](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/10 ⏳ 🔎 Finders/02 ⏳ 🔎🫥 Finder vault.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍲 Restaurant | 😃 What do you need? <br/>- [ Pay bill ]  <br/>- [ Something else ] | > Pay bill
| 🍲 Restaurant | 😃 Which bill? <br> - [ Table ] $25.00 <br/> - [ Seat ] $5.00  | > Table 
| 💳 [Payer](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/01 ✅ 💳🫥 Payer agent.md>) | 🫥 Pay $25.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10 <br/>- [ card DEF ] (free)  <br/>- [ ✂️ Split bill ] | > Split bill
| [Collector 🏦](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/03 ✅ 🏦👥 Collector helper.md>) | 😃 Split by how many?  | 🔢 2
| [Collector 🏦](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/03 ✅ 🏦👥 Collector helper.md>) | ⏳ Waiting for 2x $12.50... <br/>- [ pay my part ] <br/>- [ cancel split ] | > pay my part
| 💳 [Payer](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/01 ✅ 💳🫥 Payer agent.md>) | 🫥 Pay $12.50 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 💳 [Payer](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/01 ✅ 💳🫥 Payer agent.md>) | 🫥 Add tip? [No, 10%, +] | > 10%
| 🧢 [Persona](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/02 ✅ 🧢 Personas/02 ✅ 🧢🫥 Persona agent.md>) | 🫥 Share name? [No] <br/> - [ 🧑‍🦰 personal ] <br/> - [ 💼 work ]  <br/> - [ 🦋 private ]     | > 🧑‍🦰 personal
| [Collector 🏦](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/03 ✅ 🏦👥 Collector helper.md>) | ⓘ Part paid, thanks Alice! [+]
| [Collector 🏦](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/03 ✅ 🏦👥 Collector helper.md>) | ⏳ Waiting for 1x $12.50... <br/>- [ list payer names ] <br/>- [ pay remaining ] <br/>- [ cancel split ]
| 🍲 Restaurant | ✅ All paid, thanks Alice! [+]
| ⭐ [Reviewer](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/10 ⏳ 🔎 Finders/01 ✅ ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | > ⭐⭐⭐⭐⭐
||

