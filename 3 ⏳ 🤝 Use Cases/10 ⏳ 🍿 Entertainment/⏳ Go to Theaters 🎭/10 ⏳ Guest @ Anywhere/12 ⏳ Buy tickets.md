#TODO

Buy an anonymous ticket for a show?
---

To buy a ticket for a show (e.g., a musical in London), a user can scan a QR code (e.g., from a website, billboard, or TV show) or tap an NFC tag (e.g., from a paper magazine or flyer): 

| Service | Prompt | User
| - | - | - |
| 🎭 Venue   | 😃 Want to watch our play? [Yes, No] | > Yes
| 🎭 Venue   | 😃 How many seats do you need? [1, 2, more] | > 2
| 🎭 Venue   | 😃 What's your preferred day? <br/> - [ Today ] <br/> - [ Tomorrow ] <br/> - [ Select from calendar ] | > Tomorrow
| 🧢 [Persona](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/02 ✅ 🧢 Personas/02 ✅ 🧢🫥 Persona agent.md>) | 🫥 Share theatre preferences? [Yes, No] | > Yes
| 🎭 Venue   | 😃 OK for row E, central, $45 each? [Yes, No] | > Yes
| 🎭 Venue   | 😃 Want a drink during break? [Yes, No] | > No
| 💳 [Payer](<../../../../4 ⏳ ⚙️ Solution/30 ⏳ 🫥 Agents/04 ✅ 💳 Payers/01 ✅ 💳🫥 Payer agent.md>) | 🫥 Pay $90.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 🤵 [Broker](<../../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) | 🫥 Save theatre ticket? [Yes, No]  | > Yes
| 🎭 Venue   | ✅ You're all set, see you tomorrow!
||
