# 📍 LOCATION prompt

> Part of [blocking input prompts 🤔](<../1 📘 Prompt features/09 ✏️ as Input.md>)

<br/>

1. **What's a LOCATION prompt?**

    It's a [Prompt 🤔](<../🤔 Prompt.md>) that asks for the user's current location.

    ---
    <br/>


1. **What's an example of a [Chat 💬](<../../12 💬 Chats/💬 Chat.md>)?**

    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🤗 Host | ℹ️ Tell us where you are.
    | 🤗 Host | [📍 Share location?](<91 📍 LOCATION prompt.md>)  | > Yes
    | 🤗 Host | ✅ That's downtown, OK!

    ---
    <br/>

1. **What are business cases?**

    |Category|Use case
    |-|-
    |🍽️ Restaurants| [Chef starts shift 🧑‍🍳](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/81 🧑‍🍳 Chef: Start shift 🪪.md>)
    |🍕 Order pizza| [Driver starts shift 🛵](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/81 🛵 Driver: Start shift.md>)
    |🕺 Night clubs| [Bouncer protects door 👮](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/71 👮 Bouncer: Protect door.md>)
    |💍 Userables| [Userable emergencies 🚨](<../../../70 🌳 Ambient/74 💍 Userables/02 💍🚨 Userable emergencies.md>)

    ---
    <br/>


1. **What's the format for a [Talker 😃](<../../../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>)?**

    ```yaml
    - LOCATION >> $placeholder
    ```

    |Parameter|Details
    |-|-
    | `$placeholder` | Stores the answer in this [$placeholder 💾](<../../../../9 😃 Talkers/30 🗃️ Talker data/10 💾 $Placeholder.md>)
    
    ---
    <br/>

1. **What's an example of a [Talker 😃](<../../../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>)?**

    ```yaml
    - LOCATION >> $loc
    ```

    ---
    <br/>


1. **How is that example in a [Prompted@Host](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>) response?**

    ```yaml
    Format: LOCATION
    ```

    ---
    <br/>

1. **What's the Answer in the [Reply@Host](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>) message?**

    ```yaml
    Answer: 
        Latitude: 40.7075
        Longitude: -74.0113
    ```