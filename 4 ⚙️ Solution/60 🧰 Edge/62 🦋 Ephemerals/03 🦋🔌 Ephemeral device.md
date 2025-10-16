<!-- #TODO -->

🦋 Ephemeral pluggable devices
===

1. **What is an Ephemeral device?**

    An Ephemeral 🦋 is a [Pluggable 🔌 device](<../61 🔌 Pluggables/01 🔌 Pluggable device.md>) that generates rotating temporary QR/NFC [Locators 🔆](<../../25 Locators/15 🔆 Locators/🔆 Locator.md>) to force users to be next to the device when they [tap 🔆](<../../25 Locators/15 🔆 Locators/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>) or [scan ✨](<../../25 Locators/15 🔆 Locators/🔆⏩ Locator flows/🧑‍🦰✨ Wallet QR scan.md>) the [Locator 🔆](<../../25 Locators/15 🔆 Locators/🔆 Locator.md>) with their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>). 

    ---

1. **Isn't a rotating NFC tag enough?**

    Ephemeral 🦋 devices will cost multiple times more than a [rotating secure NFC tag 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/11 📺 NFC authentication.md>), so the question is pertinent.
    - A Ephemeral 🦋 device built with a Raspberry PI may require around $150 USD in parts (e.g., CPU, display, NFC emulator), plus business-related costs (e.g., assembly labor, shipping, sales).
    - Conversely, an NXP rotating NFC tag had a maximum price tag of $2,00 USD in 2024.
    - However, rotating NFC tags cannot have a corresponding QR code, because the QR is statically printed.

    For corporate controlled environments, where users must adhere to the rules of their organizations, not having a QR code is not an issue, so rotating NFC tags will probably be enough for most corporate use cases.
    - Conversely, for public-facing use cases (e.g., ATM machines), a QR code is an important fallback for when the smartphone's NFC reader is not working properly with the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>).
    - Faulty NFC readers on smartphones might be due to 1/ missing features on low-end brands, 2/ conflicting installations with other NFC reader apps, or 3/ unintended disabled functionality by less knowledgeable users.
   
    ---

1. **How is an Ephemeral applicable to the financial industry?**

    ![](<.📎 Assets/🦋 Ephemeral ATMs.png>)

    In a [cash machine 🤝 use case](<../../../3 🤝 Use Cases/05 🛠️ Services/03 🏧 Withdraw at ATMs/10 Customer @ ATM/11 Withdraw cash.md>), the bank wants their customer to be close to the dispenser when the order to dispense money is issued.
    - Otherwise, someone else could get the customer’s money.
    - The setup requires an [Antenna 📡 router](<../61 🔌 Pluggables/02 📡🔀 Antenna router.md>) on site, connected to the [Relayer 🛰️ domain](<../../45 🤲 Helper domains/80 🛰️ Relayers/🛰️🤲 Relayer helper.md>), to allow the ATM [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) to remotely control the Ephemeral 🦋 device.
    
    The use case is as follows:
    1. Users [tap 🔆](<../../25 Locators/15 🔆 Locators/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>) or [scan ✨](<../../25 Locators/15 🔆 Locators/🔆⏩ Locator flows/🧑‍🦰✨ Wallet QR scan.md>) the ATM's static [Locator 🔆](<../../25 Locators/15 🔆 Locators/🔆 Locator.md>) with their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) - this could be a big QR printed on a top banner;
    2. The [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) opens a [Chat 💬](<../../35 Chats/12 💬 Chats/💬 Chat.md>) with the ATM Company's [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>), and the user asks to withdraw cash;
    3. ATM [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) asks the ATM's [Relayer 🛰️ domain](<../../45 🤲 Helper domains/80 🛰️ Relayers/🛰️🤲 Relayer helper.md>) to send a command to the ATM's [Antenna 📡 router](<../61 🔌 Pluggables/02 📡🔀 Antenna router.md>) to remotely activate the specific Ephemeral 🦋 device attached to the cash dispenser where the money will come out from;
    4. The user then [taps 🔆](<../../25 Locators/15 🔆 Locators/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>) or [scans ✨](<../../25 Locators/15 🔆 Locators/🔆⏩ Locator flows/🧑‍🦰✨ Wallet QR scan.md>) the NRC/QR off the designated Ephemeral 🦋 device with their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>);
    5. When the Ephemeral 🦋 device confirms 


    ---

1. **How is an Ephemeral applicable to building security?**

    ![](<.📎 Assets/🦋 Ephemeral Doors.png>)

    When opening a door with restricted access, attackers may put the NFC/QR [Locator 🔆](<../../25 Locators/15 🔆 Locators/🔆 Locator.md>) of a high-security door A on a low-security door B on the other side of the building. 
    
    -   When a high-level user tries to open door B, they will actually be opening door A for the attacker. 
    - An Ephemeral 🦋 prevents this by periodically changing the [Locator 🔆](<../../25 Locators/15 🔆 Locators/🔆 Locator.md>).

    ---
