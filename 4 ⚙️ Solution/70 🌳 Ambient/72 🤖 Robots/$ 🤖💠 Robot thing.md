🤖 Robot Things
===

1. **What are Robots in NLWeb?**

    Robots 🤖 are [Things 💠](<../71 💠 Things/$ 💠 Thing.md>) that [Brands 🍏](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>) embed into physical devices to enable them to be controlled locally or remotely using natural language and without the need for a digital display (e.g., a coffee machine, a printer, or a vehicle). 

    ---

1. **How can Brands embed a Robot into a coffee machine?**
    
    ![](<. 📎 Assets/🤖 Robot.png>)

    For a Brand to embed a Robot 🤖 into a traditional coffee machine, it needs the following:
    - a [Pluggable 🔌](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>) controller for the mechanical parts (e.g., Raspberry Pi);
    - a [Schema Code 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) describing the commands and events in the Pluggable API;
    - an [Antenna 📡](<../../60 🧰 Edge/61 🔌 Pluggables/02 📡🔀 Antenna router.md>) to provide directional communication to the Pluggable controller;
    - a [Wi-Fier 🛜](<../../60 🧰 Edge/61 🔌 Pluggables/03 🛜🔀 Wi-Fier router.md>) to provide internet connectivity to the Antenna;
    - a Robot [Thing 💠](<../71 💠 Things/$ 💠 Thing.md>) [Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) created by a [Wand 🪄](<../../45 🤲 Helper domains/90 🪄 Wands/🪄🤲 Wand helper.md>);
    - an NFC/QR tag for the Robot 🤖 (e.g., acquired from a [Printer 🖨️](<../../45 🤲 Helper domains/75 🖨️ Printers/🖨️🤲 Printer helper.md>)).

    ---

1. **How do users interact with a coffee machine Robot?**

    ![](<. 📎 Assets/🤖 Robot$Usage.png>)

    With a Robot 🤖, users can use natural language to:
    - ask questions (e.g., `do you serve espressos?`);
    - issue commands (e.g., `serve an espresso`);
    - receive alerts and events (e.g., `add water`).

    ---

1. **How can Robots answer questions about their features?**

    [Wands 🪄](<../../45 🤲 Helper domains/90 🪄 Wands/🪄🤲 Wand helper.md>) managing Robots use the [Schema Code 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) provided by the [Brand 🍏](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>) to get the user manuals of the Robot 🤖, then typically feed it to a GenAI algorithm.
    
    ---

1. **How can Robots execute commands?**

    Additionally to answering questions, [Wands 🪄](<../../45 🤲 Helper domains/90 🪄 Wands/🪄🤲 Wand helper.md>) use the [Schema Code 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) provided by the [Brand 🍏](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>) to get the API definition of the Robot's [Pluggable 🔌](<../../60 🧰 Edge/61 🔌 Pluggables/01 🔌 Pluggable device.md>) controller, then typically run it through a GenAI agent.

    ---
