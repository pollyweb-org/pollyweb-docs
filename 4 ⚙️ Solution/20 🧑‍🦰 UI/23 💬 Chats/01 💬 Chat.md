💬 Chat FAQ
===

1. **What is a chat?**

    A chat is a structured conversation in natural language between a [Wallet 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and a [Host 🤗](<03 🤗🎭 Host role.md>) that resembles a Web 2.0 session between a client and a server.

    ---

1. **How are the intervening parties in a chat?**

    - [Host 🤗](<03 🤗🎭 Host role.md>): leads the chat, always asking first;
    - [Wallet 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>): held by the user, replies directly to the Host;
    - [Broker 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>): intermediates the conversation, receiving the Host's messages and forwarding them to the Notifier;
    - [Notifier 📣](<../02 📣 Notifiers/02 📣 Notifier domain.md>): implements the mobile push notifications, receiving the messages from the Broker and forwarding them to the Wallet.

    ---

1. **What are the message types supported in chats?**

    - 🤗 *Prompt*: a [Host 🤗](<03 🤗🎭 Host role.md>) domains send a question or information to users.
    - 🗄️ *Bind*: [Vault 🗄️](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) domains request users to [Bind 🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>) to them.
    - 💼 *Share*: [Consumer 💼](<../27 💼 Consumers/04 💼🎭 Consumer role.md>) domains request users to share data from a specific [schema](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) or to share a [Token 🎫](<../25 🎫 Tokens/01 🎫 Token.md>).
    - 💳 *Pay*: [Seller 💵](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) domains request the user's [Payer 💳](<../../30 🫥 Agents/04 💳 Payers/01 💳🫥 Payer agent.md>) vault to pay an amount.
    - 👋 *Goodbye*: ends the chat workflow.

    ---

1. **Can Hosts replace sent prompts?**

    Yes, but only temporary prompts. 
    - If an [Host 🤗](<03 🤗🎭 Host role.md>) sends  two consecutive blocking prompts while the user has not answered the first, then the first becomes readonly and the second becomes the active input.
    - If the [Host 🤗](<03 🤗🎭 Host role.md>) wants a prompt to be visually replaced, then they need to use a temporary prompt, visually represented by an hourglass ⏳ emoji. 
    - This is particularly useful when [preparing food](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/03 🍽️🍲 Eat at restaurants/03 🍲 Order @ Seat 🪑/03 🪑 Change order 🌀.md>), when [waiting food orders](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/03 🍽️🍲 Eat at restaurants/06 🍲 Staff @ Back 🧑‍🍳/02 🧑‍🍳 Prepare food 🥘.md>), and when reminding users of [upcoming bookings](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>).

    ---

1. **Can users respond to an old prompt?**

    Yes, but only to non-blocking prompts.

    - Non-blocking prompts (e.g., wait ⏳ and info ℹ️) that have not been answered by the user, allow the user to go back and interact with it.
    - This is particularly helpful when [Hosts 🤗](<03 🤗🎭 Host role.md>) want to assign default values to options to speed up the process (e.g., [navigation options](<../../../3 🤝 Use Cases/03 🧳 Travel/01 🧳 Plans trips 🧭/2 🧭 @ Destination/21 Return.md>)), while still allowing users to go back and change those default options.
    
    ---

1. **How do prompt emojis work?**

    Prompt emojis are visual clues for users.
    - **Non-blocking info ℹ️ ⓘ**
        - this is an informative prompt that does not require the user input;
        - if it contains options, then the user may click an option any time - i.e., before or after the [Host 🤗](<03 🤗🎭 Host role.md>) sends other subsequent prompts;
        - the strong info emoji ℹ️ represents the chat's [Host 🤗](<03 🤗🎭 Host role.md>);
        - the faded info emoji ⓘ represents other domains that have been pulled into the chat.
    - **Non-blocking temporary info ⏳**
        - this is an info prompt that is automatically removed when a new prompt arrives;
        - if it contains options, then the user may click an option while it's visible.
    - **Non-blocking result ✅**
        - this is an info prompt that signals the user that the transaction is completed and there are no further inputs required - they can put down the phone.
    - **Non-blocking failure ❌**
        - this is an info prompt that signals the user that the transaction was not successful;
        - it's typically followed by a prompt to help the user fix the problem.
    - **Blocking structured questions 😃 😐 🫥**
        - this is a blocking input prompt that requires the user to answer it in a structured format (e.g., date, number, radio, checklist);
        - it addresses the basic needs of a standard structured form with multiple input fields.
        - the happy emoji 😃 represent the chat's [Host 🤗](<03 🤗🎭 Host role.md>);
        - the neutral emoji 😐 also represents the [Host 🤗](<03 🤗🎭 Host role.md>), while providing an alternative neutral face when a smile is not adequate (e.g., in an emergency situation);
        - the faded emoji 🫥 represents other domains that have been pulled into the chat.
    - **Blocking unstructured questions 💬 💭**
        - this is a blocking input prompt that allows the user to type something instead of having to follow a structured format;
        - it allows for large-language models (LLMs) to interpret the user's intent from natural language text, while also providing a structured input to facilitate the user's interaction (e.g., a user may select the "Yes" option, or type "ok" in the textbox);
        - the speech emoji 💬 represent the chat's [Host 🤗](<03 🤗🎭 Host role.md>);
        - the thought emoji 💭 represents other domains that have been pulled into the chat.

    ---

1. **What input formats can Hosts ask Wallets to render?**

    Similar to HTTP, on NLWeb the [Host 🤗](<03 🤗🎭 Host role.md>) servers request the [Wallet 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) browsers to render the requested inputs.

    Supported input formats are:
    - ℹ️ *Info*: general information
    - 👍 *Confirm*: yes, no, cancel
    - 💯 *Int*: shows the numeric keypad
    - 🔄 *Quantity*: shows up/down arrows
    - 💰 *Amount*: allows for decimals
    - 💬 *OTP*: asks for 6 digits
    - 1️⃣ *One*: one of multiple options
    - 🔢 *Many*: zero or more of multiple options
    - ⭐ *Rate*: 1 to 5 stars
    - 🕓 *Time*: asks for time of day
    - 📆 *Date*: asks for a date
    - 🗓️ *Until*: asks for a date/time in the future
    - 📍 *Location*: asks for the current location
    - 🗺️ *Track*: asks to track the location
    - 👤 *Identify*: opens a pop-up for the user's [Identity 🆔](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) vault to perform a face scan
    - 🛒 *EAN*: scans for ENA-13 and EAN-8 barcodes
    - 🔆 *Scan*: asks to touch/scan a QR/NFC [Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>)
    - 🦋 *Touch*: asks to touch/scan an [Ephemeral 🦋](<../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>) QR/NFC
    - ⬆️ *Upload*: asks to upload a file or photo
    - ⬇️ *Download*: asks to download a file
    - 🔠 *Text*: asks for a text input

    ---


## See also:

- [🧑‍🦰💬 Wallet chats](<02 🧑‍🦰💬 Wallet chats.md>)
- [🤗💬 Host chats](<04 🤗💬 Host chats.md>)