📡 Antenna router device FAQ
===

![](<.📎 Assets/🔌 Antenna.png>)

1. **What is an Antenna?**

    Antennas are devices that allow offline [Pluggable 🔌](<01 🔌 Pluggable device.md>) devices to be controlled by a domain from the internet.

    ---

1. **How do Antennas work?**

    Antennas have a set of standard input connections (e.g., USB) where domains admins can plug their [Pluggable 🔌](<01 🔌 Pluggable device.md>) devices. It then uses those inputs to send commands and receive notifications from the Pluggables.
    
    ---

1. **How do Antennas know the protocol of each Pluggable device?**

    They don't. 
    * When users plug the devices to an Antenna, the Antenna registers the device in the connected [🛰️ Relayer](<04 🛰️🏭 Relayer supplier.md>);
    * The Relayer then sends the commands to Pluggable via the Antenna (e.g., `hello @port #1`).

    ---

1. **How do Antennas connect to the internet?**

    Via a [Wi-Fier 🛜](<03 🛜🔀 Wi-Fier router.md>).

    ---

1. **How do Antennas connect to the Relayer?**

    Antennas connect automatically to their [🛰️ Relayer](<04 🛰️🏭 Relayer supplier.md>) as soon as they detect internet - this is a factory setting.

    ---

1. **How can domains leverage Antennas?**

    When a domain registers an Antenna, it gains access to the [Pluggable 🔌](<01 🔌 Pluggable device.md>) devices attached to the the Antenna.

    ---

1. **How can a domain register an Antenna?**

    After buying an Antenna from a [Brand 🍏](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>), a domain admin taps/scans the Antenna's [Locator](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) and follows the option to register the Antenna. In the process, the [🛰️ Relayer](<04 🛰️🏭 Relayer supplier.md>) asks the user to share their domain ADMIN [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) issued by the domain.

    ---
