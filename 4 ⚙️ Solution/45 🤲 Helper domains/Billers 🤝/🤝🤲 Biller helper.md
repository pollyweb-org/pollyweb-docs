🤝 Biller domains
===



1. **What is a Biller domain in NLWeb?**

    A Biller 🤝 is 
    * a [Helper 🤲 domain](<../$ Helpers 🤲/🤲👥 Helper domain.md>) 
    * that handles the terms and lifecycle of payment agreements 
    * between a [Payer 💳 domain](<../../50 🫥 Agent domains/Payers 💳/03 💳🎭 Payer role.md>) and a [Collector 🏦 domain](<../Collectors 🏦/🏦🤲 Collector helper.md>) 
    * (e.g., subscriptions, free tiers, direct debits) 
    * on behalf of [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) and [Seller 💵 domains](<../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>).

    ---
    <br/>

1. **What flows are supported by billers?**

    | Flow | Details
    |-|-
    | [🧑‍🦰 User subscriptions](<🤝⏩ Biller flows/🧑‍🦰⏩🤝 User Subscription.md>) | Users agree to be charged in a billing plan.
    | [👥 Domain subscriptions](<🤝⏩ Biller flows/👥⏩🤝 Domain Subscription.md>) | Domains agree to be charged in a plan.

    --- 
    <br/>

1. **How can a user cancel a subscription?**

    User subscriptions are attached to the user's [Payer 💳 agent](<../../50 🫥 Agent domains/Payers 💳/03 💳🎭 Payer role.md>).
    * In a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>), users can ask their [Payer 💳 agent](<../../50 🫥 Agent domains/Payers 💳/03 💳🎭 Payer role.md>) to cancel the subscription.

    ---

1. **Do Billers support pay-as-go contracts?**

    Yes, that is set up in the terms.
    
    * Whenever the [Seller 💵 domain](<../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) receives a billable request, it adds the request to the Biller's 🤝 billing cycle. By the end of the cycle, the Biller will factor in billable items and the terms to produce the period's charge.

    ---

1. **Can a Seller implement the Biller API?**

    Yes. 
    * However, a Biller 🤝 domain may offer additional services that the [Seller 💵 domain](<../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) can benefit from, like digital signatures, risk assessment, support call center, dispute management, management of financial guarantees, and text-based reporting.
    
    * The Seller's customers may also benefit from budget alarms, spend anomaly detection, near-real-time streaming of billing, and text reporting.

    ---
