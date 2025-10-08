<!--
TODO: Create the API methods
-->

🔏 Verify user signatures in files FAQ
===

> Part of [Identity 🆔 domains](<01 🆔🫥 Identity agent.md>)

<br/> 

1. **How does NLWeb address digital signatures**?

    NLWeb advocates for senders to transfer files in PDF and PNG with a signature that receivers can verify 
    * these two formats accept metadata and cover the majority of use cases where paper was traditionally used before computers became ubiquitous, from contracts to photographs.

    ---
    <br/> 
    
1. **What does the Chat look like?**

    Consider the following [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) as an example.
    
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/50 🤔 Prompts/1 📘 Prompt specs/01 🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🤗 [Host](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)    | ℹ️ Sign the terms. 
    | 🆔 [Identity](<01 🆔🫥 Identity agent.md>) | 🫥 Sign terms? 📄 [Yes, No] | > Yes
    | 🆔 [Identity](<01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<21 🆔😶 Face scan.md>)
    | 🤗 [Host](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Thanks for signing!

    ---
    <br/>

1. **What are use-cases of users signing documents?**

    |Type|Use case 🤝
    |-|-
    | `Hotels` | [🏨 Sign terms when booking a hotel](<../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/01 🏨 Guest @ Home 🏠/01 🏠 Book hotel.md>)
    | `Airlines`| [💺 Sign terms when checking into a flight](<../../../3 🤝 Use Cases/03 🧳 Travel/09 🧳 Travel by air 💺/14 💺 Ticket/05 Flight check in.md>)



    ---
    <br/>
    
1. **How do users sign a document?**


    On NLWeb, documents are files (e.g., PDF, PNG) 
    * this allows users to visualize the full final version of the document, similar to what humans do today with any paper document. 

    A user signature is an offline [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) issued by an [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) that they [trust 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) confirming that:
    - 1/ the signature is for a file with the given hash; and
    - 2/ the human holding the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) has the given personally identifiable information (PII).
    
    A signature request from a [Host 🤗 domain](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) is a data set containing:
    - **the content of the file to be signed** 
      - this allows the user to read the document before accepting to sign it;
    - **the file's hash** 
      - this allows the Identity domain to [sign 🔏](<16 🆔🔏 Verify Signatures.md>) a document on behalf of a user without knowing the content of the document;
    - **user PII (e.g., passport number)** - this allows the Identity domain to match the Host's intent with the user 
      - e.g., ensure the request matches the tenant and not the landlord in a renting contract; 
    - **a signature placeholder ID**, representing the requested [signature](<16 🆔🔏 Verify Signatures.md>) in the contract 
        - this allows the [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) to reference the Host's original request.

    ---
    <br/>


1. **How does it work?**

    ![](<00 📎 Assets/🆔 Signature.png>)

    The flow of a user signing a PDF file is as follows.

    |#|Step
    |-|-
    |1| [Hosts 🤗](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) ask [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) for a user signature
    | 2| [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) validate the hash against the PDF bytes
    | 3| [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) show the PDF content to the user
    | 4| Users accept the PDF content and the signature request;
    | 5| [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) ask [Identities 🆔](<01 🆔🫥 Identity agent.md>) to sign the hash on users' behalf 
    | 6| [Identities 🆔](<01 🆔🫥 Identity agent.md>) authenticate users (e.g., with face biometrics)
    | 7| [Identities 🆔](<01 🆔🫥 Identity agent.md>) issue a signature [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) and send it to [Hosts 🤗](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)
    | 8| [Hosts 🤗](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) verify if the Token's data matches the original request

    ---
    <br/> 
    
1. **How do users sign files?**

    ![](<00 📎 Assets/🆔 Signature Users.png>)

    Users do not sign files directly - instead, they ask their Identity domains to sign the files.  
    
    * Users tell to their [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>)  that they are happy with the document, and that they allow the [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) to sign the document on their behalf. 
    
    * [Identity 🆔 domains](<01 🆔🫥 Identity agent.md>)  perform additional validations to ensure that the wallet's owner is signing, and not an attacker impersonating them (e.g., face biometrics, geolocation, OTP). 
    
    * The [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) attached to the file is signed by the [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>), with an Identity-bound reference to the user.

    ---
    <br/> 
    
1. **How do domains verify user signatures?**

    Domains accept user signatures verified by [Identity 🆔 domains](<01 🆔🫥 Identity agent.md>) that they [trust 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>). 
    
    * When a domain sends a file for the user to sign, it sends also a placeholder ID of that user in the document 
      * e.g., a renting contract needs signatures from the landlord, guarantor, and tenant. 
      * [Identity 🆔 domains](<01 🆔🫥 Identity agent.md>) include the received placeholder ID in the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), matching the user to the placeholder ID. 
    
    * Any domain can later ask the [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) for details about the signature 
      * e.g., Alex accepted the contract as tenant on July 3rd, using face biometrics, OTP, and a safe question.

    ---
    <br/> 
    
1. **What data is contained in a user-signature file Token?**

    A user-signature file [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) contains:
    * the [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>)  - e.g., `any-identity.com`
    * the user reference in the [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) - e.g., `user-1234`
    * the issue timestamp in UTC - e.g., `2024-09-21T12:34:00Z`
    * the sender's domain - e.g., `any-landlord.com`
    * the placeholder reference in the sender's domain - e.g., `contract-1234-tenent`
    * the file's hash - e.g., `pScF56kAQcFMj/2InwnfE36N6xphT+07R/8rKS5idWQ=`
    * and the [signature](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) of the Identity domain - e.g., `qD/fMEQDALK2FdZcWyy7wNns1gH8vssdOAuxxxKnEExDMMGZcZG0Dw14Xxfh3HDCpTGxvuLbtCSdJaBnEZg2G7kytG8RG/aGFM+lru7MQR81zze7GkBXmpxm+oilkXrouL63/5fQzwRBS94n7YH7abkrBi4RqPiV/mGiDsm2fLEqc12a5kOXZGPsbuuCWs8Mvbrt5teJUELiEgLnBYXArLYvofoZOt4EWYFBTXvx+/NSm1vtqsZsY+dnLLtZ7kEyUNW70jRdP0VK5ek4Rqdg3tUPVSeG7Rxl0ZH5KuvLVOnL4kbcC2CI/bijZ12YCrF3WLEdgF0KhZDjs5HvwNbZNw==`

    ---
    <br/> 
    