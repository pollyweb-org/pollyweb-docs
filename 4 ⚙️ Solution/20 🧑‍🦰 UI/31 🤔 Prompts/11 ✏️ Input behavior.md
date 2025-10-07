# Blocking input prompts 😃 🫥

> Part of [Prompts 🤔](<01 🤔 Prompt.md>)

<br/>

1. **What are blocking inputs?**
   
    These are blocking [Prompts 🤔](<01 🤔 Prompt.md>) 
    * that request a user input,
    * addressing the basic needs of a standard structured form with multiple input fields;
    * e.g., date, number, radio, checklist;
     
    This page is complemented with the following sections:
    ||Section
    |-|-
    ||[🫥 Input emojis](<12 ✏️🫥 Input emojis.md>)
    ||[⚡ Input validations](<13 ✏️⚡ Input validation.md>)

    ---
    <br/>


1. **What are the blocking formats available?**

    |Format | Description
    |-|-
    | [👍&nbsp;CONFIRM](<31 👍 CONFIRM prompt.md>) | Yes, No, Cancel
    | [🔠&nbsp;TEXT](<32 🔠 TEXT prompt.md>) | Asks for a text input
    | [🔢&nbsp;INT](<44 🔢 INT prompt.md>) | Shows the numeric keypad
    | [🔄&nbsp;QUANTITY](<42 🔄 QUANTITY prompt.md>) | Shows up/down arrows.
    | [💰&nbsp;AMOUNT](<45 💰 AMOUNT prompt.md>) | Allows for decimals
    | [🔑&nbsp;OTP](<43 🔑 OTP prompt.md>) | Asks for 6 digits
    | [1️⃣&nbsp;ONE](<55 1️⃣ ONE prompt.md>) | One of multiple options
    | [🔠&nbsp;MANY](<54 🔠 MANY prompt.md>) | Zero or more of multiple options
    | [⭐&nbsp;RATE](<56 ⭐ RATE prompt.md>) | 1 to 5 stars
    | [🕓&nbsp;TIME](<62 🕓 TIME prompt.md>) | Asks for time of day
    | [📆&nbsp;DATE](<61 📆 DATE prompt.md>) | Asks for a date
    | [🛒&nbsp;EAN](<74 🛒 EAN prompt.md>) | Scans for ENA-13 and EAN-8 barcodes
    | [🔆&nbsp;SCAN](<72 🔆 SCAN prompt.md>) | Asks to touch/scan a [QR/NFC Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>)
    | [🦋&nbsp;TOUCH](<73 🦋 TOUCH prompt.md>) | Asks to touch/scan a [QR/NFC Ephemeral 🦋 device](<../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>)
    | [⬆️&nbsp;UPLOAD](<81 ⬆️ UPLOAD prompt.md>)| Asks to upload a file or photo
    | [📍&nbsp;LOCATION](<91 📍 LOCATION prompt.md>) | Asks for the current location
    | [🗺️&nbsp;TRACK](<92 🗺️ TRACK prompt.md>) | Asks to track the location
    | [👤&nbsp;IDENTIFY](<71 👤 IDENTIFY prompt.md>) | Asks the user's [Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) to verify the user



    ---
    <br/>


1. **How can Hosts protect users from input fatigue?**

    NLWeb advocates for [Hosts 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) to request as little [Prompts 🤔](<01 🤔 Prompt.md>) from users as possible;
    * instead, request users to share datasets using [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>);
    * e.g., ask to share the code `nlweb.org/BOOKING/CONTACTS` instead of asking for the name, then the phone number, then the email address, and so on.
  
    When [Prompts 🤔](<01 🤔 Prompt.md>) are inevitable, avoid [`TEXT`](<32 🔠 TEXT prompt.md>) prompts; 
    * instead, prefer low-effort prompts like [`ONE`](<55 1️⃣ ONE prompt.md>);
    * e.g., searchable lists with one or many possible options.

    ---
    <br/>


1. **Can users reject a mandatory input prompt?**

    No. Like in a conversation between two persons, 
    * users can only stay silent 
    * or [abandon the conversation 👉](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>).

    ---
    <br/>


1. **What does a mandatory input look like?**

    Here's a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>).

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? | ` `
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ❌ Required input.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? | `0123`
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Your code is `0123`
    |

    <br/>
    
    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).

    ```yaml
    # 😃 Talker
    - INT|What's the code? >> $code
    - SUCCESS|Your code is `{$code}`
    ```
    
    ---
    <br/>



1. **How to define optional inputs?**

    [Input prompts ✏️](<11 ✏️ Input behavior.md>) 
    * can be made optional 
    * by setting the property `Optional` to `True`.
    
    ---
    <br/>


1. **What does an optional input look like?**

    Here's a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>).

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? | ` `
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ You didn't provide a code.
    |

    <br/>

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).

    ```yaml
    # 😃 Talker
    - INT|What's the code? >> $code:
        Optional: True
    - IF|$code:
        Then: SUCCESS|Your code is `{$code}`
        Else: SUCCESS|You didn't provide a code.
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: INT
    Message: 😃 What's the code?
    ```

    ---
    <br/>
