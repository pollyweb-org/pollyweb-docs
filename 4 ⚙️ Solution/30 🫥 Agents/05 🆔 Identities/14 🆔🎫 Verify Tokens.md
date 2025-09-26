🎫 Identity-bound Tokens FAQ
===

> Part of [Identity 🆔 domains](<01 🆔🫥 Identity agent.md>)

 <br/>


2. **What is an Identity-bound Token?**

    An [Identity-bound Token 🎫](<14 🆔🎫 Verify Tokens.md>)
    * is a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
    * that was [issued 🎴](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) to a specific person.

    ---
    <br/>


2. **What are the benefits of Token Identity binding?**

    Identity binding 
    * allows [Issuer 🎴 domains](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) to lock a given [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to a specific human, 
    * independent of the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) is stored in, 
    * or whoever is holding that [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) when presenting the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>);
    * e.g., a passport belongs to a specific person, regardless of who is holding the passport in their hands.

    ---
    <br/>


1. **What does a Chat look like?**

    Consider the following [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) as an example.

    | Service | Prompt | User
    | - | - | - |
    | 🤗 [Host](<../../20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) | 😃 A beer? [Yes, No]         | > Yes
    | 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Share over 21? [Yes, No]     | > Yes
    | 🆔 [Identity](<01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.  | [📸 selfie](<21 🆔😶 Face scan.md>)
    | 🤗 [Host](<../../20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) | ✅ A beer coming up!

    ---
    <br/>

2. **What are use cases for minimum age verification?**

    |Type|Use case 🤝
    |-|-
    | `Vending` | [🍺 Buy beer at a vending machine](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/12 🍺 Buy beer.md>)
    | `Casinos`|[🎰 Enter anonymously at a casino](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    |`Restaurants`|[🍽️ Order wine at restaurant](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/52 🪑 Seat: Order wine 🍷.md>)
    |`Bars`|[🍸 Order a beer at a bar](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/22 🪑 Seat: Order a beer.md>)
    |`Clubs`|[🕺 Buy an entry at a night club](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/12 🌐 Web: Buy entry 🎟️.md>)


    ---
    <br/>

2. **What are use cases for staff starting a shift?**

    |Type|Use case 🤝
    |-|-
    |`Taxis`| [👨‍✈️ Start a shift as a taxi driver](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/9 🚕 Driver @ Car 👨‍✈️/01 👨‍✈️ Start shift.md>)
    |`Street food`|[🌭 Start shift as a street food chef](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/91 🧑‍🍳 Chef: Start shift 🪪.md>)
    |`Restaurants`|[🧑‍🍳 Start shift as a restaurant chef](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/81 🧑‍🍳 Chef: Start shift 🪪.md>)
    |`Pizza places`|[🍕 Start shift as a chef at a pizza place](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/61 🧑‍🍳 Chef: Start shift.md>)
    |`Pizza places`|[💁‍♀️ Start shift as staff at a pizza place](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/71 💁‍♀️ Staff: Start shift.md>)
    |`Delivery`|[🛵 Start shift as a delivery driver](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/81 🛵 Driver: Start shift.md>)
    |`Bars`|[🍸 Start shift as a barista](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/31 💁‍♀️ Barista: Serve.md>)
    |`Night Clubs` | [👮 Start shift as a bouncer](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/71 👮 Bouncer: Protect door.md>)
    ||[🍺 Start shift as a barista](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/81 💁‍♀️ Barista: Start shift.md>)
    ---
    <br/>


3. **How do domains issue identity-bound Tokens?**

    ![](<00 📎 Assets/🆔 Tokens.png>)

    

    The flow of an [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) issuing an identity-bound [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) is as follows:
    - 1/ the user initiates a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) session with an [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>);
    - 2/ the user asks the [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) to issue a Token (e.g., flight ticket) 
        - this will depend on the specific workload;
    - 3/ the Issuer asks the user's Identity to generate a unique Identity Locator with a given expiration date:
        - unique locators prevent attackers from relating any two [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) from the same user;
        - expiration dates allow Identities to charge the Issuer for the commitment length;
    - 4/ the Issuer offers the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) for the user to download;
    - 5/ the user downloads the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) and stores it offline in the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    
3. **How do domains authenticate printed identity-bound Tokens?**

    ![](<00 📎 Assets/🆔 Offline.png>)

    Printed identity-bound [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) (or any other type of offline Tokens, like screenshot images, NFC cards, and NFC wristbands) removes user's need to carry their mobile phone charged and with internet connection. 
    - Use cases where this is important include: international flights, water sports, and luggage misplacement or theft.
    - These scenarios rely on [🖐️ palm vein scanners](<22 🆔🖐️ Palm scan.md>) scanning the users' palms, or cameras performing [😶 face scans](<21 🆔😶 Face scan.md>) on users.

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
    
4. **How do users authenticate identity-bound Tokens in their Wallets?**

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
    
5. **Can users prove eligibility anonymously?**

    Yes. 
    
    - Users can present a proof of age without disclosing their identity when: 
      - 1/ entering age-restricted venues (e.g., a casino); 
      - 2/ accessing minimum-age services (e.g., shop at a wine store); 
      - 3/ obtaining age benefits (e.g., buying discounted tickets for elderly); or 
      - 4/ claiming accessibility needs (e.g., a wheelchair at an airport). 
      
    - For that, users first need to bind their wallet to an [🆔 Identity Vault](<01 🆔🫥 Identity agent.md>) (typically a governmental authority that issues passports) to set up authentication mechanisms (e.g., voice and face biometric signatures collected in a supervised center) - users may then ask the Identity Vault for an age-related [Token 🎫](<14 🆔🎫 Verify Tokens.md>) (e.g., over 16 years old). 
    
    - When interacting with the [Seller 💵](<../04 💳 Payers/01 💵🎭 Seller role.md>)'s domain, the Seller can then ask for the Token before providing the service or granting the entrance. 
    
    - The Token can also be printed or saved into to an NCF card, so that users can access the venue or service even when their devices run out of battery.


    ---
    