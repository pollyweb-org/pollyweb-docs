🍲 How to book a table at a restaurant?
---

> From [Eat at restaurants 🍽️](<01 🍽️ Index of Restaurant.md>)

## 💬 Chat

| Service | Prompt | User
| - | - | - |
|| | > Book 🔗
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍲 Restaurant | ℹ️ The Guild, Soho
| 🍲 Restaurant | 😃 Hi! Book a table? [Yes, No] | > Yes
| 🍲 Restaurant | 😃 At The Guild, Soho? [Yes, No] | > Yes
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Flow: book [-]<br/> - your scheduler sets when 🗓️ <br/> - your persona sets contacts 🧢 <br/>- your persona sets preferences 🧢 <br/> - save it on your wallet 🤵<br/> - tap a tag when arriving ✨ | 
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/30 🫥 Agents/38 🕓 User Timeline/04 🗓️🗄️ Scheduler agent.md>) | 🫥 For how many? [1, 2, more] | > 2
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/30 🫥 Agents/38 🕓 User Timeline/04 🗓️🗄️ Scheduler agent.md>) | 🫥 For which day? <br/> - [ Today ] <br/> - [ Tomorrow ] <br/> - [ Select from calendar ] | > Tomorrow
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/30 🫥 Agents/38 🕓 User Timeline/04 🗓️🗄️ Scheduler agent.md>) | 🫥 For what time of the day? <br/> - [ Lunch ] <br/> - [ Dinner ] | > Lunch
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/30 🫥 Agents/38 🕓 User Timeline/04 🗓️🗄️ Scheduler agent.md>) | 🫥 Confirm booking? [Yes, No]<br/> - Alice's lunch break is 1h <br/>- her total commute is 45m <br/>- she'll have 15m to eat <br/>  | > Yes
| 🍲 Restaurant | ℹ️ Booking summary: [Change] <br/>- table for 2 <br/>- tomorrow, 12pm-2pm <br/>- at The Guild, Soho, W1D 3QX
| 🧢 [Persona](<../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | 🫥 Share booking contacts? [No] <br/>- [ 🧑‍🦰 personal ] <br/>- [ 💼 work ] <br/>- [ 🧔 Daniel ] | > 🧑‍🦰 personal
| 🍲 Restaurant | ℹ️ Received contacts: [Change] <br/>- name: Alice <br/>- pronouns: [ She ]<br/>- phones: [ +1 000 000 000 ]<br/>- emails: [ alice@email.com ]
| 🧢 [Persona](<../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | 🫥 Share seat preferences? [No] <br/>- [ 👤 solo ] <br/>- [ 👨‍👩‍👦 family ] <br/>- [ 🤝 business ] | > 👨‍👩‍👦 family
| 🍲 Restaurant | ℹ️ Received preferences: [Change] <br/>- no smoking area <br/>- nice view <br/>- conversational waitress
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save booking? [Yes, No]  | > Yes
| 🍲 Restaurant | ✅ Done. See you then!
| ⭐ [Reviewer](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | > ⭐⭐⭐⭐⭐
||


## Talker

```yaml
💬|Reserve a table:
- INFO|{restaurant-from-locator}
- CONFIRM|Hi! Book a table?
- IF|{has-resource}|inform-restaurant-name  # ℹ️ The Guild, Soho
- ONE|Which date?|{booking-dates}
- ONE|What time?|{booking-times}
- INT|How many people?
- SHARE|nlweb.org/PROFILE/BOOKING|Let us reach out to you if there is any problem.
- CONFIRM|{summary}
- CHARGE|1.00|USD|Reservation charge
- ISSUE|nlweb.org/HOST/BOOKING/SELF|{bookingUUID}
- GOODBYE|{booked}

inform-resource:
- INFO|{inform-restaurant-name} # ℹ️ The Guild, Soho

```