**How to serve food at a restaurant?**
---

| Service | Prompt | User
| - | - | - |
| ...
| 🍲 Restaurant  | ⏳ Waiting items... [+] | > +
| 🍲 Restaurant   | ⏳ Waiting items... <br/>- [ Order ] <br/>- [ Something else ] | > Order
| 🍲 Restaurant  | 😃 Table number? | 🔢 4
| 🍲 Restaurant  | 😃 Add item? [No] <br/> - [ normal paella 🥘 ] <br/> - [ dark paella 🥘 ] <br/> - [ tap water 🚰 ] <br/> - [ red wine glass 🍷 ] <br/> ...| `dark` <br/> > dark paella 🥘
| 🍲 Restaurant  | ℹ️ 1 dark paella 🥘 <br/> - [ Change quantity ] <br/> - [ Cancel item ] 
| 🍲 Restaurant  | 😃 Add item? [No] <br/>- ...| > red wine  🍷
| 🍲 Restaurant  | ℹ️ 1 red wine glass 🍷 [+]
| 🍲 Restaurant  | 😃 Add item? [No] <br/>- ...| > No
| 🍲 Restaurant  | 😃 Confirm? [Yes, No] <br/> - 1 dark paella 🥘 <br/> - 1 red wine glass 🍷 | > Yes
| 🍲 Restaurant  | ✅ Order submitted! <br/>- [ Change order ]
| 🍲 Restaurant  | ⏳ Waiting items... [+] 
||