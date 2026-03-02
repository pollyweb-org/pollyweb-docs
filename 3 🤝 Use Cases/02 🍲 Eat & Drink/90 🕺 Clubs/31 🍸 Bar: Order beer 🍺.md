Ask for a beer at a club with age proof
===

> Part of [🕺 Night Clubs](<01 🕺 Index.md>)

<br/>



At the club, the customer taps/scans any NFC/QR tag.
- The order is placed from a tag near the counter.
- When ready, the customer taps on a dynamic tag to be given the drink.
- The waitress has a set of drinks over named slots to deliver.

What it solves for customers:
- no need to push nor yell to ask for a drink;
- no need to be aware of queue jumpers or line cutters;
- no need to use a payment card with people looking over their shoulder;
- and no need to wait for the drink while others push and yell also.

<br/> 

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Club (4.4 ⭐) [+]
| 🕺 Club           | 😃 What do you need? <br/>- [ Order ] from bar <br/>- [ Something else ] | > Order
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/> - your vitalogist reviews 💖 <br/> - your payer pays the bill 💳 <br/> - we'll alert  when ready 📣<br/> -  tap the bar to collect ✨ <br/> - baristas check names 🧢<br/> - your vitalogist records it 💖 | > Yes
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | 🫥 Share bar preferences? <br/>- [ 👤 solo ] <br/>- [ 👨‍👩‍👦 family ] <br/>- [ 🤝 business ] | > 👤 solo
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | 💭 Here are suggestions: <br/>- [ white wine 🍷 ] <br/> - [ still water 💧 ] <br/> - [ tap water 🚰 ] | `a beer`
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | ⓘ I notice you dislike beer.
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | 💭 Try wine instead? [Yes, No] | > No
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | 💭 Which beer? <br/> - [ Lager ] <br/> - [ Pale Ale ] <br/> - [ Stout] <br/> - [ IPA ] | `something`<br/>`similar to`<br/>`Budweiser`
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | ⓘ The lager is similar. 
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | 💭 Want a lager? [Yes, No] | `the brand?`
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | ⓘ It's Stella Artois. 
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | 💭 Want a lager? [Yes, No] | > Yes
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | 💭 What size? <br/> - [ pint ] <br/> - [ half pint ] | `small`
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | ⓘ Half pint it is.
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | 💭 Anything else? [Yes, No]     | > No
| 🕺 Club           | ℹ️ Order: [Change] <br/>- 1 half pint lager 🍺 (£3.00) <br/>- to Ms. Butterfly
| 💖 [Vitalogist](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Vitalogists 💖/💖🫥 Vitalogist agent.md>) | 🫥 Confirm? [Yes, No] <br> - warning: you came by car. | > Yes
| 💳 [Payer](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | 🫥 Pay £3.00 bill? 🧾 [No] <br/>- [ Card ABC ] + $0.10 <br/>- [ Card DEF ] (free) | > Card ABC |
| 🕺 Club           | ✅ Order submitted [+]
| 🕺 Club           | ⏳ Preparing your order... <br/>- [ Cancel ] 
|...
||