# Non-blocking temporary info ⏳

> Part of [Non-blocking status prompts 🤔](<../1 📘 Prompt specs/08 ⚠️ as Status.md>)

<br/>

1. **What is a non-blocking TEMP?**

    A `TEMP`
    * is similar to an [INFO ℹ️ prompt](<21 ℹ️ INFO prompt.md>) 
    * but it is automatically removed when a new [Prompt 🤔](<../../10 📘 Talker specs/20 🤔 Prompt.md>) arrives;
    * if it contains [`Options`](<../1 📘 Prompt specs/04 🔘 with Options.md>), then the user may click an option while it's visible.


    ---
    <br/>



1. **What are use cases of TEMP?**

    |Wait for ...|Example
    |-|-
    | `hardware` | [Buy an item at a vending machine 🏪](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)
    | `software`| [Find a suitable bar nearby 🔎](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>)
    | `humans` | [Customers wait for take-away food 🍲](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/25 🍔 Fast food/11 🏪 Kiosk: Pay take-away.md>)
    | `new task` | [Baristas wait for orders 🍸](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/31 💁‍♀️ Barista: Serve.md>)
    | `network` | [Curators pull street-food menus 🌭](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    | `pick-up`| [Wait for a ride-hailing pick-up 🙋](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/11 🏠 Request.md>) | 
    | `tap` | [Tap inside the car to confirm 🙋](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/2 🙋 Customer @ Car 🚕/22 🚕 Enter wrong car.md>)
    | `drop-off` | [Expected arrival time at drop-off 🚕](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/2 🙋 Customer @ Car 🚕/21 🚕 Enter right car.md>)
    ---
    <br/>



1. **What features do TEMP prompts it implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../1 📘 Prompt specs/04 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    
    
    ---
    <br/>



1. **What's the TEMP format for a [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>)?**

    ```yaml
    # Inline
    TEMP|<statement> 
    ```
    
    | Argument| Purpose | Example
    |-|-|-
    | `<statement>` |  Message for the user. | `Running...`

    ```yaml
    # Multi-line 
    TEMP:
        Statement: <statement>
        
        # Generic optional properties
        Details: string
        Options: csv|string[]|object
        Appendix: {function}
    ```
    

    | Argument| Purpose | Example
    |-|-|-
    | `Details` | Optional [expandable details ⊕](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<../1 📘 Prompt specs/04 🔘 with Options.md>) | `A,B` `{A:B}`
    | `Appendix` | Optional [file attachment 📎](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | `{/...}`


    ---
    <br/>


1. **What do TEMP prompts look like in a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)?**

    

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ⏳ Simple temp.
    | [🛠️ Helper](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>) | ⏳ Simple temp.
    | [🫥 Agent](<../../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | ⏳ Simple temp.
    |

    <br/>

    Here's the [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>).
    
    ```yaml
    # Talker 😃
    - TEMP|Simple temp.
    ```
    
    <br/>

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: TEMP
    Statement: ⏳ Simple temp.
    ```
    
    
    ---
    <br/>



