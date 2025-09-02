🆔 Identity domains FAQ
===

1. **What is an Identity domain in NLWeb?**

    Identity 🆔 domains are [Vaults 🗄️](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) that help other domains ensure that the person physically holding the Wallet:
    * 😶 is the one mentioned in a given identification document, or
    * 🎴 is the one for whom a presented [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) was issued to, or
    * 🔏 is the one required to sign a given file.

    ---
    
1. **How do users set up an Identity domain?**

    ![](<00 📎 Assets/🆔 Biometrics.png>)

    Identity 🆔 domains require users to collect their biometric signatures in a supervised biometric collection center, typically managed by public authorities.
    
    Advantages of this restriction include: 
    - mitigated risk of identity fraud in supervised settings;
    - delegated trust in sovereign nations' management of citizen biometrics;
    - reduced AI risk exposure for domains requiring human authentication;
    - alignment with the Europe Union (EU) AI Act, released in 2024.

    The biometric center collects the user's biometrics (e.g., face, palm, voice), tag it to a limited set of verifiable codes (e.g., passport number, national ID, social security), and store it in compliance with data residency regulations.

    ---
    
1. **Do Identity domains always authenticate users the same way?**

    No. It depends on the legislation, registration, and context.

    - **Legislation**: different regions may have different ways to address biometric collection, so the authentication may be more or less automatic depending on the authorized mechanisms (e.g., China, the U.S., and the EU have different views on biometric collection and social credit systems);
    
    - **Registration**: a user may not have registered all possible ways of authentication, or may have opted out of some mechanisms for health or religious reasons;
    
    - **Context**: a user may be subject to extra validations if currently outside the country of residence, if too long has passed from the last authorization.

    ---
    
1. **How are users' biometrics protected from sellers?**

    NLWeb advocates for online face authentication between [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and Identity Vaults, without sharing user biometrics with [Seller 💵](<../04 💳 Payers/02 💵🎭 Seller role.md>) domains - e.g., when a Seller domain needs to match a person with a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), it contacts the Token's authentication domain to perform the authentication via the user's wallet in a chat, and only return a success/failure to the Seller. 
    
    When offline authentications are required, i.e. when the user only has a printed QR or and NFC card with the Token, then the Seller domain needs to take the user's picture with a fixed camera in a supervised fashion, then ask the Token's Identity domain to match the picture with the Token, and then delete the picture according to regulatory requirements. 

    ---
    
1. **Can users with dual nationality bind to two Identity domains?**

    Yes. Users with dual nationality may even have two or more bound Identity 🆔 domains, one per nationality. 

    ---
    
1. **What authentication mechanisms are supported by Wallets?**

    NLWeb natively supports key pairs (passkeys) and one time passwords (OTP). However, Identity 🆔 Vaults are free to implement whatever authentication mechanisms they want using the generic tools available. 
    
    For example: 
    - 1/ security questions can be implemented with generic inputs (e.g., text, lists, numbers); 
    - 2/ one time passwords (OTP) can be implemented with numeric inputs;
    - 3/ voice recognition can be implemented with audio inputs; 
    - 4/ simple face recognition can be implemented with selfie inputs; and 
    - 5/ complex web behaviors can be implemented with Web 2.0 i-frames.

    ---
    
1. **How is voice recognition secured with an audio input?**

    NLWeb discourages voice recognition as authentication method (except in supervised scenarios) because Generative AI can mimic a person's voice with 3 seconds of original audio.

    ---
    