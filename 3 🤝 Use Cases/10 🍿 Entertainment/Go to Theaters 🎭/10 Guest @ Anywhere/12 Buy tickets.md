<!-- #TODO -->

Buy an anonymous ticket for a show?
---

To buy a ticket for a show (e.g., a musical in London), a user can scan a QR code (e.g., from a website, billboard, or TV show) or tap an NFC tag (e.g., from a paper magazine or flyer): 

| [Domain](<../../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🎭 Venue   | 😃 Want to watch our play? [Yes, No] | > Yes
| 🎭 Venue   | 😃 How many seats do you need? [1, 2, more] | > 2
| 🎭 Venue   | 😃 What's your preferred day? <br/> - [ Today ] <br/> - [ Tomorrow ] <br/> - [ Select from calendar ] | > Tomorrow
| 🧢 [Persona](<../../../../4 ⚙️ Solution/50 🫥 Agents/70 🧢 Personas/$ 🧢🫥 Persona agent.md>) | 🫥 Share theatre preferences? [Yes, No] | > Yes
| 🎭 Venue   | 😃 OK for row E, central, $45 each? [Yes, No] | > Yes
| 🎭 Venue   | 😃 Want a drink during break? [Yes, No] | > No
| 💳 [Payer](<../../../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $90.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 🤵 [Broker](<../../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) | 🫥 Save theatre ticket? [Yes, No]  | > Yes
| 🎭 Venue   | ✅ You're all set, see you tomorrow!
||
