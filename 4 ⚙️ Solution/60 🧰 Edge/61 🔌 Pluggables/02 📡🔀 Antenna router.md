📡 Antenna router device
===

![](<.📎 Assets/🔌📡 Antenna.png>)

1. **What is an Antenna?**

    Antenna 📡 routers are devices that allow offline [Pluggable 🔌 devices](<01 🔌 Pluggable device.md>) to be controlled by a [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) from the internet.

    ----

1. **What are the technical features of Antennas?**

    | Feature | Details
    |-|-
    | `Protocol`| LoRaWA and Wi-Fi.
    | `Latency` | Around 100-milliseconds for 100-meters, increasing with distance.
    | `

    ---

1. **What are use-cases of domains with Antennas?**

    The following scenarios can be accomplished with under-100-milliseconds latency with a single antenna for every 100-meters radio:

    | [Domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) | Use case |
    |-|-
    | `Airports` | Connecting dozens of kiosks and gates.
    | `Banks` | Connecting all parts of a cash machine - e.g., [Ephemeral 🦋 device](<../62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>) for rotating QR/NFC, [Relayer 🎬 device](<../65 🎬 Relayers/04 🎬🔌 Relay device.md>) for cash drawer.
    | `Hotels` | Connecting hundreds of door locks in multiple floors with a single Antenna 📡.

    ---

1. **How do Antennas work?**

    Antennas have a set of standard input connections (e.g., USB) where domains admins can plug their [Pluggable 🔌](<01 🔌 Pluggable device.md>) devices. It then uses those inputs to send commands and receive notifications from the Pluggables.
    
    ---

1. **How do Antennas know the protocol of each Pluggable device?**

    They don't. 
    * When users plug the devices to an Antenna, the Antenna registers the device in the connected [🛰️ Relayer](<../../45 🤲 Helper domains/80 🛰️ Relayers/🛰️🤲 Relayer helper.md>);
    * The Relayer then sends the commands to Pluggable via the Antenna (e.g., `hello @port #1`).

    ---

1. **How do Antennas connect to the internet?**

    Via a [Wi-Fier 🛜](<03 🛜🔀 Wi-Fier router.md>).

    ---

1. **How do Antennas connect to the Relayer?**

    Antennas connect automatically to their [🛰️ Relayer](<../../45 🤲 Helper domains/80 🛰️ Relayers/🛰️🤲 Relayer helper.md>) as soon as they detect internet - this is a factory setting.

    ---

1. **How can domains leverage Antennas?**

    When a domain registers an Antenna, it gains access to the [Pluggable 🔌](<01 🔌 Pluggable device.md>) devices attached to the the Antenna.

    ---

1. **How can a domain register an Antenna?**

    After buying an Antenna from a [Brand 🍏](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>), a domain admin taps/scans the Antenna's [Locator](<../../25 Locators/1 🔆 Locators/🔆 Locator.md>) and follows the option to register the Antenna. In the process, the [🛰️ Relayer](<../../45 🤲 Helper domains/80 🛰️ Relayers/🛰️🤲 Relayer helper.md>) asks the user to share their domain ADMIN [Token 🎫](<../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) issued by the domain.

    ---
