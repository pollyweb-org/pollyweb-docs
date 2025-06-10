Order to the table at a fast food restaurant 🍔
---

| Service | Prompt | User
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>) table
| 🔎 [Finder](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/10 ⏳ 🔎 Finders/02 ⏳ 🔎🫥 Finder vault.md>) | ⓘ Any Fast Food (4.3 ⭐)  [+]
| 🍔 Fast Food | ℹ️ You're on table 28 [+]
| 🍔 Fast Food | 😃 Hi! What do you need? <br/>- [ Order ] <br/>- [ Something else ] | > Order
| 🍔 Fast Food | 😃 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/> - your vitalogist reviews 💖 <br/> - your payer pays 💳 <br/> - we'll deliver to your table 🍔 <br/> - your vitalogist records it 💖 | > Yes
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | 💭 Some suggestions: [All, No] <br/>- [ ] house burger 🍔 (£3.00) <br/> - [ ] still water (25 cl) 💧 (£1.00) <br/> |  > All
| 🧚 [Curator](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) | 💭 Anything else? [No] <br/> - [ ] coffee ☕ (£0.90) | > No
| 🍔 Fast Food | ℹ️ Order (£4.00) [+] <br/>- 1 house burger 🍔 (£3.00) <br/> - 1 still water (25 cl) 💧 (£1.00) <br/>  - to deliver at table 28
| 💖 [Vitalogist](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/09 ⏳ 💖 Vitalogists/01 ⏳ 💖🫥 Vitalogist agent.md>) | 🫥 Confirm? [Yes, No] <br/> - burger is outside your diet  | > Yes
| 💳 [Payer](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/01 ✅ 💳🫥 Payer agent.md>) | 🫥 Pay £4.00 bill? 🧾 [No] <br/>- [ Card ABC ] + $0.10 <br/>- [ Card DEF ] (free) | > Card ABC |
| 🍔 Fast Food | ✅ Eat-in submitted [+]
| 🍔 Fast Food | ⏳ Order in queue... [+] 
...
||