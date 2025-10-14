💍 Userables for confused senior user
===


> Mentioned in [Verify Userables 🆔](<../../30 🫥 Agents/05 🆔 Identities/15 🆔💍 Verify Userables.md>)

<br/>


1. **How can a confused senior user leverage their Userables?**

    Consider a scenario where a senior person is returning home alone and accidentally leaves their bag 👜 on a taxi 🚖, with the home keys and the phone inside in silent mode.
    * Because the phone is in silent mode, its useless to call the phone.
    * Nowadays, we don't memorize phone numbers, so the person can't call a relative.
    * FindMy apps (e.g., Apple) and [UWB tags 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/02 🔑 Smart Keys/11 📺 Apple Key UWB.md>)  can't help, because the owner typically needs another of his authenticated devices (e.g., a phone, a tablet, or laptop).

    With NLWeb, the person can ask anyone else (e.g., the staff from a restaurant nearby) to use their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and [tap 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) one of the person's [Userable 💍 things](<01 💍 Userable thing.md>) (e.g., wedding ring, neckless, watch) in order to:
    - read their landing notes for memory tips, 
    - authenticate to access their owner area (e.g., face scan),
    - call any of their emergency contacts,
    - see the current location of their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) (like Apple Find My), 
    - and remotely ring their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) (like Apple Find My). 

    ---
    <br/>



1. **How does it work?**

    ![](<00 📎 Assets/💍 Userable Phone.png>)

    |#|Category|Step|
    |-|-|-
    |1| `Tap` | A guest user uses their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to [tap 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) the [rotating NFC tag 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/11 📺 NFC authentication.md>) of the owner's [Userable 💍 thing](<01 💍 Userable thing.md>). 
    |2| `Read`| The guest's [Broker 🤵 domain](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) opens a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) with the [Userable's Wand 🪄 domain](<../71 💠 Brand Things/09 🪄🛠️ Wand helper.md>), allowing the guest user to read the landing notes that the owner user left.
    |3| `Admin` | The guest user asks the [Userable's Wand 🪄 domain](<../71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) to access the owner's admin area, who then directs the request to the [owner's Custodian 🧳 agent](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>).
    |4| `Face` | The [owner's Custodian 🧳 agent](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) asks the [owner's Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) to authenticate the owner with a [face scan 😶](<../../30 🫥 Agents/05 🆔 Identities/21 🆔😶 Face scan.md>) using the guest's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    |5| `Ring` |  The [owner's Custodian 🧳 agent](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) then informs the owner about the location of owner's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), and allows them to remotely ring the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>). 
    |6| `Circle` | The owner can then access the contact details of their personal circle via the [owner's Custodian 🧳 agent](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>). 

    ---
    <br/>


1. **What does the Chat look like?**

    Consider the following [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) as an example.
        
    
    | [Domain](<../../40 👥 Domains/41 📨 Comms/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | | | 🔆 [tap](<../../20 🧑‍🦰 UI/11 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>)
    | 🔎 [Finder](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Wand (4.3 ⭐)  [+] 
    | 🪄 [Wand](<../71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) | ℹ️ Userable: wedding ring [+]
    | 🪄 [Wand](<../71 💠 Brand Things/09 🪄🛠️ Wand helper.md>)  | 😃 Hi! What do you need? <br/>- [ Private ] access <br/>- [ Something else ]| > Private
    | 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Flow: authenticate [+]
    | 🪄 [Wand](<../71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) | 😐 Are you the owner? [Yes, No] | > Yes
    | 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Allow guest domain?](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite 🛠️.md>) [Yes, No]  <br/> - Any Identity 🆔 <br/>- [ Always ] for Any Wand 🪄 | > Yes
    | 🆔 [Identity](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's the owner.     | [📸 selfie](<../../30 🫥 Agents/05 🆔 Identities/21 🆔😶 Face scan.md>)
    | 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Allow guest domain?](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite 🛠️.md>) [Yes, No]  <br/> - Any Custodian 🧳<br/>- [ Always ] for Any Wand 🪄 | > Yes
    | 🧳 [Custodian](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>)| 🫥 What do you need? <br/>- [ Ring ] my Wallet <br/>- [ Circle ] Contacts <br/>- [ Something else ] | > Circle
    | 🧳 [Custodian](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) | 🫥 Which one? <br/>- [ Jake ] <br/>- [ Spirit ] | > Spirit
    | 🧳 [Custodian](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) | 🫥 Options for Spirit: <br/>- Call [ Mobile ] <br/>- Call [ Work ] <br/> - [ Back ] to list | > Mobile
    | 🧳 [Custodian](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) | ✅ Calling Spirit's Mobile...

    ---
    <br/>


