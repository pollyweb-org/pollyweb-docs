# Order to the table  🍔

> From [Eat fast food 🍔](<01 🍔 Index.md>)

<br/>

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) table
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Fast Food (4.3 ⭐)  [+]
| 🍔 Fast Food | ℹ️ You're on table 28 [+]
| 🍔 Fast Food | 😃 Hi! What do you need? <br/>- [ Order ] <br/>- [ Something else ] | > Order
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/> - your vitalogist reviews 💖 <br/> - your payer pays 💳 <br/> - we'll deliver to your table 🍔 <br/> - your vitalogist records it 💖 | > Yes
| 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | 💭 Some suggestions: [All, No] <br/>- [ ] house burger 🍔 (£3.00) <br/> - [ ] still water (25 cl) 💧 (£1.00) <br/> |  > All
| 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | 💭 Anything else? [No] <br/> - [ ] coffee ☕ (£0.90) | > No
| 🍔 Fast Food | ℹ️ Order (£4.00) [+] <br/>- 1 house burger 🍔 (£3.00) <br/> - 1 still water (25 cl) 💧 (£1.00) <br/>  - to deliver at table 28
| 💖 [Vitalogist](<../../../4 ⚙️ Solution/30 🫥 Agents/09 💖 Vitalogists/01 💖🫥 Vitalogist agent.md>) | 🫥 Confirm? [Yes, No] <br/> - burger is outside your diet  | > Yes
| 💳 [Payer](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay £4.00 bill? 🧾 [No] <br/>- [ Card ABC ] + $0.10 <br/>- [ Card DEF ] (free) | > Card ABC |
| 🍔 Fast Food | ✅ Eat-in submitted [+]
| 🍔 Fast Food | ⏳ Order in queue... [+] 
...
||



<br/>

## 💼 Business Setup

1. **What does the [😃 Domain Talker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/01 😃 Talker.md>) look like?**

    ```yaml
    💬 Order:
    - FLOW|order
    - SHARE|nlweb.org/CURATOR/ORDER|{menu-locator} # 🧚 
    - INFO|{order-summary}|Change
    - SHARE|nlweb.org/VITALOGIST/REVIEW|{order-details} # 💖
    - CHARGE|{amount} 
    - SUCCESS|Eat-in submitted:
      - EXPAND: {order-summary}
    - TEMP|Order in queue...:
      - EXPAND: {order-summary}
    ```

    |Functions|Returns|Description
    |-|-|-
    | `menu-locator` | string | [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) of the menu.
    | `order-summary`| markdown | [Curator 🧚 agent](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) choices:<br/>- plus ongoing status.
    |

<br/> 

1. **What does the Manifest Flow look like?**

    ```yaml
    Flows:

        order: 
            Title: Order
            Steps:
            - Input: SHARE|nlweb.org/NAVIGATOR/DESTINATION
              Purpose: your navigator sets where 🧭
            - Input: SHARE|nlweb.org/CONCIERGE/COURIER
              Purpose: your concierge sets how 🛎️  
            - Input: SHARE|nlweb.org/CURATOR/FILTER
              Purpose: your curator orders 🧚
            - Input: SHARE|nlweb.org/VITALOGIST/REVIEW
              Purpose: your vitalogist reviews 💖 
            - Input: SHARE|nlweb.org/CONCIERGE/REVIEW
              Purpose: your concierge reviews 🛎️  
            - Input: SHARE|nlweb.org/SCHEDULER/REVIEW
              Purpose: your scheduler reviews 🗓️ 
            - Input: CHARGE
              Purpose: your payer pays the bill 💳              
    ```