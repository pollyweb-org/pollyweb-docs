# 🍺 Buy age-restricted drinks at a vending machine 


> From [🏪 Drink at vending machines](<01 🏪 Index.md>)

> Built with [Owner Talker 😃](<93 😃 Owner: Talker.md>)

* Vending machines 
  * ask the user's trusted [Identity 🆔 agent](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) 
  * to perform the authentication inside the chat 
  * on the user's device (e.g., [face scan 😶](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/21 🆔😶 Face scan.md>)).

<br/>


## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>)
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Vending (4.3 ⭐)  [+]
| 🍺 Vending  | 😃 Hi! What do you need? <br/>- [ Buy ] an item <br/>- [ Something else ] | > Buy 
| 🍺 Vending  | 😃 What's the item number?   | 🔢 124
| 🍺 Vending  | 😃 A beer? [Yes, No]         | > Yes
| 🆔 [Identity](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Share over 21? [Yes, No]     | > Yes
| 🆔 [Identity](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.  | [📸 selfie](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/21 🆔😶 Face scan.md>)
| 💳 [Payer](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $4.50 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 🍺 Vending  | ⏳ Delivering...
| 🍺 Vending  | ✅ Thanks! Pick up your item. 
| ⭐ [Rate](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | ⭐ 5
|
