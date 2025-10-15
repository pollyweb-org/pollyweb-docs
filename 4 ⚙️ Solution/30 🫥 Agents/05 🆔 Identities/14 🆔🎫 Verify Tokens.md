🎫 Identity-bound Tokens
===

> Part of [Identity 🆔 domains](<01 🆔🫥 Identity agent.md>)

 <br/>


1. **What is an Identity-bound Token?**

    An [Identity-bound Token 🎫](<14 🆔🎫 Verify Tokens.md>)
    * is a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
    * that was [issued 🎴](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) to a specific person.

    ---
    <br/>


1. **What are the benefits of Token Identity binding?**

    Identity binding 
    * allows [Issuer 🎴 domains](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) to lock a given [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to a specific human, 
    * independent of the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) is stored in, 
    * or whoever is holding that [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) when presenting the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>);
    * e.g., a passport belongs to a specific person, regardless of who is holding the passport in their hands.

    ---
    <br/>


1. **What does a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) look like?**

    | [Domain](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🤗 [Host](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 A beer? [Yes, No]         | > Yes
    | 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Share over 21? [Yes, No]     | > Yes
    | 🆔 [Identity](<01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.  | [📸 selfie](<21 🆔😶 Face scan.md>)
    | 🤗 [Host](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ A beer coming up!

    ---
    <br/>

1. **What are use cases for minimum age verification?**

    The following use cases demonstrate 
    * how to access age-restricted services 
    * while ensuring [zero-knowledge proof 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/02 🧢 Personalization landscape/08 📺 SSI zero knowledge proof.md>) 
    * i.e., without disclosing user's PII.

    |Type|Use case 🤝
    |-|-
    | `Vending` | [🍺 Buy beer at a vending machine](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/12 🍺 Buy beer.md>)
    | `Casinos`|[🎰 Enter anonymously at a casino](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    |`Restaurants`|[🍽️ Order wine at restaurant](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/52 🪑 Seat: Order wine 🍷.md>)
    |`Bars`|[🍸 Order a beer at a bar](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/22 🪑 Seat: Order a beer.md>)
    |`Clubs`|[🕺 Buy an entry at a night club](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/12 🌐 Web: Buy entry 🎟️.md>)


    ---
    <br/>

1. **What are use cases for staff starting a shift?**

    |Type|Use case 🤝
    |-|-
    |`Taxis`| [👨‍✈️ Start a shift as a taxi driver](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/9 🚕 Driver @ Car 👨‍✈️/01 👨‍✈️ Start shift.md>)
    |`Street food`|[🌭 Start shift as a street food chef](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/91 🧑‍🍳 Chef: Start shift 🪪.md>)
    |`Restaurants`|[🧑‍🍳 Start shift as a restaurant chef](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/81 🧑‍🍳 Chef: Start shift 🪪.md>)
    |`Pizza places`|[🍕 Start shift as a chef at a pizza place](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/61 🧑‍🍳 Chef: Start shift.md>)
    |`Pizza places`|[💁‍♀️ Start shift as staff at a pizza place](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/71 💁‍♀️ Staff: Start shift.md>)
    |`Delivery`|[🛵 Start shift as a delivery driver](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/81 🛵 Driver: Start shift.md>)
    |`Bars`|[🍸 Start shift as a barista](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/31 💁‍♀️ Barista: Serve.md>)
    |`Night Clubs` | [👮 Start shift as a bouncer in a night club](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/71 👮 Bouncer: Protect door.md>)
    |`Night Clubs` |[🍺 Start shift as a barista in a night club](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/81 💁‍♀️ Barista: Start shift.md>)
    ---
    <br/>


1. **How does it work?**

    ![](<. 📎 Assets/🆔 Tokens.png>)

    <br/>

    The flow of an [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) issuing a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) with [Identity 🆔](<01 🆔🫥 Identity agent.md>)  is as follows.

    |#|Category|Step
    |-|-|-
    | A| `Hello`| The user initiates a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) with an [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>): <br/>• the user asks the [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) to issue a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) (e.g., flight ticket).
    | B| `Locator` | The [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) asks the user's [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) to generate a unique [Identity Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) with a given expiration date:<br/>• unique [Locators 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) prevent attackers from relating any two [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) from the same user; <br/>• expiration dates allow [Identity 🆔 domains](<01 🆔🫥 Identity agent.md>) to charge the [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) for the commitment length.
    |C| `Token` | The [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) offers the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) for the user to download: <br/> • the user downloads the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) and stores it offline in the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>).
    |

    <br/>

    The flow for a user to share a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) with a [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) using their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) is as follows.

    |#|Category|Step
    |-|-|-
    | 1| `Share` | The user initiates a chat session with a [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>): <br/> • the [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) asks the user to share [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) of a specific [Schema Code 🧩](<../../25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>); <br/> • if the [Schema Code 🧩](<../../25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) is marked as `SELF` and the [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) is the [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>), then the sharing is silent;<br/> • otherwise, the user has to explicitly select the [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to share; <br/> • the [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) verifies if the signature of the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)  matches the [DKIM 📨](<../../40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>) of the [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>).
    | 2| `Verify` | The [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>), via the [Broker 🤵 domain](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>), asks the [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) in the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to verify the user, ensuring that the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) holder is the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) owner <br/> - i.e. the human referenced in the [Identity Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>).
    | 3 | `Selfie` | The [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) authenticates the user (e.g., face scan, OTP, security questions); <br/> • the [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) confirms to the [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) that the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) holder is the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) owner.


    ---
    <br/>
    
