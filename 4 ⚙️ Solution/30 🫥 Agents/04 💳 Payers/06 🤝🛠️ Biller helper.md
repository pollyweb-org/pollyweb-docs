🤝 Biller domains FAQ
===

1. **What is a Biller domain in NLWeb?**

    A Biller domain handles the terms and lifecycle of payment agreements between a [Payer 💳](<03 💳🎭 Payer role.md>) and a [Collector 🏦](<02 🏦🛠️ Collector helper.md>) (w.g., subscriptions, free tiers, direct debits) on behalf of [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and [Sellers 💵](<01 💵🎭 Seller role.md>).

    ---

1. **How can a user sign a subscription in a Seller?**

    ![](<00 📎 Assets/💳 Biller User.png>)

    For a user to [sign](<../05 🆔 Identities/08 🆔🔏 User Signature.md>) a subscription, the following preconditions must be met:
    - 1/ the user has default [Payer 💳](<03 💳🎭 Payer role.md>) and [Identity 🆔](<../05 🆔 Identities/03 🆔🫥 Identity agent.md>) domains;
    - 2/ the Seller has a default [Collector 🏦](<02 🏦🛠️ Collector helper.md>) domain.

    The following steps describe a subscription workflow:
    - 1/ the user initiates a chat with a [Seller 💵](<01 💵🎭 Seller role.md>);
    - 2/ the user selects a subscription in the chat;
    - 3/ the Seller's Biller sends the PDF terms to the user;
    - 4/ the user accepts the PDF terms;
    - 5/ the user's [Identity 🆔](<../05 🆔 Identities/03 🆔🫥 Identity agent.md>) authenticates the user;
    - 6/ the user's Payer asks the user for a payment method;
    - 7/ the Seller confirms the subscription;
    - 8/ the Biller initiates the monthly collection.

    ---

1. **How can a domain sign a subscription?**

    ![](<00 📎 Assets/💳 Biller Domain.png>)

    Users with ADMIN [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) sign contracts on behalf of domains that issued them (e.g., for `any-contract.org` to accept the signature of a user on behalf of `any-domain.com`, the user needs to hold an ADMIN Token issued by `any-domain.com`);

    The following additional preconditions must be met:
    - the user has an ADMIN Token issued by the domain.

    The subscription workflow as the following additional steps:
    - the Seller asks the user to share the domain's ADMIN Token.

    ---

1. **How can a user cancel a subscription?**

    User subscriptions are attached to the user's [Payer 💳](<03 💳🎭 Payer role.md>) - in a chat, users can ask their Payer to cancel the subscription.

    ---

1. **Do Billers support pay-as-go contracts?**

    Yes, that is set up in the terms.
    
    Whenever the [Seller 💵](<01 💵🎭 Seller role.md>) receives a billable request, it adds the request to the Biller's billing cycle. By the end of the cycle, the Biller will factor in billable items and the terms to produce the period's charge.

    ---

1. **Can a Seller implement the Biller API?**

    Yes. However, a Biller domain may offer additional services that the [Seller 💵](<01 💵🎭 Seller role.md>) can benefit from, like digital signatures, risk assessment, support call center, dispute management, management of financial guarantees, and text-based reporting.
    
    The Seller's customers may also benefit from budget alarms, spend anomaly detection, near-real-time streaming of billing, and text reporting.

    ---
