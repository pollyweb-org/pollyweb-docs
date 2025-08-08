
**How to check in for a flight?**
----

To start the check-in over a chat, users can: 
- activate the menu of their booking Token; or 
- follow a link sent by the airline; or 
- start a chat with the airline and share the booking Token. 

| Service       | Prompt | User
| - | - | - |
| 🔎 [Finder](<../../../../../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Airline (4.4 ⭐) [+]
| 🛩️ Airline     | 😃 Hi! What do you need? <br/> - [ Check-in ] for 🇺🇸 Seattle? <br/>- [ Something else ] | > Check-in
| 🛩️ Airline     | 😃 Who is checking in? [All] <br/> - [ ] Alice <br/>- [ ] Teresa | > All
| 🛩️ Airline    | 😃 Add/remove hold bags? [Yes, No] | > No
| 🛩️ Airline    | 😃 Any forbidden items? [Yes, No] | > No
| 🤵 [Broker](<../../../../../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Share passports?  [All, No] <br/> - [ ] 🇬🇧 UK Alice <br/>- [ ] 🇬🇧 UK Teresa <br/>- [ ] 🇺🇸 US Teresa  | [X] 🇬🇧 UK Alice <br/> [X] 🇺🇸 US Teresa
| 🤵 [Broker](<../../../../../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Share visas?  [All, No] <br/> - [ ] 🇺🇸 ESTA Alice | > All
| 🤵 [Broker](<../../../../../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Share Covid certificates?  [All, No] <br/> - [ ] 🇬🇧 NHS Alice <br/>- [ ] 🇬🇧 NHS Teresa | > All
| 🧢 [Persona](<../../../../../../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | 🫥 Share flight preferences?  [Yes, No] | > Yes
| 🧚 [Curator](<../../../../../../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | 🫥 Share meal preferences?  [Yes, No] | > Yes
| 💖 [Vitalogist](<../../../../../../../../4 ⚙️ Solution/30 🫥 Agents/09 💖 Vitalogists/01 💖🫥 Vitalogist agent.md>) | 🫥 Share food allergies?  [Yes, No] | > Yes
| 🆔 [Identity](<../../../../../../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | 🫥 Sign terms? 📄 [Yes, No] | > Yes
| 🆔 [Identity](<../../../../../../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. 📸 | 🙂 smile
| 🤵 [Broker](<../../../../../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save boarding passes? [Yes, No] | > Yes
| 🛩️ Airline    | ✅ You're checked-in.
| [👀 Ads](<../../../../../../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) | 🫥 Explore follow-up actions? [No] <br/>- [ 🏨 Book a hotel ] <br/>- [ 🚙 Rent a car ] | > No
||

