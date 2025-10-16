
How to check in for a flight?
===

To start the check-in over a chat, users can: 
- activate the menu of their booking Token; or 
- follow a link sent by the airline; or 
- start a chat with the airline and share the booking Token. 

## 💬 Chat

| Service       | Prompt | User
| - | - | - |
| 🔎 [Finder](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/40 🔎 Finders/🔎🫥 Finder agent.md>) | ⓘ Any Airline (4.4 ⭐) [+]
| 🛩️ Airline     | 😃 Hi! What do you need? <br/> - [ Check-in ] for 🇺🇸 Seattle? <br/>- [ Something else ] | > Check-in
| 🛩️ Airline     | 😃 Who is checking in? [All] <br/> - [ ] Alice <br/>- [ ] Teresa | > All
| 🛩️ Airline    | 😃 Add/remove hold bags? [Yes, No] | > No
| 🛩️ Airline    | 😃 Any forbidden items? [Yes, No] | > No
| 🤵 [Broker](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Share passports?  [All, No] <br/> - [ ] 🇬🇧 UK Alice <br/>- [ ] 🇬🇧 UK Teresa <br/>- [ ] 🇺🇸 US Teresa  | [X] 🇬🇧 UK Alice <br/> [X] 🇺🇸 US Teresa
| 🤵 [Broker](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Share visas?  [All, No] <br/> - [ ] 🇺🇸 ESTA Alice | > All
| 🤵 [Broker](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Share Covid certificates?  [All, No] <br/> - [ ] 🇬🇧 NHS Alice <br/>- [ ] 🇬🇧 NHS Teresa | > All
| 🧢 [Persona](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/70 🧢 Personas/🧢🫥 Persona agent.md>) | 🫥 Share flight preferences?  [Yes, No] | > Yes
| 🧚 [Curator](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) | 🫥 Share meal preferences?  [Yes, No] | > Yes
| 💖 [Vitalogist](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/95 💖 Vitalogists/💖🫥 Vitalogist agent.md>) | 🫥 Share food allergies?  [Yes, No] | > Yes
| 🆔 [Identity](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) | 🫥 [Sign terms?](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/16 🆔🔏 Verify Signatures.md>) 📄 [Yes, No] | > Yes
| 🆔 [Identity](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/21 🆔😶 Face scan.md>)
| 🤵 [Broker](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Save boarding passes? [Yes, No] | > Yes
| 🛩️ Airline    | ✅ You're checked-in.
| [👀 Ads](<../../../../4 ⚙️ Solution/45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) | 🫥 Explore follow-up actions? [No] <br/>- [ 🏨 Book a hotel ] <br/>- [ 🚙 Rent a car ] | > No
||

