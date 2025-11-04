# How to book a table at a restaurant?

> From [Eat at restaurants 🍽️](<01 🍽️ Index.md>)

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
|| | > Book 🔗
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍽️ Restaurant | ℹ️ The Guild, Soho
| 🍽️ Restaurant | 😃 Hi! Book a table? [Yes, No] | > Yes
| 🍽️ Restaurant | 😃 At The Guild, Soho? [Yes, No] | > Yes
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ Flow: book [-]<br/> - your scheduler sets when 🗓️ <br/> - your persona sets contacts 🧢 <br/>- your persona sets preferences 🧢 <br/> - save it on your wallet 🤵<br/> - tap a tag when arriving ✨ | 
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
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 Save booking? [Yes, No]  | > Yes
| 🍽️ Restaurant | ✅ Done. See you then!
| ⭐ [Rate](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) | 🫥 Experience feedback? | ⭐ 5
||


## Talker

```yaml
💬|Reserve a table:

# Show the restaurant name
- READ|Restaurant|$.Chat.Key >> $r
- INFO|{$r.Name}

# Confirmations
- CONFIRM|Hi! Book a table?
- CONFIRM|At {$r.Name}?

# Inputs
- INFORM|Book

# Get the booking.
- SHARE|.SCHEDULER/BOOK >> $b
    Context: 
        About: {/info/{$r.ID}.md} # Get the file.
        Slots: {Slots($r.ID)}     # From the ERP.

# Get user contacts.
- SHARE|.PERSONA/BOOKING >> $c

# Get user preferences.
- SHARE|.PERSONA/SEAT/PREFERENCES >> $p

# Allow one last time for input changes.
- CONFIRM|Confirm booking?
- FREEZE >> $inputs
    Restaurant: $r
    Booking: $b
    Contacts: $c
    Preferences: $p

# Save the booking
- EVAL|Save >> $booking:
    $inputs
        
# Issue token
- ISSUE:
    Schema: .HOST/BOOKING/SELF
    Properties: 
        $booking

- SUCCESS|Done. See you then!
- GOODBYE
```


| [Command ⌘](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | Purpose
|-|-
| 🧲 [`READ`](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/📃 datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | Map the locator to a restaurant info.
| 📝 [`INFORM`](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/📃 methods 🤵/INFORM 📝/📝 INFORM ⌘ cmd.md>) | Show user instructions and allow inputs.
| 1️⃣ [`ONE`](<../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>) | Select an option, the day in this case.
| 💼 [`SHARE`](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/📃 methods 🤵/SHARE 💼/💼 SHARE ⌘ cmd.md>) | Get the user's booking contacts.
| 👍 [`CONFIRM`](<../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) | Pause to allow changing previous inputs.
| ❄️ [`FREEZE`](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/📃 methods 🤵/FREEZE ❄️/❄️ FREEZE ⌘ cmd.md>) | Freeze all previous inputs from changes.
| ⬇️ [`EVAL`](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) | Save the booking.
| 🎫 [`ISSUE`](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/📃 methods 🤵/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>) | Call the [Save Token ⏩ flow](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>).
|