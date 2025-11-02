How to collect userable payments at restaurants?
---

> From [Eat at restaurants 🍽️](<01 🍽️ Index.md>)


> [Userables 💍](<../../../4 ⚙️ Solution/25 🔆 Locators/Userables 💍/💍💠 Userable thing.md>) allow customers to pay without battery on their devices.

> Mentioned in [Verify Userables 🆔](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/4 🆔⏩💍 Verify Userables.md>)

<br/>


## 💬 Chat

- Restaurants may charge fees for customers that order directly to staff.
- Userables allow customers to pay without battery on their devices.

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| ...
| 🍽️ Restaurant | ⏳ Waiting requests... [+] | > +
| 🍽️ Restaurant | ⏳ Waiting requests... <br/> - [ Bill ] <br/> - [ Something else ] | > Bill 
| 🍽️ Restaurant | 😃 Table number? | 🔢 4
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | 🫥 Confirm $20.00? [Yes, No] <br/> - 1 dark paella 🥘 ($15.00) <br/> - 1 red wine glass 🍷 ($3.50) <br/> - staff order fee 🤗 ($1.00) <br/> - staff pay fee 🤗 ($0.50)  | > Yes
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | 🫥 Split bill? [Yes, No] | > No
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | 🫥 Add tip? [No, 10%, +] | > 10%
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | ⓘ Collecting $22.00: <br/> - 1 dark paella 🥘 ($15.00) <br/> - 1 red wine glass 🍷 ($3.50) <br/> - staff order fee 🤗 ($1.00) <br/> - staff pay fee 🤗 ($0.50) <br/> - staff tip 🤗 ($2.00)
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | 🫥 Tap the userable [+] | 🔆 [tap](<../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | ⏳ Collecting payment...
| 🆔 [Identity](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) | 🫥 Ready for ID check? [Yes]     | > Yes
| 🆔 [Identity](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/6 🆔⏩😶 Face scan.md>)
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | ⏳ Collecting payment...
| 🍽️ Restaurant | ✅ Payment received!
| 🍽️ Restaurant | ⏳ Waiting requests... [+] 
|...
||