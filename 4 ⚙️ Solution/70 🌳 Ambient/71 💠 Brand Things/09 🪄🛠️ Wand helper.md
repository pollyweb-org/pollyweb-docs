🪄 Wand supplier domains FAQ
===

1. **What is a Wand 🪄 domain in NLWeb?**

    ![](<00 📎 Assets/💠 Wand.png>)

    Wands are [Supplier 🏭 domains](<../../30 🫥 Agents/06 🛎️ Concierges/02 🏭🎭 Supplier role.md>) that create and manage user [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) for [Things 💠](<01 💠 Thing.md>) on behalf of [Brand 🍏 domains](<07 🍏🎭 Brand role.md>).

    ---

2. **What domain roles do Wands typically implement?**
   
    |Role|Description
    |-|-
    | [🪢 Integrator](<../../20 🧑‍🦰 UI/23 💬 Chats/06 🪢🎭 Integrator role.md>) | To promote the printing of [Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) in [Finder 🔎 domains](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>).
    | [🤗 Host](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) | For interacting with [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) in [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>).
    | [🏭 Supplier](<../../30 🫥 Agents/06 🛎️ Concierges/02 🏭🎭 Supplier role.md>) | For receiving printing orders and updating on their status.
    | [💼 Consumer](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) | For consuming data sets required to fill out the order.
    | [💵 Seller](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) | For receiving payments for the orders via their [Collector 🏦 helper](<../../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>).
    

    ---

2. **Why are Wands important?**

    For domains, Wands remove the overhead for Brands in implementing the NLWeb protocol.
    
    For users, Wands ensure a seamless experience when interacting with [Things 💠](<01 💠 Thing.md>) from any [Brand 🍏 suppliers](<07 🍏🎭 Brand role.md>), given that the chat session of a Thing is controlled by the Wand.

    ---

3. **Do Wands know which user registered the Locator?**

    No. That is hidden by [Custodian 🎩 vaults](<05 🎩🗄️ Custodian vault.md>).

    ---

4. **Can Brands know which user registered the placeholder?**

    No.
    * That is hidden by [Custodian 🎩 vaults](<05 🎩🗄️ Custodian vault.md>). 
    * Of course, [Brand 🍏 suppliers](<07 🍏🎭 Brand role.md>) can find alternative ways to get that information, but those are not part of the NLWeb protocol.

    ---

5. **Can a user contact the Brand?**

    Yes, when applicable. 
    
    * [Brand 🍏 suppliers](<07 🍏🎭 Brand role.md>) may provide their contact Locator when placing an order to Wand 🪄 domains;
        * in that case, Wands can leverage the [Brand 🍏 supplier](<07 🍏🎭 Brand role.md>) on behalf of users.

    * However, some [Brand 🍏 suppliers](<07 🍏🎭 Brand role.md>) may not want to provide their contact if they want to remain anonymous; 
        * this is common in white-labelling and other branding strategies.

    ---

6. **What if a Brand ceases to exist?**

    Wand 🪄 domains verify if the [Brand 🍏 supplier](<07 🍏🎭 Brand role.md>) is still active upon user interaction. 
    * A Wand may decide to keep a [Thing 💠](<01 💠 Thing.md>) working even after the [Brand 🍏 supplier](<07 🍏🎭 Brand role.md>) is inactive (e.g., if the user pays a subscription to the Wand 🪄).

    ---

7. **How can Wands monetize?**

    Wand 🪄 domains may implement a number of ways to monetize - e.g.:
    - charge [Brand 🍏 suppliers](<07 🍏🎭 Brand role.md>) for a commitment to keep the placeholder active for a certain amount of time (e.g., 10 years) when an order is placed;
    - charge [Custodian 🎩 vaults](<05 🎩🗄️ Custodian vault.md>) for each user registration or interaction with a [Thing 💠](<01 💠 Thing.md>);
    - charge a [subscription 🗓️](<../../../2 🏔️ Landscape/1 💼 Business landscape/08 🗓️ Subscriptions landscape>) to users, by leveraging a [Biller 🤝 helper](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>);
    - introduce [advertising 👀](<../../../2 🏔️ Landscape/1 💼 Business landscape/04 👀 Advertising landscape>) in the user [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), by leveraging an [Advertiser 👀 helper](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>).

    ---
