💍 Userables for emergencies
===

1. **How can users set up a health emergency script?**

    In case the owner is unconscious, any guest can [tap 🔆](<../../Locators 🔆/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>) the owner's [Userable 💍 thing](<../💍💠 Userable thing.md>) to start an emergency script previously configured by the owner.

    These emergency steps may include:
    - inform close family members, 
    - make a group phone call, 
    - notify the health insurance company.
    
    ---
    <br/>


1. **How is the [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>)?**

    Consider the following [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) as an example.
        
    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    |-|-|-
    | | | 🔆 [tap](<../../Locators 🔆/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>)
    | 🔎 [Finder](<../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Wand (4.3 ⭐)  [+] 
    | 🪄 [Wand](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) | ℹ️ Userable: wedding ring [+]
    | 🪄 [Wand](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) | 😃 Hi! What do you need? <br/>- [ Emergency ] trigger <br/>- [ Something else ] | > Emergency
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ⓘ Flow: emergency [+]
    | 🪄 [Wand](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>)| 😐 Are you the owner? [Yes, No] | > No
    | 🪄 [Wand](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>)| ℹ️ Public notes:<br/>- suffers from epilepsy <br/> - allergic to penicillin
    | 🪄 [Wand](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>)| 😐 Activate emergency? [Yes, No] <br/> - I'll need your location <br/> - your contact details <br/>- and an identity check | > Yes
    | 🪄 [Wand](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) | [📍 Share location?](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/LOCATION 📍/📍 LOCATION ⌘ cmd.md>) [Yes, No] | > Yes
    | 🧢 [Persona](<../../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) | 🫥 Share contacts ? [Yes, No] | > Yes
    | 🆔 [Identifier](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) | 🫥 Share identity? [Yes, No] | > Yes
    | 🆔 [Identifier](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) | 🫥 Let me see if it's you.   | [📸 selfie](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>)
    | 🪄 [Wand](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) | ✅ Emergency activated [+]
    
    ---
    <br/>


1. **How does it work?**

    ![](<../. 📎 Assets/💍 Userable Emergency.png>)

    |#|Category|Step
    |-|-|-
    |1| `Tap NFC` | A guest user [taps 🔆](<../../Locators 🔆/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>) the [rotating NFC tag 📺](<../../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/11 📺 NFC authentication.md>) of the [Userable 💍 thing](<../💍💠 Userable thing.md>) with their [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
    |2| `Interact`| A [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) opens with the [Userable's Wand 🪄 domain](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) (i.e., the helper defined by the [Userable's Brand 🍏 domain](<../../../41 🎭 Domain Roles/Brands 🍏/🍏🎭 Brand role.md>)) - this allows the guest user to read the landing notes that the owner user left, and allowing the guest to active the emergency script defined by the owner user.
    |3| `Identify` | The [Userable's Wand 🪄 domain](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) asks the [guest user's Identifier 🆔 agent](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) to authenticate the guest - this allows emergency services to impose legal actions on harassment frauds if necessary.
    |4| `Activate`| The guest activates the emergency workflow - this triggers the [Userable's Wand 🪄 domain](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) to ask the [guest's Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) for the guest's location, ask the [guest's Persona 🧢 agent](<../../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) for the guest's contact details, and pass that information to the [owner's Custodian 🧳 vault](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>).
    |5| `Broadcast`| The [owner's Custodian 🧳 domain](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>) executes the emergency script defined by the owner user - e.g., perform a group call with the selected phone numbers, as well as alert emergency services, trusted medical contacts, and health insurance companies.

    ---
    <br/>

1. **What data is collected in an emergency?**
    
    To streamline the process, [Custodian 🧳 domains](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>) collect the following information from the guest user.
    
    |Data|Reason
    |-|-
    | `Contact details` | For emergency personal to get in contact with the guest.
    | `Current location`| For emergency personal to quickly get there.
    | `Identity check`  | To prevent fraud and harassment.

    ---
    <br/>



1. **How can the process be simplified for speed?**

    Owners with high risk (e.g., epilepsy, heart disease) may speed up the rescue by adding instructions directly to the landing page and/or by removing the need for guests to authenticate before activating an emergency.

    ---
    <br/>

1. **How are Userable owners protected from harassment frauds?**

    To avoid harassment frauds, before issuing the emergency alarm, 
    * owners may request their [Custodian 🧳 agent](<../../../50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>) 
    * to request guests to be authenticated 
    * by a [trusted 🫡](<../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) [Identifier 🆔 domain](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>).

    ---
    <br/>



1. **How does it compare with Apple Watch emergency?**
   
    Apple Watch emergency alerts can be triggered automatically.
    - Apple can do this because the the watch is constantly monitoring the owner's vital signs and movements, is able to detect if something is wrong, and is able to automatically trigger an emergency alarm on its own.
  
    Conversely, [Userable 💍 things](<../💍💠 Userable thing.md>) are nothing more than an secure NFC tag embedded into an object carried by the user (e.g., earings, neckless).
    - Thus, they don't have any monitoring or assessment mechanism, and are unable to trigger emergencies on their own.
    - But they are much cheaper (less than 1.00$) and resilient enough to be worn all the time without ever running out of power (e.g., a wedding ring may be in place for decades straight).
    - They can also be used in non-tech environments, like airports and highly secure environments.
  
    For automatic emergency alarms,
    * see [Tapband ⌚ thing](<../../Tapbands ⌚/⌚💠 Tapband thing.md>) for collecting health sensor measurements
    * and [Vitalogists 💖 agents](<../../../50 🫥 Agent domains/Vitalogists 💖/💖🫥 Vitalogist agent.md>) for triggering emergency alarms.


    ---
    <br/>


1. **How does it compare with Apple iPhone emergency?**

    Anyone in physical control of an Apple iPhone or Android-based device (owner or not) can trigger an emergency event at any time.
    * This is done without an assessment of the owner's incapacity be assessed first, because typically the phone doesn't have health monitoring mechanisms (unless a smart watch is linked to it).
    * Some phones already have collision detection mechanisms for car accidents, and that can automatically trigger an emergency alert.

    Conversely, [Userable 💍 things](<../💍💠 Userable thing.md>) are nothing more than an secure NFC tag embedded into an object carried by the user (e.g., earings, neckless).
    - They do allow anyone to trigger an emergency alarm, but are unable to detect collisions in car accidents.
    - But they are much cheaper (less than 1.00$) and resilient enough to be worn all the time without ever running out of power (e.g., a wedding ring may be in place for decades straight).
    - They can also be used in non-tech environments, like airports and highly secure environments.

    For automatic emergency alarms,
    * see [Tapband ⌚ thing](<../../Tapbands ⌚/⌚💠 Tapband thing.md>) for collecting health sensor measurements
    * and [Vitalogists 💖 agents](<../../../50 🫥 Agent domains/Vitalogists 💖/💖🫥 Vitalogist agent.md>) for triggering emergency alarms.
    
    ---
    <br/>
