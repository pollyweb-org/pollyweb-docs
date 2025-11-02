
🔌 Pluggable devices
===

1. **What is a Pluggable?**

    In NLWeb, Pluggables 🔌 are a domain-owned peripheral devices that domains can send commands to and receive events from.

    ---


1. **How do users install a Pluggable?**

    ![](<.📎 Assets/🔌 Pluggable.png>)

    Installing a Pluggable 🔌 device requires the following steps.

    |#|Step
    |-|-
    |1| The device owner connects the Pluggable 🔌 device to the [Antenna 📡 router](<02 📡🔀 Antenna router.md>), as well as any power source required by the Pluggable 🔌 device.
    |2| The owner taps/scans the [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) of the [Antenna 📡 router](<02 📡🔀 Antenna router.md>) with their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to open a chat with its [Relayer 🛰️ helper](<../../45 🤲 Helper domains/Relayers 🛰️/🛰️🤲 Relayer helper.md>), and ask to add a Pluggable - the Relayer asks the user to tap/scan the Pluggable;

    - 3/ users taps/scans the [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) of the Pluggable 🔌 device - the [Relayer 🛰️ helper](<../../45 🤲 Helper domains/Relayers 🛰️/🛰️🤲 Relayer helper.md>) confirms that a device with the Pluggable's resource key is connected, and the Pluggable's API [Schema 🧩](<../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) is valid.

    ---


1. **What are examples of Pluggable devices?**

    | Pluggable 🛠️ | Responsibility 
    |-|-
    | ✨ [Scanners](<../66 ✨ Scanners/06 ✨🔌 Scanner device.md>) | For users to tap their  [Things 💠](<../../25 🔆 Locators/Things 💠/💠🔆 Thing locator.md>), [Userables 💍](<../../25 🔆 Locators/Userables 💍/💍💠 Userable thing.md>), and [Tapbands ⌚](<../../25 🔆 Locators/Tapbands ⌚/⌚💠 Tapband thing.md>).
    | 📸 [Cameras](<../64 📸 Selfies/01 📸🔌 Selfie device.md>) | For users to [take a selfie 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/07 🧑‍💻 Unsupervised ID landscape/00 🧑‍💻 Unsupervised ID index.md>) for their [Identity 🆔 agent](<../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>).
    | 🖐️ [Palmists](<../63 🖐️ Palmists/01 🖐️🔌 Palmist device.md>) | Tor users to [scan their palm 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/07 🖐️ Palm pay landscape/00 🖐️ Palm pay index.md>) for their [Identity 🆔 agent](<../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>).
    | 🎬 [Relays](<../65 🎬 Relayers/04 🎬🔌 Relay device.md>) | For [domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) to remotely control electrical circuits.
    | 🦋 [Ephemerals](<../62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>) | Rotates [QR/NFC Locators 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) to ensure users are standing next to the device.

    ---

1. **Do Pluggable devices connect to Wi-Fi?**

    No.
    * Instead, Pluggables 🛠️ connect to an [Antenna 📡 router device](<02 📡🔀 Antenna router.md>), which in turn connects to the Internet.

    ---

1. **Do Pluggables devices follow a standard communication protocol?**

    No. 
    - [Brand 🍏 domain](<../../41 🎭 Domain Roles/Brands 🍏/🍏🎭 Brand role.md>) specify a Pluggable 🛠️ API via when printing the [Pluggable's Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>), which includes the [API's Schema Code 🧩](<../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>).
    - [Relayer 🛰️ helpers](<../../45 🤲 Helper domains/Relayers 🛰️/🛰️🤲 Relayer helper.md>) receive commands from domains in natural language and then translate them to the Pluggable's API via de [Antenna 📡](<02 📡🔀 Antenna router.md>).

    ---

1. **Do Pluggables support bidirectional communication?**

    Yes.
    - Bidirectional communication is done via the [Antenna 📡 router device](<02 📡🔀 Antenna router.md>).
    - Pluggables receive commands from and send events to the Antenna via cable, using whatever protocol is supported by the Pluggable (e.g., USB).
    - Antennas manage the translation from the Pluggable's native protocol into a web protocol that the owner domain can handle.

    ---


1. **How do domains receive events from Pluggables?**

    Regarding events, domains receive a payload similar to a command request.

    ---
