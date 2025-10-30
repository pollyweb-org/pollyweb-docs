# 📍 LOCATION prompt

> Part of [blocking input prompts 🤔](<../../🤔⚙️ Prompt features/9 ✏️ as Input.md>)

<br/>

1. **What's a LOCATION prompt?**

    It's a [Prompt 🤔](<../../🤔 Prompt.md>) that asks for the user's current location.

    ---
    <br/>


1. **What's an example of a [Chat 💬](<../../../Chats 💬/💬 Chat.md>)?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🤗 Host | ℹ️ Tell us where you are.
    | 🤗 Host | [📍 Share location?](<LOCATION 📍 prompt.md>)  | > Yes
    | 🤗 Host | ✅ That's downtown, OK!

    ---
    <br/>

1. **What are business cases?**

    |Category|Use case
    |-|-
    |🍽️ Restaurants| [Chef starts shift 🧑‍🍳](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/81 🧑‍🍳 Chef: Start shift 🪪.md>)
    |🍕 Order pizza| [Driver starts shift 🛵](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/81 🛵 Driver: Start shift.md>)
    |🕺 Night clubs| [Bouncer protects door 👮](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/71 👮 Bouncer: Protect door.md>)
    |💍 Userables| [Userable emergencies 🚨](<../../../../25 🔆 Locators/Userables 💍/💍⏩ Userable flows/💍🚨 Emergencies.md>)

    ---
    <br/>


1. **What's the format for a [Talker 😃](<../../../Talkers 😃/😃🤲 Talker helper.md>)?**

    ```yaml
    - LOCATION >> $holder
    ```

    |Parameter|Details
    |-|-
    | `$holder` | Stores the answer in this [holder 🧠](<../../../Scripts 📃/📃 basics/Holder 🧠.md>)
    
    ---
    <br/>

1. **What's an example of a [Talker 😃](<../../../Talkers 😃/😃🤲 Talker helper.md>)?**

    ```yaml
    - LOCATION >> $loc
    ```

    ---
    <br/>


1. **How is that example in a [Prompted@Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) response?**

    ```yaml
    Format: LOCATION
    ```

    ---
    <br/>

1. **What's the Answer in the [Reply@Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>) message?**

    ```yaml
    Answer: 
        Latitude: 40.7075
        Longitude: -74.0113
    ```