Use a bus ticket to enter a bus
--

Buses with passive NFC tags:
- when entering the bus, users tap/scan the NFC/QR in the bus to validate the ticket;
- a chat opens confirming that they are in the right bus. 

Buses with active NFC scanners:
- If the user has an image or a printed version of the token's QR, they can pass the QR through a validation scanner, either on the driver's handheld device or on a fixed location inside the bus.

The chat below is for passive NFC tags only.
    

| [Domain](<../../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../4 ⚙️ Solution/35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 🔎 [Finder](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Finders 🔎/$/🔎 Finder 🫥 agent.md>) | ⓘ Any Operator (4.4 ⭐) [+]
| 🤵 [Broker](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ Ticket [token 🎟️](<../../../../4 ⚙️ Solution/30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) shared [+]
| 🚎 Operator | ℹ️ Bus 198 [+]
| 🚎 Operator | ✅ Valid, last trip used. <br/> - [ Top up trips ]
| ⭐ [Rate](<../../../../4 ⚙️ Solution/50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) | 🫥 Experience feedback? | ⭐ 5
||