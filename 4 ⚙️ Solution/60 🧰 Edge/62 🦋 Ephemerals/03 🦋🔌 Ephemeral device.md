#TODO

🦋 Ephemeral pluggable devices FAQ
===

1. **What is an Ephemeral device?**

    An Ephemeral 🦋 is a [Pluggable 🔌](<../61 🔌 Pluggables/01 🔌 Pluggable device.md>) device that generates rotating temporary QR/NFC [Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) to force users to be close to the device when they tap/scan the Locator. 

    ---

1. **How is an Ephemeral applicable to the financial industry?**

    ![](<📎 Assets/🦋 Ephemeral ATMs.png>)

    For a [cash machine](<../../../3 🤝 Use Cases/05 🛠️ Services/03 🏧 Withdraw at ATMs/10 Customer @ ATM/11 Withdraw cash.md>), the bank wants their customer to be close to the dispenser when the order to dispense money is issued.
    - Otherwise, someone else could get the customer’s money.
    - The setup requires an [Antenna 📡](<../61 🔌 Pluggables/02 📡🔀 Antenna router.md>) on site, connected to the [Relayer 🛰️](<../61 🔌 Pluggables/04 🛰️🏭 Relayer supplier.md>), to allow the ATM [Host 🤗](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) to remotely control the Ephemeral 🦋 device.
    
    
    ---

1. **How is an Ephemeral applicable to building security?**

    ![](<📎 Assets/🦋 Ephemeral Doors.png>)

    When opening a door with restricted access, attackers may put the NFC/QR [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) of a high-security door A on a low-security door B on the other side of the building. 
    
    -   When a high-level user tries to open door B, they will actually be opening door A for the attacker. 
    - An Ephemeral 🦋 prevents this by periodically changing the [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>).

    ---
