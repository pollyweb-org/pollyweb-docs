🪄 Wand supplier domains FAQ
===

1. **What is a Wand 🪄 domain in NLWeb?**

    Wands are [Helper 🛠️ domains](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) that create and manage user [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) for [Things 💠](<01 💠 Thing.md>) on behalf of [Brand 🍏 domains](<07 🍏🎭 Brand role.md>).

    ---

1. **How do Wands work?**
   
    ![](<00 📎 Assets/💠 Wand.png>)


    | # | 🧑‍🦱 Steps for guests 
    |-|-
    |A| Guests use their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to [tap 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) or [scan ✨](<../../20 🧑‍🦰 UI/22 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>) the [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) of a [Thing 💠](<01 💠 Thing.md>) from a given [Brand 🍏](<07 🍏🎭 Brand role.md>).
    |B| That opens a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with the Wand 🪄, acting on behalf of the [Brand 🍏](<07 🍏🎭 Brand role.md>).
    |C| Guests can then chat with the Wand 🪄 to search instructions, add private notes, join groups, contact the owner, call emergency, or return the item when found; all notes added by the guest are saved on the guest's own [Storage 📦 agent](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>).
    

    | # | 🧑‍🦰 Steps for owners 
    |-|-
    |1| Owners use their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to [tap 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) or [scan ✨](<../../20 🧑‍🦰 UI/22 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>) the [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) of a [Thing 💠](<01 💠 Thing.md>) with a given [Brand 🍏 domain](<07 🍏🎭 Brand role.md>).
    |2| That opens a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with the Wand 🪄, acting on behalf of the [Brand 🍏](<07 🍏🎭 Brand role.md>). Owners can then do everything that guests can.
    |3| The Wand 🪄 will detect the user's ownership by its registration on the user's [Custodian 🎩 agent](<05 🎩🗄️ Custodian vault.md>), and will will provide the user with admin access after authenticating the user via the user's [Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>).
    |4| If allowed by the [Brand 🍏 domain](<07 🍏🎭 Brand role.md>), users will also be able to get in contact with the [Brand 🍏](<07 🍏🎭 Brand role.md>).

    ---

2. **What user Agents do Wands typically invoke?**

    | [User Agent 🫥](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | Purpose
    |-|-
    | [🎩 Custodian](<05 🎩🗄️ Custodian vault.md>) | To allow users to manage their [Things 💠](<01 💠 Thing.md>).
    | [🆔 Identity](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | To authenticate users as owners of their [Things 💠](<01 💠 Thing.md>). 
    | [📦 Storage](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) | To allow users to store notes about their [Things 💠](<01 💠 Thing.md>).

    ---

3. **What domain roles do Wands typically implement?**
   
    |[Domain Role 🎭](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>)|Description
    |-|-
    | [🪢 Integrator](<../../20 🧑‍🦰 UI/23 💬 Chats/06 🪢🎭 Integrator role.md>) | To promote the printing of [Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) in [Finder 🔎 domains](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>).
    | [🤗 Host](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) | For interacting with [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) in [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>).
    | [🏭 Supplier](<../../30 🫥 Agents/06 🛎️ Concierges/02 🏭🎭 Supplier role.md>) | For receiving orders to add [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) to [Things 💠](<01 💠 Thing.md>).
    | [💼 Consumer](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) | For consuming data sets required to fill out the order.
    | [💵 Seller](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) | For receiving payments for the orders via their [Collector 🏦 helper](<../../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>).
    | [🌬️ Streamer](<../../40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) | To update the order statuses.
    

    ---

4. **Why are Wands important?**

    * **For businesses**, Wands 🪄 remove the overhead for [Brand 🍏 domains](<07 🍏🎭 Brand role.md>) in implementing the NLWeb protocol.
    
    * **For users**, Wands 🪄 ensure a seamless experience when interacting with [Things 💠](<01 💠 Thing.md>) from any [Brand 🍏 domains](<07 🍏🎭 Brand role.md>), given that the [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) session of a [Things 💠](<01 💠 Thing.md>) is controlled by the Wand 🪄.

    ---

5. **Do Wands know which user registered the Locator?**

    No. 
    * That is hidden by [Custodian 🎩 vaults](<05 🎩🗄️ Custodian vault.md>).

    ---

6. **Can Brands know which user registered the placeholder?**

    No.
    * That is hidden by [Custodian 🎩 vaults](<05 🎩🗄️ Custodian vault.md>). 
    * Of course, [Brand 🍏 suppliers](<07 🍏🎭 Brand role.md>) can find alternative ways to get that information, but those are not part of the NLWeb protocol.

    ---

7. **Can a user contact the Brand?**

    Yes, when applicable. 
    
    * [Brand 🍏 suppliers](<07 🍏🎭 Brand role.md>) may provide their contact Locator when placing an order to Wand 🪄 domains;
        * in that case, Wands can leverage the [Brand 🍏 supplier](<07 🍏🎭 Brand role.md>) on behalf of users.

    * However, some [Brand 🍏 suppliers](<07 🍏🎭 Brand role.md>) may not want to provide their contact if they want to remain anonymous; 
        * this is common in white-labelling and other branding strategies.

    ---

8. **What if a Brand ceases to exist?**

    Wand 🪄 domains verify if the [Brand 🍏 supplier](<07 🍏🎭 Brand role.md>) is still active upon user interaction. 
    * A Wand may decide to keep a [Thing 💠](<01 💠 Thing.md>) working even after the [Brand 🍏 supplier](<07 🍏🎭 Brand role.md>) is inactive (e.g., if the user pays a subscription to the Wand 🪄).

    ---

9. **How can Wands monetize?**

    Wand 🪄 domains may implement a number of ways to monetize - e.g.:
    - charge [Brand 🍏 suppliers](<07 🍏🎭 Brand role.md>) for a commitment to keep the placeholder active for a certain amount of time (e.g., 10 years) when an order is placed;
    - charge [Custodian 🎩 vaults](<05 🎩🗄️ Custodian vault.md>) for each user registration or interaction with a [Thing 💠](<01 💠 Thing.md>);
    - charge a [subscription 🗓️](<../../../2 🏔️ Landscape/1 💼 Business landscape/08 🗓️ Subscriptions landscape>) to users, by leveraging a [Biller 🤝 helper](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>);
    - introduce [advertising 👀](<../../../2 🏔️ Landscape/1 💼 Business landscape/04 👀 Advertising landscape>) in the user [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), by leveraging an [Advertiser 👀 helper](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>).

    ---
