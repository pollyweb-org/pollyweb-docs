Order a pizza for home delivery
---

> From [🍕 Order Pizza](<01 🍕 Index.md>)

<br/>


## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 Chats/20 🤔 Prompts/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
|-|-|-|
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 😃 Hi! What do you need? | `pizza`
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 💬 How can I help with that? <br> - [ Order ] from 🍕 Any Pizzeria <br/> - [ Find 🔎 ] a pizzeria to go to<br/> - [ Something else ] | > Order
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | ✅ Over to 🍕 Any Pizzeria.
| [ new chat ]
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agent domains/40 🔎 Finders/🔎🫥 Finder agent.md>) | ⓘ Any Pizzeria (4.4 ⭐) [+]
| 🍕 Pizzeria   | ℹ️ Pizza request received.
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Ready to order? [Yes, No] <br/> - your navigator sets where 🧭 <br/> - your concierge sets how 🛎️ <br/> - your curator orders 🧚 <br/> - your vitalogist reviews 💖 <br/> - your scheduler reviews 🗓️  <br/> - your payer pays the bill 💳 <br/> - your concierge delivers 🛎️ <br/> - your payer tips the courier 💳 <br/> - your vitalogist records it 💖 | > Yes
| 🧭 [Navigator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | 🫥 Share destination? [No] <br> - [ 🏠 home ] <br/> - [ 🏡 Daniel's ] <br/> - [ 📍 current location ] <br/> - [ 🗺️ Somewhere else ] | > 🏠 home
| 🛎️ [Concierge](<../../../4 ⚙️ Solution/50 🫥 Agent domains/25 🛎️ Concierges/$ 🛎️🫥 Concierge agent.md>) | ⓘ Given destination: [Change]<br/>- Ryan street, 98, 2D 
| 🛎️ [Concierge](<../../../4 ⚙️ Solution/50 🫥 Agent domains/25 🛎️ Concierges/$ 🛎️🫥 Concierge agent.md>) | ⏳ Looking for couriers...
| 🛎️ [Concierge](<../../../4 ⚙️ Solution/50 🫥 Agent domains/25 🛎️ Concierges/$ 🛎️🫥 Concierge agent.md>) | 🫥 Which courier? <br> - [ AnyCourier ] + $4.00 (5 min) <br> - [ iCourier ] + $2.99 (17 min) <br/> | > AnyCourier
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) | 🫥 Share preferences? [No] <br/>- [ 👤 solo ] <br/>- [ 👨‍👩‍👦 family ] | > 👨‍👩‍👦 family
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) | ⏳ Analyzing menu... 
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) | 💭 Here are suggestions: [No] <br/>- [ ] large Margherita with soda <br/>- [ ] small 4 Cheese with water | [X] small (...)
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) | 💭 Anything else? [Yes, No] <br/>- [ Pizzas 🍕 ] <br/>- [ Drinks 🥤 ] | > Pizzas 🍕
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) | 💭 Which pizza? <br/>- [ Margherita 🌼 ] <br/>- [ Pepperoni 🌶️ ] <br/> - ...| > Pepperoni 🌶️
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) | 💭 What size? [ S, M, L ] | > `biggest`
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) | 💭 How many? [ 1, 2, 3, + ] | > 1
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) | 💭 Want a drink with that? [No] <br/>- [ Soda ] <br/>- [ Water ] | > `a coke` 
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) | 💭 Anything else? [No] <br/>- [ Pizzas 🍕 ] <br/> - [ Drinks 🥤 ] | > No
| 🍕 Pizzeria     | ℹ️ Order ($27.00): [Change] <br/>- 1 small 4 Cheese 🧀 ($10.00) <br/>- 1 still water (25 cl) 💧 ($1.50) <br/>- 1 large Pepperoni 🌶️ ($13.00) <br/>- 1 diet coke (33 cl) 🥤 ($2.50) <br/> - preparation time ⏳ ~15 min 
| 💖 [Vitalogist](<../../../4 ⚙️ Solution/50 🫥 Agent domains/95 💖 Vitalogists/💖🫥 Vitalogist agent.md>) | 🫥 Confirm? [Yes, No] <br> - pizza: gluten allergy! <br/> - coke: sugar at 190 mg/dL | > Yes
| 🛎️ [Concierge](<../../../4 ⚙️ Solution/50 🫥 Agent domains/25 🛎️ Concierges/$ 🛎️🫥 Concierge agent.md>) | ⓘ Delivery ($4.50): [Change] <br/> - courier delivery 🛵 ($4.00) <br/> - concierge fee 🛎️ ($0.50) <br/> - delivery time ⏳ ~10 min.
| [🗓️ Scheduler](<../../../4 ⚙️ Solution/50 🫥 Agent domains/75 🗓️ Schedulers/$ 🗓️🫥 Scheduler agent.md>) | 🫥 Confirm? [Yes, No] <br/> - it will take ~30 min <br> - your flight is in 5 hours <br/> - you'll have ~1 hour to eat | > Yes
| 💳 [Payer](<../../../4 ⚙️ Solution/50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay $31.50 bill? 🧾 [No] <br/>- [ Card ABC ] + $0.10 <br/>- [ Card DEF ] (free) <br/> - [ ✂️ Split bill ] | > Card ABC |
| 🍕 Pizzeria   | ✅ Order confirmed [+]
| 🛎️ [Concierge](<../../../4 ⚙️ Solution/50 🫥 Agent domains/25 🛎️ Concierges/$ 🛎️🫥 Concierge agent.md>) | ☑️ Delivery confirmed [+]
| 🍕 Pizzeria   | ⏳ Preparing your order... [+]
|...            |...
||

<br/>

## 💼 Business Setup

1. **What does the [😃 Domain Talker](<../../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) look like?**

    ```yaml
    💬 Order:
    - INFO|Pizza request received.
    - INFORM|order

    # Collect order details.
    - SHARE|.NAVIGATOR/DESTINATION >> $destination # 🧭 
    - SHARE|.CONCIERGE/COURIER >> $courier: # 🛎️ 
        Destination: $destination
    - MAP|menus|pizzas.yaml >> $menu
    - SHARE|.CURATOR/ORDER >> $choice:  # 🧚 
        Menu: $menu
    - EVAL|Order >> $order:
        Destination: $destination
        Courier: $courier
        Choice: $choice
    
    # Confirm order details and create a Biller 🤝 ID.
    - INFO|$order.summary|Change
    - SHARE|.VITALOGIST/REVIEW|$order.details # 💖
    - SHARE|.CONCIERGE/REVIEW|$order.details # 🛎️
    - SHARE|.SCHEDULER/REVIEW|$order.details # 🗓️

    # Request aggregated payment.
    - CHARGE|{amount}|{biller-id} # 💳
    
    # Successful order.
    - SUCCESS|Order confirmed:
        Details: $order.summary
    - SHARE|.CONCIERGE/CONFIRM # 🛎️
    - TEMP|Preparing your order...:
        Details: $order.summary
    ```

    |Functions|Returns|Description
    |-|-|-
    |`destination`| string | Pass the [Navigator 🧭 agent](<../../../4 ⚙️ Solution/50 🫥 Agent domains/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) destination.
    | `menu-locator` | string | [Locator 🔆](<../../../4 ⚙️ Solution/30 Data/15 🔆 Locators/$ 🔆 Locator.md>) of the menu.
    | `order-summary`| markdown | [Curator 🧚 agent](<../../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) choices:<br/>- plus ongoing status.
    | `order-details`| object | Details for partners: <br/>- selected items,<br/>- final delivery estimates, <br/>- aggregator [Biller 🤝](<../../../4 ⚙️ Solution/45 🤲 Helper domains/20 🤝 Billers/🤝🤲 Biller helper.md>) ID.
    |

<br/> 

1. **What does the Manifest Flow look like?**

    ```yaml
    Flows:

        order: 
            Title: Order
            Steps:
            - Input: SHARE|.NAVIGATOR/DESTINATION
              Purpose: your navigator sets where 🧭
            - Input: SHARE|.CONCIERGE/COURIER
              Purpose: your concierge sets how 🛎️  
            - Input: SHARE|.CURATOR/FILTER
              Purpose: your curator orders 🧚
            - Input: SHARE|.VITALOGIST/REVIEW
              Purpose: your vitalogist reviews 💖 
            - Input: SHARE|.CONCIERGE/REVIEW
              Purpose: your concierge reviews 🛎️  
            - Input: SHARE|.SCHEDULER/REVIEW
              Purpose: your scheduler reviews 🗓️ 
            - Input: CHARGE
              Purpose: your payer pays the bill 💳              
    ```