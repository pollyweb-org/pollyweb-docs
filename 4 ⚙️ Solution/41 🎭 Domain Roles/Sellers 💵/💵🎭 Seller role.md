💵 Seller domain role
===


1. **What is a Seller domain role in NLWeb?**

    Sellers 💵 are [domains 👥](<../../40 👥 Domains/👥 Domain.md>) that ask [Payer 💳 domains](<../Payers/💳🎭 Payer role.md>) for payments to their [Collector 🏦 helpers](<../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) in return for products or services.
    
    ---

1. **How do Sellers sell to users?**

    ![](<.📎 Assets/💵 Seller.png>)

    | # | Step
    |-|-
    | 1 | As a [Host 🤗](<../Hosts 🤗/🤗🎭 Host role.md>) in a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>), a Seller 💵 charges a user for a service or product.
    | 2 | The user delegates the payment to their [Payer 💳 agent](<../../50 🫥 Agent domains/Payers 💳/💳🫥 Payer agent.md>).
    | 3 | The user's [Payer 💳 agent](<../../50 🫥 Agent domains/Payers 💳/💳🫥 Payer agent.md>) informs the Seller's [Collector 🏦 helper](<../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) about the money transfer.
    | 4 | The Seller's [Collector 🏦 helper](<../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) informs the Seller 💵 that the transaction is paid for.
    | 5 | The [Collector 🏦](<../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) issues a receipt to the user's [Payer 💳](<../../50 🫥 Agent domains/Payers 💳/💳🫥 Payer agent.md>), who may store it in the user's [Storage 🗃️ agent](<../../50 🫥 Agent domains/Storage 🗃️/🗃️🫥 Storage agent.md>).

    ---
    
1. **How can admins set up payment collection?**

    Admins of Sellers 💵 need to bind to a [Collector 🏦](<../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) domain and set up a bank account or any other means to receive money.

    ---
    
1. **Do Sellers need to trust user Payers?**

    No. 
    - Sellers 💵 delegate that [trust 👍](<../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) relationship to their [Collectors 🏦](<../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>);
        - i.e., the [Collector 🏦](<../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) and [Payer 💳](<../Payers/💳🎭 Payer role.md>) are the ones who need to have a [trust 👍](<../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) relationship.

    ---
    
1. **Do Sellers define how they want the user to pay?**

    No. 
    - The payment method is decided between the user's [Payer 💳](<../Payers/💳🎭 Payer role.md>) and the Seller's [Collector 🏦](<../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>). 
    - The Seller 💵 only defines the way they want the [Collector 🏦](<../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) to transfer the money to the Seller 💵.
    
    ---


1. **What workflows do Sellers implement?**

    |Workflow|Description
    |-|-
    | [🧑‍🦰 Charge users](<💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>) | How Sellers 💵 charge users.
    
    ---

1. **What API messages do Sellers implement?**

    |Message|Description
    |-|-
    | [🐌 Paid](<💵🅰️ Seller methods/🏦🐌💵 Paid.md>) | The [Collector 🏦 helper](<../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) confirms the payment.

    ---
