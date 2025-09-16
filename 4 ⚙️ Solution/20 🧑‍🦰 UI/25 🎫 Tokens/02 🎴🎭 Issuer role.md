🎴 Issuer domain role FAQ
===

1. **What is an Issuer domain role in NLWeb?**

    A [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) with a [Issuer 🎴 role](<02 🎴🎭 Issuer role.md>) is any [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) that 
    * issues [Tokens 🎫](<01 🎫 Token.md>)
    * for users to store on their [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    
    ---
    <br/>

2. **How do Issuers work?**

    ![](<.📎 Assets/🎫 Issuer.png>)

    | # | Step 
    |-|-
    |1| A user engages in a [Chat 💬](<../23 💬 Chats/01 💬 Chat.md>) with a [Host 🤗 domain](<../23 💬 Chats/03 🤗🎭 Host role.md>) with an [Issuer 🎴 role](<02 🎴🎭 Issuer role.md>).
    |2| The [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) issues a [Token 🎫](<01 🎫 Token.md>) for the user, and the user's [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) asks the user to confirm if they want to save the [Token 🎫](<01 🎫 Token.md>) offline in the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    <br/>
    

1. **What does the Chat look like?**

    Consider the following [Chat 💬](<../23 💬 Chats/01 💬 Chat.md>) excerpt from the [Buy Theater Tickets 🤝 use case](<../../../3 🤝 Use Cases/10 🍿 Entertainment/Go to Theaters 🎭/10 Guest @ Anywhere/12 Buy tickets.md>).
    
    
    | Service | Prompt | User
    | - | - | - |
    |...
    | 🎭 Venue   | 😃 Want to watch the play? [Yes, No] | > Yes
    | 💳 [Payer](<../../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $25.00 bill? 🧾 [No] <br/>- [ card ABC ] <br/>- [ card DEF ] | > card ABC
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save theatre ticket? [Yes, No]  | > Yes
    | 🎭 Venue   | ✅ You're all set, get in!
        

    ---
    <br/>


2. **How much data should Issuers add to a Token?**

    The less data, the better. 

    * [Tokens 🎫](<01 🎫 Token.md>) are signed but not encrypted - thus, all data in a [Token 🎫](<01 🎫 Token.md>) can be read by an attacker. 
    
    * When sharing a [Token 🎫](<01 🎫 Token.md>), users implicitly allow domains to contact the [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) for additional data about the Token - domains can leverage this direct channel to do an online verification, synchronously or asynchronously.

    ---
    <br/>
    
3. **Can an Issuer revoke a Token?**

    Yes. 

    * [Tokens 🎫](<01 🎫 Token.md>) are issued with the help of a [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) that orchestrates the relationship between the [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) and the user. 
    
    * [Issuer 🎴 domains](<02 🎴🎭 Issuer role.md>) can request the [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) to invalidate [Tokens 🎫](<01 🎫 Token.md>), and [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) will handle the propagation up to the user's [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    
    * In cases where the user is holding an offline image of the Token's QR (e.g., printed or screenshot), [Consumer 💼 domains](<../27 💼 Consumers/04 💼🎭 Consumer role.md>) may ask for a synchronous status check of the [Token 🎫](<01 🎫 Token.md>) directly with the [user's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>);
       - e.g., while validating a passport [Token 🎫](<01 🎫 Token.md>) at the border, the airport may try to reach the [user's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) to verify if the passport hasn't been revoked.

    ---
    <br/>


5. **Can users be tracked by Issuers?**

    In certain scenarios, [Consumer 💼 domains](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) may want to verify if a [Token 🎫](<01 🎫 Token.md>) has been revoked  [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) 
    * [Tokens 🎫](<01 🎫 Token.md>) are a great fit for situations where users need to be validated even when the [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) is offline;
        - e.g., a passport [Token 🎫](<01 🎫 Token.md>) needs to be usable even if the issuing nation has its services offline due to a war;
        - e.g., commercial flights cannot wait for travel agencies to come back online before allowing a traveler to board a plane with a ticket [Token 🎫](<01 🎫 Token.md>). 


    ---
    <br/>