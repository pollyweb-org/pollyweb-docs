🔏 User signatures FAQ
===

1. **How does NLWeb address digital signatures**?

    NLWeb advocates for senders to transfer files in PDF and PNG with a signature that receivers can verify - these two formats accept metadata and cover the majority of use cases where paper was traditionally used before computers became ubiquitous, from contracts to photographs.

    ---
    
1. **How do users sign a document?**

    ![](<00 📎 Assets/🆔 Signature.png>)

    On NLWeb, documents are files (e.g., PDF, PNG) - this allows users to visualize the full final version of the document, similar to what humans do today with any paper document. 

    A user signature is an offline Token issued by a trusted Identity confirming that:
    - 1/ the signature is for a file with the given hash; and
    - 2/ the human holding the [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) has the given personally identifiable information (PII).
    
    A signature request from a [Host 🤗](<../../20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) is a data set containing:
    - **the content of the file to be signed** - this allows the user to read the document before accepting to sign it;
    - **the file's hash** - this allows the Identity domain to [sign](<08 🆔🔏 User Signature.md>) a document on behalf of a user without knowing the content of the document;
    - **user PII (e.g., passport number)** - this allows the Identity domain to match the Host's intent with the user (e.g., ensure the request matches the tenant and not the landlord in a renting contract); 
    - **a signature placeholder ID**, representing the requested [signature](<08 🆔🔏 User Signature.md>) in the contract - this allows the Identity to reference the Host's original request.

    The flow of a user signing a PDF file is as follows:
    - 1/ the Host asks the Wallet for a user signature;
    - 2/ the Wallet validates the hash against the PDF bytes; 
    - 3/ the Wallet shows the PDF content to the user;
    - 4/ the user accepts the PDF content and the signature request;
    - 5/ the Wallet asks the user's Identity to sign the hash on the user's behalf; 
    - 6/ the Identity authenticates the user (e.g., with face biometrics);
    - 7/ the Identity issues a signature Token and sends it to the Host;
    - 8/ the Host verifies if the Token's data match the original request.

    ---
    
1. **How do users sign files?**

    ![](<00 📎 Assets/🆔 Signature Users.png>)

    Users do not sign files directly - instead, they ask their Identity domains to sign the files.  
    
    Users tell to their [Identity 🆔](<03 🆔🫥 Identity agent.md>) domain that they are happy with the document, and that they allow the Identity domain to sign the document on their behalf. 
    
    Identity domains perform additional validations to ensure that the wallet's owner is signing, and not an attacker impersonating them (e.g., face biometrics, geolocation, OTP). 
    
    The Token attached to the file is signed by the Identity domain, with an Identity-bound reference to the user.

    ---
    
1. **How do domains verify user signatures?**

    Domains accept user signatures verified by [Identity 🆔](<03 🆔🫥 Identity agent.md>) domains they [trust 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>). 
    
    When a domain sends a file for the user to sign, it sends also a placeholder ID of that user in the document (e.g., a renting contract needs signatures from the landlord, guarantor, and tenant). Identity domains include the received placeholder ID in the Token, matching the user to the placeholder ID. 
    
    Any domain can later ask the Identity domain for details about the signature (e.g., `Alex accepted the contract as tenant on July 3rd, using face biometrics, OTP, and a safe question`).

    ---
    
1. **What data is contained in a user-signature Token?**

    A user-signature Token contains:
    * the [Identity 🆔](<03 🆔🫥 Identity agent.md>) domain - e.g., `any-identity.com`
    * the user reference in the Identity domain - e.g., `user-1234`
    * the issue timestamp in UTC - e.g., `2024-09-21T12:34:00Z`
    * the sender's domain - e.g., `any-landlord.com`
    * the placeholder reference in the sender's domain - e.g., `contract-1234-tenent`
    * the file's hash - e.g., `pScF56kAQcFMj/2InwnfE36N6xphT+07R/8rKS5idWQ=`
    * and the [signature](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) of the Identity domain - e.g., `qD/fMEQDALK2FdZcWyy7wNns1gH8vssdOAuxxxKnEExDMMGZcZG0Dw14Xxfh3HDCpTGxvuLbtCSdJaBnEZg2G7kytG8RG/aGFM+lru7MQR81zze7GkBXmpxm+oilkXrouL63/5fQzwRBS94n7YH7abkrBi4RqPiV/mGiDsm2fLEqc12a5kOXZGPsbuuCWs8Mvbrt5teJUELiEgLnBYXArLYvofoZOt4EWYFBTXvx+/NSm1vtqsZsY+dnLLtZ7kEyUNW70jRdP0VK5ek4Rqdg3tUPVSeG7Rxl0ZH5KuvLVOnL4kbcC2CI/bijZ12YCrF3WLEdgF0KhZDjs5HvwNbZNw==`

    ---
    