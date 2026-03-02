🎫 Tokens
===

1. **What is a Token?**

    [Tokens 🎫](<🎫 Token.md>) are verifiable credentials
    * issued and signed by an [Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>), 
    * that contain data to be shared with [Consumer 💼 domains](<../../../50 🫥 Agent domains/Storage 🗃️/🗃️🫥 Storage agent.md>).

    ---
    <br/>
    
1. **What are examples of Tokens?**

    Examples of [Tokens 🎫](<🎫 Token.md>) include.
    
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
    
    ![](<../.📎 Assets/🎫 Token.png>)

    |#|Category|Step
    |-|-|-
    |1| `Issue`| An [Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) issues a [Token 🎫](<🎫 Token.md>) the the user stores offline in the [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
    |2| `In-Chat`| While in a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with a [Consumer 💼 host domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>), the user shares the [Token 🎫](<🎫 Token.md>).
    |3| `Userable` | Using their [Custodian 🧳 agent](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>), users select which [Tokens 🎫](<🎫 Token.md>) to be automatically shared by a specific [Userable 💍 thing](<../../../25 🔆 Locators/Userables 💍/💍💠 Userable thing.md>).
    | 4| `Userable`| When the NFC of the [Userable 💍 thing](<../../../25 🔆 Locators/Userables 💍/💍💠 Userable thing.md>) is [tapped 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>) on the [scanner ✨ device](<../../../60 🧰 Edge/66 ✨ Scanners/06 ✨🔌 Scanner device.md>) of a [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>), the [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) shares the [Tokens 🎫](<🎫 Token.md>).
    |5| `Printed`| From the [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>), users can print a [Token 🎫](<🎫 Token.md>).
    |6| `Printed` | The user can then present the printed [Token 🎫](<🎫 Token.md>) to the [scanner ✨ device](<../../../60 🧰 Edge/66 ✨ Scanners/06 ✨🔌 Scanner device.md>) of a [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>).
    |7| `Identity` | If the [Token 🎫](<🎫 Token.md>) contains the [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) of an [Identifier 🆔 domain](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>), then it means that the [Token 🎫](<🎫 Token.md>) was issued to a specific person only.
    |8| `Identity`| The [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) can then ask the [Token's Identifier 🆔 domain](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) to verify if it is really that person holding the presented [Token 🎫](<🎫 Token.md>) or not.

    ---
    <br/>


1. **Can Tokens be downloaded into the Wallet?**

    Yes.
    * Thus the term [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) when referring to PollyWeb browsers. 

    ---
    <br/>
    
1. **Are Tokens compatible with W3C Verifiable Credentials?**

    No.
    * They are not compatible with [W3C Verifiable Credentials 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>).
    * But they are similar in purpose.

    ---
    <br/>
    
1. **Are these crypto tokens from blockchain?**

    No. 
    * PollyWeb does not use blockchain nor cryptocurrencies. 
    * Global blockchain databases are known to have scaling issues without fully delivering the promise of decentralization, and were already abandoned by [W3C Verifiable Credential 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>) players like IATA, and by crypto start-ups like [Sam Altman's World 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/11 📺 Sam Altman's World.md>).

    ---
    <br/>
    
1. **Can Tokens be used for documents with photo validation?**

    Yes, [Tokens 🎫](<🎫 Token.md>) can be identity-bound;
    - i.e., they can allow [Consumer 💼 domains](<../../../50 🫥 Agent domains/Storage 🗃️/🗃️🫥 Storage agent.md>) to confirm that the holder of the Token is effectively the human for whom the [Token 🎫](<🎫 Token.md>)  was issue to. 
    - [Identity-bound 🆔 tokens](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/3 Verify Tokens 🆔⏩🎫/🆔⏩ Verify Tokens.md>) reference a trusted [Identifier 🆔 domain](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) that is able to authenticate the user - e.g., with a [Face scan 😶](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>).


    The following [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) excerpt from the [Casino Entry 🤝 use case](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>) illustrates the usage of an [Identity-bound 🆔 token](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/3 Verify Tokens 🆔⏩🎫/🆔⏩ Verify Tokens.md>).


    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | | | 🔆 [tap](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
    | 🔎 [Finder](<../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Casino (4.4 ⭐) [+]
    | 🎰 Casino   | ℹ️ Request for minimum age. [+]
    | 🆔 [Identifier](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) | 🫥 Share over 21? [Yes, No]      | > Yes
    | 🆔 [Identifier](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) | 🫥 Let me see if it's you.   | [📸 selfie](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>)
    | 🎰 Casino   | ✅ Welcome, please enter!
    

    ---
    <br/>

1. **Can Tokens be read in Chats without the use consent?**

    No, except for [SELF Tokens 🎫](<🎫 Token.md>).

    - Before sharing [SELF Tokens 🎫](<🎫 Token.md>) with other domains, [Broker 🤵 domains](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) ask the user for approval.
  
    - Exceptionally, if the [Schema 🧩](<../../Codes 🧩/🧩 Schema Code.md>) of the [Token 🎫](<🎫 Token.md>) is marked as SELF, then the user's [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) silently share the [Token 🎫](<🎫 Token.md>) with the [Token's Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>).


    The following [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) excerpt illustrates the usage of a [SELF Token 🎫](<🎫 Token.md>) when [passing a gate at a train station 🤝](<../../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/02 🚂 Customer @ Station/22 Pass gates 1 person.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
    | - | - | - |
    | | | 🔆 [tap](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
    | 🔎 [Finder](<../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Railway (4.3 ⭐) [+]
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ⓘ Ticket [token 🎟️](<🎫 Token.md>) shared [+]
    | 🚂 Railway | ℹ️ Ticket presented: <br>- from MAD T4 to MAD T2 
    | 🚂 Railway | ✅ Entry gate opened!
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ⓘ Ticket voided [+]
    

    ---
    <br/>

1. **Why do SELF Tokens exist?**

    [SELF Tokens 🎫](<🎫 Token.md>) are typically issued as a pass to be presented back to the [Token's Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) in a later moment in time, aiming for the least possible friction in the future - e.g.:

    - [open a train station gate with a tap 🤝](<../../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/02 🚂 Customer @ Station/22 Pass gates 1 person.md>),
    - [check-in with a booking with a tap 🤝](<../../../../3 🤝 Use Cases/05 🛠️ Services/01 💈 Cut hair at salons/20 Customer @ Salon/21 Arrive.md>). 

    Examples of [SELF Tokens 🎫](<🎫 Token.md>) include:
    - ⚽ event tickets (e.g., cinema, sports, concerts)
    - 🚌 public transport tickets (e.g., bus, train)
    - 🔑 physical access rights (e.g., doors, gates)
    - 💻 digital access rights (e.g., logins, admin rights)
    - 🍲 bookings (e.g., restaurants, medical appointments)
  
    ---
    <br/>
    
1. **Can users share Tokens in Wallets without internet?**

    Not via [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>), no, because Wallets need Internet connectivity to share the [Token 🎫](<🎫 Token.md>) with other domains. 
    
    - **Note**: PollyWeb assumes the inevitability of internet becoming ubiquitous in time - in 2024, internet is already available on London subways, on United Airline flights, and in remote regions of the globe with [Starlink 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/03 📺 Starlink @ phones.md>), while [Project Kuiper 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/04 📺 Amazon's Kuiper.md>) is on track general availability in 2026.

    ---
    <br/>
    
1. **Can users print Tokens in paper?**

    Yes. 
    - Offline [Tokens 🎫](<🎫 Token.md>) allow users to remove the dependency on the device's battery, or technical issues with the [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) resulting from low or no internet connectivity;
    - e.g., travelers in long-distance flights are advised to store their ticket and passport [Tokens 🎫](<🎫 Token.md>) offline. 
    
    Offline options include the following.

    | Option | Description
    |-|-
    | **🖨️ Paper**| Ask the [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to print it on paper.
    | **📱 Phone** | Screenshot and store it as an image on a device.
    | **[💍 Userable](<../../../25 🔆 Locators/Userables 💍/💍💠 Userable thing.md>)** | Add it to a [Userable 💍 thing](<../../../25 🔆 Locators/Userables 💍/💍💠 Userable thing.md>) via the user's [Custodian 🧳 vault](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>).
    | **[⌚ Tapband ](<../../../25 🔆 Locators/Tapbands ⌚/⌚💠 Tapband thing.md>)** | Add it to a [Tapband ⌚ thing](<../../../25 🔆 Locators/Tapbands ⌚/⌚💠 Tapband thing.md>) via the user's [Custodian 🧳 vault](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>).

    ---
    <br/>
    
1. **Can users save multiple Tokens in a single NFC card?**

    Yes. 
    - Users can reference multiple [Tokens 🎫](<🎫 Token.md>) with a single NFC via [Userable 💍 things](<../../../25 🔆 Locators/Userables 💍/💍💠 Userable thing.md>).

    ---
    <br/>
    
    
1. **What data is contained in a Token?**

    ```yaml
    Token: token-1234
    Issuer: any-issuer.dom
    Schema: any-authority.com/ANY/PATH:1.0
    Context: {A:1,B:2}

    # Time related
    Issued: 2024-09-21T12:34:00Z
    Starts: 2024-01-10T13:45:00.000Z
    Expires: 2028-12-10T13:45:00.000Z

    # Identity bound
    Identifier: any-identity.dom
    Biostamp: person-1234

    # Signature for verification
    Signature: ABCMIQDALK2Fd...
    DKIM: pk1
    ```

    |Property| Type | Details
    |-|-|-
    | `Token` |[text](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| Resource key in the [Issuer 🎴](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)
    | `Issuer` |[text](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| The [Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) name
    |`Schema` |[text](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| The Token's [Schema 🧩](<../../Codes 🧩/🧩 Schema Code.md>)
    | `Context` | [map](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) | Any optional data fields
    | `Issued` | [time](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>) | When it was issued
    |`Starts` |[time](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>)| Valid from
    |`Expires`|[time](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>)| Valid until (optional)
    |`Identifier` |[text](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)|The [Identifier 🆔 domain](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) 
    | `Biostamp` |[text](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| The stamp in the [Identifier 🆔 domain](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>)
    | `Signature`|[text](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| The Issuer's [signature](<../../Messages 📨/📨 Message/📨 Message.md>) 📨 
    | `DKIM`|[text](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| The [DKIM 📨](<../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Public Key/🕸 Public Key 🚀 call.md>) key used to sign
    


    ---
    <br/>

