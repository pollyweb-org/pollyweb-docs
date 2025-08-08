🎫 Tokens FAQ
===

![](<./📎 Assets/🎫 Token.png>)

1. **What is a Token?**

    Tokens are NFC/QR [Locators 🔆](<../22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>) issued and signed by an [Issuer 🎴](<02 ✅ 🎴🎭 Issuer role.md>), and containing information that can be shared with [💼 Consumers](<../../30 ⏳ 🫥 Agents/01 ✅ 📦 Storage/01 ✅ 📦🫥 Storage agent.md>).

    ---
    
1. **What are examples of Tokens?**

    Examples of Tokens include:
    - ⚽ event tickets (e.g., cinema, sports, live concerts)
    - 🛩️ public transport tickets (e.g., flight, train)
    - 🚌 public transport passes (e.g., return, monthly)
    - 🚗 personal documents (e.g., driver's license, passports)
    - 💉 identity-bound proofs (e.g., over 21, vaccines, disability)
    - 🎓 identity-bound credentials (e.g., graduation, professional)
    - 🔑 physical access rights (e.g., doors, gates)
    - 💻 digital access rights (e.g., logins, admin rights)
    - 👮 legal authority rights (e.g., police, business owner)
    - 🔏 digital signatures (e.g., images, videos, PDF files)
    - 📦 delivery trackers (e.g., parcels, registered letters)
    - 🍲 bookings (e.g., restaurants, medical appointments)

    ---
    
1. **Tokens be downloaded into the Wallet?**

    Yes, thus the term [Wallet 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) when referring to NLWeb browsers. 

    ---
    
1. **Are Tokens compatible with W3C Verifiable Credentials?**

    No, but they are similar in purpose.

    ---
    
1. **Are these crypto tokens from blockchain?**

    No. NLWeb does not use blockchain nor cryptocurrencies. 

    ---
    
1. **Can Tokens be used for documents with photo validation?**

    Yes, Tokens can be identity-bound - i.e., they can allow [💼 Consumers](<../../30 ⏳ 🫥 Agents/01 ✅ 📦 Storage/01 ✅ 📦🫥 Storage agent.md>) to confirm that the holder of the Token is effectively the human for whom the Token was issue to. 
    
    Identity-bound Tokens reference a trusted [Identity 🆔](<../../30 ⏳ 🫥 Agents/05 ✅ 🆔 Identities/03 ✅ 🆔🫥 Identity agent.md>) domain that is able to authenticate the user (e.g., with a face scan).

    ---
    
1. **Can users share Tokens in Wallets without internet?**

    Not via [Wallets 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>), no, because Wallets need internet to share the Token with other domains. 
    
    Note: NLWeb assumes the inevitability of internet becoming ubiquitous in time - in 2024, internet is already available on London subways, on United Airline flights, and in remote regions of the globe with Starlink, while Project Kuiper is on track general availability in 2026.

    ---
    
1. **Can users print Tokens in paper?**

    Yes. Offline Tokens allow users to remove the dependency on the device's battery, or technical issues with the Wallet resulting from low or no internet connectivity (e.g., travelers in long-distance flights are advised to store their ticket and passport Tokens offline). 
    
    Offline options include:
    - print on paper;
    - screenshot and store as an image on a device;
    - save to an NFC card;
    - save to an NFC wristband.

    ---
    
1. **Can users save multiple Tokens in a single NFC card?**

    Yes. Users can reference multiple Tokens with a single NFC via [Userables 💍](<../../70 ✅ 🌳 Ambient/74 ✅ 💍 Brand Userables/01 ✅ 💍 Userable thing.md>).

    ---
    
1. **How are users protected from attacks on Tokens?**

    To limit the attack surface to user data, NLWeb discourages user data from being saved on user devices.

    Instead, the recommendation is for domains to prefer online validations, while limiting tokens for situations where users need to be validated even when the issuer is offline (e.g., a passport needs to be valid if the issuing nation is at war, and flights cannot wait for travel agencies to come back online before allowing a traveler to board a plane). 
    
    When Tokens are required, they should contain none-or-minimum PII (e.g., a token issued by a government may confirm that the user holding the token is over 21 years old, without disclosing the user's age, birthdate, or name).

    ---
    
1. **What data is contained in a Token?**

    Tokens derive from [Locators 🔆](<../22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>), so they always contain:
    * the [Schema Code 🧩](<../24 ✅ 🗄️ Vaults/02 ✅ 🧩 Schema Code.md>) - e.g., `nlweb.org/TOKEN:1.0`
    * the [Issuer 🎴](<02 ✅ 🎴🎭 Issuer role.md>) domain - e.g., `any-issuer.com`
    * the resource key in the Issuer domain - e.g., `certificate-XYZ`
    * any optional data fields.

    Additionally, a basic Token contains:
    * the Token's specific [Schema Code 🧩](<../24 ✅ 🗄️ Vaults/02 ✅ 🧩 Schema Code.md>) - e.g., `who.int/VACCINES/COVID-2:1.0`
    * the timestamp when it was issued, in UTC - e.g., `2024-09-21T12:34:00Z`
    * and the Issuer's [signature](<../../40 ✅ 👥 Domains/41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>) 🔏 - e.g., `qD/fMEQDALK2FdZcWyy7wNns1gH8vssdOAuxxxKnEExDMMGZcZG0Dw14Xxfh3HDCpTGxvuLbtCSdJaBnEZg2G7kytG8RG/aGFM+lru7MQR81zze7GkBXmpxm+oilkXrouL63/5fQzwRBS94n7YH7abkrBi4RqPiV/mGiDsm2fLEqc12a5kOXZGPsbuuCWs8Mvbrt5teJUELiEgLnBYXArLYvofoZOt4EWYFBTXvx+/NSm1vtqsZsY+dnLLtZ7kEyUNW70jRdP0VK5ek4Rqdg3tUPVSeG7Rxl0ZH5KuvLVOnL4kbcC2CI/bijZ12YCrF3WLEdgF0KhZDjs5HvwNbZNw==`

    An identity-bound Token also contains:
    * the [Identity 🆔](<../../30 ⏳ 🫥 Agents/05 ✅ 🆔 Identities/03 ✅ 🆔🫥 Identity agent.md>) domain - e.g., `any-identity.com`
    * the resource key in the Identity domain - e.g., `person-1234`

    ---
    