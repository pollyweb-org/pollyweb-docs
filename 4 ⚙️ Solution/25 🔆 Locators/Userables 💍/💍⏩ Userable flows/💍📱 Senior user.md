💍 Userables for confused senior user
===


> Mentioned in [Verify Userables 🆔](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/4 Verify Userables 🆔⏩💍/🆔⏩ Verify Userables.md>)

<br/>


1. **How can a confused senior user leverage their Userables?**

    Consider a scenario where a senior person is returning home alone and accidentally leaves their bag 👜 on a taxi 🚖, with the home keys and the phone inside in silent mode.
    * Because the phone is in silent mode, its useless to call the phone.
    * Nowadays, we don't memorize phone numbers, so the person can't call a relative.
    * FindMy apps (e.g., Apple) and [UWB tags 📺](<../../../../2 🏔️ Landscape/3 🌳 Ambient landscape/02 🔑 Smart Keys/11 📺 Apple Key UWB.md>)  can't help, because the owner typically needs another of his authenticated devices (e.g., a phone, a tablet, or laptop).

    With PollyWeb, the person can ask anyone else (e.g., the staff from a restaurant nearby) to use their [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) and [tap 🔆](<../../Locators 🔆/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>) one of the person's [Userable 💍 things](<../💍💠 Userable thing.md>) (e.g., wedding ring, neckless, watch) in order to:
    - read their landing notes for memory tips, 
    - authenticate to access their owner area (e.g., face scan),
    - call any of their emergency contacts,
    - see the current location of their [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) (like Apple Find My), 
    - and remotely ring their [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) (like Apple Find My). 

    ---
    <br/>



1. **How does it work?**

    ![](<../. 📎 Assets/💍 Userable Phone.png>)

    |#|Category|Step|
    |-|-|-
    |1| `Tap` | A guest user uses their [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to [tap 🔆](<../../Locators 🔆/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>) the [rotating NFC tag 📺](<../../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/11 📺 NFC authentication.md>) of the owner's [Userable 💍 thing](<../💍💠 Userable thing.md>). 
    |2| `Read`| The guest's [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) opens a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with the [Userable's Wand 🪄 domain](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>), allowing the guest user to read the landing notes that the owner user left.
    |3| `Admin` | The guest user asks the [Userable's Wand 🪄 domain](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) to access the owner's admin area, who then directs the request to the [owner's Custodian 🧳 agent](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>).
    |4| `Face` | The [owner's Custodian 🧳 agent](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>) asks the [owner's Identifier 🆔 agent](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) to authenticate the owner with a [face scan 😶](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>) using the guest's [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
    |5| `Ring` |  The [owner's Custodian 🧳 agent](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>) then informs the owner about the location of owner's [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>), and allows them to remotely ring the [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>). 
    |6| `Circle` | The owner can then access the contact details of their personal circle via the [owner's Custodian 🧳 agent](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>). 

    ---
    <br/>


1. **How is the [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>)?**

    Consider the following [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) as an example.
        
    
    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | | | 🔆 [tap](<../../Locators 🔆/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>)
    | 🔎 [Finder](<../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Wand (4.3 ⭐)  [+] 
    | 🪄 [Wand](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) | ℹ️ Userable: wedding ring [+]
    | 🪄 [Wand](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>)  | 😃 Hi! What do you need? <br/>- [ Private ] access <br/>- [ Something else ]| > Private
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ⓘ Flow: authenticate [+]
    | 🪄 [Wand](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) | 😐 Are you the owner? [Yes, No] | > Yes
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 [Allow guest domain?](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>) [Yes, No]  <br/> - Any Identifier 🆔 <br/>- [ Always ] for Any Wand 🪄 | > Yes
    | 🆔 [Identifier](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) | 🫥 Let me see if it's the owner.     | [📸 selfie](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>)
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 [Allow guest domain?](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>) [Yes, No]  <br/> - Any Custodian 🧳<br/>- [ Always ] for Any Wand 🪄 | > Yes
    | 🧳 [Custodian](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>)| 🫥 What do you need? <br/>- [ Ring ] my Wallet <br/>- [ Circle ] Contacts <br/>- [ Something else ] | > Circle
    | 🧳 [Custodian](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>) | 🫥 Which one? <br/>- [ Jake ] <br/>- [ Spirit ] | > Spirit
    | 🧳 [Custodian](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>) | 🫥 Options for Spirit: <br/>- Call [ Mobile ] <br/>- Call [ Work ] <br/> - [ Back ] to list | > Mobile
    | 🧳 [Custodian](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>) | ✅ Calling Spirit's Mobile...

    ---
    <br/>


