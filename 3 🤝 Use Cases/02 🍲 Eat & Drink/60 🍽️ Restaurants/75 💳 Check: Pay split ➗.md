
**How to split the table bill at a restaurant?**
---

> From [Eat at restaurants 🍽️](<01 🍽️ Index.md>)

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) seat
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agents/40 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍽️ Restaurant | 😃 What do you need? <br/>- [ Pay bill ]  <br/>- [ Something else ] | > Pay bill
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>) | ⓘ Paying 1 part of 2 split.
| 💳 [Payer](<../../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $12.50 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 💳 [Payer](<../../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Add tip? [No, $1.25, +] | > $1.25
| 🧢 [Persona](<../../../4 ⚙️ Solution/50 🫥 Agents/70 🧢 Personas/$ 🧢🫥 Persona agent.md>) | 🫥 Share name? [No] <br/> - [ 🧑‍🦰 personal ] <br/> - [ 💼 work ]  <br/> - [ 🦋 private ]     | > 🧑‍🦰 personal
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>) | ⓘ Part paid, thanks Alice! [+]
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>) | ⏳ Waiting for 1x $12.50... <br/>- [ pay remaining ]
| 🍽️ Restaurant | ✅ All paid, thanks Alice! [+]
| ⭐ [Rate](<../../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | ⭐ 5
||

