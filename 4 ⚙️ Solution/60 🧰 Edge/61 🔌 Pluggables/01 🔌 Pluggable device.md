
🔌 Pluggable devices FAQ
===

1. **What is a Pluggable?**

    In NLWeb, Pluggables 🔌 are a domain-owned peripheral devices that domains can send commands to and receive events from.

    ---


5. **How do users install a Pluggable?**

    ![](<.📎 Assets/🔌 Pluggable.png>)

    Installing a Pluggable 🔌 device requires the following steps.

    |#|Step
    |-|-
    |1| The device owner connects the Pluggable 🔌 device to the [Antenna 📡 router](<02 📡🔀 Antenna router.md>), as well as any power source required by the Pluggable 🔌 device.
    |2| The owner taps/scans the [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) of the [Antenna 📡 router](<02 📡🔀 Antenna router.md>) with their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to open a chat with its [Relayer 🛰️ helper](<04 🛰️🛠️ Relayer helper.md>), and ask to add a Pluggable - the Relayer asks the user to tap/scan the Pluggable;

    - 3/ users taps/scans the [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) of the Pluggable 🔌 device - the [Relayer 🛰️ helper](<04 🛰️🛠️ Relayer helper.md>) confirms that a device with the Pluggable's resource key is connected, and the Pluggable's API [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) is valid.

    ---


6. **What are examples of Pluggable devices?**

    | Pluggable 🛠️ | Responsibility 
    |-|-
    | ✨ [Scanners](<../66 ✨ Scanners/06 ✨🔌 Scanner device.md>) | For users to tap their  [Things 💠](<../../70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>), [Userables 💍](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>), and [Tapbands ⌚](<../../70 🌳 Ambient/76 ⌚ Brand Tapbands/01 ⌚💠 Tapband thing.md>).
    | 📸 [Cameras](<../64 📸 Selfies/01 📸🔌 Selfie device.md>) | For users to [take a selfie 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/00 🧑‍💻 Unsupervised ID index.md>) for their [Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>).
    | 🖐️ [Palmists](<../63 🖐️ Palmists/01 🖐️🔌 Palmist device.md>) | Tor users to [scan their palm 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/07 🖐️ Palm pay landscape/00 🖐️ Palm pay index.md>) for their [Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>).
    | 🎬 [Relays](<../65 🎬 Relayers/04 🎬🔌 Relay device.md>) | For [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) to remotely control electrical circuits.
    | 🦋 [Ephemerals](<../62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>) | Rotates [QR/NFC Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) to ensure users are standing next to the device.

    ---

7. **Do Pluggable devices connect to Wi-Fi?**

    No.
    * Instead, Pluggables 🛠️ connect to an [Antenna 📡 router device](<02 📡🔀 Antenna router.md>), which in turn connects to the Internet.

    ---

8. **Do Pluggables devices follow a standard communication protocol?**

    No. 
    - [Brand 🍏 domain](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>) specify a Pluggable 🛠️ API via when printing the [Pluggable's Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>), which includes the [API's Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>).
    - [Relayer 🛰️ helpers](<04 🛰️🛠️ Relayer helper.md>) receive commands from domains in natural language and then translate them to the Pluggable's API via de [Antenna 📡](<02 📡🔀 Antenna router.md>).

    ---

9. **Do Pluggables support bidirectional communication?**

    Yes.
    - Bidirectional communication is done via the [Antenna 📡 router device](<02 📡🔀 Antenna router.md>).
    - Pluggables receive commands from and send events to the Antenna via cable, using whatever protocol is supported by the Pluggable (e.g., USB).
    - Antennas manage the translation from the Pluggable's native protocol into a web protocol that the owner domain can handle.

    ---


5. **How do domains receive events from Pluggables?**

    Regarding events, domains receive a payload similar to a command request.

    ---
