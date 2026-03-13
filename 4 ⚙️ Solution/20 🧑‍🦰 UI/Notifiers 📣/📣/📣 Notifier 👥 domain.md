📣 Notifier domains
===



1. **What is a Notifier domain in PollyWeb?**

    A [Notifier 📣](<📣 Notifier 👥 domain.md>) is any backend-for-frontend (BFF) [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) that acts as a proxy for a [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>). 
    
    * This allows [Broker 🤵 domains](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) to communicate in standard HTTPS with the [Notifier 📣 domain](<📣 Notifier 👥 domain.md>), while the [Notifier 📣 domain](<📣 Notifier 👥 domain.md>) communicates via mobile-friendly real-time protocols with the [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) (e.g., MQTT, web sockets, mobile notifications). 
    
    * Because of this tight integration between pairs of [Notifier 📣 domains](<📣 Notifier 👥 domain.md>) and [Wallet 🧑‍🦰 apps](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>), PollyWeb advocates for each pair to be built and managed by the same team.

    ---
    <br/>

1. **How do Notifier domains work?**
    
    ![](<📣🏞️ Notifier img.png>)

    |#|Step
    |-|-
    |1| A [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) sends a [Prompt 🤔 ](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) identifier to a [Broker 🤵 domain](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) in the context of a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>), which is then proxied through the [Notifier 📣 domain](<📣 Notifier 👥 domain.md>) and pushed to the [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
    |2| The [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) pulls the content of the [Prompt 🤔 ](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) using the identifier.
    |3| The user replies to the [Prompt 🤔 ](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) and the [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) sends the answer to the [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).

    ---
    <br/>


1. **Do Notifier domains store user data?**

    Not for PollyWeb. 
    
    * In PollyWeb, domain orchestration is done by [Broker 🤵 domains](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>), and storage of user data is done by [Vault 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) domains, while a [Notifier 📣 domain's](<📣 Notifier 👥 domain.md>) only responsibility is to proxy [domain messages 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) to and from the [Broker 🤵 domain](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>). 
    
    * This is by design, allowing resilient [Broker 🤵 domain](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) implementations (e.g., AWS, GCP, Azure) to assume the complexity of the undifferentiated PollyWeb protocol, while allowing app start-ups to focus on user experience differentiation. 
    
    * Of course, companies developing [Wallet 🧑‍🦰 apps](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) may wish to support unique features not supported by [Broker 🤵 domain](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>), which may eventually result in the need to store user data on the [Notifier 📣 domain](<📣 Notifier 👥 domain.md>).

    ---
    <br/>



1. **What are the Notifier message methods?**

    The following table lists the main Notifier 📣 message methods (subjects) and their purpose:

    | Message          | Group                |Description|
    |-----------------------|----------------------------|-----------------------------------|
    | [🤵🐌 Frozen](<../📨 Notifier msgs/Chats 💬 Frozen 🤵🐌📣/📣 Frozen 🐌 msg.md>)      | 💬 Chats      | Indicates a chat or wallet has been frozen.                        |
    | [🤵🐌 Open](<../📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)        | 💬 Chats        | Opens a new chat for a wallet.                                     |
    | [🤵🐌 Prompt](<../📨 Notifier msgs/Chats 💬 Prompt 🤵🐌📣/📣 Prompt 🐌 msg.md>)      | 💬 Chats      | Sends a prompt to the wallet for user input.                       |
    | [🤵🐌 Charge](<../📨 Notifier msgs/Payments 💳 Charge 🤵🐌📣/📣 Charge 🐌 msg.md>)      | 💳 Payments    | Requests a payment or charge from the wallet.                      |
    | [🤵🐌 Remove](<../📨 Notifier msgs/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>)      | 🎫 Tokens      | Removes a token or item from the wallet.                           |
    | [🤵🐌 Save](<../📨 Notifier msgs/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)        | 🎫 Tokens        | Saves a new token or credential to the wallet.                     |
    | [🤵🐌 Share](<../📨 Notifier msgs/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)       | 🎫 Tokens       | Shares a token or credential with another domain.                  |
    | [🤵🐌 Onboard](<../📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)     | 🧑‍🦰 Wallets     | Registers (onboards) a new wallet with the Notifier domain.        |
    | [🤵🐌 Updated](<../📨 Notifier msgs/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)     | 🧑‍🦰 Wallets     | Notifies the wallet of an update to its data or state.             |



    ---
    <br/>

1. **How can messages flow in Notifier domains with WebSockets?**

    The following diagram shows the message flow with WebSockets.

    ![alt text](<📣⚙️ Notifier uml.png>)

    ---
    <br/>