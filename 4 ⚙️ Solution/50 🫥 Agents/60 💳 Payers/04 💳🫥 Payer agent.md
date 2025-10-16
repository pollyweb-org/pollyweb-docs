💳🫥 Payer agent
===

1. **What is a Payer agent in NLWeb?**

    Payer agents are [Payer 💳 domains](<03 💳🎭 Payer role.md>) that act as [Agent 🫥 vault domains](<../$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) for users with [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>), interacting in [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) with [Seller 💵 host domains](<../../41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>).

    ---

1. **How are user payments processed for users?**

    ![](<. 📎 Assets/💳 Payer.png>)

    On NLWeb, payment transactions with users are handled between:
    * [Sellers 💵](<../../41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>) -  these are [Consumer 💼](<../../41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) domains that request payments;
    * Payers 💳 - these are user-bound [Vaults 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) with access to the user's money; and
    * [Collector 🏦 helpers](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>) - these are [Helper 🤲 domains](<../../45 🤲 Helper domains/$ 🤲 Helpers/🤲👥 Helper domain.md>) able to deposit money on the [Sellers 💵](<../../41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>) bank account. 
    
    Upon check-out, 
    - 1/ the [Seller 💵](<../../41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>) registers the upcoming payment to their [Collector 🏦](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>), 
    - 2/ the [Seller 💵](<../../41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>) requests a payment from the user, 
    - 3/ the user delegates the payment to a Payer 💳, 
    - 4/ the user's Payer 💳 transfers the money to the [Seller's 💵](<../../41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>) [Collector 🏦](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>), and 
    - 5/ the [Collector 🏦](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>) notifies the [Seller 💵](<../../41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>) that the transaction was paid.

    ---

1. **What user problems do Payers solve?**

    Read the [User challenges 🧑 ](<../../../2 🏔️ Landscape/1 💼 Business landscape/05 💳 Payments landscape/01 🧑 User challenges.md>) section of the [Payments landscape 💳](<../../../2 🏔️ Landscape/1 💼 Business landscape/05 💳 Payments landscape/00 💳 Payments index.md>).

    ---
    
1. **What responsibilities do Payers have in a payment?**

    Payers 💳 are responsible for:
    - receiving payment requests from [Collectors 🏦](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>);
    - memorizing the user's available payment methods;
    - collecting the payment from the user's selected payment method:
        - e.g., Visa, American Express, Google Pay, Brazilian Pix, Portuguese MBWay;
    - collecting any additional fees to pay the user's selected payment method;
    - converting the user's payment to the Collectors currency;
    - transferring the payment to Collectors over an agreed transfer protocol: 
        - e.g., national bank transfer, internal SWIFT, TransferWise, Western Union;
    - storing the payment receipts on behalf of users.

    ---

1. **After a payment, do users receive the Seller's receipt?**

    No. 
    
    - Receipts and invoices are created by the Seller's 💵 [Collector 🏦 helper](<../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>), and are sent to the user's Payer 💳 domain. 
    
    - Users should ask their Payer 💳 domain for the receipt:
        - e.g., a payment gateway may allow the receipts to be downloaded from the transaction list on their website, or they can send each receipt to a chat window every time there is a payment. 
    
    - For user data protection and device storage optimization, NLWeb discourages domains from sending receipts via chat to be downloaded on the device.

    ---