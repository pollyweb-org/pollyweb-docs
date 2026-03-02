# How to book a table at a restaurant?

> From [Eat at restaurants 🍽️](<01 🍽️ Index.md>)

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
|| | > Book 🔗
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍽️ Restaurant | ℹ️ The Guild, Soho
| 🍽️ Restaurant | 😃 Hi! Book a table? [Yes, No] | > Yes
| 🍽️ Restaurant | 😃 At The Guild, Soho? [Yes, No] | > Yes
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ⓘ Flow: book [-]<br/> - your scheduler sets when 🗓️ <br/> - your persona sets contacts 🧢 <br/>- your persona sets preferences 🧢 <br/> - save it on your wallet 🤵<br/> - tap a tag when arriving ✨ | 
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Schedulers 🗓️/$ 🗓️🫥 Scheduler agent.md>) | 🫥 For how many? [1, 2, more] | > 2
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Schedulers 🗓️/$ 🗓️🫥 Scheduler agent.md>) | 🫥 For which day? <br/> - [ Today ] <br/> - [ Tomorrow ] <br/> - [ Select from calendar ] | > Tomorrow
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Schedulers 🗓️/$ 🗓️🫥 Scheduler agent.md>) | 🫥 For what time of the day? <br/> - [ Lunch ] <br/> - [ Dinner ] | > Lunch
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Schedulers 🗓️/$ 🗓️🫥 Scheduler agent.md>) | 🫥 Confirm booking? [Yes, No]<br/> - Alice's lunch break is 1h <br/>- her total commute is 45m <br/>- she'll have 15m to eat <br/>  | > Yes
| 🍽️ Restaurant | ℹ️ Booking summary: [Change] <br/>- table for 2 <br/>- tomorrow, 12pm-2pm <br/>- at The Guild, Soho, W1D 3QX
| 🧢 [Persona](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) | 🫥 Share booking contacts? [No] <br/>- [ 🧑‍🦰 personal ] <br/>- [ 💼 work ] <br/>- [ 🧔 Daniel ] | > 🧑‍🦰 personal
| 🍽️ Restaurant | ℹ️ Received contacts: [Change] <br/>- name: Alice <br/>- pronouns: [ She ]<br/>- phones: [ +1 000 000 000 ]<br/>- emails: [ alice@email.dom ]
| 🧢 [Persona](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) | 🫥 Share seat preferences? [No] <br/>- [ 👤 solo ] <br/>- [ 👨‍👩‍👦 family ] <br/>- [ 🤝 business ] | > 👨‍👩‍👦 family
| 🍽️ Restaurant | ℹ️ Received preferences: [Change] <br/>- no smoking area <br/>- nice view <br/>- conversational waitress
| 🍽️ Restaurant | 😃 Confirm booking? [Yes, No] | > Yes
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 Save booking? [Yes, No]  | > Yes
| 🍽️ Restaurant | ✅ Done. See you then!
| ⭐ [Rate](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) | 🫥 Experience feedback? | ⭐ 5
||


## Talker

```yaml
💬 Reserve a table:

- READ >> $place:                   # Get the restaurant info
    Set: Places
    Key: $.Chat.Key
- INFO: {$place.Name}                # Show the restaurant name
- CONFIRM: Hi! Book a table?         # Confirm booking intent
- CONFIRM: At {$place.Name}?         # Confirm the restaurant   
- INFORM: Book                       # Announce query intents
- CALL: Slots|$place.ID >> $slots    # Get available slots
- READ >> $inf:                      # Get restaurant details
    Set: Files
    Key: '{$place.ID}.md'
- SHARE >> $slot:                    # Ask for slot selection
    Schema: .SCHEDULER/BOOK
    Context: 
        About: $i
        Slots: $slots     
- SHARE >> $call:                    # Ask for user contacts
    Schema: .PERSONA/BOOKING
- SHARE >> $likes:                   # Ask for preferences
    Schema: .PERSONA/MEAL/LIKES
- CONFIRM: Confirm booking?          # Ask for confirmation
- FREEZE                             # Lock the inputs
- SAVE Bookings >> $booking:         # Save the booking
    Place: $place.ID
    Slot: $slot
    Call: $call
    Likes: $likes
- ISSUE:                             # Issue a Token
    Schema: .HOST/BOOKING/SELF
    Token: $booking.ID
- GOODBYE: Done. See you then!       # Confirm booking
```

Uses||
|-|-
|[Commands ⌘](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CALL`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`CONFIRM`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>) [`DONE`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`FREEZE`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/FREEZE ❄️/❄️ FREEZE ⌘ cmd.md>) [`GOODBYE`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) [`INFORM`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) [`ISSUE`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Issuers 🎴/🎴⌘ Issuer cmds/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>) [`READ`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SHARE`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/SHARE 💼/💼 SHARE ⌘ cmd.md>) 
|[Holders 🧠](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/Holder 🧠.md>)| [`$.Chat`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>)