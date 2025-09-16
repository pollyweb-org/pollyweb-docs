🎫 Tokens FAQ
===

1. **What is a Token?**

    [Tokens 🎫](<01 🎫 Token.md>) are NFC/QR [Locators 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) issued and signed by an [Issuer 🎴](<02 🎴🎭 Issuer role.md>), and containing information that can be shared with [💼 Consumers](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>).

    ---
    <br/>
    
1. **What are examples of Tokens?**

    Examples of [Tokens 🎫](<01 🎫 Token.md>) include.
    
    | Type | Applicability
    |-|-
    | ⚽ event tickets | cinema, sports, live concerts 
    | 🛩️ public transport tickets | flight, train
    | 🚌 public transport passes | return, monthly
    | 🚗 personal documents | driver's license, passports
    | 💉 identity-bound proofs | over 21, vaccines, disability
    | 🎓 identity-bound credentials | graduation, professional
    | 🔑 physical access rights | doors, gates
    | 💻 digital access rights | logins, admin rights
    | 👮 legal authority rights | police, business owner
    | 🔏 digital signatures | images, videos, PDF files
    | 📦 delivery trackers | parcels, registered letters
    | 🍲 bookings | restaurants, medical appointments

    ---
    <br/>
    

1. **How do Tokens work?**
    
    ![](<.📎 Assets/🎫 Token.png>)

    |#|Category|Step
    |-|-|-
    |1| `Issue`| An [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) issues a [Token 🎫](<01 🎫 Token.md>) the the user stores offline in the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    |2| `In-Chat`| While in a [Chat 💬](<../23 💬 Chats/01 💬 Chat.md>) with a [Consumer 💼 host domain](<../27 💼 Consumers/04 💼🎭 Consumer role.md>), the user shares the [Token 🎫](<01 🎫 Token.md>).
    |3| `Usarable` | Using their [Custodian 🧳 agent](<../../70 🌳 Ambient/71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>), users select which [Tokens 🎫](<01 🎫 Token.md>) to be automatically shared by a specific [Userable 💍 thing](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>).
    | 4| `Usarable`| When the NFC of the [Userable 💍 thing](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) is [tapped 🔆](<../22 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) on the [scanner ✨ device](<../../60 🧰 Edge/66 ✨ Scanners/06 ✨🔌 Scanner device.md>) of a [Consumer 💼 domain](<../27 💼 Consumers/04 💼🎭 Consumer role.md>), the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) shares the [Tokens 🎫](<01 🎫 Token.md>).
    |5| `Printed`| From the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), users can print a [Token 🎫](<01 🎫 Token.md>).
    |6| `Printed` | The user can then present the printed [Token 🎫](<01 🎫 Token.md>) to the [scanner ✨ device](<../../60 🧰 Edge/66 ✨ Scanners/06 ✨🔌 Scanner device.md>) of a [Consumer 💼 domain](<../27 💼 Consumers/04 💼🎭 Consumer role.md>).
    |7| `Identity` | If the [Token 🎫](<01 🎫 Token.md>) contains the [Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) of an [Identity 🆔 domain](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>), then it means that the [Token 🎫](<01 🎫 Token.md>) was issued to a specific person only.
    |8| `Identity`| The [Consumer 💼 domain](<../27 💼 Consumers/04 💼🎭 Consumer role.md>) can then ask the [Token's Identity 🆔 domain](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) to verify if it is really that person holding the presented [Token 🎫](<01 🎫 Token.md>) or not.

    ---
    <br/>


1. **Can Tokens be downloaded into the Wallet?**

    Yes, thus the term [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) when referring to NLWeb browsers. 

    ---
    <br/>
    
1. **Are Tokens compatible with W3C Verifiable Credentials?**

    No, they are not compatible with [W3C Verifiable Credentials 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>) but they are similar in purpose.

    ---
    <br/>
    
1. **Are these crypto tokens from blockchain?**

    No. NLWeb does not use blockchain nor cryptocurrencies. 

    ---
    <br/>
    
1. **Can Tokens be used for documents with photo validation?**

    Yes, [Tokens 🎫](<01 🎫 Token.md>) can be identity-bound;
    - i.e., they can allow [Consumer 💼 domains](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) to confirm that the holder of the Token is effectively the human for whom the Token was issue to. 
    - Identity-bound Tokens reference a trusted [Identity 🆔 domain](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) that is able to authenticate the user (e.g., with a face scan).
    - See [ID Tokens 🆔🎫](<../../30 🫥 Agents/05 🆔 Identities/07 🆔🎫 ID Tokens.md>) for further details.

    ---
    <br/>

2. **Can Tokens be read in Chats without the use consent?**

    No, except for SELF [Tokens 🎫](<01 🎫 Token.md>).

    - Before sharing [Tokens 🎫](<01 🎫 Token.md>) with other domains, [Broker 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>) domains ask the user for approval.
  
    - Exceptionally, if the [Schema 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) of the [Token 🎫](<01 🎫 Token.md>) is marked as SELF, then [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) silently share the Token with the Token's [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>).


    ---
    <br/>

1. **Why do SELF Tokens exist?**

    SELF [Tokens 🎫](<01 🎫 Token.md>) are typically issued as a pass to be presented back to the Token's [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) in a later moment in time, aiming for the least possible friction in the future - e.g.:

    - open an access gate with a tap;
    - open a subway entry gate with a tap;
    - check-in a medical booking with a tap. 

    Examples of SELF [Tokens 🎫](<01 🎫 Token.md>) include:
    - ⚽ event tickets (e.g., cinema, sports, concerts)
    - 🚌 public transport tickets (e.g., bus, train)
    - 🔑 physical access rights (e.g., doors, gates)
    - 💻 digital access rights (e.g., logins, admin rights)
    - 🍲 bookings (e.g., restaurants, medical appointments)
  
    ---
    <br/>
    
2. **Can users share Tokens in Wallets without internet?**

    Not via [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), no, because Wallets need internet to share the [Token 🎫](<01 🎫 Token.md>) with other domains. 
    
    - **Note**: NLWeb assumes the inevitability of internet becoming ubiquitous in time - in 2024, internet is already available on London subways, on United Airline flights, and in remote regions of the globe with [Starlink 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/03 📺 Starlink @ phones.md>), while [Project Kuiper 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/04 📺 Amazon's Kuiper.md>) is on track general availability in 2026.

    ---
    <br/>
    
3. **Can users print Tokens in paper?**

    Yes. 
    - Offline [Tokens 🎫](<01 🎫 Token.md>) allow users to remove the dependency on the device's battery, or technical issues with the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) resulting from low or no internet connectivity;
    - e.g., travelers in long-distance flights are advised to store their ticket and passport [Tokens 🎫](<01 🎫 Token.md>) offline. 
    
    Offline options include:
    - print on paper;
    - screenshot and store as an image on a device;
    - save to an NFC card;
    - save to an NFC wristband.

    ---
    <br/>
    
4. **Can users save multiple Tokens in a single NFC card?**

    Yes. 
    - Users can reference multiple [Tokens 🎫](<01 🎫 Token.md>) with a single NFC via [Userable 💍 things](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>).

    ---
    <br/>
    
    
6. **What data is contained in a Token?**

    [Tokens 🎫](<01 🎫 Token.md>) derive from [Locators 🔆](<../22 🔆 Locators/01 🔆 Locator.md>), so they always contain:
    * the [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) - e.g., `nlweb.org/TOKEN:1.0`
    * the [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) - e.g., `any-issuer.com`
    * the resource key in the Issuer domain - e.g., `certificate-XYZ`
    * any optional data fields.

    Additionally, a basic [Token 🎫](<01 🎫 Token.md>) contains:
    * the Token's 🎫 specific [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) - e.g., `who.int/VACCINES/COVID-2:1.0`
    * the timestamp when it was issued, in UTC - e.g., `2024-09-21T12:34:00Z`
    * and the Issuer's [signature](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) 🔏 - e.g., `qD/fMEQDALK2FdZcWyy7wNns1gH8vssdOAuxxxKnEExDMMGZcZG0Dw14Xxfh3HDCpTGxvuLbtCSdJaBnEZg2G7kytG8RG/aGFM+lru7MQR81zze7GkBXmpxm+oilkXrouL63/5fQzwRBS94n7YH7abkrBi4RqPiV/mGiDsm2fLEqc12a5kOXZGPsbuuCWs8Mvbrt5teJUELiEgLnBYXArLYvofoZOt4EWYFBTXvx+/NSm1vtqsZsY+dnLLtZ7kEyUNW70jRdP0VK5ek4Rqdg3tUPVSeG7Rxl0ZH5KuvLVOnL4kbcC2CI/bijZ12YCrF3WLEdgF0KhZDjs5HvwNbZNw==`

    An identity-bound [Token 🎫](<01 🎫 Token.md>) also contains:
    * the [Identity 🆔 domain](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) - e.g., `any-identity.com`
    * the resource key in the [Identity 🆔 domain](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>)  - e.g., `person-1234`

    ---
    <br/>