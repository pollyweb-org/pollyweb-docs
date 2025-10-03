How does staff add a booking at a salon?
--

| Domain | Prompt | User
| - | - | -
| ...
| 💈 Salon   | ⏳ Waiting customers... [+] | > +
| 💈 Salon   | ⏳ Waiting customers... <br/> - [ Book ] <br/>- [ Something else ] | > Book
| 💈 Salon   | 😃 What services? <br/>- [  ] Haircut 💇<br/>- [  ]  Manicure 💅<br/>- [  ] Pedicure 🦶 | [X] Haircut 💇 <br/> [X] Manicure 💅
| 💈 Salon   | 😃 Which day? <br/> - [ Today ] <br/> - [ Tomorrow ] <br/> - ... | > Tomorrow
| 💈 Salon   | 😃 What time? <br/> - [ 9:00 ] <br/> - [ 9:30 ] <br/> - ... | > 9:30 
| 💈 Salon   | 😃 Name? | `Alice`
| 💈 Salon   | 😃 Phone number? | `1111111111`
| 💈 Salon   | 😃 Any notes? [No] | `🚫 latex`
| 💈 Salon   | 😃 Confirm? [Yes, No] <br/> - haircut and manicure <br/> - tomorrow, 9:30 to 11:30 <br/> - Alice, 1111111111 <br/> - 🚫 latex | > Yes
| 💈 Salon   | ✅ Booked.
| 💈 Salon   | ⏳ Waiting customers... [+] 
...
||