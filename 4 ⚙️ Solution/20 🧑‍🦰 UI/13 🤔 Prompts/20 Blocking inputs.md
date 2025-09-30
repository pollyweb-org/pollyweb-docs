# Blocking structured inputs 😃 😐 🫥

> Part of [Prompts 🤔](<01 🤔 Prompt.md>)

<br/>

1. **What are blocking inputs?**
   
    These are blocking [Prompts 🤔](<01 🤔 Prompt.md>) 
    * that requires the user to answer it in a structured format,
    * addressing the basic needs of a standard structured form with multiple input fields;
    * e.g., date, number, radio, checklist;
     

    ---
    <br/>

1. **What are the blocking formats available?**

    |Format | Description
    |-|-
    | [👍&nbsp;CONFIRM](<24 👍 CONFIRM prompt.md>) | Yes, No, Cancel
    | [💯&nbsp;INT](<21 💯 INT prompt.md>) | Shows the numeric keypad
    | [🔄&nbsp;QUANTITY](<21 🔄 QUANTITY prompt.md>) | Shows up/down arrows.
    | [💰&nbsp;AMOUNT](<22 💰 AMOUNT prompt.md>) | Allows for decimals
    | [🔑&nbsp;OTP](<21 🔑 OTP prompt.md>) | Asks for 6 digits
    | [1️⃣&nbsp;ONE](<25 1️⃣ ONE prompt.md>) | One of multiple options
    | [🔢&nbsp;MANY](<25 🔢 MANY prompt.md>) | Zero or more of multiple options
    | [⭐&nbsp;RATE](<26 ⭐ RATE prompt.md>) | 1 to 5 stars
    | [🕓&nbsp;TIME](<27 🕓 TIME prompt.md>) | Asks for time of day
    | [📆&nbsp;DATE](<27 📆 DATE prompt.md>) | Asks for a date
    | [🗓️&nbsp;UNTIL](<27 🗓️ UNTIL prompt.md>) | Asks for a date/time in the future
    | [📍&nbsp;LOCATION](<61 📍 LOCATION prompt.md>) | Asks for the current location
    | [🗺️&nbsp;TRACK](<62 🗺️ TRACK prompt.md>) | Asks to track the location
    | [👤&nbsp;IDENTIFY](<41 👤 IDENTIFY prompt.md>) | Opens a pop-up for the user's [Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) to perform a face scan
    | [🛒&nbsp;EAN](<44 🛒 EAN prompt.md>) | Scans for ENA-13 and EAN-8 barcodes
    | [🔆&nbsp;SCAN](<42 🔆 SCAN prompt.md>) | Asks to touch/scan a [QR/NFC Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>)
    | [🦋&nbsp;TOUCH](<43 🦋 TOUCH prompt.md>) | Asks to touch/scan a [QR/NFC Ephemeral 🦋 device](<../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>)
    | [⬆️&nbsp;UPLOAD](<51 ⬆️ UPLOAD prompt.md>)| Asks to upload a file or photo
    | [⬇️&nbsp;DOWNLOAD](<52 ⬇️ DOWNLOAD prompt.md>) | Asks to download a file
    | [🔠&nbsp;TEXT](<31 🔠 TEXT prompt.md>) | Asks for a text input


    ---
    <br/>

1. **How do emojis work?**

    Emoji | Behavior
    |-|-
    😃 | The happy emoji 😃 represent the chat's [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>).
    😐 | The neutral emoji 😐 also represents the [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>), while providing an alternative neutral face when a smile is not adequate (e.g., in an emergency situation).
    🫥 | The faded emoji 🫥 represents other domains that have been pulled into the chat. These can be either a user's [Agent 🫥 vault](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) or a [Helper 🛠️ domain](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) that was [invited ⏩](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite.md>) by a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>).

    ---
    <br/>


## Emotions

The 😃 emoji can be replaced with one of the following.

||Emoji | Application
|-|-|-
|| 😐 | Neutral
|| 😕 | Confused, sad
|| 🥺 | Pleading face
|| ✏️ | Form input field
|


1. **How can Hosts protect users from input fatigue?**

    NLWeb advocates for [Hosts 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) to request as little [Prompts 🤔](<01 🤔 Prompt.md>) from users as possible;
    * instead, request users to share datasets using [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>);
    * e.g., ask to share the code `nlweb.org/BOOKING/CONTACTS` instead of asking for the name, then the phone number, then the email address, and so on.
  
    When [Prompts 🤔](<01 🤔 Prompt.md>) are inevitable, avoid text prompts; 
    * instead, prefer low-effort prompts;
    * e.g., searchable lists with one or many possible options.

    ---
    <br/>
