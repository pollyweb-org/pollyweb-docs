🤔 Prompt FAQ
===

1. **What is a Prompt?**

    A [Prompt 🤔](<02 🤔 Prompt.md>) is 
    * a line in [Chat 💬](<01 💬 Chat.md>) 
    * sent by a [Host 🤗 domain](<04 🤗🎭 Host role.md>) 
    * with a question or information to the user
    * for a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to render.

    ---
    <br/>



1. **What input formats can Hosts ask Wallets to render?**

    Similar to HTTP, on NLWeb the [Host 🤗 domain](<04 🤗🎭 Host role.md>) servers request the [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to render the requested [Prompts 🤔](<02 🤔 Prompt.md>).

    * The supported [Prompt 🤔](<02 🤔 Prompt.md>) formats are as follow.

    | Format | Description
    |-|-
    | ℹ️&nbsp;INFO | General information.
    | ⏳&nbsp;TEMP| Temporary message.
    | ✅&nbsp;SUCCESS | Success message.
    | ❌&nbsp;FAILURE | Failure message.
    | 👍&nbsp;CONFIRM | Yes, No, Cancel.
    | 💯&nbsp;INT | Shows the numeric keypad.
    | 🔄&nbsp;QUANTITY | Shows up/down arrows.
    | 💰&nbsp;AMOUNT | Allows for decimals.
    | 🔑&nbsp;OTP | Asks for 6 digits.
    | 1️⃣&nbsp;ONE | One of multiple options.
    | 🔢&nbsp;MANY | Zero or more of multiple options.
    | ⭐&nbsp;RATE | 1 to 5 stars.
    | 🕓&nbsp;TIME | Asks for time of day.
    | 📆&nbsp;DATE | Asks for a date.
    | 🗓️&nbsp;UNTIL | Asks for a date/time in the future.
    | 📍&nbsp;LOCATION | Asks for the current location.
    | 🗺️&nbsp;TRACK | Asks to track the location.
    | 👤&nbsp;IDENTIFY | Opens a pop-up for the user's [Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) to perform a face scan.
    | 🛒&nbsp;EAN | Scans for ENA-13 and EAN-8 barcodes.
    | 🔆&nbsp;SCAN | Asks to touch/scan a [QR/NFC Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>).
    | 🦋&nbsp;TOUCH | Asks to touch/scan a [QR/NFC Ephemeral 🦋 device](<../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>).
    | ⬆️&nbsp;UPLOAD | Asks to upload a file or photo.
    | ⬇️&nbsp;DOWNLOAD | Asks to download a file.
    | 🔠&nbsp;TEXT | Asks for a text input.

    ---
    <br/>


2. **What does a Prompt request look like?**

    The following is an example of a [Prompt 🤔](<02 🤔 Prompt.md>) request, as described in [Prompted@Host 🚀](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: ONE
    Message: Which credit card to use?
    Options: 
        - ID: 1
          Translation: Personal
    Appendix: <appendix-uuid>
    Details: |
        **Note**: each cards has its own fees.
        * Check the fees for the transaction.
    ```


    |Property|Type|Description
    |-|-|-
    | `Format`  | string | One supported by a [Chat 💬](<01 💬 Chat.md>)
    | `Message` | string | Main message displayed in the [Chat 💬](<01 💬 Chat.md>)
    | `Options` | list   | List of Options with:<br/>- ID of the option for replies<br/>- Translated text of the option to display 
    | `Appendix`| UUID   | PDF or PNG appendix to download via [Download@Host 🚀](<../../../6 🅰️ APIs/50 🤗🅰️ Host/06 🧑‍🦰🚀🤗 Download.md>)
    | `Details` | string | Extended details in Markdown format, topically hidden by an expand [+] sign
    |



2. **How do Prompt emojis work?**

    [Prompt 🤔](<02 🤔 Prompt.md>) emojis are visual clues for users.

    - **Non-blocking info ℹ️ ⓘ**
        - this is an informative prompt that does not require the user input;
        - if it contains options, then the user may click an option any time 
          - i.e., before or after the [Host 🤗 domains](<04 🤗🎭 Host role.md>) sends other subsequent [Prompts 🤔](<02 🤔 Prompt.md>);
        - the strong info emoji ℹ️ represents the chat's [Host 🤗 domain](<04 🤗🎭 Host role.md>);
        - the faded info emoji ⓘ represents other domains that have been pulled into the [Chat 💬](<01 💬 Chat.md>)chat.
    
    - **Non-blocking temporary info ⏳**
        - this is an info [Prompt 🤔](<02 🤔 Prompt.md>) that is automatically removed when a new prompt arrives;
        - if it contains options, then the user may click an option while it's visible.
    
    - **Non-blocking result ✅**
        - this is an info [Prompt 🤔](<02 🤔 Prompt.md>) that signals the user that the transaction is completed and there are no further inputs required - they can put down the phone.
    
    - **Non-blocking failure ❌**
        - this is an info [Prompt 🤔](<02 🤔 Prompt.md>) that signals the user that the transaction was not successful;
        - it's typically followed by a prompt to help the user fix the problem.
    
    - **Blocking structured questions 😃 😐 🫥**
        - this is a blocking input [Prompt 🤔](<02 🤔 Prompt.md>) that requires the user to answer it in a structured format (e.g., date, number, radio, checklist);
        - it addresses the basic needs of a standard structured form with multiple input fields.
        - the happy emoji 😃 represent the chat's [Host 🤗 domain](<04 🤗🎭 Host role.md>);
        - the neutral emoji 😐 also represents the [Host 🤗 domain](<04 🤗🎭 Host role.md>), while providing an alternative neutral face when a smile is not adequate (e.g., in an emergency situation);
        - the faded emoji 🫥 represents other domains that have been pulled into the chat.
  
    - **Blocking unstructured questions 💬 💭**
        - this is a blocking input [Prompt 🤔](<02 🤔 Prompt.md>) that allows the user to type something instead of having to follow a structured format;
        - it allows for large-language models (LLMs) to interpret the user's intent from natural language text, while also providing a structured input to facilitate the user's interaction;
          - e.g., a user may select the "Yes" option, or type "ok" in the textbox;
        - the speech emoji 💬 represent the chat's [Host 🤗 domain](<04 🤗🎭 Host role.md>);
        - the thought emoji 💭 represents other domains that have been pulled into the chat.

    ---
    <br/>


8. **How can Hosts protect users from input fatigue?**

    NLWeb advocates for [Hosts 🤗 domains](<04 🤗🎭 Host role.md>) to request as little [Prompts 🤔](<02 🤔 Prompt.md>) from users as possible;
    * instead, request users to share datasets using [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>);
    * e.g., ask to share the code `nlweb.org/BOOKING/CONTACTS` instead of asking for the name, then the phone number, then the email address, and so on.
  
    When [Prompts 🤔](<02 🤔 Prompt.md>) are inevitable, avoid text prompts; 
    * instead, prefer low-effort prompts;
    * e.g., searchable lists with one or many possible options.

    ---
    <br/>


3. **Can Hosts replace sent prompts?**

    Yes, but only temporary [Prompts 🤔](<02 🤔 Prompt.md>). 
    - If a [Host 🤗 domain](<04 🤗🎭 Host role.md>) sends  two consecutive blocking [Prompts 🤔](<02 🤔 Prompt.md>) while the user has not answered the first, then the first becomes readonly and the second becomes the active input.
    - If the [Host 🤗 domain](<04 🤗🎭 Host role.md>) wants a [Prompts 🤔](<02 🤔 Prompt.md>) to be visually replaced, then they need to use a temporary [Prompts 🤔](<02 🤔 Prompt.md>), visually represented by an hourglass ⏳ emoji. 
    - This is particularly useful when [preparing food 🤝](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/03 🍽️🍲 Eat at restaurants/03 🍲 Order @ Seat 🪑/03 🪑 Change order 🌀.md>), when [waiting food orders 🤝](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/03 🍽️🍲 Eat at restaurants/06 🍲 Staff @ Back 🧑‍🍳/02 🧑‍🍳 Prepare food 🥘.md>), and when reminding users of [upcoming bookings 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>).

    ---
    <br/>

4. **Can users respond to an old prompt?**

    NLWeb [Chats 💬](<01 💬 Chat.md>) are designed to be forward-only workloads managed by a [Host 🤗 domain](<04 🤗🎭 Host role.md>) (and not by the user). 
    * This behavior is visible on LLM apps like on ChatGPT, Gemini, and others. 
  
    Just like in the previously referred LLMs, NLWeb also allows [Host 🤗 domains](<04 🤗🎭 Host role.md>) to add options in certain steps so that users can go back and change the direction of the workload from a previous step.
    * For example, the user did A, B, C, D, E; then went back to B and changed the history to A, B, X, Y, Z. 
    * This worked because step B had an option set by the [Host 🤗 domains](<04 🤗🎭 Host role.md>) that allowed the user to go back and change the workflow path.

    In NLWeb, these option sets can be added only to non-blocking [Prompts 🤔](<02 🤔 Prompt.md>).

    - The non-blocking prompts include Wait ⏳, Info ℹ️, and Result ✅.
    - This is particularly helpful when [Host 🤗 domains](<04 🤗🎭 Host role.md>) want to assign default values to options to speed up the process (e.g., [navigation options 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/01 🧳 Plans trips 🧭/2 🧭 @ Destination/21 Return.md>)), while still allowing users to go back and change those default options.
    
    ---
    <br/>
