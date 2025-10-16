
**How to book a ride for later?**
--

| [Domain](<../../../../4 ⚙️ Solution/40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../../4 ⚙️ Solution/35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
||| > Ride 🔗
| 🔎 [Finder](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) | ⓘ Any Ride Hailing (4.4 ⭐) [+]
| 🙋 Hailing | 😃 Hi! What do you need? <br/>- [ Ride now ] <br/>- [ Book ride ]  <br/> - [ Something else ] | > Book ride
| [🗓️ Scheduler](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Schedulers 🗓️/$ 🗓️🫥 Scheduler agent.md>) | 🫥 Which day? <br/> - [ Today ] <br/> - [ Tomorrow ] <br/> - [ Select from calendar ] | > Tomorrow
| [🗓️ Scheduler](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Schedulers 🗓️/$ 🗓️🫥 Scheduler agent.md>) | 🫥 What time?  | 🕑 9:30
| [🗓️ Scheduler](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Schedulers 🗓️/$ 🗓️🫥 Scheduler agent.md>) | 🫥 Are you sure? [Yes, No] <br/>- lunch at mom at 1pm. | > Yes
| 🙋 Hailing | ℹ️ Received date/time: [Change] <br/> - tomorrow, at 9:30
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Navigators 🧭/$ 🧭🫥 Navigator agent.md>) | 🫥 Share pick up location? [No] <br/>- [ current location ] <br/> - [ 🏠 home ] <br/> - [ 📍 pinpoint ] | > 🏠 home
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Navigators 🧭/$ 🧭🫥 Navigator agent.md>) | 🫥 Share drop off location? [No] <br/> - [ T1 departures, BA 17:35 ] <br/>- [ 🏢 LHR15 ] <br/>- [ 🏡 Daniel's ] <br/> - [ 📍 pinpoint ] | > 🏡 Daniel's
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Navigators 🧭/$ 🧭🫥 Navigator agent.md>) | 🫥 Any stops on the route? [Yes, No] | > No
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Navigators 🧭/$ 🧭🫥 Navigator agent.md>) | 🫥 Share route preferences? [No] <br/> - [ fastest, with shortcuts ] <br/> - [ less turns, via highway ] <br/> - [ via office ] <br> - [ type instructions... ] | > via office
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Navigators 🧭/$ 🧭🫥 Navigator agent.md>) | 🫥 Track your live location? [No] <br/>- [ Yes ] this time only <br/> - [ Always ] don't ask again| > Always
| 🙋 Hailing | ℹ️ Received route: [Change] <br/> - pick-up at St. Mary's street, 68 <br/> - drop-off at Valerian road, 231-B <br/> - drive via Whistle Woods road
| 🧢 [Persona](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Personas 🧢/🧢🫥 Persona agent.md>) | 🫥 Share car preferences? [No] <br/>- [ personal ] <br/>- [ work ] | > personal
| 🙋 Hailing | ℹ️ Received preferences: [Change] <br/> - comfort or above car <br/> - english speaker driver <br/> - warm and quiet ride 
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Navigators 🧭/$ 🧭🫥 Navigator agent.md>) | 🫥 Confirm drop-off ~9:45? [Yes, No]<br/> - tomorrow, 12pm to 2pm<br/> 📍 The Guild, Soho, W1D 3QX <br/> - Alice's lunch break is 1h <br/>- her total commute is 45m <br/>- she'll have 15m to eat <br/>  | > Yes
| 💳 [Payer](<../../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $12.95 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 🙋 Hailing | ⏳ Assigning you a driver...
| 🙋 Hailing | ℹ️ Driver assigned: <br/>- it's Daniel <br/>- on a black Tesla, ABC123 
| 🙋 Hailing | ⏳ Pick-up in 10 hours...<br/>- [ Cancel pickup ] <br/>- [ Reschedule ]
| 🙋 Hailing | ℹ️ Daniel is on your way. 
| 🙋 Hailing | ⏳ Pick-up in 14 minutes...<br/>- [ Cancel pickup ]
| 🙋 Hailing | 📣 Daniel arrived! [ Quiet, 5... 4... ] | > Quiet
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Navigators 🧭/$ 🧭🫥 Navigator agent.md>) | ⓘ The driver is at your door.
| 🙋 Hailing | ⏳ Tap inside until 12:41...<br> - [ Say "be right there" ] <br/>- [ Say something else ] <br>- [ Cancel pick-up ]
|...
||