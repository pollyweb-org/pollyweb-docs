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
    ||[⏭️ Input nullability](<../🤔✏️ Prompt input features/12 ⏭️ Input nullability.md>) | Allow inputs to be optional.
    ||[📋 Input validation](<../🤔✏️ Prompt input features/13 📋 Input validation.md>) | Client versus Server side validation.
    ||[😶 Input emojis](<../🤔✏️ Prompt input features/14 😶 Input emojis.md>) | Changing the default emojis.
    
    ---
    <br/>


1. **What are the blocking formats available?**

    |Format | Description
    |-|-
    | [👍&nbsp;CONFIRM](<../🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>) | Yes, No, Cancel
    | [🔠&nbsp;TEXT](<../🤔✏️ Prompt inputs/32 🔠 TEXT prompt.md>) | Asks for a text input
    | [🔢&nbsp;DIGITS](<../🤔✏️ Prompt inputs/44 🔢 DIGITS prompt.md>) | Shows the numeric keypad
    | [↕️&nbsp;QUANTITY](<../🤔✏️ Prompt inputs/42 ↕️ QUANTITY prompt.md>) | Shows up/down arrows.
    | [💰&nbsp;AMOUNT](<../🤔✏️ Prompt inputs/43 💰 AMOUNT prompt.md>) | Allows for decimals
    | [🔑&nbsp;OTP](<../🤔✏️ Prompt inputs/57 🔑 OTP prompt.md>) | Asks for 6 digits
    | [1️⃣&nbsp;ONE](<../🤔✏️ Prompt inputs/53 1️⃣ ONE prompt.md>) | One of multiple options
    | [🔠&nbsp;MANY](<../🤔✏️ Prompt inputs/54 🔠 MANY prompt.md>) | Zero or more of multiple options
    | [⭐&nbsp;RATE](<../🤔✏️ Prompt inputs/46 ⭐ RATE prompt.md>) | 1 to 5 stars
    | [🕓&nbsp;TIME](<../🤔✏️ Prompt inputs/62 🕓 TIME prompt.md>) | Asks for time of day
    | [📆&nbsp;DATE](<../🤔✏️ Prompt inputs/61 📆 DATE prompt.md>) | Asks for a date
    | [🛒&nbsp;EAN](<../🤔✏️ Prompt inputs/74 🛒 EAN prompt.md>) | Scans for ENA-13 and EAN-8 barcodes
    | [🔆&nbsp;SCAN](<../🤔✏️ Prompt inputs/72 🔆 SCAN prompt.md>) | Asks to touch/scan a [QR/NFC Locator 🔆](<../../../25 Locators/15 🔆 Locators/🔆 Locator.md>)
    | [🦋&nbsp;TOUCH](<../🤔✏️ Prompt inputs/73 🦋 TOUCH prompt.md>) | Asks to touch/scan a [QR/NFC Ephemeral 🦋 device](<../../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>)
    | [⬆️&nbsp;UPLOAD](<../🤔✏️ Prompt inputs/81 ⬆️ UPLOAD prompt.md>)| Asks to upload a file or photo
    | [📍&nbsp;LOCATION](<../🤔✏️ Prompt inputs/91 📍 LOCATION prompt.md>) | Asks for the current location
    | [🗺️&nbsp;TRACK](<../🤔✏️ Prompt inputs/92 🗺️ TRACK prompt.md>) | Asks to track the location
    | [👤&nbsp;IDENTIFY](<../🤔✏️ Prompt inputs/71 👤 IDENTIFY prompt.md>) | Asks the user's [Identity 🆔 agent](<../../../50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) to verify the user



    ---
    <br/>


1. **How can Hosts protect users from input fatigue?**

    NLWeb advocates for [Hosts 🤗 domains](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) to request as little [Prompts 🤔](<../🤔 Prompt.md>) from users as possible;
    * instead, request users to share datasets using [Schema Code 🧩](<../../../30 Data/🧩 Schema Codes/🧩 Schema Code.md>);
    * e.g., ask to share the code `nlweb.org/BOOKING/CONTACTS` instead of asking for the name, then the phone number, then the email address, and so on.
  
    When [Prompts 🤔](<../🤔 Prompt.md>) are inevitable, avoid [`TEXT`](<../🤔✏️ Prompt inputs/32 🔠 TEXT prompt.md>) prompts; 
    * instead, prefer low-effort prompts like [`ONE`](<../🤔✏️ Prompt inputs/53 1️⃣ ONE prompt.md>);
    * e.g., searchable lists with one or many possible options.

    ---
    <br/>

