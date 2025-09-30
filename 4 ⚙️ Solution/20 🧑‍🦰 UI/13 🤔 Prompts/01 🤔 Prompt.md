🤔 Prompt FAQ
===

1. **What is a Prompt?**

    A [Prompt 🤔](<01 🤔 Prompt.md>) is 
    * a line in [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) 
    * sent by a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) 
    * with a question or information to the user
    * for a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to render.

    ---
    <br/>



1. **What input formats can Hosts ask Wallets to render?**

    Similar to HTTP, on NLWeb the [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) servers request the [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to render the requested [Prompts 🤔](<01 🤔 Prompt.md>).

    * The supported [Prompt 🤔](<01 🤔 Prompt.md>) formats are as follow.

    |Behavior| Format 
    |-|-
    |[Status](<10 Non-blocking status.md>)| [`ℹ️ INFO`](<11 ℹ️ INFO prompt.md>) [`⏳ TEMP`](<12 ⏳ TEMP prompt.md>) [`✅ SUCCESS`](<13 ✅ SUCCESS prompt.md>) [`❌ FAILURE`](<14 ❌ FAILURE prompt.md>)
    |[Input](<20 Blocking inputs.md>)| [`💯 INT`](<21 💯 INT prompt.md>) [`🔄 QUANTITY`](<21 🔄 QUANTITY prompt.md>) [`💰 AMOUNT`](<22 💰 AMOUNT prompt.md>) [`🔑 OTP`](<21 🔑 OTP prompt.md>) [`⭐ RATE`](<26 ⭐ RATE prompt.md>) 
    || [`👍 CONFIRM`](<24 👍 CONFIRM prompt.md>) [`1️⃣ ONE`](<25 1️⃣ ONE prompt.md>) [`🔢 MANY`](<25 🔢 MANY prompt.md>) 
    || [`🕓 TIME`](<27 🕓 TIME prompt.md>) [`📆 DATE`](<27 📆 DATE prompt.md>) [`🗓️ UNTIL`](<27 🗓️ UNTIL prompt.md>) 
    |[Location](<60 Location prompts.md>)| [`📍 LOCATION`](<61 📍 LOCATION prompt.md>) [`🗺️ TRACK`](<62 🗺️ TRACK prompt.md>)
    |[Scans](<40 Scans.md>)| [`👤 IDENTIFY`](<41 👤 IDENTIFY prompt.md>) [`🛒 EAN`](<44 🛒 EAN prompt.md>) [`🔆 SCAN`](<42 🔆 SCAN prompt.md>) [`🦋 TOUCH`](<43 🦋 TOUCH prompt.md>) 
    || [`⬆️ UPLOAD`](<51 ⬆️ UPLOAD prompt.md>) [`⬇️ DOWNLOAD`](<52 ⬇️ DOWNLOAD prompt.md>) 
    |[Text](<30 Unstructured inputs.md>)| [`🔠 TEXT`](<31 🔠 TEXT prompt.md>) 

    ---
    <br/>


2. **What does a Prompt request look like?**

    The following is an example of a [Prompt 🤔](<01 🤔 Prompt.md>) request, as described in [Prompted@Host 🚀](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

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
    | `Format`  | string | One supported by a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)
    | `Message` | string | Main message displayed in the [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)
    | `Options` | list   | List of Options with:<br/>- ID of the option for replies<br/>- Translated text of the option to display 
    | `Appendix`| uuid   | PDF or PNG appendix to download via [Download@Host 🚀](<../../../6 🅰️ APIs/50 🤗🅰️ Host/06 🧑‍🦰🚀🤗 Download.md>)
    | `Details` | string | Extended details in Markdown format, topically hidden by an expand [+] sign
    |



2. **How do Prompt emojis work?**

    [Prompt 🤔](<01 🤔 Prompt.md>) emojis are visual clues for users.

    | Behavior | Prompt | Host | Guest | 
    |-|-|:-:|:-:
    | `Status`  | [`INFO`](<11 ℹ️ INFO prompt.md>) | ℹ️ | ⓘ
    |           | [`SUCCESS`](<13 ✅ SUCCESS prompt.md>) | ✅ | ☑️
    |           | [`FAILURE`](<14 ❌ FAILURE prompt.md>) | ❌ | ✖️
    |           | [`TEMP`](<12 ⏳ TEMP prompt.md>) | ⏳ | ⏳
    | `Input`   | [`TEXT`](<31 🔠 TEXT prompt.md>) | 💬 | 💭
    |           | (others) | 😃 | 🫥 | 
    | `Share`   | [`LOCATION`](<61 📍 LOCATION prompt.md>) | 📍 | -
    |           | [`TRACK`](<62 🗺️ TRACK prompt.md>) | 🗺️ | -
    

    ---
    <br/>


3. **How can Hosts protect users from input fatigue?**

    NLWeb advocates for [Hosts 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) to request as little [Prompts 🤔](<01 🤔 Prompt.md>) from users as possible;
    * instead, request users to share datasets using [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>);
    * e.g., ask to share the code `nlweb.org/BOOKING/CONTACTS` instead of asking for the name, then the phone number, then the email address, and so on.
  
    When [Prompts 🤔](<01 🤔 Prompt.md>) are inevitable, avoid text prompts; 
    * instead, prefer low-effort prompts;
    * e.g., searchable lists with one or many possible options.

    ---
    <br/>


3. **Can Hosts replace sent prompts?**

    Yes, but only temporary [Prompts 🤔](<01 🤔 Prompt.md>). 
    - If a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) sends  two consecutive blocking [Prompts 🤔](<01 🤔 Prompt.md>) while the user has not answered the first, then the first becomes readonly and the second becomes the active input.
    - If the [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) wants a [Prompts 🤔](<01 🤔 Prompt.md>) to be visually replaced, then they need to use a temporary [Prompts 🤔](<01 🤔 Prompt.md>), visually represented by an hourglass ⏳ emoji. 
    - This is particularly useful when [preparing food 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/53 🪑 Seat: Change order 🌀.md>), when [waiting food orders 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/82 🧑‍🍳 Chef: Prepare food 🥘.md>), and when reminding users of [upcoming bookings 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>).

    ---
    <br/>

4. **Can users respond to an old prompt?**

    NLWeb [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) are designed to be forward-only workloads managed by a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) (and not by the user). 
    * This behavior is visible on LLM apps like on ChatGPT, Gemini, and others. 
  
    Just like in the previously referred LLMs, NLWeb also allows [Host 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) to add options in certain steps so that users can go back and change the direction of the workload from a previous step.
    * For example, the user did A, B, C, D, E; then went back to B and changed the history to A, B, X, Y, Z. 
    * This worked because step B had an option set by the [Host 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) that allowed the user to go back and change the workflow path.

    In NLWeb, these option sets can be added only to non-blocking [Prompts 🤔](<01 🤔 Prompt.md>).

    - The non-blocking prompts include `TEMP ⏳`, `INFO ℹ️`, and `SUCCESS ✅`.
    - This is particularly helpful when [Host 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) want to assign default values to options to speed up the process (e.g., [navigation options 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/01 🧳 Plans trips 🧭/02 🧭 Return @ Destination.md>)), while still allowing users to go back and change those default options.
    
    ---
    <br/>
