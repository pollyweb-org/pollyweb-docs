How to check-in to a hotel?
---

| [Domain](<../../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../4 ⚙️ Solution/35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|-|-|-|
|...
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>) desk
| 🏨 Hotel  | ℹ️ Booking presented: <br> - Dr. Alice! <br/> - from Feb 18 to Feb 20 <br/> - room king to garden <br/> - 1 person, no breakfast 
| 🏨 Hotel  | 😃 Hi! What do you need? <br/> - [ Check-in ] <br/> - [ Something else ] | > Check-in 
| 🤵 [Broker](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ⓘ Flow: check-in [-] <br/> - your identity shares your ID 🆔 <br/> - your payer pays the stay 💳 <br/> - your curator set the room 🧚 <br/> - you save the room key 🤵  
| 🆔 [Identifier](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) | 🫥 Share identity? [Yes, No] | > Yes
| 🆔 [Identifier](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>)
| 💳 [Payer](<../../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | 🫥 Pay $250.00 bill? 🧾 [No] <br/>- [ Card ABC ] + $0.10 <br/>- [ Card DEF ] (free) <br/> - [ ✂️ Split bill ] | > Card ABC |
| 🧚 [Curator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | ⏳ Analyzing rooms... 
| 🧚 [Curator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | 💭 How about these? [No] <br/>- [ 712 ] high floor, pool view <br/>- [ 428 ] mostly empty floor <br/>- [ 132 ] ground, garden view | > 712
| 🏨 Hotel    | ℹ️ Room 712 selected. <br/> - [ Change room ] 
| 🤵 [Broker](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 Save room key? [Yes, No] | > Yes 
| 🏨 Hotel    | ℹ️ Room key saved to wallet. <br/> - [ Share key with others ]
| 🏨 Hotel    | ℹ️ To get to room 712: <br/> - take the elevators on the left <br/> - use the key to go up to 7th <br/> - on the 7th floor, turn right.
| 🏨 Hotel    | ℹ️ A few more things: <br/> - the gym is open 24x7 <br/> - pool opens from 9am to 7pm <br/> - breakfast is from 7 to 10 pm <br/> - it's served at the ground floor <br/> - enjoy your stay!
| 🏨 Hotel    | ✅ Check-in done!
| ⭐ [Rate](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) | 🫥 Experience feedback? | ⭐⭐⭐⭐⭐
| [👀 Ads](<../../../../4 ⚙️ Solution/45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) | 🫥 Explore follow-up actions? [No] <br/>- [ Book a city tour 🚌 ]  <br/>- [ See a flamenco show 💃 ] <br/> - [ Explore the neighborhood 🔎 ]
|||