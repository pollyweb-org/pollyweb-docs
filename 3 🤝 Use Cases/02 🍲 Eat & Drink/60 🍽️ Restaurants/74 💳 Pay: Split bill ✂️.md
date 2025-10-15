
How to split the table bill at a restaurant?
---

> From [Eat at restaurants 🍽️](<01 🍽️ Index.md>)

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) seat
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agents/40 🔎 Finders/$ 🔎🫥 Finder agent.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍽️ Restaurant | 😃 What do you need? <br/>- [ Pay bill ]  <br/>- [ Something else ] | > Pay bill
| 🍽️ Restaurant | 😃 Which bill? <br> - [ Table ] $25.00 <br/> - [ Seat ] $5.00  | > Table 
| 💳 [Payer](<../../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $25.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10 <br/>- [ card DEF ] (free)  <br/>- [ ✂️ Split bill ] | > Split bill
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) | 🫥 [Allow guest domain?](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/⏩ Host flows/🤗⏩🧑‍🦰 Invite 🛠️.md>) [Yes, No]  <br/> - Any Collector 🏦<br/>- [ Always ] for Any Restaurant 🍽️ | > Yes
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>) | 😃 Split by how many?  | ↕️ 2
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>) | ⏳ Waiting for 2x $12.50... <br/>- [ pay my part ] <br/>- [ cancel split ] | > pay my part
| 💳 [Payer](<../../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $12.50 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 💳 [Payer](<../../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Add tip? [No, 10%, +] | > 10%
| 🧢 [Persona](<../../../4 ⚙️ Solution/50 🫥 Agents/70 🧢 Personas/$ 🧢🫥 Persona agent.md>) | 🫥 Share name? [No] <br/> - [ 🧑‍🦰 personal ] <br/> - [ 💼 work ]  <br/> - [ 🦋 private ]     | > 🧑‍🦰 personal
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>) | ⓘ Part paid, thanks Alice! [+]
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>) | ⏳ Waiting for 1x $12.50... <br/>- [ list payer names ] <br/>- [ pay remaining ] <br/>- [ cancel split ]
| 🍽️ Restaurant | ✅ All paid, thanks Alice! [+]
| ⭐ [Rate](<../../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/⭐🫥 Reviewer agent.md>) | 🫥 Experience feedback? | ⭐ 5
||

