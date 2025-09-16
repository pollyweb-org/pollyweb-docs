💬 Chat FAQ
===

1. **What is a chat?**

    A [Chat 💬](<01 💬 Chat.md>) is 
    * a structured conversation in natural language 
    * between a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and a [Host 🤗 domain](<03 🤗🎭 Host role.md>) 
    * that resembles a Web 2.0 session between a client and a server.

    ---
    <br/>


1. **How are the intervening parties in a chat?**

    | Component | Responsibilities
    |-|-
    |[🤗 Host](<03 🤗🎭 Host role.md>) | Leads the [Chat 💬](<01 💬 Chat.md>), always asking first.
    |[🧑‍🦰 Wallet](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) | Held by the user, replies directly to the [Host 🤗 domain](<03 🤗🎭 Host role.md>).
    |[🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | Intermediates the conversation, receiving the Host's messages and forwarding them to the [Notifier 📣 domain](<../02 📣 Notifiers/02 📣 Notifier domain.md>).
    |[📣 Notifier](<../02 📣 Notifiers/02 📣 Notifier domain.md>) | Implements the mobile push notifications, receiving the messages from the [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) and forwarding them to the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    <br/>



1. **How does a user open a new chat window with a domain?**

    To open a new [Chat 💬](<01 💬 Chat.md>) window with a [Host 🤗 domain](<03 🤗🎭 Host role.md>), a user needs the [Host's Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) contained in one of the following technology forms.

    |Technology|Details
    |-|-
    |[✨ QR code](<../22 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>)| Users open the Wallet app on the device, then scan the QR code to open a chat window.
    |[🔆 NFC tag](<../22 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>)| Users tap the NFC tag with their device, regardless of having the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) open - this opens a chat window on the Wallet.
    |[🌐 Link](<../22 🔆 Locators/02 🧑‍🦰🌐 Wallet URLs.md>)| Users click the link/button on the traditional web browser of their device - this opens a chat window on the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    |[💬 Prompt](<01 💬 Chat.md>)| In a [Chat 💬](<01 💬 Chat.md>) window, the [Host 🤗 domain](<03 🤗🎭 Host role.md>) provides one or more options for the user to select from, and the user selects one - this opens a new [Chat 💬](<01 💬 Chat.md>) window.

    ----
    <br/>

2. **What if the user doesn't have the domain's Locator?**

    If a user doesn't know exactly where to find a [Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>), they can use the [Finder 🔎 domain](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) to search for it;
    * e.g., if a UK user wants to bind to the UK's national health service but doesn't know where to start, the user can ask for "health service" and the assistance replies with "NHS?".

    ---
    <br/>

3. **Can users send a sequence of messages in a chat?**

    No. 
    - NLWeb [Chats 💬](<01 💬 Chat.md>) don't implement WhatsApp's free flow conversation, where users can send multiple messages in sequence that humans typically interpret as a flow. 
    - Instead, NLWeb [Chats 💬](<01 💬 Chat.md>) work like ChatGPT, with one party sending only one message then waiting for the other party to reply. 
    - A similar mechanism is used by Amazon Retail for web and mobile customer support backed by AI workflows.

    ---
    <br/>
    

2. **What are the message types supported in chats?**

    | Component | Behavior
    |-|-
    | 🤗 *Prompt* | [Host 🤗 domains](<03 🤗🎭 Host role.md>) send a question or information to the user.
    | 🗄️ *Bind* | [Vault 🗄️ domains](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)  request the user to [Bind🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>) to them.
    | 💼 *Share* | [Consumer 💼 domains](<../27 💼 Consumers/04 💼🎭 Consumer role.md>)  request the user to share data from a specific [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) or to share a [Token 🎫](<../25 🎫 Tokens/01 🎫 Token.md>).
    | 💳 *Pay* | [Seller 💵 domains](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>)  request the user's [Payer 💳 agent](<../../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) to pay an amount.
    | 👋 *Goodbye* | Ends the [Chat 💬](<01 💬 Chat.md>) workflow.

    ---
    <br/>

5. **How do prompt emojis work?**

    Prompt emojis are visual clues for users.
    - **Non-blocking info ℹ️ ⓘ**
        - this is an informative prompt that does not require the user input;
        - if it contains options, then the user may click an option any time - i.e., before or after the [Host 🤗 domains](<03 🤗🎭 Host role.md>) sends other subsequent prompts;
        - the strong info emoji ℹ️ represents the chat's [Host 🤗 domain](<03 🤗🎭 Host role.md>);
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
        - the happy emoji 😃 represent the chat's [Host 🤗 domain](<03 🤗🎭 Host role.md>);
        - the neutral emoji 😐 also represents the [Host 🤗 domain](<03 🤗🎭 Host role.md>), while providing an alternative neutral face when a smile is not adequate (e.g., in an emergency situation);
        - the faded emoji 🫥 represents other domains that have been pulled into the chat.
    - **Blocking unstructured questions 💬 💭**
        - this is a blocking input prompt that allows the user to type something instead of having to follow a structured format;
        - it allows for large-language models (LLMs) to interpret the user's intent from natural language text, while also providing a structured input to facilitate the user's interaction (e.g., a user may select the "Yes" option, or type "ok" in the textbox);
        - the speech emoji 💬 represent the chat's [Host 🤗 domain](<03 🤗🎭 Host role.md>);
        - the thought emoji 💭 represents other domains that have been pulled into the chat.

    ---
    <br/>

6. **What input formats can Hosts ask Wallets to render?**

    Similar to HTTP, on NLWeb the [Host 🤗 domain](<03 🤗🎭 Host role.md>) servers request the [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to render the requested inputs.

    * The supported input formats are as follow.

    | Format | Description
    |-|-
    | ℹ️ *Info* | General information.
    | 👍 *Confirm* | Yes, No, Cancel.
    | 💯 *Int* | Shows the numeric keypad.
    | 🔄 *Quantity* | Shows up/down arrows.
    | 💰 *Amount* | Allows for decimals.
    | 💬 *OTP* | Asks for 6 digits.
    | 1️⃣ *One* | One of multiple options.
    | 🔢 *Many* | Zero or more of multiple options.
    | ⭐ *Rate* | 1 to 5 stars.
    | 🕓 *Time* | Asks for time of day.
    | 📆 *Date* | Asks for a date.
    | 🗓️ *Until* | Asks for a date/time in the future.
    | 📍 *Location* | Asks for the current location.
    | 🗺️ *Track* | Asks to track the location.
    | 👤 *Identify* | Opens a pop-up for the user's [Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) to perform a face scan.
    | 🛒 *EAN* | Scans for ENA-13 and EAN-8 barcodes.
    | 🔆 *Scan* | Asks to touch/scan a [QR/NFC Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>).
    | 🦋 *Touch* | Asks to touch/scan a [QR/NFC Ephemeral 🦋 device](<../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>).
    | ⬆️ *Upload* | Asks to upload a file or photo.
    | ⬇️ *Download* | Asks to download a file.
    | 🔠 *Text* | Asks for a text input.

    ---
    <br/>


7. **How can Hosts leverage reference data, like countries?**

    [Hosts 🤗 domains](<03 🤗🎭 Host role.md>) can use data sets exposed by [Dataset 🪣 helper domains](<05 🪣🎭 Dataset role.md>).

    ---
    <br/>

8. **How can Hosts protect users from input fatigue?**

    NLWeb advocates for [Hosts 🤗 domains](<03 🤗🎭 Host role.md>) to request as little prompts from users as possible;
    * instead, request users to share datasets using [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>);
    * e.g., ask for `nlweb.org/BOOKING/CONTACTS` instead of asking for the name, then the phone number, then the email address, and so on.
  
    When prompts are inevitable, avoid text prompts; 
    * instead, prefer low-effort prompts;
    * e.g., searchable lists with one or many possible options.

    ---
    <br/>


3. **Can Hosts replace sent prompts?**

    Yes, but only temporary prompts. 
    - If a [Host 🤗 domain](<03 🤗🎭 Host role.md>) sends  two consecutive blocking prompts while the user has not answered the first, then the first becomes readonly and the second becomes the active input.
    - If the [Host 🤗 domain](<03 🤗🎭 Host role.md>) wants a prompt to be visually replaced, then they need to use a temporary prompt, visually represented by an hourglass ⏳ emoji. 
    - This is particularly useful when [preparing food 🤝](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/03 🍽️🍲 Eat at restaurants/03 🍲 Order @ Seat 🪑/03 🪑 Change order 🌀.md>), when [waiting food orders 🤝](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/03 🍽️🍲 Eat at restaurants/06 🍲 Staff @ Back 🧑‍🍳/02 🧑‍🍳 Prepare food 🥘.md>), and when reminding users of [upcoming bookings 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>).

    ---
    <br/>

4. **Can users respond to an old prompt?**

    NLWeb [Chats 💬](<01 💬 Chat.md>) are designed to be forward-only workloads managed by a [Host 🤗 domain](<03 🤗🎭 Host role.md>) (and not by the user). 
    * This behavior is visible on LLM apps like on ChatGPT, Gemini, and others. 
  
    Just like in the previously referred LLMs, NLWeb also allows [Host 🤗 domains](<03 🤗🎭 Host role.md>) to add options in certain steps so that users can go back and change the direction of the workload from a previous step.
    * For example, the user did A, B, C, D, E; then went back to B and changed the history to A, B, X, Y, Z. 
    * This worked because step B had an option set by the [Host 🤗 domains](<03 🤗🎭 Host role.md>) that allowed the user to go back and change the workflow path.

    In NLWeb, these option sets can be added only to non-blocking prompts.

    - The non-blocking prompts include Wait ⏳, Info ℹ️, and Result ✅.
    - This is particularly helpful when [Host 🤗 domains](<03 🤗🎭 Host role.md>) want to assign default values to options to speed up the process (e.g., [navigation options 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/01 🧳 Plans trips 🧭/2 🧭 @ Destination/21 Return.md>)), while still allowing users to go back and change those default options.
    
    ---
    <br/>



4. **How can users report spam messages?**

    Like in WhatsApp, users can mark messages as spam.

    ---
    <br/>

5. **How can users report a domain's misconduct?**

    Like in WhatsApp, users can report or block a domain, providing the reason for it (e.g., offensive, unsolicited, spam).

    ---
    <br/>

6. **How can users contribute to a domain's reputation?**

    Users can provide feedback to domains via stars and comments. 
    * Also, by reporting on domains, users are contributing negatively to the domain's reputation. 
    * [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) share this feedback collaboratively with other Wallets via [Reviewer ⭐ domains](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>). 
    * [Host 🤗 domain](<03 🤗🎭 Host role.md>) managers are notified about the feedback, and can reply to them. Similar mechanisms have been widely adopted by Trust Pilot, Google Maps, and Google Play.

    ---
    <br/>

7. **Do chats support map navigation?**

    No. 
    - [Host 🤗 domains](<03 🤗🎭 Host role.md>) can send location pins in user chats, then users can click on them to open the device's default map navigation app.

    ---
    <br/>