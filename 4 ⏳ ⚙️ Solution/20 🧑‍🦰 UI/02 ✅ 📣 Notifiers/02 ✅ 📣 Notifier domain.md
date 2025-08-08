📣 Notifier domains FAQ
===

![](<./📎 Assets/📣 Notifier.png>)

1. **What is a Notifier domain in NLWeb?**

    A Notifier is a backend-for-frontend (BFF) domain that acts as a proxy for a [Wallet 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>). 
    
    * This allows other domains to communicate in standard HTTPS with the Notifier 📣, while the Notifier 📣 communicates via mobile-friendly real-time protocols with the [Wallet 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) (e.g., MQTT, web sockets, mobile notifications). 
    
    * Because of this tight integration between Notifiers 📣 and [Wallets 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>), NLWeb advocates for them to be built and managed by the same team.

    ---

1. **Do Notifiers store user data?**

    Not for NLWeb. 
    
    * In NLWeb, domain orchestration is done by [Broker 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) domains, and storage of user data is done by [Vault 🗄️](<../24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>) domains, while a Notifier's 📣 only responsibility is to proxy messages to and from the [Broker 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>). 
    
    * This is by design, allowing resilient [Broker 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) implementations (e.g., AWS, GCP, Azure) to assume the complexity of the undifferentiated NLWeb protocol, while allowing app start-ups to focus on user experience differentiation. 
    
    * Of course, companies developing [Wallets](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) may wish to support unique features not supported by [Broker 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>), which may eventually result in the need to store user data on the Notifier 📣.

    ---

1. **How can messages flow in Notifiers with WebSockets?**

    ![alt text](<./📎 Assets/📣 Notifier UML.png>)

    ---

1. **How to implement a Notifier on AWS?**

    ![](<./📎 Assets/📣 Notifier@AWS.png>)

    Notifiers rely on the following components for domain [📨 Messaging](<../../40 ✅ 👥 Domains/41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>):
    - 📨 **Inbox**: the combination of the Distributer plus the Endpoint;
    - 🚀 **Sync Call**: a synchronous request outbound that signed requests;
    - 📮 **Async Post**: an async message outbound that signs messages.

    This solution requires a 📜 **Manifester** to expose its [Manifest 📜](<../../40 ✅ 👥 Domains/44 ✅ 📜 Manifests/01 ✅ 📜 Domain Manifest.md>).

    ---
