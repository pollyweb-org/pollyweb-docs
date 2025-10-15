# Order to the table  🍔

> From [Eat fast food 🍔](<01 🍔 Index.md>)

<br/>

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) table
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/40 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Fast Food (4.3 ⭐)  [+]
| 🍔 Fast Food | ℹ️ You're on table 28 [+]
| 🍔 Fast Food | 😃 Hi! What do you need? <br/>- [ Order ] <br/>- [ Something else ] | > Order
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Ready to order?](<../../../9 😃 Talkers/60 ⏩ Msg flows/41 📝 INFORM msg.md>) [Yes, No] <br/> - your curator orders 🧚<br/> - your vitalogist reviews 💖 <br/> - your payer pays 💳 <br/> - we'll deliver to your table 🍔 <br/> - your vitalogist records it 💖 | > Yes
| 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/30 🧚 Curators/$ 🧚🫥 Curator agent.md>) | 💭 [Some suggestions:](<../../../9 😃 Talkers/20 🤔 Prompts/7 ✏️ Input prompts/54 🔠 MANY prompt.md>) [All, No] <br/>- [ ] house burger 🍔 (£3.00) <br/> - [ ] still water (25 cl) 💧 (£1.00) <br/> |  > All
| 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/30 🧚 Curators/$ 🧚🫥 Curator agent.md>) | 💭 [Anything else?](<../../../9 😃 Talkers/20 🤔 Prompts/7 ✏️ Input prompts/54 🔠 MANY prompt.md>) [No] <br/> - [ ] coffee ☕ (£0.90) | > No
| 🍔 Fast Food | ℹ️ [Order (£4.00)](<../../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/03 ⊕ with Details.md>) [+] <br/>- 1 house burger 🍔 (£3.00) <br/> - 1 still water (25 cl) 💧 (£1.00) <br/>  - to deliver at table 28
| 💖 [Vitalogist](<../../../4 ⚙️ Solution/30 🫥 Agents/95 💖 Vitalogists/$ 💖🫥 Vitalogist agent.md>) | 🫥 Confirm? [Yes, No] <br/> - burger is outside your diet  | > Yes
| 💳 [Payer](<../../../4 ⚙️ Solution/30 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay £4.00 bill? 🧾 [No] <br/>- [ Card ABC ] + $0.10 <br/>- [ Card DEF ] (free) | > Card ABC |
| 🍔 Fast Food | ✅ Eat-in submitted [+]
| 🍔 Fast Food | ⏳ Order in queue... [+] 
...
||



<br/>

## 💼 Business Setup

1. **What does the [😃 Domain Talker](<../../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) look like?**

    ```yaml
    💬 Order:

    - INFORM|order     # Inform the steps.
    - RUN|Selection  # Select from the menu.
    - RUN|Payment    # Ask for the payment
    - RUN|WaitReady  # Wait for it to be ready.

    # Inform readiness.
    - Case|$status.Code:
        Ready: SUCCESS|Pick up your order.
        Canceled: INFO|Order canceled.
        $: FAILURE|Unexpected problem.
    ```

    ```yaml
    Selection: 

    # Ask to select from the menu.
    - SHARE >> $selection: # 🧚 
        Code: .CURATOR/ORDER 
        Context: 
          Menu: {./menu.yaml}
          Order: {$order}
          Review: {$review}

    # Submit order.
    - EVAL|Order >> $order:
        Selection: $selection

    # Allow it to be changed.
    - INFO|{$order.Summary} >> $change:
        Options: Change
    - IF|$change:
        Then: REPEAT
    
    # Ask the user's Vitalogist to review.
    - SHARE >> $review: # 💖
        Code: .VITALOGIST/REVIEW
        Context: 
          Order: {$order.Details}

    # Repeat if rejected
    - IF|$review.Rejected:
        Then: REPEAT

    RETURN|$order
    ```
    
    ```yaml
    Payment: 

    # Ask the user's Payer to pay.
    - CHARGE:
        Amount: {$order.Total}
        Bill: {$order.Summary}

    # Submit the order.
    - EVAL|Submit >> $status:
        Order: $order
    
    # Inform submitted.
    - SUCCESS:
        Statement: Eat-in submitted:
        Details: {$order.Summary}

    - RETURN|$status
    ```

    ```yaml
    WaitReady: 

    # Show the wait message 
    - TEMP >> $temp:
        Statement: {$status.Message}
        Options: Cancel

    # Allow it to be cancelled.
    - CASE|$temp:
        Cancel: 
            - EVAL|Cancel($order)
            - RETURN

    # Monitor status changes.
    - WAIT|$status
    - IF|$status.Pending:
        Else: RETURN|$status

    # Continue to wait.
    REPEAT
    ```

    |Functions|Returns|Description
    |-|-|-
    | `menu-locator` | string | [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) of the menu.
    | `order-summary`| markdown | [Curator 🧚 agent](<../../../4 ⚙️ Solution/30 🫥 Agents/30 🧚 Curators/$ 🧚🫥 Curator agent.md>) choices:<br/>- plus ongoing status.
    |

<br/> 

1. **What does the Manifest Form look like?**

    ```yaml
    Flows:
        order: 
            Verb: order
            Steps:
            - Code: .CURATOR/FILTER
              Purpose: your curator orders 🧚
            - Code: .VITALOGIST/REVIEW
              Purpose: your vitalogist reviews 💖 
            - Code: .PAYER/CHARGE
              Purpose: your payer pays the bill 💳              
    ```