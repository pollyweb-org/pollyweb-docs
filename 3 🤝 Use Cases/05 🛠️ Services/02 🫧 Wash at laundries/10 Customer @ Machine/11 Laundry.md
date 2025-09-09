<!-- #TODO -->

<!-- #TODO -->

Use a washing machine on a self-service laundry
---


# 🧚 ADD A CURATOR TO SELECT THE TIME, TEMPERATURE, AND DETERGENTS



| Service | Prompt | User
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>)
| 🔎 [Finder](<../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Laundry (4.4 ⭐) [+]
| 🫧 Laundry | 😃 Hi! What do you need? <br/>- [ Wash ] <br/>- [ Something else ] | > Wash
| 🫧 Laundry | 😃 How many minutes? [15, 60]| > 60
| 🫧 Laundry | 😃 What temperature? [40°C, 60°C ] | > 40°C
| 💳 [Payer](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 💳🎭 Payer role.md>) | 🫥 Pay $10.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) <br/> - [ ✂️ Split bill ] | > card ABC
| 🫧 Laundry | 😃 Ready to start? [Yes, No] | > Yes
| 🫧 Laundry | ⏳ Close the door! [+]
| 🫧 Laundry | ⏳ Washing... 59 min left. 
| 🫧 Laundry | ⏳ Washing... 1 min left. 
| 🫧 Laundry | ✅ Washed! Pick up your laundry.
| ⭐ [Reviewer](<../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | > ⭐⭐⭐⭐
||