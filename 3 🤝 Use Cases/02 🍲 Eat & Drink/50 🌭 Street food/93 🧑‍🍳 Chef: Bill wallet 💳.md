# 🌭 Bill a customer's wallet at a street market stall

> From [Eat street food 🌭](<01 🌭 Index.md>)

## 💬 Chat


| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
| ...
| 🎪 Stall  | ⏳ Waiting requests... [+] | > +
| 🎪 Stall  | ⏳ Waiting requests... <br/> - [ Bill ] <br/> - [ Pause  shift ] | > Bill 
| 🎪 Stall  | 😃 Add item? [No] <br/> - [ ] hot dog 🌭 <br/> - [ ] chips 🥔 <br/>- ... | [X] hot dog 🌭 <br/> [X] chips 🥔
| 🎪 Stall  | 😃 1 hot dog 🌭? [Yes, No]  | > No
| 🎪 Stall  | 😃 How many then? | 🔄 2
| 🎪 Stall  | 😃 1 chips 🥔? [Yes, No] | Yes
| 🏦 [Collector](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | 🫥 Confirm $12.00? [Yes, No] <br/> - 2 hot dogs 🌭 (2x $5.00)  <br/> - 1 chips 🥔 ($1.00) <br/> - staff order fee 🤗 ($1.00) | > Yes
| 🏦 [Collector](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | ⏳ Waiting payment... [+]
| 🎪 Stall  | ✅ Payment received!
| 🎪 Stall  | ⏳ Waiting requests... [+] 
|...
||