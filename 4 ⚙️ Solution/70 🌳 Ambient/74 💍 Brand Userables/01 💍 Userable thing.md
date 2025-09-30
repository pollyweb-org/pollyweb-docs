💍 Userable Things FAQ
===

1. **What are Userable Things in NLWeb?**
    
    [Userables 💍](<01 💍 Userable thing.md>) are [Things 💠](<../71 💠 Brand Things/01 💠 Thing.md>) 
    * that [Brand 🍏 domains](<../71 💠 Brand Things/07 🍏🎭 Brand role.md>) embedded into objects for a user to carry 
    * e.g., jewelry, glasses, cards, keyholders, stickers, and wearables. 

    ---
    <br/>

2. **What can users do with their Userables?**

    Users can do with their [Userable 💍 things](<01 💍 Userable thing.md>) everything they do with standard [Things 💠](<../71 💠 Brand Things/01 💠 Thing.md>). 
    
    * Additionally, users can also leverage their [Userable 💍 things](<01 💍 Userable thing.md>) in the following situations.

    |||
    |-|-
    | 🚨 [Trigger an emergency](<02 💍🚨 Userable emergencies.md>)| Scripted steps to execute on health emergencies.
    | 📱 [Aid a confused senior](<13 💍📱 Userable senior user.md>) | Inform relatives using someone else's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    | 🎬 [Cross gates](<14 💍🎬 Userable gates.md>)| Cross an airport border control.
    | 💳 [Pay a salesperson](<21 💍💳 Userable pay salesperson.md>) | Pay a [Seller 💵 domain](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) using the [Seller's Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    | [💳 Pay seller at a kiosk](<22 💍💳 Userable pay kiosk.md>) | Pay a [Seller 💵 domain](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) using the [Seller's Kiosk 🖥️](<../../60 🧰 Edge/68 🏪 Terminals/01 🖥️ Info kiosk.md>).
    | [💳 Pay variable-cost rides](<23 💍💳 Userable pay metro.md>) | Pay variable length metropolitan rides.

    ---
    <br/>

3. **Are Userables trackable, like Apple AirTags?**

    No.
     
    - NFC [Userable 💍 things](<01 💍 Userable thing.md>) use passive NFC, thus requiring a powered reader to come into contact with them, similar to traditional touchless bank cards.

    - Conversely, Apple Tags can be trackable because they use Bluetooth Low Energy (BLE) to communicate with any Apple device from up to 100 meters away.

    ---
    <br/>

4. **Are Userables protected from spoofing?**

    Yes.

    - [Userable 💍 things](<01 💍 Userable thing.md>) implement the NFC authentication mechanism described in the video [NFC authentication 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/11 📺 NFC authentication.md>), generating unique sequential dynamic codes on each NFC scan based on a counter.
  
    - The authentication mechanism is implemented with a secure NFC chip with asymmetric cryptography (e.g., NTAG 424 DNA class).

    - When a [Userable 💍 thing](<01 💍 Userable thing.md>) is [tapped 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>), the user's [Custodian 🧳 agent](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) checks the validity of the unique dynamic code sent by domain that scanned the [Userable 💍 thing](<01 💍 Userable thing.md>), verifying if 
      - it has not been used before, 
      - if the signature of the code matches the Userable's public key and unique ID, 
      - and if the sequence was respected.

    ---
    <br/>

5. **How is the dynamic code generation enforced?**

    When a user registers a [Userable 💍 thing](<01 💍 Userable thing.md>) on the user's [Custodian 🧳 agent](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>),
    * the agent fetches the rotation algorithm from the [Brand 🍏 domain](<../71 💠 Brand Things/07 🍏🎭 Brand role.md>) that manufactured the [Userable 💍 thing](<01 💍 Userable thing.md>),
    * then asks the user to scan the [Userable 💍 thing](<01 💍 Userable thing.md>) twice to see if the rotation works. 

    ---
    <br/>