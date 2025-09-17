🆔 Identity face verification FAQ
===


1. **What does the Chat look like?**

    Consider the following [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) as an example of [face verification 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/01 📺 Difference.md>).
        
    | Service | Prompt | User
    | - | - | - |
    | 🤗 [Host](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) | 😐 Start risky task [Yes, No] | > Yes
    | 🆔 [Identity](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.   | [📸 smile](<../../30 🫥 Agents/05 🆔 Identities/04 🆔😶 Face scan.md>)
    | 🤗 [Host](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) | ✅ Verified, task started!
    |


    Other use cases of [face verification 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/01 📺 Difference.md>) include.

    |Industry|Use case 🤝
    |-|-
    |`Travel`| [👨‍✈️ Start a shift as a taxi driver](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/9 🚕 Driver @ Car 👨‍✈️/01 👨‍✈️ Start shift.md>)
    |`Hospitality`|[🎰 Enter anonymously at a casino](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/08 🎰 Drink at casinos/1 Customer @ Door 🚪/11. Enter anonymously.md>)
    |`Hospitality`|[🏨 Check-in at a hotel](<../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/03 🏨 Guest @ Reception 🛎️/04 🛎️ Check-in.md>)
    |`Financial`|[🏧 Withdraw cash from an ATM](<../../../3 🤝 Use Cases/05 🛠️ Services/03 🏧 Withdraw at ATMs/10 Customer @ ATM/11 Withdraw cash.md>)
    |`Governments`|[🏛️ Request a proof of address](<../../../3 🤝 Use Cases/08 🏛️ Public Services/08 📮 Prove address/1 Customer @ Anywhere/11. Proof of Address.md>)
    |`Health`| [💍 Trigger a Userable emergency](<../../70 🌳 Ambient/74 💍 Brand Userables/02 💍🚨 Userable emergencies.md>)
    

    ---
    <br/>


2. **Can a Wallet authenticate someone other than the user?**

    Yes. 
    * A [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) owned by person `A` can authenticate a person `B` in a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) when the [Chat's Host 🤗 domain](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) invites the [Identity 🆔 vault](<03 🆔🫥 Identity agent.md>) of person `B` into the [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>).
    * This is particularly useful when working with [Userable 💍 things](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) where the owner's identity needs to be confirmed on [payments 🤝 scenarios](<../../70 🌳 Ambient/74 💍 Brand Userables/05 💍💳 Userable pay salesperson.md>) and [item recovery 🤝 scenarios](<../../70 🌳 Ambient/74 💍 Brand Userables/03 💍📱 Userable senior user.md>) via another [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    Consider the following [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) as an example.
        
    
    | Service | Prompt | User
    | - | - | - |
    | 🤗 [Host](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) | ℹ️ Userable 💍 presented.
    | 🤗 [Host](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) | 😃 Are you the owner? [Yes, No] | > No
    | 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Allow guest vaults? [Yes, No]  <br/> -  #1: Any Identity 🆔 <br/>- [ Always ] for Any Host 🤗 | > Always
    | 🆔 [Identity](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's the owner.   | [📸 smile](<../../30 🫥 Agents/05 🆔 Identities/04 🆔😶 Face scan.md>)
    | 🤗 [Host](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) | ✅ Ownership confirmed.
    |

    Other use cases of [face verification 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/01 📺 Difference.md>) for guest users include.

    |Industry|Use case 🤝
    |-|-
    |`Payments`|[payments 🤝 ](<../../70 🌳 Ambient/74 💍 Brand Userables/05 💍💳 Userable pay salesperson.md>) 
    |`Payments` | [💁‍♀️ Pay a restaurant bill with a Userable](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/03 🍽️🍲 Eat at restaurants/07 🍲 Staff @ Tables 💁‍♀️/04 💁‍♀️ Bill userable 💍.md>)|
    |`Social`| [💍 Aid a confused senior with a Userable](<../../70 🌳 Ambient/74 💍 Brand Userables/03 💍📱 Userable senior user.md>)


    ---
    <br/>


3. **How does remote face verification works?**

    ![](<00 📎 Assets/🆔 Online.png>)

    When a user is requested by a [Host 🤗 domain](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) to verify their identity against a given [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>), the following steps are executed.

    | # | Step
    |-|-
    |1| The user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) <br/>• opens a web-browser window <br/>• to the liveness check URL of the [Locator's Identity 🆔 vault](<03 🆔🫥 Identity agent.md>), <br/>• passing anti-fraud information like device location and device configurations.
    |2| The webpage of the [Identity 🆔 vault](<03 🆔🫥 Identity agent.md>) <br/>• activates the device's camera to record the user's video for liveness check <br/>• extracts the relevant images <br/>• and compares them to the user images on the given [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>). 
    |3| Additionally, depending on the anti-fraud contextualized info, <br/>• the [Identity 🆔 vault](<03 🆔🫥 Identity agent.md>) asks security questions and one-time-passwords (OTP).

    ---
    <br/>


2. **How are users' face biometrics protected from Sellers?**

    NLWeb advocates for online face authentication between [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and [Identity 🆔 vaults](<03 🆔🫥 Identity agent.md>), without sharing user biometrics with [Seller 💵 domains](<../04 💳 Payers/01 💵🎭 Seller role.md>);
    - e.g., when a [Seller 💵 domain](<../04 💳 Payers/01 💵🎭 Seller role.md>) needs to match a person with a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), 
    - it contacts the [Token's  Identity 🆔 domain](<03 🆔🫥 Identity agent.md>) to perform the authentication 
    - via the user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) in a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), 
    - and only return a success/failure to the [Seller 💵 domain](<../04 💳 Payers/01 💵🎭 Seller role.md>) . 
    
    When offline authentications are required, 
    * i.e. when the user only has a printed QR or and NFC card with the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), 
    * then the [Seller 💵 domain](<../04 💳 Payers/01 💵🎭 Seller role.md>) needs to take the user's picture 
    * with a fixed camera in a supervised fashion, 
    * then ask the [Token's  Identity 🆔 domain](<03 🆔🫥 Identity agent.md>) to match the picture with the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), 
    * and then delete the picture according to regulatory requirements. 

    ---
    <br/>

3. **How is face recognition secured with a selfie input?**

    NLWeb discourages face recognition via selfie inputs (except in supervised scenarios) because bad actors can inject a fake picture. 
    
    - Instead, NLWeb recommends using liveness checks from a remote service exposed via a Web 2.0 browser;
    - e.g., by using Amazon Rekognition Face Liveness or other similar products. 

    ---
    <br/>
    
4. **How is face recognition secured with remote liveness checks?**

    Services implementing liveness checks mitigate frauds and replay attacks even if the device of the [ Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) is running a sophisticated forgery software, is being used by an AI bot, or has been compromised by an attacker. 
    
    Liveness checks are video-based checks supported by a remote Web 2.0 page that typically include the following features:
    
    - **Facial motion analysis**: Tracks real-time facial movements like blinking.
    
    - **Challenge-response**: Prompts users to perform actions, making it hard for fraudulent software to mimic.
    
    - **Presentation attacks detection**: Detects spoof attacks presented to the camera, such as printed 2D photos, 2D cut-out paper masks, and hi-res photos or videos on a digital screen.
    
    - **Bypass attacks detection**: Detects spoof attacks that bypass the camera, such as pre-recorded, synthetic, and deepfake videos directly injected into the video capture sub-system.
    
    - **3D mask attacks detection**: Detects spoof attacks that use 3D masks made of silicone, latex, plastic, cloth, and more.
    
    ---
    <br/>
    
    
5. **What's the error rate on liveness checks?**

    Amazon’s Face Liveness feature has been independently tested by iBeta Quality Assurance, a NIST/NVLAP-accredited lab, under ISO/IEC 30107‑3 PAD (Presentation Attack Detection) standards.

    - Level 1 test, conducted in September 2023, on a Samsung Galaxy S21 running Android 12. It assessed 900 spoof presentation attacks and resulted in an Attack Presentation Classification Error Rate (APCER) of 0%. The Bona Fide Presentation Classification Error Rate (BPCER) is also available in the full report. 
    Amazon Web Services, Inc.

    - Level 2 test, conducted in October 2023, also on the same device and OS, with 750 spoof attempts, likewise returned an APCER of 0%. BPCER details are in the final report. 

    The confirmation letters (PDFs) are available on the iBeta website, although the full BPCER statistics aren't public in those letters.

    ---
    <br/>

1. **What are the conditions for face biometrics to be spoofed?**

    On NLWeb, the [face biometric verification 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/01 📺 Difference.md>) works as follows:

    - the user always first presents something they own (e.g., a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)) plus context information (e.g., GPS coordinates and device configuration);

    - then the user almost always presents who they are (e.g., their face, with a liveness check), which may be skipped soon after a successful authentication around the same geographic region with the same device;

    - eventually, in highly secure scenarios, the user may also have to present something they know (e.g., a password).

    To be able to spoof the authentication, an attacker would have to have the user's device and be able to inject a stream that passes a liveness check. Occasionally, the password also.

    - This is already more secure than a Visa touchless payment, where only the card is required to be presented always, and the password is required occasionally.

    ---
    <br/>