# 🤔✏️ Blocking input prompts 😃 🫥

> Part of [Prompts 🤔](<../../Chats 💬/🤔 Prompt.md>)

## FAQ

1. **What are blocking inputs?**
   
    These are blocking [Prompts 🤔](<../../Chats 💬/🤔 Prompt.md>) 
    * that request a user input,
    * addressing the basic needs of a standard structured form with multiple input fields;
    * e.g., date, number, radio, checklist;
     
    This page is complemented with the following sections:
    
    ||Section | Details
    |-|- | -
    ||[⏭️ Input nullability](<../🤔✏️ Prompt inputs/⏭️ Input nullability.md>) | Allow inputs to be optional.
    ||[📋 Input validation](<../🤔✏️ Prompt inputs/📋 Input validation.md>) | Client versus Server side validation.
    ||[😶 Input emojis](<../🤔✏️ Prompt inputs/😶 Input emojis.md>) | Changing the default emojis.
    
    ---
    <br/>


1. **What are the blocking formats available?**

    |Format | Description
    |-|-
    | [👍&nbsp;CONFIRM](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) | Yes, No, Cancel
    | [🔠&nbsp;TEXT](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>) | Asks for a text input
    | [🔢&nbsp;DIGITS](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/DIGITS 🔢/DIGITS 🔢 prompt.md>) | Shows the numeric keypad
    | [↕️&nbsp;QUANTITY](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/QUANTITY ↕️/QUANTITY ↕️ prompt.md>) | Shows up/down arrows.
    | [💰&nbsp;AMOUNT](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/AMOUNT 💰/AMOUNT 💰 prompt.md>) | Allows for decimals
    | [🔑&nbsp;OTP](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/OTP 🔑/OTP 🔑 prompt.md>) | Asks for 6 digits
    | [1️⃣&nbsp;ONE](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) | One of multiple options
    | [🔠&nbsp;MANY](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/MANY 🔠/🔠 MANY ⌘ cmd.md>) | Zero or more of multiple options
    | [⭐&nbsp;RATE](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/RATE ⭐/RATE ⭐ prompt.md>) | 1 to 5 stars
    | [🕓&nbsp;TIME](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TIME 🕓/TIME 🕓 prompt.md>) | Asks for time of day
    | [📆&nbsp;DATE](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/DATE 📆/DATE 📆 prompt.md>) | Asks for a date
    | [🛒&nbsp;EAN](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/EAN 🛒/EAN 🛒 prompt.md>) | Scans for ENA-13 and EAN-8 barcodes
    | [🔆&nbsp;SCAN](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/SCAN 🔆/SCAN 🔆 prompt.md>) | Asks to touch/scan a [QR/NFC Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
    | [🦋&nbsp;TOUCH](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TOUCH 🦋/TOUCH 🦋 prompt.md>) | Asks to touch/scan a [QR/NFC Ephemeral 🦋 device](<../../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>)
    | [⬆️&nbsp;UPLOAD](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/UPLOAD ⬆️/UPLOAD ⬆️ prompt.md>)| Asks to upload a file or photo
    | [📍&nbsp;LOCATION](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/LOCATION 📍/LOCATION 📍 prompt.md>) | Asks for the current location
    | [🗺️&nbsp;TRACK](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TRACK 🗺️/TRACK 🗺️ prompt.md>) | Asks to track the location
    | [👤&nbsp;IDENTIFY](<../../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/IDENTIFY 🆔/🆔 IDENTIFY ⌘ cmd.md>) | Asks the user's [Identity 🆔 agent](<../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) to verify the user



    ---
    <br/>


1. **How can Hosts protect users from input fatigue?**

    NLWeb advocates for [Hosts 🤗 domains](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) to request as little [Prompts 🤔](<../../Chats 💬/🤔 Prompt.md>) from users as possible;
    * instead, request users to share datasets using [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>);
    * e.g., ask to share the code `nlweb.dom/BOOKING/CONTACTS` instead of asking for the name, then the phone number, then the email address, and so on.
  
    When [Prompts 🤔](<../../Chats 💬/🤔 Prompt.md>) are inevitable, avoid [`TEXT`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>) prompts; 
    * instead, prefer low-effort prompts like [`ONE`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>);
    * e.g., searchable lists with one or many possible options.

    ---
    <br/>

