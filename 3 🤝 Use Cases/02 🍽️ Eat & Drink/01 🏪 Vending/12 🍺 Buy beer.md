🍺 Buy age-restricted drinks at a vending machine 
---

> From [🏪 Drink at vending machines](<01 🏪 Index.md>)

> Vending machines ask the user's trusted [Identity 🆔 agent](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) to perform the authentication inside the chat on the user's device (e.g., [face scan 😶](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/04 🆔😶 Face scan.md>)).

## 💬 Chat

| Service | Prompt | User
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>)
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Vending (4.3 ⭐)  [+]
| 🍺 Vending  | 😃 Hi! What do you need? <br/>- [ Buy ] an item <br/>- [ Something else ] | > Buy 
| 🍺 Vending  | 😃 What's the item number?   | 🔢 124
| 🍺 Vending  | 😃 A beer? [Yes, No]         | > Yes
| 🆔 [Identity](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | 🫥 Share over 21? [Yes, No]     | > Yes
| 🆔 [Identity](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.  | [📸 selfie](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/04 🆔😶 Face scan.md>)
| 💳 [Payer](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $4.50 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 🍺 Vending  | ⏳ Delivering...
| 🍺 Vending  | ✅ Thanks! Pick up your item. 
| ⭐ [Reviewer](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | > ⭐⭐⭐⭐⭐
|
