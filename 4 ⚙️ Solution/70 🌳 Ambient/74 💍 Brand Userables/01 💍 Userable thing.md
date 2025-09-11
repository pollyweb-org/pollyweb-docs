💍 Userable Things FAQ
===

1. **What are Userable Things in NLWeb?**
    
    Userables are [Things 💠](<../71 💠 Brand Things/01 💠 Thing.md>) that [Brand 🍏 domains](<../71 💠 Brand Things/07 🍏🎭 Brand role.md>) embedded into objects for a user to carry (e.g., jewelry, glasses, cards, keyholders, stickers, and wearables). 

    ---

2. **What can users do with their Userables?**

    Users can do with their Userables 💍 everything they do with standard [Things 💠](<../71 💠 Brand Things/01 💠 Thing.md>). 
    
    Additionally, users can also leverage their Userables 💍 in the following situations:
    - 🚨 [Emergencies use case](<02 💍🚨 Userable emergencies.md>):
        - script steps for execute on health emergencies;
    - 📱 [Misplaced phone use case](<03 💍📱 Userable lost phone.md>):
        - find their phones using someone else's Wallet;
    - 💳 [Payments use case](<04 💍💳 Userable payments.md>):
        - pay to [Seller 💵 domains](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) using the [Seller's Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>);
        - pay to [Seller 💵 domains](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) using the [Seller's Kiosk 🖥️ devices](<../../60 🧰 Edge/68 🏪 Terminals/01 🖥️ Info kiosk.md>); 
        - pay small-fee transport tickets in a bus;
        - pay variable length metropolitan rides;
    - 🎬 [Gates use case](<05 💍🎬 Userable gates.md>):
        - cross an airport border control.

    ---

3. **Are Userables trackable, like Apple AirTags?**

    No.
     
    - NFC Userables 💍 use passive NFC, thus requiring a powered reader to come into contact with them, similar to traditional touchless bank cards.

    - Conversely, Apple Tags can be trackable because they use Bluetooth Low Energy (BLE) to communicate with any Apple device from up to 100 meters away.

    ---

4. **Are Userables protected from spoofing?**

    Yes.

    - Userables 💍 implement the NFC authentication mechanism described in the video [NFC authentication 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/11 📺 NFC authentication.md>), generating unique sequential dynamic codes on each NFC scan based on a counter.
  
    - The authentication mechanism is implemented with a secure NFC chip with asymmetric cryptography (e.g., NTAG 424 DNA class).

    - When a Userable 💍 is [tapped 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>), the user's [Custodian 🧳 agent](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) checks the validity of the unique dynamic code sent by domain that scanned the Userable 💍, verifying if it has not been used before, if the signature of the code matches the Userable's public key and unique ID, and if the sequence was respected.

    ---

5. **How is the dynamic code generation enforced?**

    When a user registers a Userable 💍 on the user's [Custodian 🧳 agent](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>):
    - the agent fetches the rotation algorithm from the [Brand 🍏 domain](<../71 💠 Brand Things/07 🍏🎭 Brand role.md>) that manufactured the Userable 💍;
    - then asks the user to scan the Userable 💍 twice to see if the rotation works. 

    ---