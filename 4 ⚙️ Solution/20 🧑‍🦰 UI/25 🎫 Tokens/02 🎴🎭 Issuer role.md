🎴 Issuer domain role FAQ
===

1. **What is an Issuer domain role in NLWeb?**

    A [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) with a [Issuer 🎴 role](<02 🎴🎭 Issuer role.md>) is any [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) that 
    * issues [Tokens 🎫](<01 🎫 Token.md>)
    * for users to store on their [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    
    ---
    <br/>

1. **How do Issuers work?**

    ![](<.📎 Assets/🎫 Issuer.png>)

    | # | Step 
    |-|-
    |1| A user engages in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) with a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) with an [Issuer 🎴 role](<02 🎴🎭 Issuer role.md>).
    |2| The [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) issues a [Token 🎫](<01 🎫 Token.md>) for the user, and the user's [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) asks the user to confirm if they want to save the [Token 🎫](<01 🎫 Token.md>) offline in the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    <br/>
    

1. **What does the [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) look like?**

    Consider the following [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) excerpt from the [Buy Theater Tickets 🤝 use case](<../../../3 🤝 Use Cases/10 🍿 Entertainment/Go to Theaters 🎭/10 Guest @ Anywhere/12 Buy tickets.md>).
    
    
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/50 🤔 Prompts/1 📘 Prompt specs/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    |...
    | 🎭 Venue   | 😃 Want a ticket? [Yes, No] | > Yes
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save theatre ticket? [Yes, No] <br/> - self booking Token 🎫 <br/> - issued by Any Venue 🎭 <br/> - expiring 7:30pm today <br/> - play: the funny ones | > Yes
    | 🎭 Venue   | ✅ You're all set, get in!
        

    ---
    <br/>


1. **How much data should Issuers add to a Token?**

    The less data, the better. 

    * [Tokens 🎫](<01 🎫 Token.md>) are signed but not encrypted - thus, all data in a [Token 🎫](<01 🎫 Token.md>) can be read by an attacker. 
    
    * When sharing a [Token 🎫](<01 🎫 Token.md>), users implicitly allow domains to contact the [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) for additional data about the Token - domains can leverage this direct channel to do an online verification, synchronously or asynchronously.

    ---
    <br/>
    
1. **Can an Issuer domain suspend or revoke a Token?**

    Yes. 

    * [Tokens 🎫](<01 🎫 Token.md>) are issued with the help of a [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) that orchestrates the relationship between the [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) and the user. 
    
    * [Issuer 🎴 domains](<02 🎴🎭 Issuer role.md>) track to what [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) where their [Tokens 🎫](<01 🎫 Token.md>) issue to, so that they can request the same [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) to suspend or revoke the [Token 🎫](<01 🎫 Token.md>).
  
    * [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) will handle the revocation propagation up to the user's [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    * [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) only share active [Tokens 🎫](<01 🎫 Token.md>) when [Consumer 💼 domains](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) ask for them in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>).

    ---
    <br/>    
    
1. **What if the user presents a QR Token printed on paper?**

    In cases where the user is holding an offline image of the Token's QR (e.g., printed or screenshot), [Consumer 💼 domains](<../27 💼 Consumers/04 💼🎭 Consumer role.md>) may ask for a synchronous status check of the [Token 🎫](<01 🎫 Token.md>) directly with the [user's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>);
    
    - e.g., while validating a printed QR of a [passport Token 🎫](<01 🎫 Token.md>) at the airport border control, the [Consumer 💼 domain](<../27 💼 Consumers/04 💼🎭 Consumer role.md>) of the airport may try to reach the [user's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) to verify if the passport hasn't been suspended or revoked.

    The airport knows what [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) to reach out to, 
    * because the printed QR version of a [Token 🎫](<01 🎫 Token.md>) does not contain the Token's content;
    * instead, the QR presented by [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) contain only a [Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>) with the ID of the [Token 🎫](<01 🎫 Token.md>) and the [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) that holds the content and the status of the [Token 🎫](<01 🎫 Token.md>).

    ---
    <br/>


1. **Why not check revocation directly with Issuers?**

    Given that [Issuer 🎴 domains](<02 🎴🎭 Issuer role.md>) are the ones revoking [Tokens 🎫](<01 🎫 Token.md>) it intuitively makes sense for [Consumer 💼 domains](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) to ask them directly for the status of a given printed [Token 🎫](<01 🎫 Token.md>), instead of asking the [user's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>).

    * However, that approach raises concerns with privacy and availability.
        
    On privacy:
    
    * Given the ability of a recipient [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) to know who sent a given [Message 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) (e.g., a status request from a [Consumer 💼 domain](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>)), an [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) would be able to track when and where a given [Token 🎫](<01 🎫 Token.md>) was used by the user to whom it was issued to.
    
    * For example, a private company could track the shopping behavior of their named customers without their consent, and a nation's government could track the movement of targeted political opponents.
    
    * In [W3C Verifiable Credentials (VCs)](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>), this is an anti-pattern often called "phone-home check", "issuer call-back verification", or "online status checking" — the W3C recommendation is for VC implementers to adopt the bitmap-like Status List 2021 approach published by the W3C CCG (Credentials Community Group).

    * NLWeb avoids bitmap status lists because of their scaling limitations and their overhead on the businesses that own [Issuer 🎴 domains](<02 🎴🎭 Issuer role.md>).
    
    * Instead, in NLWeb, [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) protect the privacy of users by answering the online [Token 🎫](<01 🎫 Token.md>) status queries by [Consumer 💼 domains](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>), based on the [Token 🎫](<01 🎫 Token.md>) status update events sent asynchronously by [Issuer 🎴 domains](<02 🎴🎭 Issuer role.md>).
    
    * Furthermore, because [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) simplify the process by only sharing active [Tokens 🎫](<01 🎫 Token.md>) when [Consumer 💼 domains](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) send sharing requests in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>), this allows [Consumer 💼 domains](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) to only need to verify the status of [Tokens 🎫](<01 🎫 Token.md>) presented in an offline fashion (e.g., a printed QR on a paper).

    On availability: 

    * Consider the scenario of a [passport Token 🎫](<01 🎫 Token.md>) that needs to be usable even if the [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) of the issuing nation has its services offline due to an ongoing war.
    
    * Consider also a scenario where a commercial flight cannot wait for the [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) of a travel agency to come back online before allowing a traveler to board a plane with a [ticket Token 🎫](<01 🎫 Token.md>). 
    
    * [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) are expected to have the required level of high availability and low latency, while having to pass the protocol compliancy requirements of NLWeb before being trusted by the [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) of the NLWeb Organization.


    ---
    <br/>