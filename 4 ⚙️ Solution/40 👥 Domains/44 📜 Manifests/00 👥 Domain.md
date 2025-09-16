👥 Domains FAQ
===

1. **What is a Domain in NLWeb?**

    In NLWeb, a Domain 👥 is any public web service that:
    * sends and receives domain [Messages 📨](<../41 📨 Comms/01 📨 Domain Message.md>), and;
    * publishes a domain [Manifest 📜](<01 📜 Domain Manifest.md>).


    ---

2. **What API methods does a Domain need to expose?**

    Supported API methods differ based on the number roles assumed by the domain 👥, from none to many.

    ---

3. **What roles can a Domain assume?**

    | Role | Responsibility
    |-|-
    | [🍏 Brand](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>) | Bundles and sells physical smart products (i.e., [Things 💠](<../../70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>)).
    | [💼 Consumer](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) | Consumes data from [Vault 🗄️ domains](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) and  [Issuer 🎴 domains](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>).
    | [🪣 Dataset](<../../20 🧑‍🦰 UI/23 💬 Chats/05 🪣🎭 Dataset role.md>) |
    | [🛠️ Helper](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | Helps other domains 👥 by offloading undifferentiated protocol logic.
    | [🤗 Host](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) | Hosts [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) for [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) via [Broker 🤵 domains](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>).
    | [🪢 Integrator](<../../20 🧑‍🦰 UI/23 💬 Chats/06 🪢🎭 Integrator role.md>) | Exposes custom endpoints in its [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>), to be indexed by [Finder 🔎 domains](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>).
    | [🎴 Issuer](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) | Issues [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to be stored offline in the users' [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    | [🌬️ Streamer](<../41 📨 Comms/02 🌬️🎭 Streamer role.md>) |
    | [🔔 Subscriber](<../41 📨 Comms/04 🔔🎭 Subscriber role.md>) |
    | [🗄️ Vault](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) |
    | [🏭 Supplier](<../../30 🫥 Agents/06 🛎️ Concierges/02 🏭🎭 Supplier role.md>) |
    
    ---