# Non-blocking temporary info ⏳

> Part of [Non-blocking status prompts 🤔](<08 🤔✨ with Status behavior.md>)

<br/>

1. **What is a non-blocking TEMP?**

    This is an [INFO ℹ️ prompt](<11 ℹ️ INFO prompt.md>) that is automatically removed when a new prompt arrives;
    - if it contains options, then the user may click an option while it's visible.


    ---
    <br/>

1. **How does it look in a Chat?**

    Consider the following [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    TEMP|Simple temp.
    ```

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ⏳ Simple temp.
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | ⏳ Simple temp.
    | [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | ⏳ Simple temp.
    
    
    
    ---
    <br/>




1. **What are use cases of TEMP?**

    |Type|Example
    |-|-
    | `Wait for hardware` | [Buy an item at a vending machine 🏪](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)
    | `Wait for software`| [Find a suitable bar nearby 🔎](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>)
    | `Wait for humans` | [Customers wait for take-away food 🍲](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/25 🍔 Fast food/11 🏪 Kiosk: Pay take-away.md>)
    | `Wait for new task` | [Baristas wait for orders 🍸](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/31 💁‍♀️ Barista: Serve.md>)
    | `Wait for network` | [Curators pull street-food menus 🌭](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    | `Wait for pick-up`| [Wait for a ride-hailing pick-up 🙋](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/11 🏠 Request.md>) | 
    | `Count-down to tap` | [Tap inside the car to confirm 🙋](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/2 🙋 Customer @ Car 🚕/22 🚕 Enter wrong car.md>)
    | `Time to drop-off` | [Expected arrival time at drop-off 🚕](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/2 🙋 Customer @ Car 🚕/21 🚕 Enter right car.md>)
    ---
    <br/>


1. **What's the format for a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    TEMP|<message>|<options> >> <key>
    ```
    
    ---
    <br/>



1. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: TEMP
    Message: <message>
    Options: <options>
    ```
    ---
    <br/>

1. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    Answer: <selected-option> # if any
    ```
    
    ---
    <br/>