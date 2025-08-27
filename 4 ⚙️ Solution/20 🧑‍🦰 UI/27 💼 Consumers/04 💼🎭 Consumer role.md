💼 Consumer domain role FAQ
===

![](<../24 🗄️ Vaults/.📎 Assets/🗄️ Consumer.png>)

1. **What is a Consumer domain role in NLWeb?**

    Consumers 💼 are [Hosts 🤗](<../23 💬 Chats/03 🤗🎭 Host role.md>) that request users to share their data, typically to execute a workflow without the user having to type in the data.

    ---

1. **What kind of user data is supported by Consumers?**

    Consumers 💼 receive data from the following sources:
    - schema-bound datasets shared directly by users' [Vaults 🗄️](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>), and
    - downloaded [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) issued by an [Issuer 🎴](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>) and stored on the Wallet.

    ---

1. **How do Consumers receive downloaded Tokens?**

    Tokens are shared with Consumers 💼 by [Brokers 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) in a number of ways.

    - **Request on a chat**: 
        - in a chat, Consumers can ask the user to share a specific [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>);
        - if the user accepts, the Wallet shares with the Consumer both the bound [Vaults 🗄️](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) and the downloaded [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) that match that [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>);
        - e.g., an airline may ask a user to share their passport Token.

    - **On chat hello**: 
        - when a [Broker 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) initiates a chat session with a Consumer, it automatically shares the [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) issued by that Consumer if the Token's [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) is marked as SELF;
        - e.g., booking and ticket Schema Codes typically allow users to tap on for check-in when arrival at the place of destination, like a restaurant.

    - **When users tap/scan offline Tokens**: 
        - when users tap or scan an offline [Token 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) on a Consumer's scanner (e.g., a printed flight ticket at an airport gate), the Consumer can validate the [Token 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) without the need for a chat or any interactions with the user's [Broker 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>).

    - **When users tap Userables**: 
        - when users tap a [Userable 💍](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) on a [Consumer's 💼](<04 💼🎭 Consumer role.md>) scanner (e.g., a wristband at an airport gate), the [Consumer 💼](<04 💼🎭 Consumer role.md>) can ask the user's [Custodian 🎩](<../../70 🌳 Ambient/71 💠 Brand Things/05 🎩🗄️ Custodian vault.md>) domain to silently share all [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) marked as public by the user and matching a list of expected [Schema Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>);
        - see [Userable at gates 💍🎬](<../../70 🌳 Ambient/74 💍 Brand Userables/05 💍🎬 Userable gates.md>) for details.

    ---

2. **Can Consumers use SELF Tokens to tracked domains?**

    Yes. Just like with first-party cookies on Web 2.0 internet. 
    
    - Tokens using a [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) marked as SELF are silently shared with Consumer domains, who can then track users;
    - e.g., a luxury holding company with multiple brands may issue a loyalty card for a specific branded stored, then use that card to track the user across all businesses it manages.

    ---

3. **Can Consumers use SELF Tokens to behave like Vaults?**

    Yes, but that may produce a poor user experience.

    - SELF Tokens are silently shared with Consumers who issued them, the same way a user's [Vault 🗄️](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) [Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) is shared silently with the corresponding Vault - this allows for developers to choose either a Consumer or [Vault 🗄️](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) role for personalized features. 
    
    - Domain admins should evaluate the impact of one design decision over another when it comes to how the domain's relationship is presented to the user.


    ---
    
2. **How can Consumers validate the data schema when consuming?**

    When consuming data from a [Vault 🗄️](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>), the data envelope indicates the [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) and the version (e.g., `any-authority.com/any-schema:1.0`). 
    
    - The code identifies the Manifest where the schema is defined (e.g., `any-schema` is defined in the [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) of `any-authority.com`), so consumer domains can then fetch the schema definitions from a cached [Graph 🕸](<../../40 👥 Domains/44 📜 Manifests/03 🕸👥 Graph helper.md>) or directly from the [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>).

    ---

3. **How do Consumers verify a Token's signature?**

    When issuing [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>), [Issuers 🎴](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>) sign them with the same key-pair used in their [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) public key. 
    - Other domains can use the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) key to verify the signature on the Token.

    ---

