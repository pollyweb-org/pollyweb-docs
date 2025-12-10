# 🍺 Buy age-restricted drinks at a vending machine 


> From [🏪 Drink at vending machines](<01 🏪 Index.md>)

> Built with [Owner Talker 😃](<93 😃 Owner: Talker.md>)

* Vending machines 
  * ask the user's trusted [Identity 🆔 agent](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔 Identity agent/🆔🫥 Identity agent.md>) 
  * to perform the authentication inside the chat 
  * on the user's device (e.g., [face scan 😶](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>)).

<br/>


## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Vending (4.3 ⭐)  [+]
| 🍺 Vending  | 😃 Hi! What do you need? <br/>- [ Buy ] an item <br/>- [ Something else ] | > Buy 
| 🍺 Vending  | 😃 What's the item number?   | 🔢 124
| 🍺 Vending  | 😃 A beer? [Yes, No]         | > Yes
| 🆔 [Identity](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔 Identity agent/🆔🫥 Identity agent.md>) | 🫥 Share over 21? [Yes, No]     | > Yes
| 🆔 [Identity](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔 Identity agent/🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.  | [📸 selfie](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>)
| 💳 [Payer](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | 🫥 Pay $4.50 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 🍺 Vending  | ⏳ Delivering...
| 🍺 Vending  | ✅ Pick up the item. 
| ⭐ [Rate](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) | 🫥 Experience feedback? | ⭐ 5
|
