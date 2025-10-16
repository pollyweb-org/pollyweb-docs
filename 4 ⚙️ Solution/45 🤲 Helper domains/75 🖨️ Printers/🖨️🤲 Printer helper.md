🖨️ Printer domains
===

1. **What is a Printer domain in NLWeb?**

    Printers 🖨️ are [Helper 🤲 domains](<../$ 🤲 Helpers/🤲👥 Helper domain.md>) 
    * specialized in printing and managing [NFC/QR Locators 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) 
    * on behalf of [Brand 🍏 domains](<../../41 🎭 Domain Roles/Brands 🍏/🍏🎭 Brand role.md>) or any other [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>).

    ---

1. **What domain roles do Printers typically implement?**
   
    |Role|Description
    |-|-
    | [🪢 Integrator](<../../41 🎭 Domain Roles/Integrators 🪢/🪢🎭 Integrator role.md>) | To promote the printing of [Locators 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) in [Finder 🔎 domains](<../../50 🫥 Agent domains/40 🔎 Finders/🔎🫥 Finder agent.md>).
    | [🤗 Host](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | For interacting with [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) in [Chats 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>).
    | [🏭 Supplier](<../../41 🎭 Domain Roles/Suppliers 🏭/🏭🎭 Supplier role.md>) | For receiving printing orders and updating on their status.
    | [💼 Consumer](<../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | For consuming data sets required to fill out the order.
    | [💵 Seller](<../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) | For receiving payments for the orders via their [Collector 🏦 helper](<../30 🏦 Collectors/🏦🤲 Collector helper.md>).
    

    ---

1. **Why are Printers important?**

    For users:
    * Printer 🖨️ domains allow users to turn any object into a smart object - i.e., a [Thing 💠](<../../25 🔆 Locators/2 💠 Things/💠🔆 Thing locator.md>);
    * e.g., before going on trip through Asia, a user can buy a smart sticker in a supermarket then stick it on their old-yet-cherished notebook of memories so that anyone can return it free of charge if left behind.

    For businesses:
    * Printer 🖨️ domains offload from [Host 🤗 domains](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) the undifferentiated task of printing and distributing [NFC/QR Locators 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>). 

    ---


1. **How do Printers monetize?**

    The monetizing strategy is up to each Printer 🖨️ domain. 
    
    Possible ways are:

    - **Direct sell**: Printers 🖨️ may sell generic stickers and tags in supermarkets for users to enhance their existing objects.
    
    - **Supplier sell**: Printers 🖨️ may supply [Brand 🍏 domains](<../../41 🎭 Domain Roles/Brands 🍏/🍏🎭 Brand role.md>) and other [Host 🤗 domains](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) with printing [Locators 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) that these domains then integrate into their products.

    ---

1. **What are the possible formats and sizes?**

    Printed [Locators 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) come in many shapes and sizes, including:
    - 👕 textile labels for [clothing 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/14 📺 NFC in clothing.md>);
    - 🐬 under-skin chips for animals;
    - 💍 micro NFC chips for jewelry;
    - 📚 stickers for everyday objects (e.g., books);
    - 🖨️ plastic plaques to embed in home appliances;
    - 🐶 ID tags for pets;
    - 🌳 metal plaques for landmarks.

    ---

1. **Do Hosts have to know the Locators in advance?**

    Not necessarily. 
    
    Printers 🖨️ work with two options:

    - **with provided Locators**: 
        - the [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) sends a supply order with the [Locators 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) to be printed, the quantity, and the format;
        - these are preferred where the [Locator 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) is customized for a certain [Host 🤗](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) resource 
        - e.g., `any-supermarket.com/london-store` to reference a specific store in a chain of supermarkets.

    - **with anonymous Locators**: 
        - the [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) sends a supply order just specifying the quantity, the format, and the commitment lifetime;
        - these are preferred where the [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) wants to bind the [Locator 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) at the final manufacturing stage, saving the logistical challenge of matching [Locators 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) to the right product through the assembly process.

    ---

9.  **How are anonymous Locators translated?**

    Printers 🖨️ manage anonymous [Locators 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) with a redirection (e.g., `any-printer.com/random-locator`) that will be bound later to a final [Locator 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>). 
    - For this, Printers charge [Host 🤗 domains](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) for a commitment lifetime.
    - After the commitment, the redirection stops working, turning the [Locator 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) useless.

    ---
