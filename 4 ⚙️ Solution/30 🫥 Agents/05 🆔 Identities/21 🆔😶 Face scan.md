🆔 Identity face verification FAQ
===

> Part of [Identity 🆔 domains](<01 🆔🫥 Identity agent.md>)

<br/> 


1. **What is a face verification?**

    A [Face scan 😶](<21 🆔😶 Face scan.md>)
    * is a [face verification 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/01 📺 Difference.md>)  by an [Identity 🆔 vault](<01 🆔🫥 Identity agent.md>) 
    * to verify if the person in front of the camera
    * is really the owner of something they are presenting
    * has part of a multi-factor authentication workflow.
    
    ---
    <br/>

2. **What can users present in the first step of the flow?**
    
    | Presented | Question
    |-|-
    | 🧑‍🦰 [Wallet](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) | Is it really the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) owner holding the device?
    |[🎫 Token](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)| Was the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) really issued to the person holding the device?
    |[💍 Userable](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>)| Is it really the [Userable 💍](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) owner [tapping 🔆](<../../20 🧑‍🦰 UI/04 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) it on a scanner?
  
    ---
    <br/>



3. **How is face recognition secured with a selfie input?**

    NLWeb discourages face recognition via selfie pictures,
    * except in [supervised 👮 scenarios](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/00 👮 Supervised ID Index.md>) (e.g., a government office),
    * because hackers can use [Generative AI 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/08 📺 Deep fakes.md>) to interfere with the device's face biometrics.
    
    Instead, 
    - NLWeb recommends using [liveness-checks 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/09 📺 Amazon liveness.md>) from a remote service exposed via a Web 2.0 browser;
    - e.g., by using Amazon Rekognition Face Liveness or other similar products. 

    ---
    <br/>
    
4. **How is face recognition secured with remote liveness checks?**

    Services implementing [liveness-checks 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/09 📺 Amazon liveness.md>) mitigate frauds and replay attacks even if the device of the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) is running a sophisticated forgery software, is being used by an AI bot, or has been compromised by an attacker. 
    
    Liveness checks are video-based checks supported by a remote Web 2.0 page that typically include the following features:
    
    - **Facial motion analysis**: Tracks real-time facial movements like blinking.
    
    - **Challenge-response**: Prompts users to perform actions, making it hard for fraudulent software to mimic.
    
    - **Presentation attacks detection**: Detects spoof attacks presented to the camera, such as printed 2D photos, 2D cut-out paper masks, and hi-res photos or videos on a digital screen.
    
    - **Bypass attacks detection**: Detects spoof attacks that bypass the camera, such as pre-recorded, synthetic, and deepfake videos directly injected into the video capture sub-system.
    
    - **3D mask attacks detection**: Detects spoof attacks that use 3D masks made of silicone, latex, plastic, cloth, and more.
    
    ---
    <br/>
    
    
5. **What's the error rate on liveness checks?**

    Amazon’s Face [liveness-checks 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/09 📺 Amazon liveness.md>) feature has been independently tested by iBeta Quality Assurance, a NIST/NVLAP-accredited lab, under ISO/IEC 30107‑3 PAD (Presentation Attack Detection) standards.

    - Level 1 test, conducted in September 2023, on a Samsung Galaxy S21 running Android 12. It assessed 900 spoof presentation attacks and resulted in an Attack Presentation Classification Error Rate (APCER) of 0%. The Bona Fide Presentation Classification Error Rate (BPCER) is also available in the full report. 
    Amazon Web Services, Inc.

    - Level 2 test, conducted in October 2023, also on the same device and OS, with 750 spoof attempts, likewise returned an APCER of 0%. BPCER details are in the final report. 

    The confirmation letters (PDFs) are available on the iBeta website, although the full BPCER statistics aren't public in those letters.

    ---
    <br/>

6. **What are the conditions for face biometrics to be spoofed?**

    On NLWeb, the [face biometric verification 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/01 📺 Difference.md>) works as follows:

    - the user always first presents *something they own* (e.g., a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)) plus context information (e.g., GPS coordinates and device configuration);

    - then the user almost always presents *who they are* (e.g., their face, with a liveness check), which may be skipped soon after a successful authentication around the same geographic region with the same device;

    - eventually, in highly secure scenarios, the user may also have to present *something they know* (e.g., a password).

    To be able to spoof the authentication, an attacker would have to have the user's device and be able to inject a stream that passes a liveness check. Occasionally, the password also.

    - This is already more secure than a Visa touchless payment, where only the card is required to be presented always, and the password is required occasionally.

    ---
    <br/>


1. **What are examples of unsupervised face biometrics in use today?**

    * [🌎 Uber 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/01 📺 Uber remote ID.md>) authenticates drivers with face biometrics before rides.
    * [🇬🇧 Al Rayan Bank UK 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/02 📺 🇬🇧 Al Rayan Bank UK.md>) remotely onboards new customers using face biometrics with movement-based liveness checks.
    * [🇸🇬 Singapore 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/04 🆔 Digital ID landscape/10 📺 🇸🇬 Singapore's DID.md>) adopted face biometrics with color-based liveness checks for their national identity program.
    * [🇸🇬 OCBC Bank Singapore 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/04 📺 🇸🇬 OCBC Bank.md>) customers withdraw money from ATMs using face biometrics with color-based liveness checks.
    

    ---
    <br/>

2. **How does NLWeb face verification compares with other technologies?**

    The following table compares some of the top payment technologies.
    * NLWeb has a high security when we evaluate what the user has, is, and knows.

    | Something<br/>the user | Apple<br/>Pay | Google<br/>Pay | Asian<br/>Wallets | NLWeb <br/>Wallet | Western<br/>ATMs | Asian<br/>ATMs | NLWeb<br/>Userable |
    |-|-|-|-|-|-|-|-
    | `Has`   | Phone | Phone | QR code | [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) | NFC card | - | [NFC 💍](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) |
    | `Is`    | - | - | - | [Face 📸](<21 🆔😶 Face scan.md>) | - | Face | [Face 📸](<21 🆔😶 Face scan.md>) |
    | `Knows` | - | - | - | [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) | Card pin | User pin | [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) |
    | `Screen`<br/>`Lock ⚠️` | Pin, Face,<br/>Fingers | Pin, Face,<br/>Fingers | Pin, Face,<br/>Fingers | Pin, Face,<br/>Fingers | - | - | - |
    |


    ⚠️ Warning note:
    * Apple's and Google's face biometrics doesn't verify if the user holding the phone is the expected one for the presented payment token (e.g., the owner of the Visa card that has their name written on the card).
    * Instead, it only verifies if the user holding the phone has their biometrics registered to unlock the phone (e.g., a bored 11-years-hold child).
  
    See the following resources for details:
    - Apple's [🍏 Face ID 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/05 📺 Apple Face ID.md>) is design for *users* to unlock phones, and not to authenticate the *owner*;
    - the owner's [family members 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/06 📺 Apple's security.md>) can also unlock the phone and perform transactions;
    - thieves can [replace the face ID 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/07 📺 Apple's thief.md>) to drain the owner's bank accounts.



    ---
    <br/>