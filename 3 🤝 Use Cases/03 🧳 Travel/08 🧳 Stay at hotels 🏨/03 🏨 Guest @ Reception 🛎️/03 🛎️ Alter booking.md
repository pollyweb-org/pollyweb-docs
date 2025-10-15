How to alter a hotel booking at the reception?
---

| [Domain](<../../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
|-|-|-|
|...
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) desk
| 🏨 Hotel  | ℹ️ Booking presented: <br> - Dr. Alice! <br/> - from Feb 18 to Feb 20 <br/> - room king to garden <br/> - 1 person, no breakfast 
| 🏨 Hotel  | 😃 Hi! What do you need? <br/> - [ Alter ] booking <br/> - [ Something else ] | > Alter 
| 🏨 Hotel  | 😃 What to alter? <br/> - [ ] from Feb 18 to Feb 20 <br/> - [ ] room king to garden <br/> - [ ] 1 person <br/> - [ ] no breakfast | > [X] no breakfast
| 🏨 Hotel  | 😃 Add breakfast? [Yes, No] | > Yes
| 🏨 Hotel  | ✅ Booking altered: <br> - Dr. Alice! <br/> - from Feb 18 to Feb 20 <br/> - room king to garden <br/> - 1 person, no breakfast 
| 🏨 Hotel  | 😃 Anything else? [No] <br/> - [ Check-in ] <br/> - [ Something else ] | > No
| ⭐ [Rate](<../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | ⭐⭐⭐⭐⭐
| [👀 Ads](<../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) | 🫥 Explore follow-up actions? [No] <br/>- [ Book a city tour 🚌 ]  <br/>- [ See a flamenco show 💃 ]
|||