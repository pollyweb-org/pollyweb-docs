# Order to the table  🍔

> From [Eat fast food 🍔](<01 🍔 Index.md>)

<br/>

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>) table
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Fast Food (4.3 ⭐)  [+]
| 🍔 Fast Food | ℹ️ You're on table 28 [+]
| 🍔 Fast Food | 😃 Hi! What do you need? <br/>- [ Order ] <br/>- [ Something else ] | > Order
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 [Ready to order?](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) [Yes, No] <br/> - your curator orders 🧚<br/> - your vitalogist reviews 💖 <br/> - your payer pays 💳 <br/> - we'll deliver to your table 🍔 <br/> - your vitalogist records it 💖 | > Yes
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | 💭 [Some suggestions:](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/MANY 🔠/🔠 MANY ⌘ cmd.md>) [All, No] <br/>- [ ] house burger 🍔 (£3.00) <br/> - [ ] still water (25 cl) 💧 (£1.00) <br/> |  > All
| 🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | 💭 [Anything else?](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/MANY 🔠/🔠 MANY ⌘ cmd.md>) [No] <br/> - [ ] coffee ☕ (£0.90) | > No
| 🍔 Fast Food | ℹ️ [Order (£4.00)](<../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>) [+] <br/>- 1 house burger 🍔 (£3.00) <br/> - 1 still water (25 cl) 💧 (£1.00) <br/>  - to deliver at table 28
| 💖 [Vitalogist](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Vitalogists 💖/💖🫥 Vitalogist agent.md>) | 🫥 Confirm? [Yes, No] <br/> - burger is outside your diet  | > Yes
| 💳 [Payer](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | 🫥 Pay £4.00 bill? 🧾 [No] <br/>- [ Card ABC ] + $0.10 <br/>- [ Card DEF ] (free) | > Card ABC |
| 🍔 Fast Food | ✅ Eat-in submitted [+]
| 🍔 Fast Food | ⏳ Order in queue... [+] 
...
||



<br/>

## 💼 Business Setup

1. **What does the [`Script`](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/Script 📃.md>) look like?**

    ```yaml
    💬 Order:

    - INFORM: order     # Inform the steps.
    - RUN: Selection  # Select from the menu.
    - RUN: Payment    # Ask for the payment
    - RUN: WaitReady  # Wait for it to be ready.

    # Inform readiness.
    - CASE $status.Code:
        Ready: DONE Pick up your order.
        Canceled: INFO Order canceled.
        $: FAIL Unexpected problem.
    ```
    
    Uses: [`CASE`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`INFORM`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) [`RUN`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)

    ```yaml
    Selection: 

    # Ask to select from the menu.
    - SHARE >> $selection: # 🧚 
        Schema: .CURATOR/ORDER 
        Context: 
          Menu: {./menu.yaml}
          Order: {$order}
          Review: {$review}

    # Submit order.
    - CALL Order >> $order:
        Selection: $selection

    # Allow it to be changed.
    - INFO >> $change:
        Text: {$order.Summary} 
        Options: Change

    # Repeat if changed.
    - IF $change:
        REPEAT
    
    # Ask the user's Vitalogist to review.
    - SHARE >> $review: # 💖
        Schema: .VITALOGIST/REVIEW
        Context: 
          Order: {$order.Details}

    # Repeat if rejected
    - IF $review.Rejected:
        REPEAT

    - RETURN: $order
    ```
    
    ```yaml
    Payment: 

    # Ask the user's Payer to pay.
    - CHARGE:
        Amount: {$order.Total}
        Bill: {$order.Summary}

    # Submit the order.
    - CALL Submit >> $status:
        Order: $order
    
    # Inform submitted.
    - DONE:
        Text: Eat-in submitted
        Details: {$order.Summary}

    - RETURN: $status
    ```

    ```yaml
    WaitReady: 

    # Show the wait message 
    - TEMP >> $temp:
        Text: {$status.Message}
        Options: Cancel

    # Allow it to be cancelled.
    - CASE $temp:
        Cancel: 
            - CALL Cancel($order)
            - RETURN

    # Monitor status changes.
    - WAIT: $status
    - IFNOT $status.Pending:
        RETURN: $status

    # Continue to wait.
    - REPEAT
    ```
    Uses: [`CASE`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`REPEAT`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/REPEAT 🔁/🔁 REPEAT ⌘ cmd.md>) [`TEMP`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/TEMP ⏳/TEMP ⏳ prompt.md>) [`IFNOT`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IFNOT ⤵️/⤵️ IFNOT ⌘ cmd.md>) [`WAIT`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>) 

    |Functions|Returns|Description
    |-|-|-
    | `menu-locator` |text| [Locator 🔆](<../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>) of the menu.
    | `order-summary`| markdown | [Curator 🧚 agent](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) choices:<br/>- plus ongoing status.
    |

<br/> 

1. **What does the Manifest Form look like?**

    ```yaml
    Flows:
        order: 
            Title: Order a meal
            Steps:
            - Schema: .CURATOR/CURATE
              Purpose: your curator orders 🧚
            - Schema: .VITALOGIST/REVIEW
              Purpose: your vitalogist reviews 💖 
            - Schema: .PAYER/CHARGE
              Purpose: your payer pays the bill 💳              
    ```