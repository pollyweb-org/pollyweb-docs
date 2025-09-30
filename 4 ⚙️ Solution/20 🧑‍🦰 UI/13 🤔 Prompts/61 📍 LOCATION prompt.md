# 📍 LOCATION prompt

> Part of [blocking input prompts 🤔](<20 Blocking inputs.md>)

<br/>

1. **What is an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    | Service | Prompt | User
    | - | - | - |
    | 🤗 Host | ℹ️ Tell us where you are.
    | 🤗 Host | 📍 Share location?  | > Yes
    | 🤗 Host | ✅ That's downtown, OK!

    ---
    <br/>

2. **What are usage examples?**

    |Category|Use case
    |-|-
    |`🍽️ Restaurants`| [Chefs start shifts](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/81 🧑‍🍳 Chef: Start shift 🪪.md>)

    ---
    <br/>

3. **What is the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) call?**

    ```yaml
    Format: LOCATION
    ```

    ---
    <br/>

4. **What is the content for a [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>)?**

    ```yaml
    - LOCATION >> <key>
    ```

    |Parameter|Details
    |-|-
    | `key` | Stores the answer with this key
    
    ---
    <br/>