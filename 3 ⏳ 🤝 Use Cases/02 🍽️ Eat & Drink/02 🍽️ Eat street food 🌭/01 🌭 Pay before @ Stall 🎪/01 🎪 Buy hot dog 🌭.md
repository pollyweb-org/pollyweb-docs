**How to buy food at a street market stall?**
---

| Service | Prompt | User
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>) stall
| 🔎 [Finder](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/10 ⏳ 🔎 Finders/02 ⏳ 🔎🫥 Finder vault.md>) | ⓘ Any Stall (4.4 ⭐) [+]
| 🌭 Stall      | 😃 What do you need? <br/>- [ Order ] <br/>- [ Something else ] | > Order
| 🌭 Stall      | 😃 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/> - your vitalogist reviews 💖 <br/> - your payer pays the bill 💳 <br/> - we'll call you when ready 🧢 <br/> - your vitalogist records it 💖 | > Yes
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | 🫥 Share preferences? [No] <br/>- [ 👤 solo ] | > 👤 solo
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | ⏳ Analyzing menu... 
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | 💭 Here are suggestions: <br/> - [ ] hot dog 🌭 -sauce <br/>- [ ] chips 🥔 <br/>- [ ] beer 🍺 | `all good`
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | 💭 Anything else? [Yes, No] | > No
| 🌭 Stall         | ℹ️ Order ($8): [Change] <br/> - hot dog 🌭 (-sauce) ($5) <br/>- chips 🥔 ($1) <br/>- beer 🍺 ($2)
| 💖 [Vitalogist](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/09 ⏳ 💖 Vitalogists/01 ⏳ 💖🫥 Vitalogist agent.md>) | 🫥 Confirm? [Yes, No] <br> - outside your diet <br/> - beer: you came by car | > No
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | 💭 Change something? | `water,`<br>`not beer`
| 🌭 Stall         | ℹ️ Order ($7): [Change] <br/> - hot dog 🌭 (-sauce) ($5) <br/>- chips 🥔 ($1) <br/>- water 💧 ($1)
| 💖 [Vitalogist](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/09 ⏳ 💖 Vitalogists/01 ⏳ 💖🫥 Vitalogist agent.md>) | 🫥 Confirm? [Yes, No] <br> - outside your diet | > Yes
| 🧢 [Persona](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/02 ✅ 🧢 Personas/02 ✅ 🧢🫥 Persona agent.md>) | 🫥 Share social name? [No] <br/> - [ 🧑‍🦰 personal ] <br/> - [ 💼 work ] <br/> - [ 🦋 private ]      | > 🧑‍🦰 personal
| 🌭 Stall      | ℹ️ Thanks, Alice!
| 💳 [Payer](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/01 ✅ 💳🫥 Payer agent.md>) | 🫥 Pay $7.50 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 🌭 Stall      | ✅ Request submitted [+]
| 🌭 Stall      | ⏳ We'll call you when ready.<br/>- [ Cancel request ] <br/> - [ Alter request ]
...
||

