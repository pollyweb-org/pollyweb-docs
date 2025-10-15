🛍️ Boutique self-service check-out 
---

### Setup

* Add [NFC/QR Locators 🔆](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) on the checkout stations;
* Create a check-out workflow for customers.

---

### 💬 Chat

| [Domain](<../../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>)
| 🔎 [Finder](<../../../../4 ⚙️ Solution/50 🫥 Agents/40 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Store (4.4 ⭐) [+]
| 🛍️ Store   | ℹ️ Self check-out 4 [+]
| 🛍️ Store   | 😃 Hi! What do you need? <br/>- [ Check out ] <br/>- [ Something else ] | > Check out
| 🛍️ Store   | 😃 Scan the 1st item [No] | ✨ [scan](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) 
| 🛍️ Store   | ℹ️ Item: dress 👗 ($25) [+]
| 🛍️ Store   | ⏳ Total ($25): <br/>- [ Scan ] another <br/> - [ List ] items <br/> - [ Pay ] total | > Scan
| 🛍️ Store   | 😃 Scan another item [No] | ✨ [scan](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) 
| 🛍️ Store   | ℹ️ Item: hat 👒 ($15) [+]
| 🛍️ Store   | ⏳ Total ($50): <br/>- [ Scan ] another <br/> - [ List ] items <br/> - [ Pay ] total | > List
| 🛍️ Store | ℹ️ Items: <br/> -  [ dress 👗 ] ($25) <br/> - [ hat 👒 ] ($15) 
| 🛍️ Store   | ⏳ Total ($50): <br/>- [ Scan ] another <br/> - [ List ] items <br/> - [ Pay ] total | > Pay
| 🛍️ Store   | ℹ️ Total ($50): <br/> - [ dress 👗 ] ($25) <br/> - [ hat 👒 ] ($15) 
| 🛍️ Store   | 😃 Confirm? [Yes, No] | > Yes
| 💳 [Payer](<../../../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $50.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 🛍️ Store   | ✅ Paid, take your items.
| ⭐ [Rate](<../../../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | ⭐ 5 |
||
