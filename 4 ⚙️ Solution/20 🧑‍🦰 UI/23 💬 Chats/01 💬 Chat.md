💬 Chat FAQ
===

1. **What is a chat?**

    A [Chat 💬](<01 💬 Chat.md>) is 
    * a structured conversation in natural language 
    * between a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and a [Host 🤗 domain](<04 🤗🎭 Host role.md>) 
    * that resembles a Web 2.0 session between a client and a server.

    ---
    <br/>


1. **How are the intervening parties in a chat?**

    | Component | Responsibilities
    |-|-
    |[🤗 Host](<04 🤗🎭 Host role.md>) | Leads the [Chat 💬](<01 💬 Chat.md>), always asking first.
    |[🧑‍🦰 Wallet](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) | Held by the user, replies directly to the [Host 🤗 domain](<04 🤗🎭 Host role.md>).
    |[🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | Intermediates the conversation, receiving the Host's messages and forwarding them to the [Notifier 📣 domain](<../02 📣 Notifiers/02 📣 Notifier domain.md>).
    |[📣 Notifier](<../02 📣 Notifiers/02 📣 Notifier domain.md>) | Implements the mobile push notifications, receiving the messages from the [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) and forwarding them to the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    <br/>



1. **How does a user open a new chat window with a domain?**

    To open a new [Chat 💬](<01 💬 Chat.md>) window with a [Host 🤗 domain](<04 🤗🎭 Host role.md>), a user needs the [Host's Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) contained in one of the following technology forms.

    |Technology|Details
    |-|-
    |[✨ QR code](<../22 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>)| Users open the Wallet app on the device, then scan the QR code to open a chat window.
    |[🔆 NFC tag](<../22 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>)| Users tap the NFC tag with their device, regardless of having the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) open - this opens a chat window on the Wallet.
    |[🌐 Link](<../22 🔆 Locators/02 🧑‍🦰🌐 Wallet URLs.md>)| Users click the link/button on the traditional web browser of their device - this opens a chat window on the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    |[🤔 Prompt](<02 🤔 Prompt.md>)| In a [Chat 💬](<01 💬 Chat.md>) window, the [Host 🤗 domain](<04 🤗🎭 Host role.md>) provides one or more options for the user to select from, and the user selects one - this opens a new [Chat 💬](<01 💬 Chat.md>) window.

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
    | [🤔 Prompt](<02 🤔 Prompt.md>) | [Host 🤗 domains](<04 🤗🎭 Host role.md>) send a question or information to the user.
    | 🗄️ *Bind* | [Vault 🗄️ domains](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)  request the user to [Bind🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>) to them.
    | 💼 *Share* | [Consumer 💼 domains](<../27 💼 Consumers/04 💼🎭 Consumer role.md>)  request the user to share data from a specific [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) or to share a [Token 🎫](<../25 🎫 Tokens/01 🎫 Token.md>).
    | 💳 *Pay* | [Seller 💵 domains](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>)  request the user's [Payer 💳 agent](<../../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) to pay an amount.
    | 👋 *Goodbye* | Ends the [Chat 💬](<01 💬 Chat.md>) workflow.

    ---
    <br/>




7. **How can Hosts leverage reference data, like countries?**

    [Hosts 🤗 domains](<04 🤗🎭 Host role.md>) can use data sets exposed by [Dataset 🪣 helper domains](<07 🪣🎭 Dataset role.md>).

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
    * [Host 🤗 domain](<04 🤗🎭 Host role.md>) managers are notified about the feedback, and can reply to them. Similar mechanisms have been widely adopted by Trust Pilot, Google Maps, and Google Play.

    ---
    <br/>

7. **Do chats support map navigation?**

    No. 
    - [Host 🤗 domains](<04 🤗🎭 Host role.md>) can send location pins in user chats, then users can click on them to open the device's default map navigation app.

    ---
    <br/>