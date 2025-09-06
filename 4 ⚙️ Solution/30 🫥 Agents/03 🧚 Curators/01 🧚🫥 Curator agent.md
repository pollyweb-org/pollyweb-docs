<!-- #TODO -->

🧚🗄️ Curator vault FAQ
===

1. **How do curators work?**

    Curators 🧚 are invoked by [Hosts 🤗](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) to parse a set of choices and return a list of codes back to the Host - e.g.:
    
    - restaurants share menus and receive [food orders 🥘](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/03 🍽️🍲 Eat at restaurants/03 🍲 Order @ Seat 🪑/01 🪑 Order food 🥘.md>)
    - travel agencies share hotel options and receive [bookings 🏨](<../../../3 🤝 Use Cases/03 🧳 Travel/08 🧳 Stay at hotels 🏨/01 🏨 Guest @ Home 🏠/01 🏠 Book.md>)
    - cash machines share bills and receive [withdraw orders 🏧](<../../../3 🤝 Use Cases/05 🛠️ Services/03 🏧 Withdraw at ATMs/10 Customer @ ATM/11 Withdraw cash.md>)
    - social networks share posts and receive filtered lists.

    ---

1. **How do curators protect users?**

    Curators 🧚 protect users by filtering out from the available options given by [Hosts 🤗](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) instead of sharing details about the user - e.g.:
    - chose meat for dinner, instead of disclosing an allergy to shrimp;
    - chose a back seat at a show, instead of disclosing a maximum budget.

    ---

1. **How do curators protect themselves from prompt injection?**

    Curators 🧚 assess [Host 🤗](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) inputs before acting on them. 
    - Suspicious behaviors are reported to [Firewalls 🔥](<../../40 👥 Domains/43 👍 Trusts/03 🔥🛠️ Firewall helper.md>).

    ---

1. **How do curators protect themselves from data breaches?**

    While Curators 🧚 communicate using natural language with [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), they output to [Hosts 🤗](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) only a filtered list of codes referenced in the input.

    ---

1. **How much user data should a curator store?**

    NLWeb advocates for Curators 🧚 to rely on [Persona 🧢](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) vaults to assess user intent, while storing the nuances of those intents in the Curator's 🧚 memory:
    - this addresses the different speed of developments between humans and machines; 
    - i.e., humans change their tastes and behaviors slower as they age, while new and better machine algorithms appear exponentially faster;
    - this separation of concerns allows users to retain their legacy [Persona 🧢](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) vault while constantly upgrading to new smarter Curators 🧚 as they are released.

    ---

1. **How should curators deal with ethical issues?**

    Ethics vary by civilization. 
    - Thus, users are advised to exercise conscience when selecting the provider of their Curator 🧚 agent.
    - Is is expected that users will select the Curator 🧚 provider most aligned to their social values.

    Nonetheless, Curators 🧚 should thrive to follow a generic set of globally accepted ethical norms.

    - **Safety guardrails**: 
        - protect the physical and mental safety of the human, leveraging their [Identity 🆔](<../05 🆔 Identities/03 🆔🫥 Identity agent.md>) vault to guardrail legal and cultural nuances.
        - e.g., when suggesting alcoholic beverages to an American user visiting Portugal, consider both the minimum drinking age on the current country (18 in Portugal) and in the user's nationality country (21 in the USA).
  
    - **Cognitive dissonance**: 
        - respect the human's intent behavior by leveraging [Persona 🧢](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) vaults while addressing the emotional side of the human;
        - e.g., if a human says they prefer to eat vegetables but reject all dishes that contain vegetables, then the Curator 🧚 should memorize repetitive misalignments and work with the [Vitalogist 💖](<../09 💖 Vitalogists/01 💖🫥 Vitalogist agent.md>) vault to help the human achieve their desired behavior (instead of reinforcing the misalignment by defaulting to what the human likes to hear).
  
    - **Collaborative growth**:
        - adapt to the human's growth and environmental changes by suggesting changes to the human's [Persona 🧢](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) settings.

    ---

2. **What does an LLM prompt for a Curator looks like?**

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