1. **How do domains authenticate printed identity-bound Tokens?**

    ![](<. 📎 Assets/🆔 Offline.png>)

    Printed identity-bound [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) (or any other type of offline Tokens, like screenshot images, NFC cards, and NFC wristbands) removes user's need to carry their mobile phone charged and with internet connection. 
    - Use cases where this is important include: international flights, water sports, and luggage misplacement or theft.
    - These scenarios rely on [🖐️ palm vein scanners](<22 🆔🖐️ Palm scan.md>) scanning the users' palms, or cameras performing [😶 face scans](<21 🆔😶 Face scan.md>) on users.

    The flow for a user to share an offline [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) with a [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) is as follows:
    - 1/ the user taps or scans the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) on the Consumer's scanner:
        - at airports, this can be the border-control gate for passport verification;
        - at an embassy or a bank, this can be a fixed kiosk;
        - at a traffic checkpoint, this can be a police agent holding an Android device;
    - 2/ the [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) verifies the [Trust 👍 relationships](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>)  with the [Token's Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) and [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>);
    - 3/ the [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) verifies if the [Token's 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) signature matches the [DKIM 📨](<../../40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>)  of the [Issuer 🎴 domain](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>);
    - 4/ the [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) collects the user's biometrics;
        - for general services, this can be a scanner taking the user's palm biometrics;
        - for authorized public services, this could be a camera on an mobile device;
    - 5/ the [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) asks the [Token's Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) to match the biometrics with the [Identity Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>);
    - 6/ the [Identity 🆔 domain](<01 🆔🫥 Identity agent.md>) confirms to the [Consumer 💼 domain](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) that the biometrics match the [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) owner.

    ---
    
    
1. **Can users prove eligibility anonymously?**

    Yes. 
    
    - Users can present a proof of age without disclosing their identity when: 
      - 1/ entering age-restricted venues (e.g., a casino); 
      - 2/ accessing minimum-age services (e.g., shop at a wine store); 
      - 3/ obtaining age benefits (e.g., buying discounted tickets for elderly); or 
      - 4/ claiming accessibility needs (e.g., a wheelchair at an airport). 
      
    - For that, users first need to bind their wallet to an [🆔 Identity Vault](<01 🆔🫥 Identity agent.md>) (typically a governmental authority that issues passports) to set up authentication mechanisms (e.g., voice and face biometric signatures collected in a supervised center) - users may then ask the Identity Vault for an age-related [Token 🎫](<14 🆔🎫 Verify Tokens.md>) (e.g., over 16 years old). 
    
    - When interacting with the [Seller 💵](<../../41 🎭 Domain Roles/70 💵 Sellers/$ 💵🎭 Seller role.md>)'s domain, the Seller can then ask for the Token before providing the service or granting the entrance. 
    
    - The Token can also be printed or saved into to an NCF card, so that users can access the venue or service even when their devices run out of battery.


    ---
    