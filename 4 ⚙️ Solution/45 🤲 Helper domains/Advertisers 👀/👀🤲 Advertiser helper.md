<!-- #TODO -->

👀 Advertiser helper domains
===

1. **What is an Advertiser helper domain in PollyWeb?**

    Advertisers 👀 are [Helper 🤲 domains](<../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) that intermediate the registration, distribution, and payment flows for ads on PollyWeb. 

    ---


1. **How are ads presented to users?**

    When a [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) ends a [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>), an Advertiser 👀 presents contextualized next-best actions for the user, e.g.: 

    - *given you like diving and are flying to Miami, consider diving at the Neptune Memorial Reef - here's a company that accepts your SSI Open Water certification and a list of nice restaurants nearby.*

    See the following examples for details:
    * [🏪 Buy water at a vending machine](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)
    * [🛎️ Check-in at a hotel](<../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/03 🏨 Guest @ Reception 🛎️/04 🛎️ Check-in.md>)
    * [🍕 Order a pizza for home delivery](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/22 🏠 Home: Wait for pizza.md>)

    ---


1. **What are the setup requirements for ads to work?**

    The set required for ads to work is as follows:

    * Users set up one [Curator 🧚 agent](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) on their [Wallet 🧑‍🦰 App](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
    
    * [Seller 💵 domains](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) set up one [Payer 💳 helper](<../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) to pay for ads.
    
    * Advertiser 👀 domains set up one [Biller 🤝 helper](<../Billers 🤝/🤝 Biller/🤝 Biller 🤲 helper.md>) to charge [Seller 💵 domains](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) for ads, one [Collector 🏦 helper](<../Collectors 🏦/🏦 Collector/🏦🤲 Collector helper.md>) to receive the ad payments, and one [Payer 💳 helper](<../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) for paying ad-printing commissions to [Host 🤗 domains](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) and [Curator 🧚 agents](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>).
    
    * [Broker 🤵 domains](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) set up one Advertiser 👀 helper to manage ads, and one [Biller 🤝 helper](<../Billers 🤝/🤝 Biller/🤝 Biller 🤲 helper.md>) to orchestrate the payments to all domains involved in ad printing for its registered [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).


    ---


1. **How are ads selected?**

    ![](<.📎 Assets/👀 Advertiser.png>)

    | # | Posting ads
    |-|-
    | 0 | [Seller 💵 domains](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) bind to one or more Advertisers 👀, then register their ads on the Advertiser's 👀 UX or API.

    | # | Showing ads
    |-|-
    | 1 | When closing a [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>), [Host 🤗 domains](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) send a Goodbye via the chat's [Broker 🤵 domain](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>).
    2 | The [Broker 🤵 domain](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) registers a new bill on a supporting [Biller 🤝 helper](<../Billers 🤝/🤝 Biller/🤝 Biller 🤲 helper.md>) (this a synchronous call the returns the ID as a response, allowing the other parties to add tracking information to the ad transaction).
    3 | The [Broker 🤵 domain](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) asks the Chat's 💬 [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) to share the [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) summary with the user's [Curator 🧚 agent](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>), passing the bill's [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>).
    4 | The [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) sends an anonymized [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) summary to the user's [Curator 🧚 agent](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>), plus the bill's [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>).
    5 | The user's [Curator 🧚 agent](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) sends analysis requests to one or more Advertisers 👀 containing the user's context (e.g., country), the user's advertising preferences, the anonymized [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) summary, and the bill [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>).
    6 | The Advertisers 👀 compile a list of potential options for next actions and send it to the user's [Curator 🧚 agent](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>).
    7 | The [Curator 🧚 agent](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) evaluates the options sent by the multiple Advertisers 👀, considering its knowledge about the user's inferred preferences, and then informs of the Advertiser 👀 about the final selection of options - this allows for additional filtering based on users' private preferences that Advertisers 👀 should not be exposed to.
    8 | The Advertiser 👀 helper shows the options to the user on the [Wallet 🧑‍🦰 App](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
    9 | The user selects one of the options presented by the Advertiser 👀.
    10 | The Advertiser 👀 asks the [Broker 🤵 domain](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) to open a new [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) to the user-selected [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>).

    | # | Periodic billing
    |-|-
    | A | Monthly, the Broker's [Biller 🤝 helper](<../Billers 🤝/🤝 Biller/🤝 Biller 🤲 helper.md>) will debit its Advertiser's 👀 [Payer 💳 helper](<../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) a lump sump for all contributions of the multiple domains in the advertisement workflow during the billing period.  
    | B | The Advertiser's 👀 [Payer 💳 helper](<../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) sends the corresponding part to the [Collector 🏦 helper](<../Collectors 🏦/🏦 Collector/🏦🤲 Collector helper.md>) of each [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) for their [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) summaries.
    | C | Sends the corresponding part to the [Collector 🏦 helper](<../Collectors 🏦/🏦 Collector/🏦🤲 Collector helper.md>) of each [Curator 🧚 agent](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) for their filtering and sorting of the ads.
    | D | And sends the corresponding part to the [Collector 🏦 helper](<../Collectors 🏦/🏦 Collector/🏦🤲 Collector helper.md>) of the [Broker 🤵 domain](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) for orchestrating the ad workflows.
    | E | Periodically, the Advertiser's 👀 [Biller 🤝 helper](<../Billers 🤝/🤝 Biller/🤝 Biller 🤲 helper.md>) will debit each [Seller 💵 domain](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) for their printed and clicked ads in the billing period.
    | F | Each Seller's 💵 [Payer 💳 helper](<../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) then sends the corresponding payment to the Advertiser's 👀 [Collector 🏦 helper](<../Collectors 🏦/🏦 Collector/🏦🤲 Collector helper.md>).
    

    ---

1. **How can Sellers 💵 register ads?**

    For a [Seller 💵 domain](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) to register an ad, it needs first do set up a [Payer 💳 helper](<../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) and bind to the Advertiser. 
    - The configuration of the ads will then depend on the Advertiser's UX and API.

    ---

1. **How are Sellers 💵 charged for ads?**

    Similar to Google Ads, [Sellers 💵](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) are charged for:
    - 1/ ads showed to the user, and 
    - 2/ ads clicked by the user.
    
    Advertisers register the displays and clicks on their [Biller 🤝](<../Billers 🤝/🤝 Biller/🤝 Biller 🤲 helper.md>).
    - These then charge the monthly totals to [Sellers 💵](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>).

    ---

1. **How do parties monetize by displaying Ads?**

    Monthly, the Broker's [Biller 🤝 helper](<../Billers 🤝/🤝 Biller/🤝 Biller 🤲 helper.md>) debits the transaction fees and percentages to the Advertisers, who then have to pay the [Curator 🧚 agents](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) and the [Host 🤗 domains](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)

    ---

1. **What are the preconditions for ads to work?**

    - Users need to select their default [Curator 🧚 agent](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) on their [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
    - [Seller 💵 domains](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) need to promote ads on an Advertiser.
    - All domains interacting directly need a [trust 🫡](<../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) path between them.

    ---

1. **How are frauds prevented?**

    [Broker 🤵 domains](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) register contracts on [Billers 🤝](<../Billers 🤝/🤝 Biller/🤝 Biller 🤲 helper.md>) that require a number of matching values from the multiple parties involve in each advertising transaction:
    
    For ad displays: 
    - Advertisers and [Curator 🧚 agents](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) send the number of ads offered to the Persona;
    - Advertisers, [Curator 🧚 agents](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>), and [Seller 💵 domains](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) send the IDs of the selected list of ads presented to the user;
    - [Curator 🧚 agents](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) and [Broker 🤵 domains](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) send the number of options in the next-action prompt;
    - Advertisers and [Seller 💵 domains](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) send the display value charged to Sellers.
    
    For ad clicks: 
    - [Curator 🧚 agents](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>), Advertisers 👀, and [Seller 💵 domains](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) send the IDs of ads translated from option number to option Locator;
    - Advertisers 👀 and [Seller 💵 domains](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) send the click value charged to Sellers.

    ---

1. **How is PII protected?**

    The following strategies protect users' personal identifiable information (PII) from [profiling practices 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/01 🕵 Profiling landscape/00 🕵 Profiling landscape.md>):

    * [Host 🤗 domains](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) send chat summaries directly to [Curator 🧚 agents](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>), not to [Broker 🤵 domains](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>).
  
        * The summaries should not contained sensitive information, but each [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) can arbitrarily decide how much is "too much information".
        
        * There is still the risk of [Curator 🧚 agents](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) collecting "too much information" about a user, but at least the blast radius is limited to a domain that already has the responsibility of holding PII.
        
        * [Curator 🧚 agents](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) should reject summaries with PII, as a way to educate [Host 🤗 domains](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) to filter out PII when summarizing session chats.
  
    * When [Curator 🧚 agents](<../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) ask Advertisers 👀 for next best actions, they first anonymize the [Chat's 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) context, the user preferences, and the [Host 🤗](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) summary.
  
        - This mitigates the abilities of both Advertisers 👀 and [Sellers 💵](<../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>) to [profile 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/01 🕵 Profiling landscape/00 🕵 Profiling landscape.md>) users.

    ---
