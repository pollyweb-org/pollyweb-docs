

**How to get extra supplies for a product?**
--

A user can scan/tap the NFC/QR on the product (e.g., printer).

| Service | Prompt | User
| - | - | - |
| 🖨️ Seller   | 😃 Hi! What do you need? <br/>- [ Supplies ] <br/>- [ Something else ] | > Supplies
| 🖨️ Seller   | 😃 How many? [1, 2, more] | > 1
| 🧢 [Persona](<../../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | 🫥 Share delivery address? [No] <br/>- [ office ] <br/>- [ Alice's ] | > Alice's
| 🖨️ Seller   | 🙏 Confirm: [OK, Cancel] <br>- arrival: Friday<br/>- total cost: 20 dollars | > OK
| 💳 [Payer](<../../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/02 💳🎭 Payer role.md>) | 🫥 Pay $20.00 bill? 🧾 [No] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC
| 🤵 [Broker](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save parcel delivery? [Yes, No] <br/> | > Yes
| 🖨️ Seller   | 😉 You're all set, bye!
|||

