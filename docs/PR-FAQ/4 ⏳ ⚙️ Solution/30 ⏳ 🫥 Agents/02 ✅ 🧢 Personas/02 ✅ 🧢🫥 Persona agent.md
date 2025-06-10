🧢 Persona agent FAQ
===

![](<./00 ✅ 📎 Assets/🧢 Persona.png>)

1. **What is a Persona domain in NLWeb?**

    A Persona 🧢 agent is a [Vault 🗄️](<../../20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>) specialized in user preferences.

    ---

1. **How do Persona vaults differ from Identity vaults?**

    Persona 🧢 vaults are controlled by users, allowing them to define their preferences according to specific circumstances (e.g., a user may have different preferences when traveling for work or on family holidays). 
    
    [Identity 🆔](<../05 ✅ 🆔 Identities/03 ✅ 🆔🫥 Identity agent.md>) vaults are controlled by nations on behalf of their citizens (e.g., the UK), allowing users to legally identity themselves at home and abroad.

    ---

1. **How can users set up a Persona domain?**

    Similar to setting up a [Storage 📦](<../01 ✅ 📦 Storage/01 ✅ 📦🫥 Storage agent.md>) vault.

    ---

1. **Can users leverage their social network instead?**

    Yes. A Persona 🧢 is an NLWeb role that can be implemented by any social network. Thus, once the user's social network onboards to NLWeb as a Persona, users can use it.

    ---

1. **How are Personas kept from selling user data?**

    Personas 🧢 should follow the principle of benevolence - i.e., only collect data for users' benefit, not for users' manipulation.

    - [Brokers 🤵](<../../20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) may revoke their [trust 👍](<../../40 ✅ 👥 Domains/43 ✅ 👍 Trusts/01 ✅ 👍 Domain Trust.md>) in misbehaved Personas who don't comply with this principle.

    ---

1. **How do Personas comply with data residency policies?**

    By leveraging [Storage 📦](<../01 ✅ 📦 Storage/01 ✅ 📦🫥 Storage agent.md>) vaults.

    ---
    
1. **What is the role of Personas in advertising?**

    See [Advertiser 👀](<../10 ⏳ 🔎 Finders/03 ⏳ 👀👥 Advertiser helper.md>) domains.

    ---
    
1. **How to implement a Persona domain on AWS?**

    ![](<./00 ✅ 📎 Assets/🧢 Persona$Vault @AWS.png>)

    Personas rely on the following components for domain [📨 Messaging](<../../40 ✅ 👥 Domains/41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>):
    - 📨 **Inbox**: the combination of the Distributer plus the Endpoint;
    - 📮 **Async Post**: an async message outbound that signs messages.

    Personas also rely on:
    - 📜 **Manifester**: to expose its [Manifest 📜](<../../40 ✅ 👥 Domains/44 ✅ 📜 Manifests/01 ✅ 📜 Domain Manifest.md>); 
    - 🧠 **Ragger**: to enable [RAG GenAI](<01 ✅ 🧠 Ragger feature.md>) inferences on a vector database;
    - 📦 **Storage cache**: to maintain a local cache for [Storage 📦](<../01 ✅ 📦 Storage/01 ✅ 📦🫥 Storage agent.md>) vaults.
    
    ---
    
1. **Should Personas hold medical information?**

    No.
    - Medical information, like allergies, fall under specific data protection and privacy regulations like HIPAA (Health Insurance Portability and Accountability Act - U.S.).
    - Personas 🧢 should leave that responsibility to [Vitalogist 💖](<../09 ⏳ 💖 Vitalogists/01 ⏳ 💖🫥 Vitalogist agent.md>) vaults.

    ---

1. **Should Personas hold credit card information?**

    No.
    - Storing card details required special security settings defined by PCI/DSS policies.
    - Personas 🧢 should leave that responsibility to [Payer 💳](<../04 ✅ 💳 Payers/01 ✅ 💳🫥 Payer agent.md>) vaults.

    ---