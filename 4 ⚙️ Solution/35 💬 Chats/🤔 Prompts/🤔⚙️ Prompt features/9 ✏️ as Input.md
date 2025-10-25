# Blocking input prompts 😃 🫥

> Part of [Prompts 🤔](<../🤔 Prompt.md>)

<br/>

1. **What are blocking inputs?**
   
    These are blocking [Prompts 🤔](<../🤔 Prompt.md>) 
    * that request a user input,
    * addressing the basic needs of a standard structured form with multiple input fields;
    * e.g., date, number, radio, checklist;
     
    This page is complemented with the following sections:
    
    ||Section | Details
    |-|- | -
    ||[⏭️ Input nullability](<../🤔✏️ Prompt input features/⏭️ Input nullability.md>) | Allow inputs to be optional.
    ||[📋 Input validation](<../🤔✏️ Prompt input features/📋 Input validation.md>) | Client versus Server side validation.
    ||[😶 Input emojis](<../🤔✏️ Prompt input features/😶 Input emojis.md>) | Changing the default emojis.
    
    ---
    <br/>


1. **What are the blocking formats available?**

    |Format | Description
    |-|-
    | [👍&nbsp;CONFIRM](<../🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) | Yes, No, Cancel
    | [🔠&nbsp;TEXT](<../🤔✏️ Prompt inputs/TEXT 🔠 prompt.md>) | Asks for a text input
    | [🔢&nbsp;DIGITS](<../🤔✏️ Prompt inputs/DIGITS 🔢/DIGITS 🔢 prompt.md>) | Shows the numeric keypad
    | [↕️&nbsp;QUANTITY](<../🤔✏️ Prompt inputs/QUANTITY ↕️/QUANTITY ↕️ prompt.md>) | Shows up/down arrows.
    | [💰&nbsp;AMOUNT](<../🤔✏️ Prompt inputs/AMOUNT 💰/AMOUNT 💰 prompt.md>) | Allows for decimals
    | [🔑&nbsp;OTP](<../🤔✏️ Prompt inputs/OTP 🔑/OTP 🔑 prompt.md>) | Asks for 6 digits
    | [1️⃣&nbsp;ONE](<../🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>) | One of multiple options
    | [🔠&nbsp;MANY](<../🤔✏️ Prompt inputs/MANY 🔠/MANY 🔠 prompt.md>) | Zero or more of multiple options
    | [⭐&nbsp;RATE](<../🤔✏️ Prompt inputs/RATE ⭐/RATE ⭐ prompt.md>) | 1 to 5 stars
    | [🕓&nbsp;TIME](<../🤔✏️ Prompt inputs/TIME 🕓 prompt.md>) | Asks for time of day
    | [📆&nbsp;DATE](<../🤔✏️ Prompt inputs/DATE 📆/DATE 📆 prompt.md>) | Asks for a date
    | [🛒&nbsp;EAN](<../🤔✏️ Prompt inputs/EAN 🛒/EAN 🛒 prompt.md>) | Scans for ENA-13 and EAN-8 barcodes
    | [🔆&nbsp;SCAN](<../🤔✏️ Prompt inputs/SCAN 🔆 prompt.md>) | Asks to touch/scan a [QR/NFC Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
    | [🦋&nbsp;TOUCH](<../🤔✏️ Prompt inputs/TOUCH 🦋 prompt.md>) | Asks to touch/scan a [QR/NFC Ephemeral 🦋 device](<../../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>)
    | [⬆️&nbsp;UPLOAD](<../🤔✏️ Prompt inputs/UPLOAD ⬆️ prompt.md>)| Asks to upload a file or photo
    | [📍&nbsp;LOCATION](<../🤔✏️ Prompt inputs/LOCATION 📍/LOCATION 📍 prompt.md>) | Asks for the current location
    | [🗺️&nbsp;TRACK](<../🤔✏️ Prompt inputs/TRACK 🗺️ prompt.md>) | Asks to track the location
    | [👤&nbsp;IDENTIFY](<../🤔✏️ Prompt inputs/IDENTIFY 👤/IDENTIFY 👤 prompt.md>) | Asks the user's [Identity 🆔 agent](<../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) to verify the user



    ---
    <br/>


1. **How can Hosts protect users from input fatigue?**

    NLWeb advocates for [Hosts 🤗 domains](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) to request as little [Prompts 🤔](<../🤔 Prompt.md>) from users as possible;
    * instead, request users to share datasets using [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>);
    * e.g., ask to share the code `nlweb.dom/BOOKING/CONTACTS` instead of asking for the name, then the phone number, then the email address, and so on.
  
    When [Prompts 🤔](<../🤔 Prompt.md>) are inevitable, avoid [`TEXT`](<../🤔✏️ Prompt inputs/TEXT 🔠 prompt.md>) prompts; 
    * instead, prefer low-effort prompts like [`ONE`](<../🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>);
    * e.g., searchable lists with one or many possible options.

    ---
    <br/>

