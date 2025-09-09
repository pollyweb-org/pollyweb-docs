How to collect userable payments at restaurants?
---

- Restaurants may charge fees for customers that order directly to staff.
- Userables allow customers to pay without battery on their devices.

| Service | Prompt | User
| - | - | - |
| ...
| 🍲 Restaurant | ⏳ Waiting requests... [+] | > +
| 🍲 Restaurant | ⏳ Waiting requests... <br/> - [ Bill ] <br/> - [ Something else ] | > Bill 
| 🍲 Restaurant | 😃 Table number? | 🔢 4
| [Collector 🏦](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 🏦🛠️ Collector helper.md>) | 🫥 Confirm $20.00? [Yes, No] <br/> - 1 dark paella 🥘 ($15.00) <br/> - 1 red wine glass 🍷 ($3.50) <br/> - staff order fee 🤗 ($1.00) <br/> - staff pay fee 🤗 ($0.50)  | > Yes
| [Collector 🏦](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 🏦🛠️ Collector helper.md>) | 🫥 Split bill? [Yes, No] | > No
| [Collector 🏦](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 🏦🛠️ Collector helper.md>) | 🫥 Add tip? [No, 10%, +] | > 10%
| [Collector 🏦](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 🏦🛠️ Collector helper.md>) | ⓘ Collecting $22.00: <br/> - 1 dark paella 🥘 ($15.00) <br/> - 1 red wine glass 🍷 ($3.50) <br/> - staff order fee 🤗 ($1.00) <br/> - staff pay fee 🤗 ($0.50) <br/> - staff tip 🤗 ($2.00)
| [Collector 🏦](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 🏦🛠️ Collector helper.md>) | 🫥 Tap the userable [+] | 🔆 [tap](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>)
| [Collector 🏦](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 🏦🛠️ Collector helper.md>) | ⏳ Collecting payment...
| 🆔 [Identity](<../../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | 🫥 Ready for ID check? [Yes]     | > Yes
| 🆔 [Identity](<../../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. 📸 | 🙂 smile
| [Collector 🏦](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 🏦🛠️ Collector helper.md>) | ⏳ Collecting payment...
| 🍲 Restaurant | ✅ Payment received!
| 🍲 Restaurant | ⏳ Waiting requests... [+] 
|...
||