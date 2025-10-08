# 📍 LOCATION prompt

> Part of [blocking input prompts 🤔](<../10 Prompt definitions/11 ✏️ Input behavior.md>)

<br/>

1. **What's a LOCATION prompt?**

    It's a [Prompt 🤔](<../10 Prompt definitions/01 🤔 Prompt.md>) that asks for the user's current location.

    ---
    <br/>


1. **What's an example of a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)?**

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../10 Prompt definitions/01 🤔 Prompt.md>) | [User](<../0../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Promp../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md
    | - | - | - |
    | 🤗 Host | ℹ️ Tell us where you are.
    | 🤗 Host | [📍 Share location?](<91 📍 LOCATION prompt.md>)  | > Yes
    | 🤗 Host | ✅ That's downtown, OK!

    ---
    <br/>

1. **What are business cases?**

    |Category|Use case
    |-|-
    |🍽️ Restaurants| [Chef starts shift 🧑‍🍳](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/81 🧑‍🍳 Chef: Start shift 🪪.md>)
    |🍕 Order pizza| [Driver starts shift 🛵](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/81 🛵 Driver: Start shift.md>)
    |🕺 Night clubs| [Bouncer protects door 👮](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/71 👮 Bouncer: Protect door.md>)
    |💍 Userables| [Userable emergencies 🚨](<../../../4 ⚙️ Solution/70 🌳 Ambient/74 💍 Brand Userables/02 💍🚨 Userable emergencies.md>)

    ---
    <br/>


1. **What's the format for a [Talker 😃](<../../01 😃 Talker.md>)?**

    ```yaml
    - LOCATION >> $placeholder
    ```

    |Parameter|Details
    |-|-
    | `$placeholder` | Stores the answer in this placeholder
    
    ---
    <br/>

1. **What's an example of a [Talker 😃](<../../01 😃 Talker.md>)?**

    ```yaml
    - LOCATION >> $loc
    ```

    ---
    <br/>


1. **How is that example in a [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) response?**

    ```yaml
    Format: LOCATION
    ```

    ---
    <br/>

1. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    Answer: 
        Latitude: 40.7075
        Longitude: -74.0113
    ```