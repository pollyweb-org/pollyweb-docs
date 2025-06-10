🤗 Host domain role FAQ
===

![](<📎 Assets/💬 Host.png>)

1. **What is a Host domain role in NLWeb?**

    A domain with a Host 🤗 role is a [Domain 👥](<../../40 ✅ 👥 Domains/44 ✅ 📜 Manifests/00 ✅ 👥 Domain.md>) that [chats 💬](<01 ✅ 💬 Chat.md>) with [Wallets 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) via [Brokers 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>). 

    ---

1. **How are users protected from stalking from Hosts?**

    NLWeb sees [chats 💬](<01 ✅ 💬 Chat.md>) as temporary sessions, always initiated by users; 
    - i.e., the Host receives a temporary ID while the [chat 💬](<01 ✅ 💬 Chat.md>) session is open, but no other ID to track the user across sessions;
    - although Hosts 🤗 can proactively send messages on an open [chat 💬](<01 ✅ 💬 Chat.md>) session, users can close the session at any time. 

    ---

1. **What incentives do Hosts have to close sessions?**

    [Advertising 👀](<../../../2 ✅ 🏔️ Landscape/1 ✅ 💼 Business landscape/04 ✅ 👀 Advertising landscape/00 ✅ 👀 Advertising index.md>) is triggered at the end of a session for next-best actions.
    - This, hosts willing to monetize via cross-domain advertising are incentivized to close sessions. 
    - See [Advertiser 👀](<../../30 ⏳ 🫥 Agents/10 ⏳ 🔎 Finders/03 ⏳ 👀👥 Advertiser helper.md>) for details.

    ---

1. **Do Hosts send messages to users via web sockets?**

    No. 
    - Hosts send [Messages 📨](<../../40 ✅ 👥 Domains/41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>) via HTTPS POST to a proxy [Broker 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) that then communicate with the user's [Wallet 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) with real-time protocols (e.g., web sockets, MQTT). 

    ---

1. **What proxy services are involved in the flow?**

    [Messages 📨](<../../40 ✅ 👥 Domains/41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>) from hosts first reach a [Broker 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) via HTTPS POST:
    - this service is responsible for orchestrating chats between users and hosts using the NLWeb protocol, 
    - and is typically implemented by a main cloud provider. 
    
    The [Broker 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) then sends the message to a [Notifier 📣](<../02 ✅ 📣 Notifiers/02 ✅ 📣 Notifier domain.md>), also via HTTPS POST:
    - this service is responsible for pushing the message to the [Wallet 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) via whatever real-time mechanisms the Wallet supports (e.g., web sockets, MQTT), 
    - so typically is implemented by the same team that implemented the Wallet.

    ---


1. **Are chat prompt messages encrypted from Hosts to Wallets?**

    Not applicable - Host 🤗 don't send [Messages 📨](<../../40 ✅ 👥 Domains/41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>) to [Wallets 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>). 

    * Hosts 🤗 only send unencrypted asynchronous intents to the Wallet's [Broker 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>), who then sends it to the Wallet's [Notifier 📣](<../02 ✅ 📣 Notifiers/02 ✅ 📣 Notifier domain.md>). 

    * When the [Wallet 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) app receives the intent from the [Notifier 📣](<../02 ✅ 📣 Notifiers/02 ✅ 📣 Notifier domain.md>), it pulls the unencrypted message content directly from the Host 🤗 with a synchronous HTTPS call. 

    * This keeps the [Broker 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) and the [Notifier 📣](<../02 ✅ 📣 Notifiers/02 ✅ 📣 Notifier domain.md>) in dark regarding the content of [Message 📨](<../../40 ✅ 👥 Domains/41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>) (even in the event of a cryptography attack) because no content actually passes by these proxy services.

    ---


1. **Are chat reply messages encrypted from Wallets to Hosts?**

    Yes. 
    - Although the user's [Messages 📨](<../../40 ✅ 👥 Domains/41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>) content is not encrypted, it is sent over HTTPS POST directly from the [Wallet 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) to the Host 🤗.
    - The HTTPS channel ensures the message is encrypted between the [Wallet 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) and the Host 🤗. 
    - NLWeb relies on the HTTPS ability to continue to evolve has [post-quantum 📺](<../../../2 ✅ 🏔️ Landscape/2 ✅ 🧑‍🦰 User landscape/08 ✅ 🔐 Passwordless ID landscape/10 ✅ 📺 Post-quantum keys.md>) cryptography attacks become more sophisticated.

    ---