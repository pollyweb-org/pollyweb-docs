# 📍 LOCATION prompt

> Part of [blocking input prompts 🤔](<20 Blocking inputs.md>)

<br/>

1. **What's an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    | Service | Prompt | User
    | - | - | - |
    | 🤗 Host | ℹ️ Tell us where you are.
    | 🤗 Host | [📍 Share location?](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/61 📍 LOCATION prompt.md>)  | > Yes
    | 🤗 Host | ✅ That's downtown, OK!

    ---
    <br/>

2. **What are business cases?**

    |Category|Use case
    |-|-
    |🍽️ Restaurants| [Chef starts shift 🧑‍🍳](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/81 🧑‍🍳 Chef: Start shift 🪪.md>)
    |🍕 Order pizza| [Driver starts shift 🛵](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/81 🛵 Driver: Start shift.md>)
    |🕺 Night clubs| [Bouncer protects door 👮](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/71 👮 Bouncer: Protect door.md>)
    |💍 Userables| [Userable emergencies 🚨](<../../70 🌳 Ambient/74 💍 Brand Userables/02 💍🚨 Userable emergencies.md>)

    ---
    <br/>


3. **What's the content for a [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>)?**

    ```yaml
    - LOCATION >> <key>
    ```

    |Parameter|Details
    |-|-
    | `key` | Stores the answer with this key
    
    ---
    <br/>


5. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: LOCATION
    ```

    ---
    <br/>

6. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    Answer: 
        Latitude: 40.7075
        Longitude: -74.0113
    ```