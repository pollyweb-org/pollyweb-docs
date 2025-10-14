🪄 Wand supplier domains
===

1. **What is a Wand domain in NLWeb?**

    A [Wand 🪄](<09 🪄🛠️ Wand helper.md>) is
    * any [Helper 🛠️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) 
    * that creates and manages [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) 
    * for [Things 💠](<01 💠 Thing.md>) (including [Userables 💍](<../74 💍 Brand Userables/01 💍 Userable thing.md>), [Tapbands ⌚](<../76 ⌚ Brand Tapbands/01 ⌚💠 Tapband thing.md>) and [Robots 🤖](<../72 🤖 Brand Robots/01 🤖💠 Robot thing.md>))
    * on behalf of [Brand 🍏 domains](<07 🍏🎭 Brand role.md>).

    ---
    <br/>

1. **How do Wands work?**
   
    ![](<00 📎 Assets/💠 Wand.png>)


    | # | Category | 🧑‍🦱 Steps for guests 
    |-|-|-
    |A| `Tap/Scan` | Guest users use their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to [tap 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) or [scan ✨](<../../20 🧑‍🦰 UI/11 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>) the [Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) of a [Thing 💠](<01 💠 Thing.md>) from a given [Brand 🍏 domain](<07 🍏🎭 Brand role.md>).
    |B| `Open`| That opens a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) with the [Wand 🪄 domain](<09 🪄🛠️ Wand helper.md>), acting on behalf of the [Thing's Brand 🍏 domain](<07 🍏🎭 Brand role.md>).
    |C| `Interact` | Guests can then chat with the [Wand 🪄 domain](<09 🪄🛠️ Wand helper.md>) to search instructions, add private notes, join groups, contact the owner, call emergency, or return the item when found; all notes added by the guest are saved on the [guest's Storage 📦 agent](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>).
    

    | # | Category | 🧑‍🦰 Steps for owners 
    |-|-|-
    |1| `Tap/Scan` | Owners use their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to [tap 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) or [scan ✨](<../../20 🧑‍🦰 UI/11 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>) the [Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) of a [Thing 💠](<01 💠 Thing.md>) with a given [Brand 🍏 domain](<07 🍏🎭 Brand role.md>).
    |2| `Open` | That opens a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) with the [Wand 🪄 domain](<09 🪄🛠️ Wand helper.md>), acting on behalf of the [Brand 🍏](<07 🍏🎭 Brand role.md>). Owners can then do everything that guests can.
    |3| `Identify` | The [Wand 🪄 domain](<09 🪄🛠️ Wand helper.md>) will detect the user's ownership by its registration on the [owner's Custodian 🧳 agent](<05 🧳🗄️ Custodian vault.md>), and will will provide the owner with admin access after authenticating the owner via the [owner's Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>).
    |4| `Contact` | If allowed by the [Brand 🍏 domain](<07 🍏🎭 Brand role.md>), users will also be able to get in contact with the [Brand 🍏 domain](<07 🍏🎭 Brand role.md>).

    ---
    <br/>

1. **What user Agents do Wands typically invoke?**

    | [User Agent 🫥](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | Purpose
    |-|-
    | [🧳 Custodian](<05 🧳🗄️ Custodian vault.md>) | To allow users to manage their [Things 💠](<01 💠 Thing.md>).
    | [🆔 Identity](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | To authenticate users as owners of their [Things 💠](<01 💠 Thing.md>). 
    | [📦 Storage](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>) | To allow users to store notes about their [Things 💠](<01 💠 Thing.md>).

    ---
    <br/>

1. **What domain roles do Wands typically implement?**
   
    |[Domain Role 🎭](<../../40 👥 Domains/41 📨 Msgs/00 👥 Domain.md>)|Description
    |-|-
    | [🪢 Integrator](<../../20 🧑‍🦰 UI/12 💬 Chats/06 🪢🎭 Integrator role.md>) | To promote the printing of [Locators 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) in [Finder 🔎 domains](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>).
    | [🤗 Host](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | For interacting with [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) in [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).
    | [🏭 Supplier](<../../30 🫥 Agents/06 🛎️ Concierges/02 🏭🎭 Supplier role.md>) | For receiving orders to add [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) to [Things 💠](<01 💠 Thing.md>).
    | [💼 Consumer](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) | For consuming data sets required to fill out the order.
    | [💵 Seller](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) | For receiving payments for the orders via their [Collector 🏦 helper](<../../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>).
    | [🌬️ Streamer](<../../40 👥 Domains/42 🌬️ Streams/02 🌬️🎭 Streamer role.md>) | To update the order statuses.
    

    ---
    <br/>

1. **Why are Wands important?**

    * **For businesses**, [Wand 🪄 domains](<09 🪄🛠️ Wand helper.md>) remove the overhead for [Brand 🍏 domains](<07 🍏🎭 Brand role.md>) in implementing the NLWeb protocol.
    
    * **For users**, [Wand 🪄 domains](<09 🪄🛠️ Wand helper.md>) ensure a seamless experience when interacting with [Things 💠](<01 💠 Thing.md>) from any [Brand 🍏 domains](<07 🍏🎭 Brand role.md>), given that the [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) session of a [Things 💠](<01 💠 Thing.md>) is controlled by the [Wand 🪄 domain](<09 🪄🛠️ Wand helper.md>).

    ---
    <br/>

1. **Do Wands know which user registered the Locator?**

    No. 
    * The owner of a [Thing 💠](<01 💠 Thing.md>) is hidden from [Wand 🪄 domains](<09 🪄🛠️ Wand helper.md>) by [Custodian 🧳 vault domains](<05 🧳🗄️ Custodian vault.md>).

    ---
    <br/>

1. **Can Brands know which user registered the placeholder?**

    No.
    * The owner of a [Thing 💠](<01 💠 Thing.md>) is hidden from [Brand 🍏 domains](<07 🍏🎭 Brand role.md>) by [Custodian 🧳 vault domains](<05 🧳🗄️ Custodian vault.md>). 
    * Of course, [Brand 🍏 domains](<07 🍏🎭 Brand role.md>) can find alternative ways to get that information, but those are not part of the NLWeb protocol.

    ---
    <br/>

1. **Can a user contact the Brand?**

    Yes, when applicable. 
    
    * [Brand 🍏 domains](<07 🍏🎭 Brand role.md>) may provide their contact details when placing an order to [Wand 🪄 domains](<09 🪄🛠️ Wand helper.md>);
        * in that case, [Wand 🪄 domains](<09 🪄🛠️ Wand helper.md>) can leverage the [Brand 🍏 domain](<07 🍏🎭 Brand role.md>) on behalf of users.

    * However, some [Brand 🍏 domain](<07 🍏🎭 Brand role.md>) may not want to provide their contact details if they want to remain anonymous; 
        * this is common in white-labelling and other branding strategies.

    ---
    <br/>

1. **What if a Brand ceases to exist?**

    [Wand 🪄 domains](<09 🪄🛠️ Wand helper.md>) verify if the [Brand 🍏 domains](<07 🍏🎭 Brand role.md>) is still active upon user interaction. 
    * A [Wand 🪄 domain](<09 🪄🛠️ Wand helper.md>) may decide to keep a [Thing 💠](<01 💠 Thing.md>) working even after the [Brand 🍏 domains](<07 🍏🎭 Brand role.md>) is inactive;
    * e.g., if the user pays a subscription to the [Wand 🪄 domain](<09 🪄🛠️ Wand helper.md>).

    ---
    <br/>

1. **How can Wands monetize?**

    [Wand 🪄 domains](<09 🪄🛠️ Wand helper.md>) may implement a number of ways to monetize - e.g.:
    - charge [Brand 🍏 domains](<07 🍏🎭 Brand role.md>) for a commitment to keep the placeholder active for a certain amount of time (e.g., 10 years) when an order is placed;
    - charge [Custodian 🧳 vault domains](<05 🧳🗄️ Custodian vault.md>) for each user registration or interaction with a [Thing 💠](<01 💠 Thing.md>);
    - charge a [subscription 🗓️](<../../../2 🏔️ Landscape/1 💼 Business landscape/08 🗓️ Subscriptions landscape>) to users, by leveraging a [Biller 🤝 helper domain](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>);
    - introduce [advertising 👀](<../../../2 🏔️ Landscape/1 💼 Business landscape/04 👀 Advertising landscape>) in the user [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>), by leveraging an [Advertiser 👀 helper domain](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>).

    ---
    <br/>
