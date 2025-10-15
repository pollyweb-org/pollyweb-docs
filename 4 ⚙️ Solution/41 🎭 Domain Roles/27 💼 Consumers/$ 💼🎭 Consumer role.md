💼 Consumer domain role
===

1. **What is a Consumer domain role in NLWeb?**

    Consumers 💼 
    * are [Host 🤗 domains](<../30 🤗 Hosts/$ 🤗🎭 Host role.md>) 
    * that request users to share their data,
    * typically to execute a workflow without the user having to type in the data.

    ---
    <br/>

1. **How do Consumers work?**

    ![](<.📎 Assets/💼 Consumer.png>)

    <!-- 
    TODO: add a table with steps.
    -->

    ---
    <br/>

1. **What kind of user data is supported by Consumers?**

    Consumers 💼 receive data from the following sources:
    - schema-bound datasets shared directly by users' [Vault 🗄️ domains](<../80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>), and
    - downloaded [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) issued by an [Issuer 🎴 domain](<../40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) and stored on the Wallet.

    ---
    <br/>

1. **How do Consumers receive downloaded Tokens?**

    [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) are shared with Consumers 💼 by [Broker 🤵 domains](<../../20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) in a number of ways.

    - **Request on a chat**: 
        - in a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>), [Consumers 💼](<$ 💼🎭 Consumer role.md>) can ask the user to share a specific [Schema Code 🧩](<../../25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>);
        - if the user accepts, the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) shares with the [Consumer 💼](<$ 💼🎭 Consumer role.md>) both the [bound 🔗 Vaults](<../../25 Data/20 🔗 Binds/$ 🔗 Bind.md>) and the downloaded [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) that match that [Schema Code 🧩](<../../25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>);
        - e.g., an airline may ask a user to share their passport [Token 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>).

    - **On chat hello**: 
        - when a [Broker 🤵 domain](<../../20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) initiates a chat session with a [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>), it automatically shares the [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) issued by that [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>) if the [Token's Schema Code 🧩](<../../25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>) is marked as SELF;
        - e.g., booking and ticket [Schema Codes 🧩](<../../25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>) typically allow users to tap on for check-in when arrival at the place of destination, like a restaurant.

    - **When users tap/scan offline Tokens**: 
        - when users tap or scan an offline [Token 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) on a scanner of a [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>) (e.g., a printed flight ticket at an airport gate), the [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>) can validate the [Token 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) without the need for a chat or any interactions with the [user's Broker 🤵 domain](<../../20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>).

    - **When users tap Userables**: 
        - when users tap a [Userable 💍](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) on the scanner of a [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>) (e.g., a wristband at an airport gate), the [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>) can ask the [user's Custodian 🧳 domain](<../../70 🌳 Ambient/71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) to silently share all [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) marked as public by the user and matching a list of expected [Schema Codes 🧩](<../../25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>);
        - see [Userable at gates 💍🎬](<../../70 🌳 Ambient/74 💍 Brand Userables/14 💍🎬 Userable gates.md>) for details.

    ---
    <br/>

1. **Can Consumers use SELF Tokens to tracked domains?**

    Yes. Just like with first-party cookies on Web 2.0 internet. 
    
    - [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) using a [Schema Code 🧩](<../../25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>) marked as SELF are silently shared with [Consumer 💼 domains](<$ 💼🎭 Consumer role.md>), who can then track users;
    - e.g., a luxury holding company with multiple brands may issue a loyalty card for a specific branded stored, then use that card to track the user across all businesses it manages.

    ---
    <br/>

1. **Can Consumers use SELF Tokens to behave like Vaults?**

    Yes, but that may produce a poor user experience.

    - [SELF Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) are silently shared with Consumers who issued them, the same way the [Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) of a user's [Vault 🗄️ domain](<../80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) is shared silently with the corresponding [Vault 🗄️ domain](<../80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) - this allows for developers to choose either a [Consumer 💼](<$ 💼🎭 Consumer role.md>) or [Vault 🗄️](<../80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) role for personalized features. 
    
    - Domain admins should evaluate the impact of one design decision over another when it comes to how the domain's relationship is presented to the user.


    ---
    <br/>
    
1. **How can Consumers validate the data schema when consuming?**

    When consuming data from a [Vault 🗄️ domain](<../80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>), the data envelope indicates the [Schema Code 🧩](<../../25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>) and the version (e.g., `any-authority.com/any-schema:1.0`). 
    
    - The code identifies the [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) where the [Schema Code 🧩](<../../25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>) is defined (e.g., `any-schema` is defined in the [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) of `any-authority.com`), so [Consumer 💼 domains](<$ 💼🎭 Consumer role.md>) can then fetch the schema definitions from a cached [Graph 🕸 domain](<../../45 🛠️ Helper domains/40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) or directly from the [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>).

    ---
    <br/>

1. **How do Consumers verify a Token's signature?**

    When issuing [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>), the [Issuer 🎴 domains](<../40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) sign them with the same key-pair used in their [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) public key. 
    - Other [domains 👥](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) can use the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) key to verify the signature on the [Token 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>).

    ---
    <br/>

1. **Can Consumers verify Tokens when Issuers are offline?**

    Yes. 
    
    - NLWeb advocates for domains to ask [Graph 🕸 domains](<../../45 🛠️ Helper domains/40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) for the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) of the [Issuer 🎴 domain](<../40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) when verifying [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>). 

    ---
    <br/>

1. **Can Consumers verify Tokens when Issuers rotate a DKIM?**

    [Graph 🕸 domains](<../../45 🛠️ Helper domains/40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) will find the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) of the [Issuer 🎴 domain](<../40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) that was in use when the [Token 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) was issued.

    ---
    <br/>

