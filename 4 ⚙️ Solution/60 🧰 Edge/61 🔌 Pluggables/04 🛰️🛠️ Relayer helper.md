🛰️ Relayer domains FAQ
===


1. **What is a Relayer domains?**

    Relayers 🛰️ are [Helper 🛠️ domains](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) 
    * that control on-premise [Antenna 📡 router devices](<02 📡🔀 Antenna router.md>) 
    * owned by other [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).
  
    ---


3. **Why are Relayer domains important?**

    | Feature | Description
    |-|-
    | `Connectivity` | Relayer 🛰️ helpers ensure that there is a bidirectional real-time communication over the internet between an on-premise [Pluggable 🔌 device](<01 🔌 Pluggable device.md>) and the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) who owns the [Antenna 📡 router device](<02 📡🔀 Antenna router.md>), thus removing the undifferentiated heavy-lifting of managing Wi-Fi onboarding and real-time communication with MQTT or WebSockets.
    | `API`| Relayer 🛰️ helpers help translate the machine-level APIs of [Pluggable 🔌 devices](<01 🔌 Pluggable device.md>) into natural language commands described in the [API Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) specified by the [Pluggable's Brand 🍏 domain](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>), thus allowing LLMs to use natural language to control the devices.

    ---

4. **How do Relayers work?**

    ![](<.📎 Assets/🔌🛰️ Relayer.png>)


    |#|Step|Description
    |-|-|-
    |1| `Antenna` | The on-premise [Antenna 📡 router device](<02 📡🔀 Antenna router.md>) creates a bidirectional channel with the Relayer 🛰️ helper.
    |2| `Pluggable` | The [Antenna 📡](<02 📡🔀 Antenna router.md>) detects the connection with the [Pluggable 🔌 device](<01 🔌 Pluggable device.md>) and informs the Relayer 🛰️.
    |3| `Brand` | The Relayer 🛰️ registers the [Pluggable's Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) in the [Pluggable's Brand 🍏 domain](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>).
    |4| `API Schema`| The [Brand 🍏](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>) tells the Relayer 🛰️ where to read the [API Schema 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) of the [Pluggable 🔌 device](<01 🔌 Pluggable device.md>).
    |5| `Graph`|  The Relayer 🛰️ domain reads the [API Schema 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) from a [Graph 🕸 helper domain](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>).
    |6| `Domain` | The Relayer 🛰️ domain informs the owner [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) of the newly-plugged [Pluggable 🔌 device](<01 🔌 Pluggable device.md>).
    |A| `Command`| The owner [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) sends a natural language command (e.g., `Test`) on the [Pluggable 🔌 device](<01 🔌 Pluggable device.md>).
    |B| `Translate`| The Relayer 🛰️ translates it with a cached [API Schema 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) and relays it via the [Antenna 📡 device](<02 📡🔀 Antenna router.md>).
    |C| `Execute` | The [Antenna 📡 router device](<02 📡🔀 Antenna router.md>) executes the translated command to the [Pluggable 🔌 device](<01 🔌 Pluggable device.md>).
    |X| `Listen` | The [Antenna 📡 router device](<02 📡🔀 Antenna router.md>) listens to machine-level events ⚠️ from the [Pluggable 🔌 device](<01 🔌 Pluggable device.md>).
    |Y| `Translate` | The [Antenna 📡 device](<02 📡🔀 Antenna router.md>) sends the events to the Relayer 🛰️ domain for natural language translation.
    |Z| `Propagate` | The Relayer 🛰️ sends sends the translated events to the [Buffer ⏳ helper](<../../40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) of the owner [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).

    ---


5. **How do domains send commands to Pluggables?**

    For a [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) to send an API command to a [Pluggable 🔌 device](<01 🔌 Pluggable device.md>) via a Relayer 🛰️ domain, it needs to send the following parameters.

    |Parameter|Description
    |-|-
    | `Antenna` | The UUID key of the [Antenna 📡 device](<02 📡🔀 Antenna router.md>) on the Relayer 🛰️ domain.
    | `Pluggable` | The UUID registration key of the [Pluggable 🔌 device](<01 🔌 Pluggable device.md>) in the context of the Relayer 🛰️ domain.
    | `Command` | The name of the command in the [Pluggable's API Schema 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) set by by the [Brand 🍏 domain](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>).
    | `Parameters`| Any command parameters, as defined by the [Pluggable's API Schema 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>).

    ---