4. **Can Consumers verify Tokens when Issuers are offline?**

    Yes. 
    
    - NLWeb advocates for domains to ask [Graphs 🕸](<../../40 👥 Domains/44 📜 Manifests/03 🕸👥 Graph helper.md>) for the [Issuer's 🎴](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>) [DKIM](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) when verifying [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>). 

    ---

5. **Can Consumers verify Tokens when Issuers rotate a DKIM?**

    Graphs will find the [Issuer 🎴](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>)'s [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) in use when the [Token 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) was issued.

    ---

6. **How are Consumers protected when Graph are compromised by attackers?**

    [Firewalls 🔥](<../../40 👥 Domains/43 👍 Trusts/03 🔥👥 Firewall helper.md>) monitor the behavior of any [Graph 🕸](<../../40 👥 Domains/44 📜 Manifests/03 🕸👥 Graph helper.md>) and match domain information with other Graphs. 
    * If necessary, [Firewalls 🔥](<../../40 👥 Domains/43 👍 Trusts/03 🔥👥 Firewall helper.md>) immediately revoke a Graph's [trust 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>).

    ---

7. **How are Users protected from Consumers that ask too much data?**

    Consumers 💼 must publicly [manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) their potential sharing requests, in a similar way apps must manifest it when publishing into Apple's App Store or Google Play.
    - [Brokers 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) only process sharing requests that are publicly manifested in advance.
    - [Authorities 🏛️](<../../40 👥 Domains/43 👍 Trusts/02 🏛️👥 Authority helper.md>) monitor the [manifests 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) for dataset requests that don't match the domain's business or exception requests, and if necessary may revoke Consumer's 💼 [trust 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>).

    ---

8. **Why aren't all Tokens validated online?**

    In scenarios where physical gates need to allow for large influx of people (e.g., a concert or a subway station), it is quicker to validate the [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) offline at the edge, opening the gate if the Token seems valid. 
    
    * The Consumer 💼 may then perform an asynchronous validation of the [Token 🎫](<../25 🎫 Tokens/01 🎫 Token.md>), marking it as expired in a local database so that the passage is blocked on the next pass.

    ---

9. **Can Consumers verify if a Token was issued to the holder?**

    Yes. 
    
    - Certain scenarios require the Consumer 💼 to verify if the person holding the [Token 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) is the person to whom the Token was issue to - e.g.:
        - at an airport border control, automatic gates need to match the face of the passport holder with the biometric signature contained in the electronic passport. 
    
    - This requires an online request to an [Identity 🆔](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) domain [bound 🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>) to the user and [trusted 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) by the Consumer 💼, allowing the token to be matched to the holder without disclosing the holder's Identity 🆔 to the Consumer 💼:
        - e.g., while entering a casino, the casino can validate that the 21-years-old token is valid, and that the holder is the owner of the token, without knowing who the holder is. 
    
    - The [Identity 🆔](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) domain can perform the authentication:
        - on the user's device (e.g., via multi-factor authentication or using the camera in the device), 
        - or through an external device (e.g., [Amazon One 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/07 🖐️ Palm pay landscape/02 📺 Amazon One.md>) palm reader).

    ---

10. **How do sellers prevent swapping of identity Tokens?**

    [Sellers 💵](<../../30 🫥 Agents/04 💳 Payers/02 💵🎭 Seller role.md>) can prevent frauds where users share their [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) with someone else.
    - e.g., an adult may give their wallet's device to an under-aged child so that they can buy age-restricted goods at a self-service store. 
    
    In low-budget validations, 
    - Sellers ask the user's trusted [Identity 🆔](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) domain to perform the authentication inside the chat on the user's device;
    - depending on the circumstances, this can be a biometric face scan, voice recognition, OTP, security questions, or other. 
    
    In offline scenarios, 
    - where users carry an NFC card or a printed QR, 
    - the [Seller 💵](<../../30 🫥 Agents/04 💳 Payers/02 💵🎭 Seller role.md>) takes a photo of the user with a fixed camera, and then ask the Token's [Identity 🆔](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) vault to match the Token with the picture.

    ---

11. **How can users be protected from consumers collecting too much PII?**

    To protect users from Consumers that collect too much Personally Identifiable Information (PII), [Brokers 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) verify if any Consumer request is explicitly mentioned on their [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>).

    * Consumers manifest the unique contexts in which they will collecting data, and what data is collected in each context.
  
    * When interacting in a chat, Consumers need to notify the [Brokers 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) of a context change before requesting data under that context.

    * [Brokers 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) inform users of every context change, identifying the data that may be collected, then block any data request from the Consumer that does not comply with that context.

    * Because the [Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) are public and prone to automatic evaluation by domains like [Firewalls 🔥](<../../40 👥 Domains/43 👍 Trusts/03 🔥👥 Firewall helper.md>) and [Reviewers ⭐](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>), Consumers are exposed to public scrutiny regarding the data  their are collecting, namely: what, why, how, and how much.