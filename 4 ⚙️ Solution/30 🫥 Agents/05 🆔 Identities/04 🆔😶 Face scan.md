🆔 Identity face scans FAQ
===

1. **What are examples of remote face verification?**

    |Category|Purpose
    |-|-
    |[💍 Userable guests](<../../70 🌳 Ambient/74 💍 Brand Userables/03 💍📱 Userable lost phone.md>) | View private contacts from a guest device.
    |[🎫 Identity Tokens](<../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/03 🏨 Guest @ Reception 🛎️/04 🛎️ Check-in.md>)| Share identity on hotel check-ins.

    ---
    <br/>

2. **How does remote face verification works?**

    ![](<00 📎 Assets/🆔 Online.png>)

    When a user is requested by a [Host 🤗 domain](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) to verify their identity against a given [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>), the following steps are executed.

    | # | Step
    |-|-
    |1| The user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) opens a web-browser window to the liveness check URL of the [Locator's Identity 🆔 vault](<03 🆔🫥 Identity agent.md>), passing anti-fraud information like device location and device configurations.
    |2| The webpage of the [Identity 🆔 vault](<03 🆔🫥 Identity agent.md>) activates the device's camera to record the user's video for liveness check. It then extracts the relevant images and compares them to the user images on the given [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>).

    ---
    <br/>


2. **How are users' face biometrics protected from Sellers?**

    NLWeb advocates for online face authentication between [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and [Identity 🆔 vaults](<03 🆔🫥 Identity agent.md>), without sharing user biometrics with [Seller 💵 domains](<../04 💳 Payers/01 💵🎭 Seller role.md>);
    - e.g., when a [Seller 💵 domain](<../04 💳 Payers/01 💵🎭 Seller role.md>) needs to match a person with a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), 
    - it contacts the [Token's  Identity 🆔 domain](<03 🆔🫥 Identity agent.md>) to perform the authentication via the user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) in a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), 
    - and only return a success/failure to the [Seller 💵 domain](<../04 💳 Payers/01 💵🎭 Seller role.md>) . 
    
    When offline authentications are required, 
    * i.e. when the user only has a printed QR or and NFC card with the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), 
    * then the [Seller 💵 domain](<../04 💳 Payers/01 💵🎭 Seller role.md>) needs to take the user's picture with a fixed camera in a supervised fashion, 
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