1. **How are Consumers protected when Graph are compromised by attackers?**

    [Firewall 🔥 domains](<../../45 🛠️ Helper domains/21 🔥 Firewalls/$ 🔥🛠️ Firewall helper.md>) monitor the behavior of any [Graph 🕸 domain](<../../45 🛠️ Helper domains/40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) and match domain information with other [Graphs 🕸](<../../45 🛠️ Helper domains/40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>). 
    * If necessary, [Firewall 🔥 domains](<../../45 🛠️ Helper domains/21 🔥 Firewalls/$ 🔥🛠️ Firewall helper.md>) immediately revoke a Graph's [trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>).

    ---
    <br/>

1. **Why aren't all Tokens validated online?**

    In scenarios where physical gates need to allow for large influx of people (e.g., a concert or a subway station), it is quicker to validate the [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) offline at the edge, opening the gate if the [Token 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) seems valid. 
    
    * The [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>) may then perform an asynchronous validation of the [Token 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>), marking it as expired in a local database so that the passage is blocked on the next pass.

    ---
    <br/>

1. **Can Consumers verify if a Token was issued to the holder?**

    Yes. 
    
    - Certain scenarios require the [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>) to verify if the person holding the [Token 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) is the person to whom the [Token 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) was issue to - e.g.:
        - at an airport border control, automatic gates need to match the face of the passport holder with the biometric signature contained in the electronic passport. 
    
    - This requires an online request to an [Identity 🆔 domain](<../../30 🫥 Agents/45 🆔 Identities/01 🆔🫥 Identity agent.md>) that is [bound 🔗](<../../25 Data/20 🔗 Binds/$ 🔗 Bind.md>) to the user and [trusted 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) by the [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>), allowing the token to be matched to the holder without disclosing the holder's identity to the [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>):
        - e.g., while entering a casino, the casino can validate that the 21-years-old token is valid, and that the holder is the owner of the token, without knowing who the holder is. 
    
    - The [Identity 🆔 domain](<../../30 🫥 Agents/45 🆔 Identities/01 🆔🫥 Identity agent.md>) can perform the authentication:
        - on the user's device (e.g., via multi-factor authentication or using the camera in the device), 
        - or through an external device (e.g., [Amazon One 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/07 🖐️ Palm pay landscape/02 📺 Amazon One.md>) palm reader).


    Consider the following [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) as an example. 

    | [Domain](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🎰 Casino   | ℹ️ Request for minimum age. [+]
    | 🆔 [Identity](<../../30 🫥 Agents/45 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Share over 21? [Yes, No]      | > Yes
    | 🆔 [Identity](<../../30 🫥 Agents/45 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.   | [📸 selfie](<../../30 🫥 Agents/45 🆔 Identities/21 🆔😶 Face scan.md>)
    | 🎰 Casino   | ✅ Welcome, please enter!
    


    ---
    <br/>

1. **How do sellers prevent swapping of identity Tokens?**

    [Seller 💵 domains](<../70 💵 Sellers/$ 💵🎭 Seller role.md>) can prevent frauds where users share their [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) with someone else.
    - e.g., an adult may give their wallet's device to an under-aged child so that they can buy age-restricted goods at a self-service store. 
    
    In low-budget validations, 
    - [Seller 💵 domains](<../70 💵 Sellers/$ 💵🎭 Seller role.md>) ask the user's trusted [Identity 🆔 domain](<../../30 🫥 Agents/45 🆔 Identities/01 🆔🫥 Identity agent.md>) to perform the authentication inside the [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) on the user's device;
    - depending on the circumstances, this can be a biometric face scan, voice recognition, OTP, security questions, or other. 
    
    In offline scenarios, 
    - where users carry an NFC card or a printed QR, 
    - the [Seller 💵 domain](<../70 💵 Sellers/$ 💵🎭 Seller role.md>) takes a photo of the user with a fixed camera, and then asks the [Token's Identity 🆔 domain](<../../30 🫥 Agents/45 🆔 Identities/01 🆔🫥 Identity agent.md>) to match the [Token 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) with the picture.

    ---
    <br/>



1. **How are consumers prevented from collecting too much user data?**

    To protect users from [Consumer 💼 domains](<$ 💼🎭 Consumer role.md>) that collect too much Personally Identifiable Information (PII), [Broker 🤵 domains](<../../20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) verify if any [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>) request is explicitly mentioned on their [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>).

    * [Consumer 💼 domains](<$ 💼🎭 Consumer role.md>) must publicly manifest their potential sharing requests in their [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>), in a similar way apps must manifest it when publishing into Apple's App Store or Google Play.
    
    * [Consumer 💼 domains](<$ 💼🎭 Consumer role.md>) manifest the unique contexts in which they will collect data, and what data is collected in each context.
  
    * When interacting in a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>), [Consumer 💼 domains](<$ 💼🎭 Consumer role.md>) need to notify the [Broker 🤵 domain](<../../20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) of a context change before requesting data under that context.

    * [Broker 🤵 domains](<../../20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) only process sharing requests that are publicly manifested in advance.

    * [Broker 🤵 domains](<../../20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) inform users of every context change, identifying the data that may be collected, then block any data request from the Consumer that does not comply with that context - e.g., [Order pizza 🍕](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/21 🏠 Home: Order pizza.md>), [Hotel check-in 🛎️](<../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/03 🏨 Guest @ Reception 🛎️/04 🛎️ Check-in.md>).

    * Because the [domain Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) are public and prone to automatic evaluation by domains like [Firewall 🔥 domains](<../../45 🛠️ Helper domains/21 🔥 Firewalls/$ 🔥🛠️ Firewall helper.md>) and [Reviewer ⭐ domains](<../../30 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer vault.md>), [Consumer 💼 domains](<$ 💼🎭 Consumer role.md>) are exposed to public scrutiny regarding the data  their are collecting, namely: what, why, how, and how much.

    * [Authority 🏛️ domains](<../../45 🛠️ Helper domains/14 🏛️ Authorities/$ 🏛️🛠️ Authority helper.md>) monitor the [domain Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) for dataset requests that don't match the domain's business or exception requests, and if necessary may revoke the [trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) on the [Consumer 💼 domain](<$ 💼🎭 Consumer role.md>).

    * Consider the following example of a [domain Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>).
    
        ```yaml
        Flows:

            check-in-flow: 
                Title: Check-in
                Details: <long optional description>
                Steps:
                - Input: SHARE|nlweb.org/IDENTITY/ID
                    Purpose: your identity 🆔 shares your ID
                - Input: SHARE|nlweb.org/CURATOR/FILTER
                    Purpose: your curator 🧚 sets the room 
                - Input: CHARGE
                    Purpose: your payer 💳 pays the stay
                - Input: ISSUE|any-hotel.com/KEY
                    Purpose: your broker 🤵 saves the room key 
        ```

    
    * That configuration would result in the following [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) excerpt. 

        | [Domain](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
        |-|-|-|
        | 🏨 Hotel  | 😃 Hi! What do you need? <br/> - [ Check-in ] <br/> - [ Something else ] | > Check-in 
        | 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) | 🫥 Ready to check-in? [Yes, No] <br/> - your identity 🆔 shares your ID <br/> - your curator 🧚 sets the room  <br/> - your payer 💳 pays the stay   <br/> - your broker 🤵 saves the room key  | > Yes
        | 🆔 [Identity](<../../30 🫥 Agents/45 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Share identity? [Yes, No] |
        | ... | 



    ---
    <br/>


   
1. **What API methods does a Consumer expose?**

    |  Method | Purpose
    |-|-
    |[🗄️🐌 Consume](<../../../6 🅰️ APIs/30 💼🅰️ Consumer/02 🗄️🐌💼 Consume.md>) | Collect user data from a [Vault 🗄️ domain](<../80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>)
    | [🧑‍🦰🐌 Receive](<../../../6 🅰️ APIs/30 💼🅰️ Consumer/03 🧑‍🦰🐌💼 Receive.md>) | Receive [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) from a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    
    ---
    <br/>

1. **What flows does a Consumer initiate?**
   
    |  Flow | Purpose
    |-|-
    | [⏩🧑‍🦰 Query Vault](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>) | Ask for [Schema Codes 🧩](<../../25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>) in [Vaults 🗄️](<../80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) 
    | [⏩🧑‍🦰 Share Token](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>) | Ask for [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>) in  [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) 
    | [⏩🧑‍🦰 Share ID Token](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/05 🧑‍🦰👉💼 Share Token+ID.md>) | Ask for [Identity 🆔](<../../30 🫥 Agents/45 🆔 Identities/01 🆔🫥 Identity agent.md>) bound [Tokens 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>)
    | [⏩🧑‍🦰 Token status](<05 💼⏩🤵 Token status.md>) | Ask for the status of a [Token 🎫](<../../25 Data/30 🎫 Tokens/$ 🎫 Token.md>)

    ---
    <br/>