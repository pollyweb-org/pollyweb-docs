# 🌭 Bill a customer's wallet at a street market stall

> From [Eat street food 🌭](<01 🌭 Index.md>)

## 💬 Chat


| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| - | - | - |
| ...
| 🎪 Stall  | ⏳ Waiting requests... [+] | > +
| 🎪 Stall  | ⏳ Waiting requests... <br/> - [ Bill ] <br/> - [ Pause  shift ] | > Bill 
| 🎪 Stall  | 😃 Add item? [No] <br/> - [ ] hot dog 🌭 <br/> - [ ] chips 🥔 <br/>- ... | [X] hot dog 🌭 <br/> [X] chips 🥔
| 🎪 Stall  | 😃 1 hot dog 🌭? [Yes, No]  | > No
| 🎪 Stall  | 😃 How many then? | ↕️ 2
| 🎪 Stall  | 😃 1 chips 🥔? [Yes, No] | Yes
| 🏦 [Collector](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>) | 🫥 Confirm $12.00? [Yes, No] <br/> - 2 hot dogs 🌭 (2x $5.00)  <br/> - 1 chips 🥔 ($1.00) <br/> - staff order fee 🤗 ($1.00) | > Yes
| 🏦 [Collector](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>) | ⏳ Waiting payment... [+]
| 🎪 Stall  | ✅ Payment received!
| 🎪 Stall  | ⏳ Waiting requests... [+] 
|...
||