🤗 Host domain role FAQ
===

1. **What is a Host domain role in NLWeb?**

    A [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) with a [Host 🤗 domain role](<04 🤗🎭 Host role.md>) is any [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) that
    * hosts a [Chat 💬](<01 💬 Chat.md>) with [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) 
    * via a [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>). 

    ---
    <br/>

1. **How do Host domains work?**

    ![](<.📎 Assets/💬🤗 Host.png>)

    |#|Category|Step
    |-|-|-
    |1| `Hello`| The [user's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) checks-in into a [Host 🤗 domain](<04 🤗🎭 Host role.md>), passing it context parameters, [Binds 🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>), and [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>).
    |2| `Chat` | The [Host 🤗 domain](<04 🤗🎭 Host role.md>) sets a new [Chat 💬](<01 💬 Chat.md>) context.
    |3| `Interact` | The [Host 🤗 domain](<04 🤗🎭 Host role.md>) starts interacting with prompts.

    ---
    <br/>


1. **What data is sent in the Check-in hello?**

    The [user's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) sends the following data to the [Host 🤗 domain](<04 🤗🎭 Host role.md>) on check-in.

    | Data | Example | Reason
    |-|-|-
    | `ChatID` | `{GUID}` | The ID of the [Chat 💬](<01 💬 Chat.md>) on the [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>).
    | `Language` | `en-us` | The user's preferred language.
    | `Locator`| `{GUID}` | The [Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) on the [Host 🤗 domain](<04 🤗🎭 Host role.md>).
    | `Code` | `nlweb.org/HOST`| The [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) of the [Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>).
    | `Binds []` | `[{GUID}]` | The user's [Binds 🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>) to the [Host 🤗 domain](<04 🤗🎭 Host role.md>).
    | `Tokens []` | `[{GUID}]` | The user's [Tokens](<../25 🎫 Tokens/01 🎫 Token.md>) automatically sharable.
    | `Request`  | `Back to hotel` | User request from a previous [Chat 💬](<01 💬 Chat.md>).

    ---
    <br/>

1. **How are users protected from stalking from Hosts?**

    NLWeb sees [Chats 💬](<01 💬 Chat.md>) as temporary sessions, always initiated by users; 
    - i.e., the [Host 🤗 domain](<04 🤗🎭 Host role.md>) receives a temporary ID from the [user's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) when the [Chat 💬 session](<01 💬 Chat.md>)  is open, but no other ID to track the user across sessions;
    - although [Host 🤗 domains](<04 🤗🎭 Host role.md>) can proactively send messages on an open [Chat 💬 session](<01 💬 Chat.md>), users can close the session at any time. 

    ---
    <br/>

2. **What incentives do Hosts have to close sessions?**

    [Advertising 👀](<../../../2 🏔️ Landscape/1 💼 Business landscape/04 👀 Advertising landscape/00 👀 Advertising index.md>) is triggered at the end of a [Chat 💬](<01 💬 Chat.md>) for next-best actions.
    - Thus, [Host 🤗 domains](<04 🤗🎭 Host role.md>) willing to monetize via cross-domain advertising are incentivized to close [Chats 💬](<01 💬 Chat.md>). 
    - See the [Advertiser 👀 helper domains](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) for details.

    ---
    <br/>

3. **Do Hosts send messages to users via web sockets?**

    No. 
    - [Host 🤗 domains](<04 🤗🎭 Host role.md>) send [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) via HTTPS POST to a proxy [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) that then communicate with the user's [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) with real-time protocols (e.g., web sockets, MQTT). 

    ---
    <br/>

4. **What proxy services are involved in the flow?**

    [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) sent from [Host 🤗 domains](<04 🤗🎭 Host role.md>) first reach the user's [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) via HTTPS POST:
    - these [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) are responsible for orchestrating [Chats 💬](<01 💬 Chat.md>) between users and [Host 🤗 domains](<04 🤗🎭 Host role.md>) using the NLWeb protocol, 
    - and they are typically implemented by a main cloud provider that is able to ensure high availability and low latency communication between globally dispersed entities. 
    
    The [user's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) then sends the message to a [user's Notifier 📣 domain](<../02 📣 Notifiers/02 📣 Notifier domain.md>), also via HTTPS POST:
    - the [user's Notifier 📣 domain](<../02 📣 Notifiers/02 📣 Notifier domain.md>) is responsible for pushing the message to the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) via whatever real-time mechanisms the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) supports (e.g., web sockets, MQTT);
    - because of this technical dependency, a [Notifier 📣 domain](<../02 📣 Notifiers/02 📣 Notifier domain.md>) is typically implemented by the same team that implemented the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    <br/>


6. **Are chat prompt messages encrypted from Hosts to Wallets?**

    Not applicable - [Host 🤗 domains](<04 🤗🎭 Host role.md>) don't send [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) to [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>). 

    * [Host 🤗 domains](<04 🤗🎭 Host role.md>) only send asynchronous HTTPS intents to the [user's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>), who then sends it to the [user's Notifier 📣 domain](<../02 📣 Notifiers/02 📣 Notifier domain.md>) also via asynchronous HTTPS. 

    * When the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) app receives the intent from the [Notifier 📣 domain](<../02 📣 Notifiers/02 📣 Notifier domain.md>), it pulls the [Message 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) content directly from the [Host 🤗 domain](<04 🤗🎭 Host role.md>) with a synchronous HTTPS call. 

    * This keeps the [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) and the [Notifier 📣 domain](<../02 📣 Notifiers/02 📣 Notifier domain.md>) in the dark regarding the content of the [Message 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) (even in the event of a cryptography attack) because no content actually passes by these proxy services.

    ---
    <br/>

2. **Are chat reply messages encrypted from Wallets to Hosts?**

    Yes. 

    - Although the user's [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) content is JSON not encrypted, it is sent over HTTPS POST directly from the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to the [Host 🤗 domain](<04 🤗🎭 Host role.md>).

    - The HTTPS channel ensures the message is encrypted between the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and the [Host 🤗 domain](<04 🤗🎭 Host role.md>) . 

    - Unencrypted JSON requests sent over HTTPS are a standard practice in the service APIs of the major cloud providers (e.g., AWS, GCP), and are widely viewed as secure.

    - NLWeb relies on the HTTPS ability to continue to evolve has [post-quantum 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/10 📺 Post-quantum keys.md>) cryptography attacks become more sophisticated.

    ---
    <br/>


1. **What API methods are exposed by a Host domain?**

    | Caller | Method | Store | Description
    |-|-|-|-
    🤵 Broker | [🐌 Hello](<../../../6 🅰️ APIs/50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>) | Chats | The user started a Chat.
    🧑‍🦰 Wallet | [🐌 Home](<../../../6 🅰️ APIs/50 🤗🅰️ Host/02 🤵🐌🤗 Home.md>) | Chats | Show the top menu on the Chat.
    🤵 Broker | [🐌 Abandoned](<../../../6 🅰️ APIs/50 🤗🅰️ Host/03 🤵🐌🤗 Abandoned.md>) | Chats | The user abandoned a Chat.
    🧑‍🦰 Wallet | [🚀 Prompted](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) | Prompts | Return the Prompt's content.
    🧑‍🦰 Wallet | [🐌 Reply](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) | Prompts | Accept the reply to the Prompt.
    🧑‍🦰 Wallet | [🚀 Download](<../../../6 🅰️ APIs/50 🤗🅰️ Host/06 🧑‍🦰🚀🤗 Download.md>) | Attachments | Download the attachment.
    🧑‍🦰 Wallet | [🚀 Upload](<../../../6 🅰️ APIs/50 🤗🅰️ Host/07 🧑‍🦰🚀🤗 Upload.md>) | Attachments | Upload an attachment.
    🖐️ Palmist | [🐌 Found](<../../../6 🅰️ APIs/50 🤗🅰️ Host/08 🖐️🐌🤗 Found.md>) | Chats | A Palmist found the Chat's user.
    ⭐ Reviewer | [🐌 Rated](<../../../6 🅰️ APIs/50 🤗🅰️ Host/09 ⭐🐌🤗 Rated.md>) | Chats | The Chat received user reviews.
    🤵 Broker | [🐌 Summarize](<../../../6 🅰️ APIs/50 🤗🅰️ Host/10 🤵🐌🤗 Summarize.md>) | Chats | Return an advertising summary.

    ---
    <br/>


1. **What flows are initiated by Host domains?**

    | Flow  | Description
    |-|-
    | [🤗⏩🧑‍🦰 Prompt](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | Sends a [Prompt 🤔](<02 🤔 Prompt.md>) to a user [Chat 💬](<01 💬 Chat.md>)
    | [🤗⏩🧑‍🦰 Goodbye](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/02 🤗⏩🧑‍🦰 Goodbye.md>) | Triggers the [👀 advertising](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) flow
    |