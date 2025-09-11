🍏 Brand domain role FAQ
===


1. **What is a Brand domain role in NLWeb?**

    A Brand 🍏 is any [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) that orders [Things 💠](<01 💠 Thing.md>) from a [Wand 🪄 helper](<09 🪄🛠️ Wand helper.md>) in order to [enhance and personalize](<../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/00 🔆 Scanning index.md>) the Brand's products - e.g.:
    * `Coca-Cola` may talk about their history and nutritional info. 
    * `Nike` may talk about a shoe and allow orders for home delivery.
    * `HP` may allow for usage monitoring and ordering of ink cartridges.

    ---

2. **How does it work?**

    ![](<00 📎 Assets/💠 Brand.png>)

    |Category|Step
    |-|-
    | `Orchestrate` | Brands 🍏 ask [Wand 🪄 helper domains](<09 🪄🛠️ Wand helper.md>) to create digital [Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) for the embedded [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) of their physical products.
    | `Supply` | Brands then 🍏 ask [Printer 🖨️ helper domains](<08 🖨️🏭 Printer helper.md>) to print those [Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) into physical NFQ/QR tags.
    | `Assembly` | A Brand 🍏 domain orders 
    | `Tap/Scan`|
    

    ---

3. **What Helper domains does a Brand typically uses?**

    | [Helper 🛠️](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | Reason
    |-|-
    | [Printer 🖨️](<08 🖨️🏭 Printer helper.md>) | To print the [NFC/QR Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) for the Brand's [Things 💠](<01 💠 Thing.md>).
    | [Wand 🪄](<09 🪄🛠️ Wand helper.md>) | To order and manage the lifecycle of [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) for the Brand's [Things 💠](<01 💠 Thing.md>).
    | [Payer 💳](<../../30 🫥 Agents/04 💳 Payers/05 💳🛠️ Payer helper.md>) | To pay for the services of the other [Helper 🛠️ domains](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>).
    | [Buffer ⏳](<../../40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) | To receive order updates from the [Wand 🪄](<09 🪄🛠️ Wand helper.md>) and the [Printer 🖨️](<08 🖨️🏭 Printer helper.md>) domains.

    ---

4. **What can a Brand configure for a Thing?**

    Brands 🍏 can set the following properties for [Things 💠](<01 💠 Thing.md>) in [Wand 🪄 helper domains](<09 🪄🛠️ Wand helper.md>).

    | Property | Purpose
    |-|-
    | `Message` | The landing message for guest users.
    | `Knowledge` | Body of knowledge for [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) interactions with guest users - e.g., instruction manuals and frequently asked questions;
    | `Contacts` | Additional contact details for support.

    ---

5. **How can Brands print NFC/QR tags for their Things?**

    Brands 🍏 can either:
    * print the [Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) of the [Wand 🪄 helper domains](<09 🪄🛠️ Wand helper.md>) by themselves, 
    * or they can order [Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) from [Printer 🖨️ helper domains](<08 🖨️🏭 Printer helper.md>).

    ---

6. **Can Brands configure Things by EAN-13 or SKU?**

    Yes, and that's the default behavior. 

    ---
