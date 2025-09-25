🆔 Identity-bound tokens FAQ
===

> Part of [🆔 Identity domains](<01 🆔🫥 Identity agent.md>)

 <br/>



1. **How do domains issue identity-bound Tokens?**

    ![](<00 📎 Assets/🆔 Tokens.png>)

    Identity binding allows [Issuers 🎴](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) to lock a given [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to a specific human, independent of the Wallet the Token is stored in, or whoever is holding that Wallet when presenting the Token (e.g., a passport belongs to a specific person, regardless of who is holding the passport in their hands).

    The flow of an Issuer issuing an identity-bound Token is as follows:
    - 1/ the user initiates a chat session with an Issuer domain;
    - 2/ the user asks the Issuer to issue a Token (e.g., flight ticket) 
        - this will depend on the specific workload;
    - 3/ the Issuer asks the user's Identity to generate a unique Identity Locator with a given expiration date:
        - unique locators prevent attackers from relating any two Tokens from the same user;
        - expiration dates allow Identities to charge the Issuer for the commitment length;
    - 4/ the Issuer offers the Token for the user to download;
    - 5/ the user downloads the Token and stores it offline in the [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    
2. **How do domains authenticate printed identity-bound Tokens?**

    ![](<00 📎 Assets/🆔 Offline.png>)

    Printed identity-bound [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) (or any other type of offline Tokens, like screenshot images, NFC cards, and NFC wristbands) removes user's need to carry their mobile phone charged and with internet connection. 
    - Use cases where this is important include: international flights, water sports, and luggage misplacement or theft.
    - These scenarios rely on [🖐️ palm vein scanners](<11 🆔🖐️ Palm scan.md>) scanning the users' palms, or cameras performing [😶 face scans](<10 🆔😶 Face scan.md>) on users.

    The flow for a user to share an offline [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) with a [Consumer 💼](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) is as follows:
    - 1/ the user taps or scans the Token on the Consumer's scanner:
        - at airports, this can be the border-control gate for passport verification;
        - at an embassy or a bank, this can be a fixed kiosk;
        - at a traffic checkpoint, this can be a police agent holding an Android device;
    - 2/ the Consumer verifies the Trust relationships with the Token's Issuer and Identity;
    - 3/ the Consumer verifies if the Token's signature matches the Issuer's public key;
    - 4/ the Consumer collects the user's biometrics;
        - for general services, this can be a scanner taking the user's palm biometrics;
        - for authorized public services, this could be a camera on an mobile device;
    - 5/ the Consumer asks the Token's Identity to match the biometrics with the Identity Locator;
    - 6/ the Identity confirms to the Consumer that the biometrics match the Token owner.

    ---
    
3. **How do users authenticate identity-bound Tokens in their Wallets?**

    The flow for a user to share a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) with a [Consumer 💼](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) using their [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) is as follows:
    - 1/ the user initiates a chat session with a [Consumer 💼](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) domain;
    - 2/ the [Consumer 💼](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) asks the user to share [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) of a specific [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>):
        - if the [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) is marked as SELF and the [Consumer 💼](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) is the [Issuer 🎴](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>), then the sharing is silent;
        - otherwise, the user has to explicitly select the [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to share;
    - 3/ the [Consumer 💼](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) verifies if the Token's signature matches the [Issuer's 🎴](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) public key;
    - 4/ the [Consumer 💼](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) asks the [Identity 🆔](<01 🆔🫥 Identity agent.md>) domain in the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to authenticate the user, ensuring that the [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) holder is the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) owner (i.e. the human referenced in the Identity [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>)).
    - 5/ the [Identity 🆔](<01 🆔🫥 Identity agent.md>) authenticates the user (e.g., face scan, OTP, security questions);
    - 6/ the [Identity 🆔](<01 🆔🫥 Identity agent.md>) confirms to the [Consumer 💼](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) that the [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) holder is the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) owner.

    ---
    
4. **Can users prove eligibility anonymously?**

    Yes. 
    
    - Users can present a proof of age without disclosing their identity when: 
      - 1/ entering age-restricted venues (e.g., a casino); 
      - 2/ accessing minimum-age services (e.g., shop at a wine store); 
      - 3/ obtaining age benefits (e.g., buying discounted tickets for elderly); or 
      - 4/ claiming accessibility needs (e.g., a wheelchair at an airport). 
      
    - For that, users first need to bind their wallet to an [🆔 Identity Vault](<01 🆔🫥 Identity agent.md>) (typically a governmental authority that issues passports) to set up authentication mechanisms (e.g., voice and face biometric signatures collected in a supervised center) - users may then ask the Identity Vault for an age-related [Token 🎫](<04 🆔🎫 Verify Tokens.md>) (e.g., over 16 years old). 
    
    - When interacting with the [Seller 💵](<../04 💳 Payers/01 💵🎭 Seller role.md>)'s domain, the Seller can then ask for the Token before providing the service or granting the entrance. 
    
    - The Token can also be printed or saved into to an NCF card, so that users can access the venue or service even when their devices run out of battery.


    ---
    