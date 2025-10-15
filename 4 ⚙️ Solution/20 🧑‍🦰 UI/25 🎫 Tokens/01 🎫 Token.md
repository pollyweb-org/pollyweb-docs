🎫 Tokens
===

1. **What is a Token?**

    [Tokens 🎫](<01 🎫 Token.md>) are NFC/QR [Locators 🔆](<../11 🔆 Locators/01 🔆 Locator.md>) 
    * issued and signed by an [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>), 
    * that contain data to be shared with [Consumer 💼 domains](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>).

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
    |2| `In-Chat`| While in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) with a [Consumer 💼 host domain](<../27 💼 Consumers/04 💼🎭 Consumer role.md>), the user shares the [Token 🎫](<01 🎫 Token.md>).
    |3| `Userable` | Using their [Custodian 🧳 agent](<../../70 🌳 Ambient/71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>), users select which [Tokens 🎫](<01 🎫 Token.md>) to be automatically shared by a specific [Userable 💍 thing](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>).
    | 4| `Userable`| When the NFC of the [Userable 💍 thing](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) is [tapped 🔆](<../11 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) on the [scanner ✨ device](<../../60 🧰 Edge/66 ✨ Scanners/06 ✨🔌 Scanner device.md>) of a [Consumer 💼 domain](<../27 💼 Consumers/04 💼🎭 Consumer role.md>), the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) shares the [Tokens 🎫](<01 🎫 Token.md>).
    |5| `Printed`| From the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), users can print a [Token 🎫](<01 🎫 Token.md>).
    |6| `Printed` | The user can then present the printed [Token 🎫](<01 🎫 Token.md>) to the [scanner ✨ device](<../../60 🧰 Edge/66 ✨ Scanners/06 ✨🔌 Scanner device.md>) of a [Consumer 💼 domain](<../27 💼 Consumers/04 💼🎭 Consumer role.md>).
    |7| `Identity` | If the [Token 🎫](<01 🎫 Token.md>) contains the [Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>) of an [Identity 🆔 domain](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>), then it means that the [Token 🎫](<01 🎫 Token.md>) was issued to a specific person only.
    |8| `Identity`| The [Consumer 💼 domain](<../27 💼 Consumers/04 💼🎭 Consumer role.md>) can then ask the [Token's Identity 🆔 domain](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) to verify if it is really that person holding the presented [Token 🎫](<01 🎫 Token.md>) or not.

    ---
    <br/>


1. **Can Tokens be downloaded into the Wallet?**

    Yes.
    * Thus the term [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) when referring to NLWeb browsers. 

    ---
    <br/>
    
1. **Are Tokens compatible with W3C Verifiable Credentials?**

    No.
    * They are not compatible with [W3C Verifiable Credentials 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>).
    * But they are similar in purpose.

    ---
    <br/>
    
1. **Are these crypto tokens from blockchain?**

    No. 
    * NLWeb does not use blockchain nor cryptocurrencies. 
    * Global blockchain databases are known to have scaling issues without fully delivering the promise of decentralization, and were already abandoned by [W3C Verifiable Credential 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>) players like IATA, and by crypto start-ups like [Sam Altman's World 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/11 📺 Sam Altman's World.md>).

    ---
    <br/>
    
1. **Can Tokens be used for documents with photo validation?**

    Yes, [Tokens 🎫](<01 🎫 Token.md>) can be identity-bound;
    - i.e., they can allow [Consumer 💼 domains](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) to confirm that the holder of the Token is effectively the human for whom the [Token 🎫](<01 🎫 Token.md>)  was issue to. 
    - [Identity-bound 🆔 tokens](<../../30 🫥 Agents/05 🆔 Identities/14 🆔🎫 Verify Tokens.md>) reference a trusted [Identity 🆔 domain](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) that is able to authenticate the user - e.g., with a [Face scan 😶](<../../30 🫥 Agents/05 🆔 Identities/21 🆔😶 Face scan.md>).


    The following [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) excerpt from the [Casino Entry 🤝 use case](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>) illustrates the usage of an [Identity-bound 🆔 token](<../../30 🫥 Agents/05 🆔 Identities/14 🆔🎫 Verify Tokens.md>).


    | [Domain](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | | | 🔆 [tap](<../11 🔆 Locators/01 🔆 Locator.md>)
    | 🔎 [Finder](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Casino (4.4 ⭐) [+]
    | 🎰 Casino   | ℹ️ Request for minimum age. [+]
    | 🆔 [Identity](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Share over 21? [Yes, No]      | > Yes
    | 🆔 [Identity](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.   | [📸 selfie](<../../30 🫥 Agents/05 🆔 Identities/21 🆔😶 Face scan.md>)
    | 🎰 Casino   | ✅ Welcome, please enter!
    

    ---
    <br/>

1. **Can Tokens be read in Chats without the use consent?**

    No, except for [SELF Tokens 🎫](<01 🎫 Token.md>).

    - Before sharing [SELF Tokens 🎫](<01 🎫 Token.md>) with other domains, [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) ask the user for approval.
  
    - Exceptionally, if the [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) of the [Token 🎫](<01 🎫 Token.md>) is marked as SELF, then the user's [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) silently share the [Token 🎫](<01 🎫 Token.md>) with the [Token's Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>).


    The following [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) excerpt illustrates the usage of a [SELF Token 🎫](<01 🎫 Token.md>) when [passing a gate at a train station 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/02 🚂 Customer @ Station/22 Pass gates 1 person.md>).

    | [Domain](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) 
    | - | - | - |
    | | | 🔆 [tap](<../11 🔆 Locators/01 🔆 Locator.md>)
    | 🔎 [Finder](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Railway (4.3 ⭐) [+]
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Ticket [token 🎟️](<01 🎫 Token.md>) shared [+]
    | 🚂 Railway | ℹ️ Ticket presented: <br>- from MAD T4 to MAD T2 
    | 🚂 Railway | ✅ Entry gate opened!
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Ticket voided [+]
    

    ---
    <br/>

1. **Why do SELF Tokens exist?**

    [SELF Tokens 🎫](<01 🎫 Token.md>) are typically issued as a pass to be presented back to the [Token's Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) in a later moment in time, aiming for the least possible friction in the future - e.g.:

    - [open a train station gate with a tap 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/02 🚂 Customer @ Station/22 Pass gates 1 person.md>),
    - [check-in with a booking with a tap 🤝](<../../../3 🤝 Use Cases/05 🛠️ Services/01 💈 Cut hair at salons/20 Customer @ Salon/21 Arrive.md>). 

    Examples of [SELF Tokens 🎫](<01 🎫 Token.md>) include:
    - ⚽ event tickets (e.g., cinema, sports, concerts)
    - 🚌 public transport tickets (e.g., bus, train)
    - 🔑 physical access rights (e.g., doors, gates)
    - 💻 digital access rights (e.g., logins, admin rights)
    - 🍲 bookings (e.g., restaurants, medical appointments)
  
    ---
    <br/>
    
1. **Can users share Tokens in Wallets without internet?**

    Not via [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), no, because Wallets need Internet connectivity to share the [Token 🎫](<01 🎫 Token.md>) with other domains. 
    
    - **Note**: NLWeb assumes the inevitability of internet becoming ubiquitous in time - in 2024, internet is already available on London subways, on United Airline flights, and in remote regions of the globe with [Starlink 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/03 📺 Starlink @ phones.md>), while [Project Kuiper 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/01 🛰️ Connectivity landscape/04 📺 Amazon's Kuiper.md>) is on track general availability in 2026.

    ---
    <br/>
    
1. **Can users print Tokens in paper?**

    Yes. 
    - Offline [Tokens 🎫](<01 🎫 Token.md>) allow users to remove the dependency on the device's battery, or technical issues with the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) resulting from low or no internet connectivity;
    - e.g., travelers in long-distance flights are advised to store their ticket and passport [Tokens 🎫](<01 🎫 Token.md>) offline. 
    
    Offline options include the following.

    | Option | Description
    |-|-
    | **🖨️ Paper**| Ask the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to print it on paper.
    | **📱 Phone** | Screenshot and store it as an image on a device.
    | **[💍 Userable](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>)** | Add it to a [Userable 💍 thing](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) via the user's [Custodian 🧳 vault](<../../70 🌳 Ambient/71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>).
    | **[⌚ Tapband ](<../../70 🌳 Ambient/76 ⌚ Brand Tapbands/01 ⌚💠 Tapband thing.md>)** | Add it to a [Tapband ⌚ thing](<../../70 🌳 Ambient/76 ⌚ Brand Tapbands/01 ⌚💠 Tapband thing.md>) via the user's [Custodian 🧳 vault](<../../70 🌳 Ambient/71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>).

    ---
    <br/>
    
1. **Can users save multiple Tokens in a single NFC card?**

    Yes. 
    - Users can reference multiple [Tokens 🎫](<01 🎫 Token.md>) with a single NFC via [Userable 💍 things](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>).

    ---
    <br/>
    
    
1. **What data is contained in a Token?**

    [Tokens 🎫](<01 🎫 Token.md>) derive from [Locators 🔆](<../11 🔆 Locators/01 🔆 Locator.md>), so they contain the following properties.

    ```yaml
    Code: .TOKEN
    Domain: any-issuer.com
    TokenID: <token-uuid>
    Properties:
        Property1: Value1
        Property2: Value2
    ```

    |Property| Type | Details
    |-|-|-
    | `Code` | string |  [`.TOKEN`](<../../../7 🧩 Codes/$/🧩 TOKEN code.md>)
    | `Domain` | string | The [Issuer 🎴 domain](<02 🎴🎭 Issuer role.md>) name
    | `TokenID` | uuid |  The resource key in the [Issuer 🎴](<02 🎴🎭 Issuer role.md>)
    | `Properties` | object | Any optional data fields
    |

    
    
    Additionally, a basic [Token 🎫](<01 🎫 Token.md>) contains the following properties.
    
    ```yaml
    Schema: who.int/VACCINES/COVID-2:1.0
    Issued: 2024-09-21T12:34:00Z
    Starts: 2024-01-10T13:45:00.000Z
    Expires: 2028-12-10T13:45:00.000Z
    Signature: ABCMIQDALK2Fd...
    DKIM: pk1
    ```
    |Property| Type | Details
    |-|-|-
    |`Schema` | string | The Token's [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>)
    | `Issued` | timestamp | When it was issued
    |`Starts` |timestamp| Valid from
    |`Expires`|timestamp| Valid until (optional)
    | `Signature`| string | The Issuer's [signature](<../../40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>) 📨 
    | `DKIM`| string | The [DKIM 📨](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/07 👥🚀🕸 Public Key.md>) key used to sign
    |


    An identity-bound [Token 🎫](<01 🎫 Token.md>) also contains the following.

    ```yaml
    Identity: any-identity.com
    IdentityKey: person-1234
    ```

    |Property| Type | Details
    |-|-|-
    |`Identity` | string |The [Identity 🆔 domain](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) 
    | `IdentityKey` | string | The resource key in the [Identity 🆔 domain](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>)


    ---
    <br/>