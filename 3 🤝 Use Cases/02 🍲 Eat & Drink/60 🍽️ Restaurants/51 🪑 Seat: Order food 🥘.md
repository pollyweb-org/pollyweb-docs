How to order food to the table at a restaurant?
---

> From [Eat at restaurants 🍽️](<01 🍽️ Index.md>)

## 💬 Chat

| Domain | Prompt | User
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) seat
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍽️ Restaurant | 😃 Hi! What do you need? <br/>- [ Order ] <br/>- [ Something else ] | > Order
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/> - your vitalogist reviews 💖 <br/> - your ID allows alcohol 🆔 <br/> - we'll deliver to your seat 🍽️ <br/> - your vitalogist records it 💖<br/> - you pay when leaving 💳 | > Yes
| 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | 💭 Some suggestions: [No] <br/>- [ ] dark paella 🥘 <br/>- [ ] shrimp salad 🥗 <br/> - [ ] detox juice 🍹 |  `water`
| 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | 💭 What water? <br/> - [ tap ] in a glass <br/> - [ still ] 500ml <br/> - [ sparkling ] 250ml | > tap
| 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | ⓘ A glass of tap water it is. 
| 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | 💭 Try traditional paella? <br/>- [ traditional paella 🥘 ] <br/> - [ dark paella 🥘 ] | `why dark?`
| 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | ⓘ It's squid or cuttlefish ink. 
| 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | 💭 Try paella? <br/>- [ traditional paella 🥘 ] <br/> - [ dark paella 🥘 ] | > dark paella 🥘
| 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | 💭 Anything else? [No] <br/> - [ ] bread 🍞 <br/> - [ ] olives 🫒 | > No
| 🍽️ Restaurant  | ℹ️ Order ($15): [Change] <br/> - 1 tap water 🚰 (free) <br/> - 1 dark paella 🥘 ($15) 
| 💖 [Vitalogist](<../../../4 ⚙️ Solution/30 🫥 Agents/09 💖 Vitalogists/01 💖🫥 Vitalogist agent.md>) | 🫥 Confirm? [Yes, No] <br/> - water: may be mishandled. <br/> - paella: may cause allergy | > Yes
| 🍽️ Restaurant | 😃 Food will take ~10 min: <br/> - [ OK ] no problem <br/> - [ Change ] order | > OK
| 🍽️ Restaurant | ✅ Order submitted [+]
| 🍽️ Restaurant | ⏳ Preparing your order... [+]
|...
||