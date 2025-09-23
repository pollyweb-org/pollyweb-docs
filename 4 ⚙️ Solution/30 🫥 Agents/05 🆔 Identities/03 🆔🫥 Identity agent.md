🆔 Identity agent FAQ
===

1. **What is an Identity domain in NLWeb?**

    An Identity 🆔 domain
    * is an [Agent 🫥 vault](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) 
    * that verifies the identity of the user
    * on behalf of other [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).

    They ensure that the person physically holding the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    * is either is the mentioned in the identification document,
    * or is the one to whom the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) was issued to, 
    * or is the one required to sign a given file.

    ---
    <br/>
    
1. **What are examples of Identity domain usage?**

    |Scenario |
    |-
    |[🏪 Buy beer at a vending machine 🍺](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/01 🏪 Drink at vendings/12 🏪 Buy beer 🍺.md>)

    ---
    <br/>
    
2. **How do users set up an Identity domain?**

    ![](<00 📎 Assets/🆔 Biometrics.png>)

    [Identity 🆔 vaults](<03 🆔🫥 Identity agent.md>) require users to collect their biometric signatures in a [supervised 👮](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/00 👮 Supervised ID Index.md>) biometric collection center, typically managed by public authorities.
    
    Advantages of this restriction include: 
    - mitigated risk of identity fraud in supervised settings;
    - delegated trust in sovereign nations' management of citizen biometrics;
    - reduced AI risk exposure for domains requiring human authentication;
    - alignment with the Europe Union (EU) AI Act, released in 2024.

    The biometric center:
    * collects the user's biometrics (e.g., face, palm, voice), 
    * tags it to a limited set of verifiable codes (e.g., passport number, national ID, social security), 
    * and stores it in compliance with data residency regulations.

    ---
    <br/>
    
3. **Do Identity domains always authenticate users the same way?**

    No. It depends on the legislation, registration, and context.

    - **Legislation**: different regions may have different ways to address biometric collection, so the authentication may be more or less automatic depending on the authorized mechanisms (e.g., China, the U.S., and the EU have different views on biometric collection and social credit systems);
    
    - **Registration**: a user may not have registered all possible ways of authentication, or may have opted out of some mechanisms for health or religious reasons;
    
    - **Context**: a user may be subject to extra validations if currently outside the country of residence, if too long has passed from the last authorization.

    ---
    <br/>
    
4. **Can users with dual nationality bind to two Identity domains?**

    Yes. 
    * Users with dual nationality may even have two or more bound [Identity 🆔 vault](<03 🆔🫥 Identity agent.md>), one per nationality. 

    ---
    <br/>
    
5. **What authentication mechanisms are supported by Wallets?**

    NLWeb natively supports key pairs (passkeys) and one time passwords (OTP). 
    * However, [Identity 🆔 vault](<03 🆔🫥 Identity agent.md>) are free to implement whatever authentication mechanisms they want using the generic tools available. 
    
    For example: 
    - security questions can be implemented with generic inputs (e.g., text, lists, numbers); 
    - one time passwords (OTP) can be implemented with numeric inputs;
    - voice recognition can be implemented with audio inputs; 
    - simple face recognition can be implemented with selfie inputs; and 
    - complex web behaviors can be implemented with Web 2.0 i-frames.

    ---
    <br/>
    
6. **How is voice recognition secured with an audio input?**

    NLWeb discourages voice recognition as authentication method,
    * except in [supervised 👮 scenarios](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/00 👮 Supervised ID Index.md>) (e.g., a government office),
    * because Generative AI can mimic a person's voice with 3 seconds of original audio.

    ---
    <br/>
    