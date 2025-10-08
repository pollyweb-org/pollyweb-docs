# Blocking input prompts 😃 🫥

> Part of [Prompts 🤔](<01 🤔 Prompt.md>)

<br/>

1. **What are blocking inputs?**
   
    These are blocking [Prompts 🤔](<01 🤔 Prompt.md>) 
    * that request a user input,
    * addressing the basic needs of a standard structured form with multiple input fields;
    * e.g., date, number, radio, checklist;
     
    This page is complemented with the following sections:
    
    ||Section | Details
    |-|- | -
    ||[⏭️ Input nullability](<../25 Input defintions/12 ✏️⏭️ Input nullability.md>) | Allow inputs to be optional.
    ||[📋 Input validation](<../25 Input defintions/13 ✏️📋 Input validation.md>) | Client versus Server side validation.
    ||[😶 Input emojis](<../25 Input defintions/14 ✏️😶 Input emojis.md>) | Changing the default emojis.
    
    ---
    <br/>


1. **What are the blocking formats available?**

    |Format | Description
    |-|-
    | [👍&nbsp;CONFIRM](<../30 Input prompts/31 👍 CONFIRM prompt.md>) | Yes, No, Cancel
    | [🔠&nbsp;TEXT](<../30 Input prompts/32 🔠 TEXT prompt.md>) | Asks for a text input
    | [🔢&nbsp;DIGITS](<../30 Input prompts/44 🔢 DIGITS prompt.md>) | Shows the numeric keypad
    | [🔄&nbsp;QUANTITY](<../30 Input prompts/42 🔄 QUANTITY prompt.md>) | Shows up/down arrows.
    | [💰&nbsp;AMOUNT](<../30 Input prompts/43 💰 AMOUNT prompt.md>) | Allows for decimals
    | [🔑&nbsp;OTP](<../30 Input prompts/57 🔑 OTP prompt.md>) | Asks for 6 digits
    | [1️⃣&nbsp;ONE](<../30 Input prompts/53 1️⃣ ONE prompt.md>) | One of multiple options
    | [🔠&nbsp;MANY](<../30 Input prompts/54 🔠 MANY prompt.md>) | Zero or more of multiple options
    | [⭐&nbsp;RATE](<../30 Input prompts/46 ⭐ RATE prompt.md>) | 1 to 5 stars
    | [🕓&nbsp;TIME](<../30 Input prompts/62 🕓 TIME prompt.md>) | Asks for time of day
    | [📆&nbsp;DATE](<../30 Input prompts/61 📆 DATE prompt.md>) | Asks for a date
    | [🛒&nbsp;EAN](<../30 Input prompts/74 🛒 EAN prompt.md>) | Scans for ENA-13 and EAN-8 barcodes
    | [🔆&nbsp;SCAN](<../30 Input prompts/72 🔆 SCAN prompt.md>) | Asks to touch/scan a [QR/NFC Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>)../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md
    | [🦋&nbsp;TOUCH](<../30 Input prompts/73 🦋 TOUCH prompt.md>) | Asks to touch/scan a [QR/NFC Ephemeral 🦋 device](<../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ep../../../4 ⚙️ Solution/60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md
    | [⬆️&nbsp;UPLOAD](<../30 Input prompts/81 ⬆️ UPLOAD prompt.md>)| Asks to upload a file or photo
    | [📍&nbsp;LOCATION](<../30 Input prompts/91 📍 LOCATION prompt.md>) | Asks for the current location
    | [🗺️&nbsp;TRACK](<../30 Input prompts/92 🗺️ TRACK prompt.md>) | Asks to track the location
    | [👤&nbsp;IDENTIFY](<../30 Input prompts/71 👤 IDENTIFY prompt.md>) | Asks the user's [Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 ../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md



    ---
    <br/>


1. **How can Hosts protect users from input fatigue?**

    NLWeb advocates for [Hosts 🤗 domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) to request as little [Prompts 🤔](<01 🤔 Prompt.md>)../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.mdpossible;
    * instead, request users to share datasets using [Schema Code 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>);
    * e.g., ask to share the code `nlweb.org/BOOKING/CONTACTS` instead of asking for the name, then the phone number, then the email address, and so on.
  
    When [Prompts 🤔](<../30 Input prompts/32 🔠 TEXT prompt.md>) prompts; 
    * instead, prefer low-effort prompts like [`ONE`](<../30 Input prompts/53 1️⃣ ONE prompt.md>);
    * e.g., searchable lists with one or many possible options.

    ---
    <br/>

