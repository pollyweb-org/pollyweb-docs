💠 Thing locators
===

1. **What is a Thing?**

    A Thing 💠 
    * is an [🔆 NFC/QR Locator](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) 
    * brought to life by a [Wand 🪄 domain](<../../45 🛠️ Helper domains/90 🪄 Wands/$ 🪄🛠️ Wand helper.md>)
    * to allow users to interact with the physical world via [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>).

    ---

1. **Why are Things important?** 

    While it's already possible to 
    * interact with any electronic device that has a display (e.g., washing machines, air conditioners, home printers), as well as with electronic devices without a display (e.g., smart lights), 
    * adding an internet-connected touch display or a mobile app-based remote control to any electrical device brings significant challenges and costs, 
    * while being close to impossible for non-electrical objects and animals (e.g., hats, pencils, and dogs).

    ---

1. **What are examples of Things?**

    ![](<00 📎 Assets/💠 Thing.png>)

    Things 💠 come in a number of forms:

    - **[💠 Standard Things](<01 💠 Thing.md>)**: 
        - all Things 💠 provide a user-controlled experience of an item bought and registered by a specific user, allowing other users to interact with it as guests - e.g.:
            - tags in T-shirts, 
            - NFC chips under the skin of pets and endangered wild animals, 
            - NFC/QR codes to stick on a 30-year-old book or pin to a 300-year-old tree.

    - [**💍 Userable specialization**](<../74 💍 Brand Userables/01 💍 Userable thing.md>): 
        - besides supporting all features of standard Things 💠, [Userables 💍](<../74 💍 Brand Userables/01 💍 Userable thing.md>) allow users without a smart device to make payments and access restricted areas, and are typically an NFC embedded into objects that a user may carry;
          - e.g.: jewelry, glasses, key holders.

    - [**⌚ Tapbands**](<../76 ⌚ Brand Tapbands/01 ⌚💠 Tapband thing.md>): 
        - besides supporting all features of [Userables 💍](<../74 💍 Brand Userables/01 💍 Userable thing.md>), a [⌚ Tapband](<../76 ⌚ Brand Tapbands/01 ⌚💠 Tapband thing.md>) allow users to also open [Padlocks 🔒](<../75 🔒 Brand Padlocks/01 🔒 Padlock device.md>) while assuring users cannot be traced between interactions with [Host 🤗 domains](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>).


    - [**🤖 Robot specialization**](<../72 🤖 Brand Robots/01 🤖💠 Robot thing.md>): 
        - besides supporting all features of standard Things 💠, [🤖 Robots](<../72 🤖 Brand Robots/01 🤖💠 Robot thing.md>) can be embed into physical devices to enable them to be controlled remotely, even without a display; 
            - e.g.: a coffee machine, a printer, or a vehicle. 

    ---

1. **What can a user do with a Thing?**

    ![](<00 📎 Assets/💠 Thing$Actions.png>)

    Things 💠 behave differently when interacting with Owners (the user who registered the Thing 💠 after buying it) and Guests (users who are not the owner).

    Owner features, available via their [Custodian 🧳 agent](<../../50 🫥 Agents/35 🧳 Custodians/$ 🧳🗄️ Custodian vault.md>):
    - **Register**: take ownership of a recently acquired unregistered Thing 💠;
    - **Transfer**: give ownership to a second-hand owner;
    - **Contact Brand**: ask for after-sales support - e.g., troubleshooting;
    - **Report lost/stolen**: activate the "return found item" for Guests;
    - **Set landing page**: create Wikipedia like descriptions for landmarks;
    - **Manage groups**: create groups for note sharing, invite/promote users;
    - **Set permissions**: give groups (e.g., family) access to owner features;
    - All other features available to guests.
    
    Guest features:
    - **Search instructions**: use natural language to navigate manuals;
    - **Add private notes**: e.g, write down passwords and attach invoices;
    - **Join groups**: e.g., operate and remotely control family devices;
    - **Call emergency services**: in one click, share location and contacts;
    - **Contact the owner**: e.g., notify that a runaway pet was found;
    - **Return found item**: start a logistics workflow to return the Thing.

    ---

1. **Are Things similar to digital twins of physical devices?**

    Yes, but more. 
    
    * Digital twins are a digital representation of an object's characteristics and functionalities;
        * e.g., a machine in a factory.

    * While Things 💠 can work as digital twins, they also expand the functionalities of the object they represent, proving an anthropomorphic (human-like) behavior to non-human entities, such as animals, landmarks, and objects;
        * e.g., a seashell can now have a conversation with you about the story of its life.

    ---


1. **How cans Things make a vintage book smarter?**

    ![](<00 📎 Assets/💠 Printer Sticker.png>)

    |#|Category|Step
    |-|-|-
    |1| `Order` | A [Printer 🖨️ domain](<../../45 🛠️ Helper domains/75 🖨️ Printers/$ 🖨️🛠️ Printer helper.md>) orders a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) interaction from a [Wand 🪄 helper domain](<../../45 🛠️ Helper domains/90 🪄 Wands/$ 🪄🛠️ Wand helper.md>). 
    |2| `Create` | The [Wand 🪄 domain](<../../45 🛠️ Helper domains/90 🪄 Wands/$ 🪄🛠️ Wand helper.md>) creates a [Thing 💠](<01 💠 Thing.md>) and shares its [digital Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>). |
    |3| `Print` | The [Printer 🖨️](<../../45 🛠️ Helper domains/75 🖨️ Printers/$ 🖨️🛠️ Printer helper.md>) prints the [Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) of the [Thing 💠](<01 💠 Thing.md>) into a QR/NFC  smart sticker.
    |4| `Sell` | The [Printer 🖨️](<../../45 🛠️ Helper domains/75 🖨️ Printers/$ 🖨️🛠️ Printer helper.md>) distributes the smart sticker to commercial end-users.
    |5| `Buy` | A user buys the smart sticker from a store to stick on a vintage book.
    |6| `Register` | The user scans it with their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) to register on their [Custodian 🧳 vault](<../../50 🫥 Agents/35 🧳 Custodians/$ 🧳🗄️ Custodian vault.md>).
    |7| `Chat` | Guest users tap/scan the book's smart sticker to interact with it in a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>).

    ---

1. **How can Things make a dog collar smarter?**

    ![](<00 📎 Assets/💠 Printer Collar.png>)

    |#|Category|Step
    |-|-|-
    |1| `Create` | A [Brand 🍏 domain](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>) orders a [Thing 💠](<01 💠 Thing.md>) from a [Wand 🪄 helper domain](<../../45 🛠️ Helper domains/90 🪄 Wands/$ 🪄🛠️ Wand helper.md>). 
    |2| `Print` | The [Brand 🍏 domain](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>) orders the physical [Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) from a [Printer 🖨️ helper domain](<../../45 🛠️ Helper domains/75 🖨️ Printers/$ 🖨️🛠️ Printer helper.md>).
    |3| `Sell` | The [Brand 🍏 domain](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>) sells the physical [Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) on a smart collar product bundle.
    |4| `Buy` | A user buys the smart collar from a pet store, and give it to their pet.
    |5| `Register` | The user scans it with their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) to register on their [Custodian 🧳 vault](<../../50 🫥 Agents/35 🧳 Custodians/$ 🧳🗄️ Custodian vault.md>).
    |7| `Chat` | Guest users (e.g., vets) tap/scan the pet's smart collar to interact with it in a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>).
    
    ---