🍏 Brand domain role
===


1. **What is a Brand domain role in NLWeb?**

    A [Brand 🍏](<🍏🎭 Brand role.md>) 
    * is any [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) 
    * that orders [Things 💠](<../../25 🔆 Locators/Things 💠/💠🔆 Thing locator.md>) from a [Wand 🪄 helper domain](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) 
    * in order to [enhance and personalize](<../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/00 🔆 Scanning index.md>) the Brand's products. 
    
    Examples:
    * `Coca-Cola` may talk about their history and nutritional info. 
    * `Nike` may talk about a shoe and allow orders for home delivery.
    * `HP` may allow for usage monitoring and ordering of ink cartridges.

    ---

1. **How does it work?**

    ![](<../../25 🔆 Locators/Things 💠/. 📎 Assets/💠 Brand.png>)

    |Category|Step
    |-|-
    | `Orchestrate` | A [Brand 🍏 domains](<🍏🎭 Brand role.md>) ask a [Wand 🪄 helper domain](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) to create a digital [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) for the embedded [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) of their physical product (i.e., a [Thing 💠 extension](<../../25 🔆 Locators/Things 💠/💠🔆 Thing locator.md>)).
    | `Supply` | The [Brand 🍏 domain](<🍏🎭 Brand role.md>) then asks a [Printer 🖨️ helper domain](<../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>) to print that [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) into physical NFQ/QR tag (i.e., a [Thing 💠 tag](<../../25 🔆 Locators/Things 💠/💠🔆 Thing locator.md>)).
    | `Assembly` | The [Brand 🍏 domain](<🍏🎭 Brand role.md>) then bundles the product with the tag, and sells it.
    | `Tap/Scan`| Users then pick up the product (e.g., a shirt in a fashion store) and tap/scan the [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) to initiate a [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) with the [Wand 🪄 domain](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>).
    

    ---

1. **What Helper domains does a Brand typically uses?**

    | [Helper 🤲](<../Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) | Reason
    |-|-
    | [Printer 🖨️](<../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>) | To print the [NFC/QR Locators 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) for the Brand's [Things 💠](<../../25 🔆 Locators/Things 💠/💠🔆 Thing locator.md>).
    | [Wand 🪄](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) | To order and manage the lifecycle of [Chats 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) for the Brand's [Things 💠](<../../25 🔆 Locators/Things 💠/💠🔆 Thing locator.md>).
    | [Payer 💳](<../../45 🤲 Helper domains/Payers 💳/💳🤲 Payer helper.md>) | To pay for the services of the other [Helper 🤲 domains](<../Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>).
    | [Buffer ⏳](<../../45 🤲 Helper domains/Buffers ⏳/⏳ Buffer/⏳🤲 Buffer helper.md>) | To receive order updates from the [Wand 🪄](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) and the [Printer 🖨️](<../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>) domains.

    ---

1. **What can a Brand configure for a Thing?**

    Brands 🍏 can set the following properties for [Things 💠](<../../25 🔆 Locators/Things 💠/💠🔆 Thing locator.md>) in [Wand 🪄 helper domains](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>).

    | Property | Purpose
    |-|-
    | `Message` | The landing message for guest users.
    | `Knowledge` | Body of knowledge for [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) interactions with guest users - e.g., instruction manuals and frequently asked questions;
    | `Contacts` | Additional contact details for support.

    ---

1. **How can Brands print NFC/QR tags for their Things?**

    Brands 🍏 can either:
    * print the [Locators 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) of the [Wand 🪄 helper domains](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) by themselves, 
    * or they can order [Locators 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) from [Printer 🖨️ helper domains](<../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>).

    ---

1. **Can Brands configure Things by EAN-13 or SKU?**

    Yes, and that's the default behavior. 

    ---
