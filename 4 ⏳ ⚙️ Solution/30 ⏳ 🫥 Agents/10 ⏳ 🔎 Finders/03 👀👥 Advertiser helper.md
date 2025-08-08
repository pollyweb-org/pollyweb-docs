#TODO

👀 Advertiser domains FAQ
===

![](<00 ✅ 📎 Assets/🔎 Advertiser.png>)

1. **What is an Advertiser domain in NLWeb?**

    Advertiser domains intermediate the registration, distribution, and payment flows for ads on NLWeb. 

    ---

1. **How are adds presented to users?**

    When a [Host 🤗](<../../20 ✅ 🧑‍🦰 UI/23 ✅ 💬 Chats/03 ✅ 🤗🎭 Host role.md>) ends a workflow, the wallet's [Curator 🧚](<../03 ⏳ 🧚 Curators/01 ⏳ 🧚🫥 Curator agent.md>) vault suggests contextualized next-best actions for the user, e.g.: 
    - *given you like diving and are flying to Miami, consider diving at the Neptune Memorial Reef - here's a company that accepts your SSI Open Water certification and a list of nice restaurants nearby.*

    ---

1. **How can Sellers register ads?**

    For a [Seller 💵](<../04 ✅ 💳 Payers/02 ✅ 💵🎭 Seller role.md>) to register an ad, it needs first do set up a [Payer 💳](<../04 ✅ 💳 Payers/01 ✅ 💳🫥 Payer agent.md>) and bind to the Advertiser. 
    - The configuration of the ads will then depend on the Advertiser's user interface.

    ---

1. **How are ads selected?**

    | # | Step
    |-|-
    | 1 | when closing a chat, [Hosts 🤗](<../../20 ✅ 🧑‍🦰 UI/23 ✅ 💬 Chats/03 ✅ 🤗🎭 Host role.md>) send a Goodbye via the chat's [Broker 🤵](<../../20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>)
    2 | the Broker registers a new bill on a supporting [Biller 🤝](<../04 ✅ 💳 Payers/04 ✅ 🤝👥 Biller helper.md>) (this a synchronous call the returns the ID as a response, allowing the other parties to add tracking information to the ad transaction);
    3 | the Broker asks the Host for to share the chat's summary with the user's [Persona 🧢](<../02 ✅ 🧢 Personas/02 ✅ 🧢🫥 Persona agent.md>), passing the bill's [Locator 🔆](<../../20 ✅ 🧑‍🦰 UI/22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>);
    4 | the Host send an anonymized chat summary to the Persona, plus the bill's Locator;
    5 | the Persona sends analysis requests to one or more Advertisers containing the user's context (e.g., country), the user's advertising preferences, the anonymized chat summary, and the bill Locator;
    6 | the Advertisers compiles a list of potential options for next actions and sends it to the Persona;
    7 | the Persona evaluates the options sent by the multiple advertisers, considering its knowledge about the user's inferred preferences (this allows for additional filtering based on users' private preferences that Advertisers should know be exposed to), and then informs of the Advertisers about the final selection of options (this allows Advertisers to know which ad prints to charge Sellers);
    8 | the Persona shows the options to the user on the same chat;
    9 | if and when the user select one of the options, the Persona then asks the Advertiser to translate the options number into a Locator (this allows Advertisers to know which clicks to charge Sellers);
    10 | the Persona sends the Locator to the Wallet, for it to open a new chat for the clicked Locator.

    ---

1. **How are Sellers charged for ads?**

    Similar to Google Ads, [Sellers 💵](<../04 ✅ 💳 Payers/02 ✅ 💵🎭 Seller role.md>) are charged for:
    - 1/ ads showed to the user, and 
    - 2/ ads clicked by the user.
    
    Advertisers register the displays and clicks on their [Biller 🤝](<../04 ✅ 💳 Payers/04 ✅ 🤝👥 Biller helper.md>).
    - These then charge the monthly totals to [Sellers 💵](<../04 ✅ 💳 Payers/02 ✅ 💵🎭 Seller role.md>).

    ---

1. **How do parties monetize by displaying Ads?**

    Monthly, the [Broker 🤵](<../../20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>)'s [Biller 🤝](<../04 ✅ 💳 Payers/04 ✅ 🤝👥 Biller helper.md>) debits the transaction fees and percentages to the Advertisers, who then have to pay the [🧢 Personas](<../02 ✅ 🧢 Personas/02 ✅ 🧢🫥 Persona agent.md>) and [Hosts 🤗](<../../20 ✅ 🧑‍🦰 UI/23 ✅ 💬 Chats/03 ✅ 🤗🎭 Host role.md>)

    ---

1. **What are the preconditions for ads to work?**

    - Users need to select their default [Persona 🧢](<../02 ✅ 🧢 Personas/02 ✅ 🧢🫥 Persona agent.md>) on their [Wallets 🧑‍🦰](<../../20 ✅ 🧑‍🦰 UI/01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>).
    - [Sellers 💵](<../04 ✅ 💳 Payers/02 ✅ 💵🎭 Seller role.md>) need to promote ads on an Advertiser.
    - All domains interacting directly need a [trust 👍](<../../40 ✅ 👥 Domains/43 ✅ 👍 Trusts/01 ✅ 👍 Domain Trust.md>) path between them.

    ---

1. **How are frauds prevented?**

    [Brokers 🤵](<../../20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) register contracts on [Billers 🤝](<../04 ✅ 💳 Payers/04 ✅ 🤝👥 Biller helper.md>) that require a number of matching values from the multiple parties involve in each advertising transaction:
    
    For ad displays: 
    - Advertisers and [🧢 Personas](<../02 ✅ 🧢 Personas/02 ✅ 🧢🫥 Persona agent.md>) send the number of adds offered to the Persona;
    - Advertisers, Personas, and [Sellers 💵](<../04 ✅ 💳 Payers/02 ✅ 💵🎭 Seller role.md>) send the IDs of the selected list of adds presented to the user;
    - Personas and Brokers send the number of options in the next-action prompt;
    - Advertisers and Sellers send the display value charged to Sellers.
    
    For ad clicks: 
    - Personas, Advertiser, and Sellers send the IDs of ads translated from option number to option Locator;
    - Advertisers and Sellers send the click value charged to Sellers.

    ---

1. **How is PII protected?**

    The following strategies protect users' personal identifiable information (PII):
    * [Hosts 🤗](<../../20 ✅ 🧑‍🦰 UI/23 ✅ 💬 Chats/03 ✅ 🤗🎭 Host role.md>) send chat summaries directly to [🧢 Personas](<../02 ✅ 🧢 Personas/02 ✅ 🧢🫥 Persona agent.md>), not to Brokers.
        - The summaries should not contained sensitive information, but each Host can arbitrarily decide how much is too much information.
        - There is still the risk of Personas collecting too much information about a user, but at least the blast radius is limited to a domain that already has the responsibility of holding PII.
        - Personas should reject summaries with PII, as a way to educate Hosts to filter out PII when summarizing session chats.
    * Personas anonymize the context, preferences, and Host summaries when asking Advertisers for next best actions.
        - This removes tracking abilities from Advertisers and [Sellers 💵](<../04 ✅ 💳 Payers/02 ✅ 💵🎭 Seller role.md>).

    ---
