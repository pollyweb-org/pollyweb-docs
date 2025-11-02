<!-- #TODO -->

<!-- #TODO -->

Use a washing machine on a self-service laundry
---


# 🧚 ADD A CURATOR TO SELECT THE TIME, TEMPERATURE, AND DETERGENTS



| [Domain](<../../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 🔎 [Finder](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) | ⓘ Any Laundry (4.4 ⭐) [+]
| 🫧 Laundry | 😃 Hi! What do you need? <br/>- [ Wash ] <br/>- [ Something else ] | > Wash
| 🫧 Laundry | 😃 How many minutes? [15, 60]| > 60
| 🫧 Laundry | 😃 What temperature? [40°C, 60°C ] | > 40°C
| 💳 [Payer](<../../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | 🫥 Pay $10.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) <br/> - [ ✂️ Split bill ] | > card ABC
| 🫧 Laundry | 😃 Ready to start? [Yes, No] | > Yes
| 🫧 Laundry | ⏳ Close the door! [+]
| 🫧 Laundry | ⏳ Washing... 59 min left. 
| 🫧 Laundry | ⏳ Washing... 1 min left. 
| 🫧 Laundry | ✅ Washed! Pick up your laundry.
| ⭐ [Rate](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐🫥 Reviewer agent.md>) | 🫥 Experience feedback? | ⭐ 4
||