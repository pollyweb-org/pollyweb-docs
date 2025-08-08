🗄️ Vault domain role FAQ
===

![](<.📎 Assets/🗄️ Vault.png>)

1. **What is a Vault domain role in NLWeb?**

    Vaults are [Hosts 🤗](<../23 💬 Chats/03 🤗🎭 Host role.md>) that manage user data (e.g., banks, health services, governments). 

    ---

1. **Can users ask Vaults to share data with other Hosts?**

    Yes. 
    - Upon a share request from another Host during a chat, users can authorize their Vaults to disclose a data set with that Host. 
    - This requires both Vault and Host to [trust 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) one another for the [Schema Code 🧩](<02 🧩 Schema Code.md>) of the dataset to be shared.

    ---

1. **Can users ask Vaults to download data to the device?**

    No. That is covered by the [Issuer 🎴](<../27 🎫 Tokens/02 🎴🎭 Issuer role.md>) domain role. 

    ---

1. **How can Vaults comply with data residency?**

    Vaults can ask users to share their [Storage 📦](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) domain, then store the user data on the Storage domain.

    ---

1. **Do users have private vaults, like the Solid Project?**

    No. 
    * Unlike the [Solid Project 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/05 📺 Berners-Lee vaults.md>), by Sir Tim Berners-Lee, NLWeb users don't have a private repository (a.k.a. Vault) for all their data, so they don't effectively own their data. 
    * Instead, a user's data is scattered across a number of vaults managed by different providers who decide how much of the user's data is accessible and by whom.
    * This is a better representation of reality as we know it (e.g., a person's bank history is with banks, and location history is with Google Maps).

    ---

1. **How about a central place for user preferences?**

    Exceptionally, NLWeb advocates for the use of [Persona 🧢](<../../30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) vaults aimed for preference-based personalization 
    - e.g., nicknames, seat preferences, film genres;
    - but, even here, users rent storage on Persona vaults as a service that is owned and managed by a company.

    ---

1. **How is data residency solved by vaults?**

    Where nations require their citizens' data to be stored within nation's borders, vaults can leverage the user's [📦 Storage vault 📦](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) to store their data. 
    
    - [Storage vaults 📦](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) are multi-tenant cloud repositories rented by users, where users can allow bound vaults to write their data into. 
    
    - The [Storage vault 📦](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) will comply with the user's [data-residency 🏔️](<../../../2 🏔️ Landscape/1 💼 Business landscape/02 🏳️ Sovereignty landscape/00 🏳️ Sovereignty index.md>) requirements by choosing in which region to store the user's data. 
    
    - This solution also allows for free services to offload the cost of storage to the user.

    ---

1. **What if the user only wants to have one Vault?**

    A user may wish to [bind 🔗](<01 🔗 Bind.md>) to a single Vault that is able to implement all the [Schema Codes 🧩](<02 🧩 Schema Code.md>) the user is interested in sharing, and is able to establish trust relationships with all the domains the user is interested in interacting with. 
    - However, this solution doesn't seem scalable, if at all realistic.

    ---

1. **How are users protected from tracking by Vault consortiums?**

    User tracking is typically done by a consortium of domains crossing information about a user's interaction with each one of them, allowing them to reconstruct the user's journey. 
    
    - To avoid this, each Vault domain is bounded to a wallet using a unique key-pair, so that there are no common properties between two Vault [binds 🔗](<01 🔗 Bind.md>) of the same user, thus no way to cross the Vault interactions.

    ---

1. **How are users protected from stalking from vaults?**

    Vaults are hosts that store user data. When a user [binds 🔗](<01 🔗 Bind.md>) to a [Host 🤗](<../23 💬 Chats/03 🤗🎭 Host role.md>), the [Wallet 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) passes a unique [bind 🔗](<01 🔗 Bind.md>) ID to the Host to be able to identify the user across sessions, turning the Host into a Vault.
    
    - While the Vault is now able to track the user across sessions, it cannot track the user across hosts because the [bind 🔗](<01 🔗 Bind.md>) ID is unique for the relationship between that user and that Host.

    ---

1. **How do Vaults protect user data from Consumers?**

    [Consumer 💼](<../25 💼 Consumers/04 💼🎭 Consumer role.md>) domains can't request user data directly to vaults domains. 
    
    * Instead, [Consumers 💼](<../25 💼 Consumers/04 💼🎭 Consumer role.md>) request such data directly to the user. 

    * When prompted, the user selects the preferred Vault to answer the Consumer's request, then signs and sends a disclose request to the selected Vault, asking it to disclose the requested data to the Consumer. 
    
    * At that point, the Vault may ask the user for additional data (e.g., which credit card to use on a payment) or perform additional validations (e.g., a one-time-password via SMS to approve a bank transfer). 
    
    * Finally, the Vault sends the data directly to the consumer domain who requested it.

    ---
    
1. **How can users do selective disclosure?**

    [Selective disclosure 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/07 📺 SSI selective disclosure.md>) (i.e., the ability for a user to select which fields to disclose from a given schema code) is not allowed by design on NLWeb. 
    
    * Instead, NLWeb advocates for purpose-driven datasets that are self-contained and requested under the principle of least-privilege, e.g.:
        - a hotel should not ask for all passport fields for a check-in; 
        - instead, it should ask only for required booking data like first/last name, check-in/out dates, and PNR.

    ---