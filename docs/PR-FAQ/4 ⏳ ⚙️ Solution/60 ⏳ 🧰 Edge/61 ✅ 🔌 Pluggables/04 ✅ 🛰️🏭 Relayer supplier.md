🛰️ Pluggable domains FAQ
===

![](<./📎 Assets/🔌 Relayer.png>)

1. **What is a Relayer?**

    Relayers are [Suppliers 🏭](<../../30 ⏳ 🫥 Agents/06 ✅ 🛎️ Concierges/02 ✅ 🏭🎭 Supplier role.md>) of [Antenna 📡](<02 ✅ 📡🔀 Antenna router.md>) routers.

    ---

1. **Why are Relayers important?**

    Relayers ensure there is a bidirectional communication with [Pluggable 🔌](<01 ✅ 🔌 Pluggable device.md>) devices, and transform the machine communication with Pluggables into the natural language commands described in the Pluggable's API.

    ---

1. **Where do Relayers get the Pluggable's API from?**

    To get the [Pluggable 🔌](<01 ✅ 🔌 Pluggable device.md>)'s API description, Relayers take the following steps:
    - 1/ receive a registration request for a Pluggable device;
    - 2/ extract the API [Schema Code 🧩](<../../20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/02 ✅ 🧩 Schema Code.md>) from the Pluggable's [Locator 🔆](<../../20 ✅ 🧑‍🦰 UI/22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>);
    - 3/ get the Schema Code definition from a [Graph 🕸](<../../40 ✅ 👥 Domains/44 ✅ 📜 Manifests/03 ✅ 🕸👥 Graph helper.md>).

    ---

1. **How do domains send commands to Pluggables?**

    For a domain to send a command to a Pluggable, it sends the command to the Relayer mentioning:
    - the key of the [Antenna 📡](<02 ✅ 📡🔀 Antenna router.md>);
    - the key of the [Pluggable 🔌](<01 ✅ 🔌 Pluggable device.md>) in that Antenna;
    - the name of the command in the Pluggable's API;
    - any command parameters.

    ---

1. **How do domains receive events from Pluggables?**

    Regarding events, domains receive a payload similar to a command request.

    ---
