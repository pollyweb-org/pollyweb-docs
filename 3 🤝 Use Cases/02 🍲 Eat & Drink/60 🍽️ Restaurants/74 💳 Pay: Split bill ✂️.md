
How to split the table bill at a restaurant?
---

> From [Eat at restaurants 🍽️](<01 🍽️ Index.md>)

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>) seat
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎🫥 Finder agent.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍽️ Restaurant | 😃 What do you need? <br/>- [ Pay bill ]  <br/>- [ Something else ] | > Pay bill
| 🍽️ Restaurant | 😃 Which bill? <br> - [ Table ] $25.00 <br/> - [ Seat ] $5.00  | > Table 
| 💳 [Payer](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | 🫥 Pay $25.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10 <br/>- [ card DEF ] (free)  <br/>- [ ✂️ Split bill ] | > Split bill
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 [Allow guest domain?](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>) [Yes, No]  <br/> - Any Collector 🏦<br/>- [ Always ] for Any Restaurant 🍽️ | > Yes
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | 😃 Split by how many?  | ↕️ 2
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | ⏳ Waiting for 2x $12.50... <br/>- [ pay my part ] <br/>- [ cancel split ] | > pay my part
| 💳 [Payer](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | 🫥 Pay $12.50 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 💳 [Payer](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | 🫥 Add tip? [No, 10%, +] | > 10%
| 🧢 [Persona](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) | 🫥 Share name? [No] <br/> - [ 🧑‍🦰 personal ] <br/> - [ 💼 work ]  <br/> - [ 🦋 private ]     | > 🧑‍🦰 personal
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | ⓘ Part paid, thanks Alice! [+]
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | ⏳ Waiting for 1x $12.50... <br/>- [ list payer names ] <br/>- [ pay remaining ] <br/>- [ cancel split ]
| 🍽️ Restaurant | ✅ All paid, thanks Alice! [+]
| ⭐ [Rate](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐🫥 Reviewer agent.md>) | 🫥 Experience feedback? | ⭐ 5
||

