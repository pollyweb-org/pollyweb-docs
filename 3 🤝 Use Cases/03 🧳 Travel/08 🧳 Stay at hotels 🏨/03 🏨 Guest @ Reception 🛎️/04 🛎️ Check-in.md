How to check-in to a hotel?
---

| Service | Prompt  | User |
|-|-|-|
|...
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) desk
| 🏨 Hotel  | ℹ️ Booking presented: <br> - Dr. Alice! <br/> - from Feb 18 to Feb 20 <br/> - room king to garden <br/> - 1 person, no breakfast 
| 🏨 Hotel  | 😃 Hi! What do you need? <br/> - [ Check-in ] <br/> - [ Something else ] | > Check-in 
| 🏨 Hotel  | 😃 Ready to check-in? [Yes, No] <br/> - your identity shares your ID 🆔 <br/> - your payer pays the stay 💳 <br/> - your curator set the room 🧚 <br/> - you save the room key 🤵  | Yes
| 🆔 [Identity](<../../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | 🫥 Share identity? [Yes, No] | > Yes
| 🆔 [Identity](<../../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. 📸 | 🙂 smile
| 💳 [Payer](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 💳🫥 Payer agent.md>) | 🫥 Pay $250.00 bill? 🧾 [No] <br/>- [ Card ABC ] + $0.10 <br/>- [ Card DEF ] (free) <br/> - [ ✂️ Split bill ] | > Card ABC |
| 🧚 [Curator](<../../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | ⏳ Analyzing rooms... 
| 🧚 [Curator](<../../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | 💭 How about these? [No] <br/>- [ 712 ] high floor, pool view <br/>- [ 428 ] mostly empty floor <br/>- [ 132 ] ground, garden view | > 712
| 🏨 Hotel    | ℹ️ Room 712 selected. <br/> - [ Change room ] 
| 🤵 [Broker](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save room key? [Yes, No] | > Yes 
| 🏨 Hotel    | ℹ️ Room key saved to wallet. <br/> - [ Share key with others ]
| 🏨 Hotel    | ℹ️ To get to room 712: <br/> - take the elevators on the left <br/> - use the key to go up to 7th <br/> - on the 7th floor, turn right.
| 🏨 Hotel    | ℹ️ A few more things: <br/> - the gym is open 24x7 <br/> - pool opens from 9am to 7pm <br/> - breakfast is from 7 to 10 pm <br/> - it's served at the ground floor <br/> - enjoy your stay!
| 🏨 Hotel    | ✅ Check-in done!
| ⭐ [Reviewer](<../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | ⭐⭐⭐⭐⭐
| [👀 Ads](<../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) | 🫥 Explore follow-up actions? [No] <br/>- [ Book a city tour 🚌 ]  <br/>- [ See a flamenco show 💃 ] <br/> - [ Explore the neighborhood 🔎 ]
|||