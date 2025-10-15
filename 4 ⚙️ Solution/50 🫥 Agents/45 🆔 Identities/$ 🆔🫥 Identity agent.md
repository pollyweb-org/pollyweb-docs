🆔 Identity agent
===

1. **What is an Identity domain in NLWeb?**

    An Identity 🆔 domain
    * is an [Agent 🫥 vault](<../$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) 
    * that verifies the identity of the user
    * on behalf of other [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>).

    ---
    <br/>

1. **How is this chapter broken down?**

    |Category|Section|Purpose
    |-|-|-
    |`Registration` | [👮 Register biometrics](<02 🆔👮 Register biometrics.md>)| Map user biometrics to their Wallet.
    |`Verification` |[🧑‍🦰 Verify Wallets](<13 🆔🧑‍🦰 Verify Wallets.md>) | Verify is its the Wallet's owner.
    ||[🎫 Verify Tokens](<14 🆔🎫 Verify Tokens.md>) | Verify if it's Token's legit holder.
    ||[💍 Verify Userables](<15 🆔💍 Verify Userables.md>) | Verify if it's the Userable's owner.
    ||[🔏 Verify Signatures](<16 🆔🔏 Verify Signatures.md>) | Verify is its the Wallet's owner.
    |`Technology`|[😶 Face scans](<21 🆔😶 Face scan.md>) | Liveness checks on user devices.
    ||[🖐️ Palm scans](<22 🆔🖐️ Palm scan.md>) | Alternative to face in public spaces.



    ---
    <br/>

1. **Why are Identity domains important?**

    They ensure that the person physically holding the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    * is either is the mentioned in the identification document,
    * or is the one to whom the [Token 🎫](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) was issued to, 
    * or is the one required to sign a given file.

    ---
    <br/>
    

    
    
1. **Do Identity domains always authenticate users the same way?**

    No. It depends on the legislation, registration, and context.

    - **Legislation**: different regions may have different ways to address biometric collection, so the authentication may be more or less automatic depending on the authorized mechanisms (e.g., China, the U.S., and the EU have different views on biometric collection and social credit systems);
    
    - **Registration**: a user may not have registered all possible ways of authentication, or may have opted out of some mechanisms for health or religious reasons;
    
    - **Context**: a user may be subject to extra validations if currently outside the country of residence, if too long has passed from the last authorization.

    ---
    <br/>
    
1. **Can users with dual nationality bind to two Identity domains?**

    Yes. 
    * Users with dual nationality may even have two or more bound [Identity 🆔 vault](<$ 🆔🫥 Identity agent.md>), one per nationality. 

    ---
    <br/>
    
1. **What authentication mechanisms are supported by Wallets?**

    NLWeb natively supports key pairs (passkeys) and one time passwords (OTP). 
    * However, [Identity 🆔 vault](<$ 🆔🫥 Identity agent.md>) are free to implement whatever authentication mechanisms they want using the generic tools available. 
    
    For example: 
    - security questions can be implemented with generic inputs (e.g., text, lists, numbers); 
    - one time passwords (OTP) can be implemented with numeric inputs;
    - voice recognition can be implemented with audio inputs; 
    - simple face recognition can be implemented with selfie inputs; and 
    - complex web behaviors can be implemented with Web 2.0 i-frames.

    ---
    <br/>
    
1. **How is voice recognition secured with an audio input?**

    NLWeb discourages voice recognition as authentication method,
    * except in [supervised 👮 scenarios](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/06 👮 Supervised ID landscape/00 👮 Supervised ID Index.md>) (e.g., a government office),
    * because Generative AI can mimic a person's voice with 3 seconds of original audio.

    ---
    <br/>
    