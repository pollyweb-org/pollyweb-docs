🎴 Issuer domain role
===

1. **What is an Issuer domain role in NLWeb?**

    A [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) with a [Issuer 🎴 role](<🎴🎭 Issuer role.md>) is any [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) that 
    * issues [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
    * for users to store on their [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).
    
    ---
    <br/>

1. **How do Issuers work?**

    ![](<../../../30 🧩 Data/Tokens 🎫/.📎 Assets/🎫 Issuer.png>)

    | # | Step 
    |-|-
    |1| A user engages in a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with a [Host 🤗 domain](<../../Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) with an [Issuer 🎴 role](<🎴🎭 Issuer role.md>).
    |2| The [Issuer 🎴 domain](<🎴🎭 Issuer role.md>) issues a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) for the user, and the user's [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) asks the user to confirm if they want to save the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) offline in the [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

    ---
    <br/>
    

1. **What does the [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) look like?**

    Consider the following [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) excerpt from the [Buy Theater Tickets 🤝 use case](<../../../../3 🤝 Use Cases/10 🍿 Entertainment/Go to Theaters 🎭/10 Guest @ Anywhere/12 Buy tickets.md>).
    
    
    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    |...
    | 🎭 Venue   | 😃 Want a ticket? [Yes, No] | > Yes
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 Save theatre ticket? [Yes, No] <br/> - self booking Token 🎫 <br/> - issued by Any Venue 🎭 <br/> - expiring 7:30pm today <br/> - play: the funny ones | > Yes
    | 🎭 Venue   | ✅ You're all set, get in!
        

    ---
    <br/>


1. **How much data should Issuers add to a Token?**

    The less data, the better. 

    * [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) are signed but not encrypted - thus, all data in a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) can be read by an attacker. 
    
    * When sharing a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>), users implicitly allow domains to contact the [Issuer 🎴 domain](<🎴🎭 Issuer role.md>) for additional data about the Token - domains can leverage this direct channel to do an online verification, synchronously or asynchronously.

    ---
    <br/>
    
1. **Can an Issuer domain suspend or revoke a Token?**

    Yes. 

    * [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) are issued with the help of a [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) that orchestrates the relationship between the [Issuer 🎴 domain](<🎴🎭 Issuer role.md>) and the user. 
    
    * [Issuer 🎴 domains](<🎴🎭 Issuer role.md>) track to what [Broker 🤵 domains](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) where their [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) issue to, so that they can request the same [Broker 🤵 domains](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) to suspend or revoke the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).
  
    * [Broker 🤵 domains](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) will handle the revocation propagation up to the user's [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

    * [Broker 🤵 domains](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) only share active [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) when [Consumer 💼 domains](<../../../50 🫥 Agent domains/Storage 🗃️/🗃️🫥 Storage agent.md>) ask for them in a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

    ---
    <br/>    
    
1. **What if the user presents a QR Token printed on paper?**

    In cases where the user is holding an offline image of the Token's QR (e.g., printed or screenshot), [Consumer 💼 domains](<../../Consumers 💼/💼🎭 Consumer role.md>) may ask for a synchronous status check of the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) directly with the [user's Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>);
    
    - e.g., while validating a printed QR of a [passport Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) at the airport border control, the [Consumer 💼 domain](<../../Consumers 💼/💼🎭 Consumer role.md>) of the airport may try to reach the [user's Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) to verify if the passport hasn't been suspended or revoked.

    The airport knows what [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) to reach out to, 
    * because the printed QR version of a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) does not contain the Token's content;
    * instead, the QR presented by [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) contain only a [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) with the ID of the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) and the [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) that holds the content and the status of the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).

    ---
    <br/>


1. **Why not check revocation directly with Issuers?**

    Given that [Issuer 🎴 domains](<🎴🎭 Issuer role.md>) are the ones revoking [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) it intuitively makes sense for [Consumer 💼 domains](<../../../50 🫥 Agent domains/Storage 🗃️/🗃️🫥 Storage agent.md>) to ask them directly for the status of a given printed [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>), instead of asking the [user's Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>).

    * However, that approach raises concerns with privacy and availability.
        
    On privacy:
    
    * Given the ability of a recipient [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) to know who sent a given [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) (e.g., a status request from a [Consumer 💼 domain](<../../../50 🫥 Agent domains/Storage 🗃️/🗃️🫥 Storage agent.md>)), an [Issuer 🎴 domain](<🎴🎭 Issuer role.md>) would be able to track when and where a given [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) was used by the user to whom it was issued to.
    
    * For example, a private company could track the shopping behavior of their named customers without their consent, and a nation's government could track the movement of targeted political opponents.
    
    * In [W3C Verifiable Credentials (VCs)](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>), this is an anti-pattern often called "phone-home check", "issuer call-back verification", or "online status checking" — the W3C recommendation is for VC implementers to adopt the bitmap-like Status List 2021 approach published by the W3C CCG (Credentials Community Group).

    * NLWeb avoids bitmap status lists because of their scaling limitations and their overhead on the businesses that own [Issuer 🎴 domains](<🎴🎭 Issuer role.md>).
    
    * Instead, in NLWeb, [Broker 🤵 domains](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) protect the privacy of users by answering the online [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) status queries by [Consumer 💼 domains](<../../../50 🫥 Agent domains/Storage 🗃️/🗃️🫥 Storage agent.md>), based on the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) status update events sent asynchronously by [Issuer 🎴 domains](<🎴🎭 Issuer role.md>).
    
    * Furthermore, because [Broker 🤵 domains](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) simplify the process by only sharing active [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) when [Consumer 💼 domains](<../../../50 🫥 Agent domains/Storage 🗃️/🗃️🫥 Storage agent.md>) send sharing requests in a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>), this allows [Consumer 💼 domains](<../../../50 🫥 Agent domains/Storage 🗃️/🗃️🫥 Storage agent.md>) to only need to verify the status of [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) presented in an offline fashion (e.g., a printed QR on a paper).

    On availability: 

    * Consider the scenario of a [passport Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) that needs to be usable even if the [Issuer 🎴 domain](<🎴🎭 Issuer role.md>) of the issuing nation has its services offline due to an ongoing war.
    
    * Consider also a scenario where a commercial flight cannot wait for the [Issuer 🎴 domain](<🎴🎭 Issuer role.md>) of a travel agency to come back online before allowing a traveler to board a plane with a [ticket Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>). 
    
    * [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) are expected to have the required level of high availability and low latency, while having to pass the protocol compliancy requirements of NLWeb before being trusted by the [domain Manifest 📜](<../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) of the NLWeb Organization.


    ---
    <br/>