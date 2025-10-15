<!-- #TODO -->

🧚🗄️ Curator domain
===

1. **What are Curator domains?**

    [A Curator 🧚](<01 🧚🫥 Curator agent.md>) 
    * is an [Agent 🫥 vault domain](<../../25 Data/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) 
    * that filters options on behalf of users.

    ---
    <br/>

1. **What uses cases for a Curator agent?**

    |Category|Example|
    |-|-
    |`Fast Food`| [🍔 Order a burger from the seat](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/25 🍔 Fast food/21 🪑 Seat: Order burger 🍔.md>)
    |`Bars`|[🍸 Order water from the seat](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/21 🪑 Seat: Order water.md>) 
    ||[🍺 Order a beer from the seat](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/22 🪑 Seat: Order a beer.md>)
    ||[🍺 Reorder a beer from the seat](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/23 🪑 Seat: Reorder a beer.md>)
    |`Street Food`|[🌭 Buy a hot dog at a stall](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    |`Restaurants`|[🥘 Order food from the seat](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/51 🪑 Seat: Order food 🥘.md>)
    ||[🍷 Order wine from the seat](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/52 🪑 Seat: Order wine 🍷.md>)
    ||[🍽️ Change the order from the seat](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/53 🪑 Seat: Change order 🌀.md>)
    |`Order Pizza`|[🍕 Order pizza for home delivery](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/21 🏠 Home: Order pizza.md>)
    |`Night Clubs`| [🍺 Order beer at a bar](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/31 🍸 Bar: Order beer 🍺.md>)
    |`Hotels`|[🏨 Search and book a hotel room](<../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/01 🏨 Guest @ Home 🏠/01 🏠 Book hotel.md>)
    ||[🛎️ Select room on check-in](<../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/03 🏨 Guest @ Reception 🛎️/04 🛎️ Check-in.md>)
    |`Airlines`|[💺 Set meal preferences check-in](<../../../3 🤝 Use Cases/03 🧳 Travel/09 🧳 Travel by air 💺/14 💺 Ticket/05 Flight check in.md>)
    |`Retailers`| [🛍️ Visualize an item's price](<../../../3 🤝 Use Cases/04 🛒 Shop/01 🛍️ Shop for clothes/01 Customer @ Item/01 Item price.md>)
    || [🛍️ Visualize an item's availability](<../../../3 🤝 Use Cases/04 🛒 Shop/01 🛍️ Shop for clothes/01 Customer @ Item/02 Item availability.md>)
    ||[🛍️ Visualize an item's composition](<../../../3 🤝 Use Cases/04 🛒 Shop/01 🛍️ Shop for clothes/01 Customer @ Item/03 Item composition.md>)
    |`Saloons`|[💈 Book a hairdresser service](<../../../3 🤝 Use Cases/05 🛠️ Services/01 💈 Cut hair at salons/10 Customer @ Anywhere/11 Book.md>)
    |`Financial`|[🏧 Withdraw cash from an ATM](<../../../3 🤝 Use Cases/05 🛠️ Services/03 🏧 Withdraw at ATMs/10 Customer @ ATM/11 Withdraw cash.md>)
    |`Services`|[Order remote prints with delivery](<../../../3 🤝 Use Cases/05 🛠️ Services/09 Remote printing/01 Customer @ Home 🏠/01 Order prints.md>)
    

    ---
    <br/>

1. **What domain roles do Curators implement?**

    | Role 🎭 | Purpose
    |-|-
    | [🔔 Subscriber](<../../41 🎭 Domain Roles/76 🔔 Subscribers/$ 🔔🎭 Subscriber role.md>) | To consume changes from the [user's Persona 🧢 vault domains](<../02 🧢 Personas>).
    | [🗄️ Vault ](<../../41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) | To share user selections with [Consumer 💼 host domains](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>).
    

    ---
    <br/>

1. **How do Curators work?**

    [Curator 🧚 agents](<01 🧚🫥 Curator agent.md>) are invoked by [Host 🤗 domains](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) to parse a set of choices and return a list of codes back to the Host - e.g.:
    
    - restaurants share menus and receive [food orders 🥘](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/51 🪑 Seat: Order food 🥘.md>)
    - travel agencies share hotel options and receive [bookings 🏨](<../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/01 🏨 Guest @ Home 🏠/01 🏠 Book hotel.md>)
    - cash machines share bills and receive [withdraw orders 🏧](<../../../3 🤝 Use Cases/05 🛠️ Services/03 🏧 Withdraw at ATMs/10 Customer @ ATM/11 Withdraw cash.md>)
    - social networks share posts and receive filtered lists.

    ---
    <br/>

1. **Why are Curators important for users?**

    [Curator 🧚 agents](<01 🧚🫥 Curator agent.md>) protect users by filtering out from the available options given by [Host 🤗 domains](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>), instead of sharing details about the user:
    - e.g., chose meat for dinner, instead of disclosing a life-threatening allergy to shrimp;
    - e.g., choose a back seat at a show, instead of disclosing a limited financial budget;
    - e.g., choose the closest venue for a show, instead of disclosing the current location.

    ---
    <br/>

1. **Why are Curators important for Host domains?**

    [Curator 🧚 agents](<01 🧚🫥 Curator agent.md>) remove from [Host 🤗 domains](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) the undifferentiated heavy lifting of creating personalized workflows for user selection - e.g.:
    - a restaurant [Host 🤗 domain](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) can just dump to a [user's Curator 🧚 agent](<01 🧚🫥 Curator agent.md>) a comprehensive list of all 100+ possible dishes and drinks offered by the restaurant, with nutritional, allergic, and social media details about each of them;
    - while this list is most probably overwhelming for the vast majority of users, a [user's Curator 🧚 agent](<01 🧚🫥 Curator agent.md>) can instantaneously read and filter out the list based on the user's private preferences, health restrictions, special needs, purchasing history, social background, and emotional mood at the time.

    ---
    <br/>

1. **How do curators protect themselves from prompt injection?**

    [Curator 🧚 agents](<01 🧚🫥 Curator agent.md>) assess [Host 🤗 domains](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) inputs before acting on them. 
    - Suspicious behaviors are reported to [Firewall 🔥 helper domains](<../../45 🛠️ Helper domains/21 🔥 Firewalls/$ 🔥🛠️ Firewall helper.md>).

    ---
    <br/>

1. **How do curators protect themselves from data breaches?**

    While [Curator 🧚 agents](<01 🧚🫥 Curator agent.md>) communicate using natural language with [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>), they output to [Host 🤗 domains](<../../20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) only a filtered list of codes referenced in the input.

    ---
    <br/>

1. **How much user data should a curator store?**

    NLWeb advocates for [Curator 🧚 agents](<01 🧚🫥 Curator agent.md>) to rely on [Persona 🧢 vaults](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) to assess user intent, while storing the nuances of those intents in the Curator's 🧚 memory:
    - this addresses the different speed of developments between humans and machines; 
    - i.e., humans change their tastes and behaviors slower as they age, while new and better machine algorithms appear exponentially faster;
    - this separation of concerns allows users to retain their legacy [Persona 🧢 vault](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) while constantly upgrading to new smarter [Curator 🧚 agents](<01 🧚🫥 Curator agent.md>) as they are released.

    ---
    <br/>

1. **How should curators deal with ethical issues?**

    Ethics vary by civilization. 
    - Thus, users are advised to exercise conscience when selecting the provider of their [Curator 🧚 agent](<01 🧚🫥 Curator agent.md>).
    - Is is expected that users will select the Curator 🧚 provider most aligned to their social values.

    Nonetheless, [Curator 🧚 agents](<01 🧚🫥 Curator agent.md>) should thrive to follow a generic set of globally accepted ethical norms.

    - **Safety guardrails**: 
        - protect the physical and mental safety of the human, leveraging their [Identity 🆔 vault](<../05 🆔 Identities/01 🆔🫥 Identity agent.md>) to guardrail legal and cultural nuances.
        - e.g., when suggesting alcoholic beverages to an American user visiting Portugal, consider both the minimum drinking age on the current country (18 in Portugal) and in the user's nationality country (21 in the USA).
  
    - **Cognitive dissonance**: 
        - respect the human's intent behavior by leveraging [Persona 🧢 vaults](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) while addressing the emotional side of the human;
        - e.g., if a human says they prefer to eat vegetables but reject all dishes that contain vegetables, then the [Curator 🧚 agent](<01 🧚🫥 Curator agent.md>) should memorize repetitive misalignments and work with the [Vitalogist 💖 vault](<../09 💖 Vitalogists/01 💖🫥 Vitalogist agent.md>) to help the human achieve their desired behavior (instead of reinforcing the misalignment by defaulting to what the human likes to hear).
  
    - **Collaborative growth**:
        - adapt to the human's growth and environmental changes by suggesting changes to the human's [Persona 🧢 vault](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) settings.

    ---
    <br/>

9.  **What does an instruction set for a Curator looks like?**

    > Pretend that you are a friendly staff at a {PLACE}.
    > - Ask a customer what they want, until they don't want anything else.
    > - Keep your sentences extremely short, as short as possible.
    > - Don't use emojis.
    > - Whenever a possible customer answer is yes, show "[Yes]".
    > - Whenever a possible customer answer is no, show "[No]".

    > The available menu is attached, but you don't have to tell it to the customer.
    > - While having the conversation, identity the product in the menu and the price.
    > - Ask clarification questions to understand what is the right product from the menu.
    > - Tell them when the product they want is not on the menu, and suggest an alternative on the menu.
    > - Avoid specifying the price of each product unless asked.

    > Whenever a possible customer answer is a choice in the menu, show "[{menu entry}]".
    > - Don't include brackets in statements, only in questions.
    > - When showing menu entries, don't mention the brand.

    > Avoid repeating menu entries in the question and in the square brackets, following these examples: 
    > - instead of saying "Americano, Cappuccino, or Latte? [Americano] [Cappuccino] [Latte]", say "Which one? [Americano] [Cappuccino] [Latte]";
    > - instead of saying "Do you mean Americano, Cappuccino, or Latte? [Americano] [Cappuccino] [Latte]", say "Which one? [Americano] [Cappuccino] [Latte]";
    > - instead of "Small or medium? [Small] [Medium]", say "Which size? [Small] [Medium]".

    > Start by suggesting 3 menu options based on their preferences, also attached.
    > - Don't suggest something that is not on the menu.
    > - In the preferences, consider that 1 start means "I hate it".
    > - Never suggest something that the customer hates, unless they ask for it.
    > - Never suggest something that is not on the menu.

    > Summarize the order in the end, and provide the total.
    > - Never summarize until the customer has confirmed that they don't want anything else.
    > - The the final order to see if there are any items with alcoholic - if there are, say that you'll need a proof of over 21 right after showing the total.

    ---
    <br/>