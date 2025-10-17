🆔 Identity to verify Wallets
===

> Part of [Identity 🆔 domains](<../🆔🫥 Identity agent.md>)

 <br/>



1. **How to verify a Wallet ownership?**

    Consider the following [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) excerpt
    * as an example of [face verification 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/01 📺 Difference.md>) 
    * for the ownership of a [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).
        
    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🤗 [Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😐 Start risky task [Yes, No] | > Yes
    | 🆔 [Identity](<../🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.   | [📸 selfie](<6 🆔⏩😶 Face scan.md>)
    | 🤗 [Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ Verified, task started!

    ---
    <br/>

1. **What are industry use cases for age verification?**

    |Industry|Use case 🤝
    |-|-
    |`Hospitality`|[🏨 Check-in when staying at a hotel](<../../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/03 🏨 Guest @ Reception 🛎️/04 🛎️ Check-in.md>)
    |`Financial`|[🏧 Withdraw cash from an ATM](<../../../../3 🤝 Use Cases/05 🛠️ Services/03 🏧 Withdraw at ATMs/10 Customer @ ATM/11 Withdraw cash.md>)
    |`Governments`|[🏛️ Request a proof of address](<../../../../3 🤝 Use Cases/08 🏛️ Public Services/08 📮 Prove address/1 Customer @ Anywhere/11. Proof of Address.md>)
    |`Health`| [💍 Trigger a Userable emergency](<../../../25 🔆 Locators/Userables 💍/💍⏩ Userable flows/💍🚨 Emergencies.md>)
    

    ---
    <br/>



1. **How does remote face verification works?**

    ![](<../. 📎 Assets/🆔 Online.png>)

    When a user is requested by a [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) to verify their identity against a given [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>), the following steps are executed.

    | # | Step
    |-|-
    |1| The user's [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) <br/>• opens a web-browser window <br/>• to the liveness check URL of the [Locator's Identity 🆔 vault](<../🆔🫥 Identity agent.md>), <br/>• passing anti-fraud information like device location and device configurations.
    |2| The webpage of the [Identity 🆔 vault](<../🆔🫥 Identity agent.md>) <br/>• activates the device's camera to record the user's video for liveness check <br/>• extracts the relevant images <br/>• and compares them to the user images on the given [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>). 
    |3| Additionally, depending on the anti-fraud contextualized info, <br/>• the [Identity 🆔 vault](<../🆔🫥 Identity agent.md>) asks security questions and one-time-passwords (OTP).

    ---
    <br/>


1. **How are users' face biometrics protected from Sellers?**

    NLWeb advocates for online face authentication between [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) and [Identity 🆔 vaults](<../🆔🫥 Identity agent.md>), without sharing user biometrics with [Seller 💵 domains](<../../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>);
    - e.g., when a [Seller 💵 domain](<../../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) needs to match a person with a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>), 
    - it contacts the [Token's  Identity 🆔 domain](<../🆔🫥 Identity agent.md>) to perform the authentication 
    - via the user's [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) in a [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>), 
    - and only return a success/failure to the [Seller 💵 domain](<../../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) . 
    
    When offline authentications are required, 
    * i.e. when the user only has a printed QR or and NFC card with the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>), 
    * then the [Seller 💵 domain](<../../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) needs to take the user's picture 
    * with a fixed camera in a supervised fashion, 
    * then ask the [Token's  Identity 🆔 domain](<../🆔🫥 Identity agent.md>) to match the picture with the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>), 
    * and then delete the picture according to regulatory requirements. 

    ---
    <br/>