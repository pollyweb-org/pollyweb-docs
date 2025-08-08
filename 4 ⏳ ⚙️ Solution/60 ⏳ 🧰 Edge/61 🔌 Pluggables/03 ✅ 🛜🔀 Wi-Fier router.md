🛜 Wi-Fier add-on device FAQ
===

![](<./📎 Assets/🔌 Wi-Fier.png>)

1. **What is a Wi-Fier device in NLWeb?**

    In NLWeb, Wi-Fier devices are side-cars that enable other devices to access the user's Wi-Fi network. 

    ---

1. **How is it handled by Wallets?**

    There are two ways of operation.

    **🛜 Direct Wi-Fier Locator**
    - in this scenario, the Wi-Fier [Locator 🔆](<../../20 ✅ 🧑‍🦰 UI/22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>) contains the location and credentials of the Wi-Fier; 
    - when users tap/scan the Wi-Fier's NFC/QR, the Wallet asks the user's [Persona 🧢](<../../30 ⏳ 🫥 Agents/02 ✅ 🧢 Personas/02 ✅ 🧢🫥 Persona agent.md>) to share the home Wi-Fi name and password, then momentarily opens a direct connection to the side-car to share network access credentials.

    **🪄 Indirect Wi-Fier configuration via a Wand**: 
    - in this scenario, the Wi-Fier's configuration is managed by a [Wand 🪄](<../../70 ✅ 🌳 Ambient/71 ✅ 💠 Brand Things/09 ✅ 🪄🏭 Wand supplier.md>); 
    - when users tap/scan the Wand's NFC/QR Locator, the Wallet asks the Wand for the Wi-Fier configurations, instead of parsing them from the Wand's Locator;
    - this option provides a better user experience for [🤖 Robots](<../../70 ✅ 🌳 Ambient/72 ✅ 🤖 Brand Robots/01 ✅ 🤖💠 Robot thing.md>), because users will only see one NFC/QR to handle both the Wi-Fier connectivity and the Wand-provided menus in the Robot.

    ---

1. **Why are Wi-Fiers important?**

    Wi-Fiers allow [Brands 🍏](<../../70 ✅ 🌳 Ambient/71 ✅ 💠 Brand Things/07 ✅ 🍏🎭 Brand role.md>) to easily make their products smarter:
    - users have a standard way to enable internet connectivity on any device using their generic Wallets.
    - Brands can develop edge APIs (e.g., on Raspberry Pi) with the assumption that internet connectivity will be available.

    ---

1. **What if the home Wi-Fi password changes?**

    Users can just repeat the connection process.

    ---
