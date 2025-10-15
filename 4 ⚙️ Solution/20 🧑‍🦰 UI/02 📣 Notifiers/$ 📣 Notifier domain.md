📣 Notifier domains
===



1. **What is a Notifier domain in NLWeb?**

    A [Notifier 📣](<$ 📣 Notifier domain.md>) is any backend-for-frontend (BFF) [domain 👥](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) that acts as a proxy for a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>). 
    
    * This allows [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) to communicate in standard HTTPS with the [Notifier 📣 domain](<$ 📣 Notifier domain.md>), while the [Notifier 📣 domain](<$ 📣 Notifier domain.md>) communicates via mobile-friendly real-time protocols with the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) (e.g., MQTT, web sockets, mobile notifications). 
    
    * Because of this tight integration between pairs of [Notifier 📣 domains](<$ 📣 Notifier domain.md>) and [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>), NLWeb advocates for each pair to be built and managed by the same team.

    ---
    <br/>

1. **How do Notifier domains work?**
    
    ![](<.📎 Assets/📣 Notifier.png>)

    |#|Step
    |-|-
    |1| A [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) sends a [Prompt 🤔 ](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) identifier to a [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) in the context of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>), which is then proxied through the [Notifier 📣 domain](<$ 📣 Notifier domain.md>) and pushed to the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>).
    |2| The [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) pulls the content of the [Prompt 🤔 ](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) using the identifier.
    |3| The user replies to the [Prompt 🤔 ](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) and the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) sends the answer to the [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>).

    ---
    <br/>


1. **Do Notifier domains store user data?**

    Not for NLWeb. 
    
    * In NLWeb, domain orchestration is done by [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>), and storage of user data is done by [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) domains, while a [Notifier 📣 domain's](<$ 📣 Notifier domain.md>) only responsibility is to proxy [domain messages 📨](<../../40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>) to and from the [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>). 
    
    * This is by design, allowing resilient [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) implementations (e.g., AWS, GCP, Azure) to assume the complexity of the undifferentiated NLWeb protocol, while allowing app start-ups to focus on user experience differentiation. 
    
    * Of course, companies developing [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) may wish to support unique features not supported by [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>), which may eventually result in the need to store user data on the [Notifier 📣 domain](<$ 📣 Notifier domain.md>).

    ---
    <br/>

1. **How can messages flow in Notifier domains with WebSockets?**

    The following diagram shows the message flow with WebSockets.

    ![alt text](<.📎 Assets/📣 Notifier UML.png>)

    ---
