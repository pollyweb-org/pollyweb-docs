
**How to split the table bill at a restaurant?**
---

| Service | Prompt | User
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) seat
| 🔎 [Finder](<../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍲 Restaurant | 😃 What do you need? <br/>- [ Pay bill ]  <br/>- [ Something else ] | > Pay bill
| [Collector 🏦](<../../../../4 ⚙️ Solution/30 🫥 Agents/01 📦 Storage/03 🏦🛠️ Collector helper.md>) | ⓘ Paying 1 part of 2 split.
| 💳 [Payer](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 💳🫥 Payer agent.md>) | 🫥 Pay $12.50 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 💳 [Payer](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 💳🫥 Payer agent.md>) | 🫥 Add tip? [No, $1.25, +] | > $1.25
| 🧢 [Persona](<../../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | 🫥 Share name? [No] <br/> - [ 🧑‍🦰 personal ] <br/> - [ 💼 work ]  <br/> - [ 🦋 private ]     | > 🧑‍🦰 personal
| [Collector 🏦](<../../../../4 ⚙️ Solution/30 🫥 Agents/01 📦 Storage/03 🏦🛠️ Collector helper.md>) | ⓘ Part paid, thanks Alice! [+]
| [Collector 🏦](<../../../../4 ⚙️ Solution/30 🫥 Agents/01 📦 Storage/03 🏦🛠️ Collector helper.md>) | ⏳ Waiting for 1x $12.50... <br/>- [ pay remaining ]
| 🍲 Restaurant | ✅ All paid, thanks Alice! [+]
| ⭐ [Reviewer](<../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | > ⭐⭐⭐⭐⭐
||

