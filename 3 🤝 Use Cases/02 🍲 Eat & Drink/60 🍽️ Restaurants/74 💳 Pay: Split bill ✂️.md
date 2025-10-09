
How to split the table bill at a restaurant?
---

> From [Eat at restaurants 🍽️](<01 🍽️ Index.md>)

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) seat
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍽️ Restaurant | 😃 What do you need? <br/>- [ Pay bill ]  <br/>- [ Something else ] | > Pay bill
| 🍽️ Restaurant | 😃 Which bill? <br> - [ Table ] $25.00 <br/> - [ Seat ] $5.00  | > Table 
| 💳 [Payer](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $25.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10 <br/>- [ card DEF ] (free)  <br/>- [ ✂️ Split bill ] | > Split bill
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Allow guest domain?](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite 🛠️.md>) [Yes, No]  <br/> - Any Collector 🏦<br/>- [ Always ] for Any Restaurant 🍽️ | > Yes
| [🏦 Collector](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | 😃 Split by how many?  | ↕️ 2
| [🏦 Collector](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | ⏳ Waiting for 2x $12.50... <br/>- [ pay my part ] <br/>- [ cancel split ] | > pay my part
| 💳 [Payer](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $12.50 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 💳 [Payer](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Add tip? [No, 10%, +] | > 10%
| 🧢 [Persona](<../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | 🫥 Share name? [No] <br/> - [ 🧑‍🦰 personal ] <br/> - [ 💼 work ]  <br/> - [ 🦋 private ]     | > 🧑‍🦰 personal
| [🏦 Collector](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | ⓘ Part paid, thanks Alice! [+]
| [🏦 Collector](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | ⏳ Waiting for 1x $12.50... <br/>- [ list payer names ] <br/>- [ pay remaining ] <br/>- [ cancel split ]
| 🍽️ Restaurant | ✅ All paid, thanks Alice! [+]
| ⭐ [Rate](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | ⭐ 5
||

