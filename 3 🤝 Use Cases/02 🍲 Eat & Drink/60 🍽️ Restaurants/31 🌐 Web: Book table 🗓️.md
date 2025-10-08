# How to book a table at a restaurant?

> From [Eat at restaurants 🍽️](<01 🍽️ Index.md>)

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/50 🤔 Prompts/1 📘 Prompt specs/01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
|| | > Book 🔗
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Restaurant (4.3 ⭐)  [+]
| 🍽️ Restaurant | ℹ️ The Guild, Soho
| 🍽️ Restaurant | 😃 Hi! Book a table? [Yes, No] | > Yes
| 🍽️ Restaurant | 😃 At The Guild, Soho? [Yes, No] | > Yes
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Flow: book [-]<br/> - your scheduler sets when 🗓️ <br/> - your persona sets contacts 🧢 <br/>- your persona sets preferences 🧢 <br/> - save it on your wallet 🤵<br/> - tap a tag when arriving ✨ | 
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/30 🫥 Agents/38 🕓 User Timeline/04 🗓️🗄️ Scheduler agent.md>) | 🫥 For how many? [1, 2, more] | > 2
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/30 🫥 Agents/38 🕓 User Timeline/04 🗓️🗄️ Scheduler agent.md>) | 🫥 For which day? <br/> - [ Today ] <br/> - [ Tomorrow ] <br/> - [ Select from calendar ] | > Tomorrow
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/30 🫥 Agents/38 🕓 User Timeline/04 🗓️🗄️ Scheduler agent.md>) | 🫥 For what time of the day? <br/> - [ Lunch ] <br/> - [ Dinner ] | > Lunch
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/30 🫥 Agents/38 🕓 User Timeline/04 🗓️🗄️ Scheduler agent.md>) | 🫥 Confirm booking? [Yes, No]<br/> - Alice's lunch break is 1h <br/>- her total commute is 45m <br/>- she'll have 15m to eat <br/>  | > Yes
| 🍽️ Restaurant | ℹ️ Booking summary: [Change] <br/>- table for 2 <br/>- tomorrow, 12pm-2pm <br/>- at The Guild, Soho, W1D 3QX
| 🧢 [Persona](<../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | 🫥 Share booking contacts? [No] <br/>- [ 🧑‍🦰 personal ] <br/>- [ 💼 work ] <br/>- [ 🧔 Daniel ] | > 🧑‍🦰 personal
| 🍽️ Restaurant | ℹ️ Received contacts: [Change] <br/>- name: Alice <br/>- pronouns: [ She ]<br/>- phones: [ +1 000 000 000 ]<br/>- emails: [ alice@email.com ]
| 🧢 [Persona](<../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | 🫥 Share seat preferences? [No] <br/>- [ 👤 solo ] <br/>- [ 👨‍👩‍👦 family ] <br/>- [ 🤝 business ] | > 👨‍👩‍👦 family
| 🍽️ Restaurant | ℹ️ Received preferences: [Change] <br/>- no smoking area <br/>- nice view <br/>- conversational waitress
| 🍽️ Restaurant | 😃 Confirm booking? [Yes, No] | > Yes
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save booking? [Yes, No]  | > Yes
| 🍽️ Restaurant | ✅ Done. See you then!
| ⭐ [Rate](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | ⭐ 5
||


## Talker

```yaml
💬|Reserve a table:

# Show the restaurant name
- MAP|Restaurant|{.Chat.Key} >> $r
- INFO|{$r.Name}

# Confirmations
- CONFIRM|Hi! Book a table?
- CONFIRM|At {$r.Name}?

# Inputs
- FORM|Book

# Get the booking.
- SHARE|@SCHEDULER/BOOK >> $b
    Context: 
        About: {/info/{$r.ID}.md} # Get the file.
        Slots: {Slots($r.ID)}     # From the ERP.

# Get user contacts.
- SHARE|@PERSONA/BOOKING >> $c

# Get user preferences.
- SHARE|@PERSONA/SEAT/PREFERENCES >> $p

# Allow one last time for input changes.
- CONFIRM|Confirm booking?
- FREEZE >> $inputs
    Restaurant: $r
    Booking: $b
    Contacts: $c
    Preferences: $p

# Save the booking
- EVAL|{Save($inputs)} >> $token 
        
# Issue token
- OFFER|{$token}
- SUCCESS|Done. See you then!
- GOODBYE
```


| [Command ⌘](<../../../9 😃 Talkers/20 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
|-|-
| 
| 🪣 [`MAP`](<../../../9 😃 Talkers/30 🗃️ Talker data/61 🪣 MAP item.md>) | Map the locator to a restaurant info.
| 📝 [`FORM`](<../../../9 😃 Talkers/60 ⏩ Msg flows/41 📝 FORM msg.md>) | Show user instructions and allow inputs.
| 1️⃣ [`ONE`](<../../../9 😃 Talkers/50 🤔 Prompts/7 ✏️ Input prompts/53 1️⃣ ONE prompt.md>) | Select an option, the day in this case.
| 💼 [`SHARE`](<../../../9 😃 Talkers/60 ⏩ Msg flows/45 💼 SHARE msg.md>) | Get the user's booking contacts.
| 👍 [`CONFIRM`](<../../../9 😃 Talkers/50 🤔 Prompts/7 ✏️ Input prompts/31 👍 CONFIRM prompt.md>) | Pause to allow changing previous inputs.
| ❄️ [`FREEZE`](<../../../9 😃 Talkers/60 ⏩ Msg flows/42 ❄️ FREEZE msg.md>) | Freeze all previous inputs from changes.
| ⬇️ [`EVAL`](<../../../9 😃 Talkers/30 🗃️ Talker data/20 ⬇️ EVAL flow.md>) | Save the booking.
|