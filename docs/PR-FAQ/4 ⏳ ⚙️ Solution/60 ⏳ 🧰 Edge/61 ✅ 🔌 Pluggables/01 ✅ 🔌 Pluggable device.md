
🛠️ Pluggable devices FAQ
===

![](<./📎 Assets/🔌 Pluggable.png>)

1. **What is a Pluggable?**

    In NLWeb, Pluggables are a domain-owned peripheral devices that domains can send commands to and receive events from.

    ---

1. **What are examples of Pluggables?**

    Examples of Pluggables include:
    * ✨ [Scanners](<../66 ⏳ ✨ Scanners/06 ⏳ ✨🔌 Scanner device.md>) for users to tap/scan their NFQ/QR Tokens, Things, and Userables;
    * 📸 [Cameras](<../64 ⏳ 📸 Selfies/01 ⏳ 📸🔌 Selfie device.md>) to take a selfie for [Identity 🆔](<../../30 ⏳ 🫥 Agents/05 ✅ 🆔 Identities/03 ✅ 🆔🫥 Identity agent.md>) domains;
    * 🖐️ [Palmists](<../63 ✅ 🖐️ Palmists/01 ✅ 🖐️🔌 Palmist device.md>) for users to scan their palm for [Identity 🆔](<../../30 ⏳ 🫥 Agents/05 ✅ 🆔 Identities/03 ✅ 🆔🫥 Identity agent.md>) domains;
    * 🎬 [Relays](<../65 ⏳ 🎬 Relayers/04 ⏳ 🎬🔌 Relay device.md>) to open doors and gates;
    * 🦋 [Ephemerals](<../62 ⏳ 🦋 Ephemerals/03 ⏳ 🦋🔌 Ephemeral device.md>) to ensure users are standing next to a Relay.

    ---

1. **Do Pluggables connect to Wi-Fi?**

    No. Pluggables connect via cable to an [Antenna 📡](<02 ✅ 📡🔀 Antenna router.md>), which in turn connects to the internet connectivity.

    ---

1. **To Pluggables follow a standard communication protocol?**

    No. 
    - [Brands 🍏](<../../70 ✅ 🌳 Ambient/71 ✅ 💠 Brand Things/07 ✅ 🍏🎭 Brand role.md>) specify a Pluggable API via when printing the Pluggable's [Locator 🔆](<../../20 ✅ 🧑‍🦰 UI/22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>), which includes the API's [Schema Code 🧩](<../../20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/02 ✅ 🧩 Schema Code.md>).
    - [🛰️ Relayers](<04 ✅ 🛰️🏭 Relayer supplier.md>) receive commands from domains in natural language and then translate them to the Pluggable's API via de [Antenna 📡](<02 ✅ 📡🔀 Antenna router.md>).

    ---

1. **Do Pluggables support bidirectional communication?**

    Yes, via the [Antenna 📡](<02 ✅ 📡🔀 Antenna router.md>).
    - Pluggables receive commands from and send events to the Antenna via cable, using whatever protocol is supported by the Pluggable (e.g., USB).
    - Antennas manage the translation from the Pluggable's native protocol into a web protocol that the owner domain can handle.

    ---

1. **How do users install a Pluggable?**

    Installing a Pluggable requires the following steps:

    - 1/ users physically connect the Pluggable's cable to the [Antenna 📡](<02 ✅ 📡🔀 Antenna router.md>), as well as any power source required by the Pluggable;

    - 2/ users tap/scan the Antenna's [Locator 🔆](<../../20 ✅ 🧑‍🦰 UI/22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>) to open a chat with its [🛰️ Relayer](<04 ✅ 🛰️🏭 Relayer supplier.md>), and ask to add a Pluggable - the Relayer asks the user to tap/scan the Pluggable;

    - 3/ users tap/scan the Pluggable's Locator - the Relayer confirms that a device with the Pluggable's resource key is connected, and the Pluggable's API [Schema Code 🧩](<../../20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/02 ✅ 🧩 Schema Code.md>) is valid.

    ---
