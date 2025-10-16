🛰️ Relayer domains
===


1. **What is a Relayer domains?**

    Relayers 🛰️ are [Helper 🤲 domains](<../$ 🤲 Helpers/🤲👥 Helper domain.md>) 
    * that control on-premise [Antenna 📡 router devices](<../../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>) 
    * owned by other [domains 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>).
  
    ---


1. **Why are Relayer domains important?**

    | Feature | Description
    |-|-
    | `Connectivity` | Relayer 🛰️ helpers ensure that there is a bidirectional real-time communication over the internet between an on-premise [Pluggable 🔌 device](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>) and the [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) who owns the [Antenna 📡 router device](<../../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>), thus removing the undifferentiated heavy-lifting of managing Wi-Fi onboarding and real-time communication with MQTT or WebSockets.
    | `API`| Relayer 🛰️ helpers help translate the machine-level APIs of [Pluggable 🔌 devices](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>) into natural language commands described in the [API Schema Code 🧩](<../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) specified by the [Pluggable's Brand 🍏 domain](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>), thus allowing LLMs to use natural language to control the devices.

    ---

1. **How do Relayers work?**

    ![](<../../60 🧰 Edge/61 🔌 Pluggables/.📎 Assets/🔌🛰️ Relayer.png>)


    |#|Step|Description
    |-|-|-
    |1| `Antenna` | The on-premise [Antenna 📡 router device](<../../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>) creates a bidirectional channel with the Relayer 🛰️ helper.
    |2| `Pluggable` | The [Antenna 📡](<../../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>) detects the connection with the [Pluggable 🔌 device](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>) and informs the Relayer 🛰️.
    |3| `Brand` | The Relayer 🛰️ registers the [Pluggable's Locator 🔆](<../../25 Locators/15 🔆 Locators/🔆 Locator.md>) in the [Pluggable's Brand 🍏 domain](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>).
    |4| `API Schema`| The [Brand 🍏](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>) tells the Relayer 🛰️ where to read the [API Schema 🧩](<../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) of the [Pluggable 🔌 device](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>).
    |5| `Graph`|  The Relayer 🛰️ domain reads the [API Schema 🧩](<../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) from a [Graph 🕸 helper domain](<../50 🕸 Graphs/🕸🤲 Graph helper.md>).
    |6| `Domain` | The Relayer 🛰️ domain informs the owner [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) of the newly-plugged [Pluggable 🔌 device](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>).
    |A| `Command`| The owner [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) sends a natural language command (e.g., `Test`) on the [Pluggable 🔌 device](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>).
    |B| `Translate`| The Relayer 🛰️ translates it with a cached [API Schema 🧩](<../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) and relays it via the [Antenna 📡 device](<../../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>).
    |C| `Execute` | The [Antenna 📡 router device](<../../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>) executes the translated command to the [Pluggable 🔌 device](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>).
    |X| `Listen` | The [Antenna 📡 router device](<../../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>) listens to machine-level events ⚠️ from the [Pluggable 🔌 device](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>).
    |Y| `Translate` | The [Antenna 📡 device](<../../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>) sends the events to the Relayer 🛰️ domain for natural language translation.
    |Z| `Propagate` | The Relayer 🛰️ sends sends the translated events to the [Buffer ⏳ helper](<../27 ⏳ Buffers/⏳🤲 Buffer helper.md>) of the owner [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>).

    ---


1. **How do domains send commands to Pluggables?**

    For a [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) to send an API command to a [Pluggable 🔌 device](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>) via a Relayer 🛰️ domain, it needs to send the following parameters.

    |Parameter|Description
    |-|-
    | `Antenna` | The UUID key of the [Antenna 📡 device](<../../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>) on the Relayer 🛰️ domain.
    | `Pluggable` | The UUID registration key of the [Pluggable 🔌 device](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>) in the context of the Relayer 🛰️ domain.
    | `Command` | The name of the command in the [Pluggable's API Schema 🧩](<../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) set by by the [Brand 🍏 domain](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>).
    | `Parameters`| Any command parameters, as defined by the [Pluggable's API Schema 🧩](<../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>).

    ---
