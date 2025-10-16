How does staff finish a customer at a salon?
--

| [Domain](<../../../../4 ⚙️ Solution/40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | -
| ...
| 💈 Salon   | ⏳ Customer queue... <br/> - [ ✨1 ] 09:30 Alice 💇 💅 <br/> - [ ⏳2 ] Mrs Parker 💅 <br/> - [ ✨3 ] 10:00 Leo 💇 <br/>- [ Something else ] | > ✨1
| 💈 Salon   | 😃 Finish? [Yes, No, +] <br/> - 09:30 Alice 💇 💅 <br/> - 🚫 allergic to latex  | > Yes
| 💈 Salon   | 😃 Confirm $40 [Yes]? <br/> - Haircut 💇 ($30) <br/> - Manicure 💅 ($10) | > Yes
| 💈 Salon   | ℹ️ Issued $40 bill [+]
| 💈 Salon   | ⏳ Customer queue... <br/> - [ 💳1 ] 09:30 Alice 💇 💅 <br/> - [ ⏳2 ] Mrs Parker 💅 <br/> - [ ✨3 ] 10:00 Leo 💇 <br/>- [ Something else ]
| 💈 Salon   | 📣 Alice paid [+]
| 💈 Salon   | ⏳ Customer queue...  <br/> - [ ⏳2 ] Mrs Parker 💅 <br/> - [ ✨3 ] 10:00 Leo 💇 <br/>- [ Something else ]
| ...
|