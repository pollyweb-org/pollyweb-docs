# ⏳ Non-blocking temporary info 

> Part of [Non-blocking status prompts 🤔](<../../🤔⚙️ Prompt features/8 ⚠️ as Status.md>)

<br/>

1. **What is a non-blocking TEMP?**

    A `TEMP`
    * is similar to an [INFO ℹ️ prompt](<../INFO ℹ️/INFO ℹ️ prompt.md>) 
    * but it is automatically removed when a new [Prompt 🤔](<../../🤔 Prompt.md>) arrives;
    * if it contains [`Options`](<../../🤔⚙️ Prompt features/4 🔘 with Options.md>), then the user may click an option while it's visible.


    ---
    <br/>



1. **What are use cases of TEMP?**

    |Wait for ...|Example
    |-|-
    | `hardware` | [Buy an item at a vending machine 🏪](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)
    | `software`| [Find a suitable bar nearby 🔎](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>)
    | `humans` | [Customers wait for take-away food 🍲](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/25 🍔 Fast food/11 🏪 Kiosk: Pay take-away.md>)
    | `new task` | [Baristas wait for orders 🍸](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/31 💁‍♀️ Barista: Serve.md>)
    | `network` | [Curators pull street-food menus 🌭](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    | `pick-up`| [Wait for a ride-hailing pick-up 🙋](<../../../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/11 🏠 Request.md>) | 
    | `tap` | [Tap inside the car to confirm 🙋](<../../../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/2 🙋 Customer @ Car 🚕/22 🚕 Enter wrong car.md>)
    | `drop-off` | [Expected arrival time at drop-off 🚕](<../../../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/2 🙋 Customer @ Car 🚕/21 🚕 Enter right car.md>)
    ---
    <br/>



1. **What features do TEMP prompts it implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../../🤔⚙️ Prompt features/4 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    
    
    ---
    <br/>



1. **What's the TEMP format for a [Talker 😃](<../../../😃 Talkers/😃 Talker role.md>)?**

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
    | `Details` | Optional [expandable details ⊕](<../../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<../../🤔⚙️ Prompt features/4 🔘 with Options.md>) | `A,B` `{A:B}`
    | `Appendix` | Optional [file attachment 📎](<../../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | `{/...}`


    ---
    <br/>


1. **What do TEMP prompts look like in a [Chat 💬](<../../../💬 Chats/💬 Chat.md>)?**

    

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ⏳ Simple temp.
    | [🤲 Helper](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | ⏳ Simple temp.
    | [🫥 Agent](<../../../../50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) | ⏳ Simple temp.
    |

    <br/>

    Here's the [Talker 😃](<../../../😃 Talkers/😃 Talker role.md>).
    
    ```yaml
    # Talker 😃
    - TEMP|Simple temp.
    ```
    
    <br/>

    Here's the [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted/🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: TEMP
    Statement: ⏳ Simple temp.
    ```
    
    
    ---
    <br/>



