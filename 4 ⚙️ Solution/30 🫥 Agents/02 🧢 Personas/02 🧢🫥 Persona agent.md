🧢 Persona vault domain
===


1. **What is a Persona in NLWeb?**

    A [Persona 🧢 domain](<02 🧢🫥 Persona agent.md>) is an [Agent 🫥 vault](<../../25 Data/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) specialized in user preferences.

    ---
    <br/>

1. **What other domains do Personas need?**

    |Domain|Purpose
    |-|-
    | [📦 Storage](<../01 📦 Storage/01 📦🫥 Storage agent.md>) | To comply with data residency.

    ---
    <br/>

1. **What domain roles do Personas implement?**

    | Role | Purpose
    |-|-
    | [🗄️ Vault](<../../25 Data/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | For sharing user data with [Consumer 💼 domains](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>).
    | [🤗 Host](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | For managing [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) with users.
    | [🫥 Agent ](<../../25 Data/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | To participate in [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) from other [Host 🤗 domains](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>).
    | [🌬️ Streamer](<../../40 👥 Domains/42 🌬️ Streams/02 🌬️🎭 Streamer role.md>) | For streaming events to [Subscriber 🔔 domains](<../../40 👥 Domains/42 🌬️ Streams/04 🔔🎭 Subscriber role.md>).

    ---
    <br/>

1. **What domains subscribe to Persona events?**

    | Domain | Purpose
    |-|-
    | [🛎️ Concierge](<../06 🛎️ Concierges/01 🛎️🫥 Concierge agent.md>) | Subscribes to delivery and contact changes.
    | [🧚 Curator](<../03 🧚 Curators/01 🧚🫥 Curator agent.md>) | subscribes to multiple types of user preferences.
    | [📇 Mingler](<../08 📇 Minglers/01 📇🫥 Mingler agent.md>) | Subscribes to contact preferences.

    ---
    <br/>

1. **How do Persona agents work?**

    ![](<00 📎 Assets/🧢 Persona.png>)

    ---
    <br/>

1. **How do Persona vaults differ from Identity vaults?**

    [Persona 🧢 vaults](<02 🧢🫥 Persona agent.md>) are controlled by users, allowing them to define their preferences according to specific circumstances (e.g., a user may have different preferences when traveling for work or on family holidays). 
    
    - Conversely, [Identity 🆔 vaults](<../05 🆔 Identities/01 🆔🫥 Identity agent.md>)  are controlled by nations on behalf of their citizens (e.g., the UK), allowing users to legally identity themselves at home and abroad.


    ---
    <br/>

1. **Can users leverage their social network instead?**

    Yes. A [Persona 🧢](<02 🧢🫥 Persona agent.md>) is an NLWeb role that can be implemented by any social network. Thus, once the user's social network onboards to NLWeb as a Persona, users can use it.

    ---
    <br/>

1. **How are Personas kept from selling user data?**

    Personas 🧢 should follow the principle of benevolence - i.e., only collect data for users' benefit, not for users' manipulation.

    - [Brokers 🤵](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) may revoke their [trust 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) in misbehaved Personas who don't comply with this principle.

    ---
    <br/>

1. **How do Personas comply with data residency policies?**

    By leveraging [Storage 📦](<../01 📦 Storage/01 📦🫥 Storage agent.md>) vaults.

    ---
    <br/>
    
1. **What is the role of Personas in advertising?**

    See [Advertiser 👀](<../10 🔎 Finders/03 👀👥 Advertiser helper.md>) domains.

    ---
    <br/>
    
1. **Should Personas hold medical information?**

    No.
    - Medical information, like allergies, fall under specific data protection and privacy regulations like HIPAA (Health Insurance Portability and Accountability Act - U.S.).
    - Personas 🧢 should leave that responsibility to [Vitalogist 💖](<../09 💖 Vitalogists/01 💖🫥 Vitalogist agent.md>) vaults.

    ---
    <br/>

1. **Should Personas hold credit card information?**

    No.
    - Storing card details required special security settings defined by PCI/DSS policies.
    - Personas 🧢 should leave that responsibility to [Payer 💳](<../04 💳 Payers/03 💳🎭 Payer role.md>) vaults.

    ---
    <br/>