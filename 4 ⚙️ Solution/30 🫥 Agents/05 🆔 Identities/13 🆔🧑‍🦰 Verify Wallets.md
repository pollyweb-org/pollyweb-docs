🆔 Identity to verify Wallets FAQ
===

> Part of [Identity 🆔 domains](<01 🆔🫥 Identity agent.md>)

 <br/>



1. **How to verify a Wallet ownership?**

    Consider the following [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) excerpt
    * as an example of [face verification 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/01 📺 Difference.md>) 
    * for the ownership of a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
        
    | Service | Prompt | User
    | - | - | - |
    | 🤗 [Host](<../../20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) | 😐 Start risky task [Yes, No] | > Yes
    | 🆔 [Identity](<01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.   | [📸 selfie](<21 🆔😶 Face scan.md>)
    | 🤗 [Host](<../../20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Verified, task started!

    ---
    <br/>

1. **What are industry use cases for age verification?**

    |Industry|Use case 🤝
    |-|-
    |`Hospitality`|[🏨 Check-in when staying at a hotel](<../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/03 🏨 Guest @ Reception 🛎️/04 🛎️ Check-in.md>)
    |`Financial`|[🏧 Withdraw cash from an ATM](<../../../3 🤝 Use Cases/05 🛠️ Services/03 🏧 Withdraw at ATMs/10 Customer @ ATM/11 Withdraw cash.md>)
    |`Governments`|[🏛️ Request a proof of address](<../../../3 🤝 Use Cases/08 🏛️ Public Services/08 📮 Prove address/1 Customer @ Anywhere/11. Proof of Address.md>)
    |`Health`| [💍 Trigger a Userable emergency](<../../70 🌳 Ambient/74 💍 Brand Userables/02 💍🚨 Userable emergencies.md>)
    

    ---
    <br/>



3. **How does remote face verification works?**

    ![](<00 📎 Assets/🆔 Online.png>)

    When a user is requested by a [Host 🤗 domain](<../../20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) to verify their identity against a given [Locator 🔆](<../../20 🧑‍🦰 UI/04 🔆 Locators/01 🔆 Locator.md>), the following steps are executed.

    | # | Step
    |-|-
    |1| The user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) <br/>• opens a web-browser window <br/>• to the liveness check URL of the [Locator's Identity 🆔 vault](<01 🆔🫥 Identity agent.md>), <br/>• passing anti-fraud information like device location and device configurations.
    |2| The webpage of the [Identity 🆔 vault](<01 🆔🫥 Identity agent.md>) <br/>• activates the device's camera to record the user's video for liveness check <br/>• extracts the relevant images <br/>• and compares them to the user images on the given [Locator 🔆](<../../20 🧑‍🦰 UI/04 🔆 Locators/01 🔆 Locator.md>). 
    |3| Additionally, depending on the anti-fraud contextualized info, <br/>• the [Identity 🆔 vault](<01 🆔🫥 Identity agent.md>) asks security questions and one-time-passwords (OTP).

    ---
    <br/>


2. **How are users' face biometrics protected from Sellers?**

    NLWeb advocates for online face authentication between [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and [Identity 🆔 vaults](<01 🆔🫥 Identity agent.md>), without sharing user biometrics with [Seller 💵 domains](<../04 💳 Payers/01 💵🎭 Seller role.md>);
    - e.g., when a [Seller 💵 domain](<../04 💳 Payers/01 💵🎭 Seller role.md>) needs to match a person with a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), 
    - it contacts the [Token's  Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) to perform the authentication 
    - via the user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) in a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), 
    - and only return a success/failure to the [Seller 💵 domain](<../04 💳 Payers/01 💵🎭 Seller role.md>) . 
    
    When offline authentications are required, 
    * i.e. when the user only has a printed QR or and NFC card with the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), 
    * then the [Seller 💵 domain](<../04 💳 Payers/01 💵🎭 Seller role.md>) needs to take the user's picture 
    * with a fixed camera in a supervised fashion, 
    * then ask the [Token's  Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) to match the picture with the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), 
    * and then delete the picture according to regulatory requirements. 

    ---
    <br/>