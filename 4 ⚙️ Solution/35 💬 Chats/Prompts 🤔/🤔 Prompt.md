🤔 Prompt
===

> Part of a [Chat 💬](<../Chats 💬/💬 Chat.md>) 

<br/>

1. **What is a Prompt?**

    A [Prompt 🤔](<🤔 Prompt.md>) 
    * is a line in [Chat 💬](<../Chats 💬/💬 Chat.md>) 
    * with a question or information to the user
    * sent to a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
    * by a [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) 
    * via the [Prompt 🤗⏩🧑‍🦰](<../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) flow.

    ---
    <br/>



1. **What input formats can Hosts ask Wallets to render?**

    Similar to HTTP, on NLWeb the [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) servers request the [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to render the requested [Prompts 🤔](<🤔 Prompt.md>).

    * The supported [Prompt 🤔](<🤔 Prompt.md>) formats are as follow.

    |Behavior| Format 
    |-|-
    |[`Status`](<🤔⚙️ Prompt features/8 ⚠️ as Status.md>)| [`ℹ️ INFO`](<🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`⏳ TEMP`](<🤔📢 Prompt status/TEMP ⏳/TEMP ⏳ prompt.md>) [`✅ SUCCESS`](<🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>) [`❌ FAILURE`](<🤔📢 Prompt status/FAILURE ❌/FAILURE ❌ prompt.md>)
    |[`Inputs`](<🤔⚙️ Prompt features/9 ✏️ as Input.md>)| [`🔢 DIGITS`](<🤔✏️ Prompt inputs/DIGITS 🔢/DIGITS 🔢 prompt.md>) [`↕️ QUANTITY`](<🤔✏️ Prompt inputs/QUANTITY ↕️/QUANTITY ↕️ prompt.md>) [`💰 AMOUNT`](<🤔✏️ Prompt inputs/AMOUNT 💰/AMOUNT 💰 prompt.md>) [`🔑 OTP`](<🤔✏️ Prompt inputs/OTP 🔑/OTP 🔑 prompt.md>) [`⭐ RATE`](<🤔✏️ Prompt inputs/RATE ⭐/RATE ⭐ prompt.md>) 
    || [`👍 CONFIRM`](<🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`1️⃣ ONE`](<🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`🔢 MANY`](<🤔✏️ Prompt inputs/MANY 🔠/🔠 MANY ⌘ cmd.md>) 
    || [`🕓 TIME`](<🤔✏️ Prompt inputs/TIME 🕓/TIME 🕓 prompt.md>) [`📆 DATE`](<🤔✏️ Prompt inputs/DATE 📆/DATE 📆 prompt.md>) 
    || [`⬆️ UPLOAD`](<🤔✏️ Prompt inputs/UPLOAD ⬆️/UPLOAD ⬆️ prompt.md>)
    || [`🔠 TEXT`](<🤔✏️ Prompt inputs/TEXT 🔠/TEXT 🔠 prompt.md>) 
    || [`👤 IDENTIFY`](<🤔✏️ Prompt inputs/IDENTIFY 👤/IDENTIFY 👤 prompt.md>) [`🛒 EAN`](<🤔✏️ Prompt inputs/EAN 🛒/EAN 🛒 prompt.md>) [`🔆 SCAN`](<🤔✏️ Prompt inputs/SCAN 🔆/SCAN 🔆 prompt.md>) [`🦋 TOUCH`](<🤔✏️ Prompt inputs/TOUCH 🦋/TOUCH 🦋 prompt.md>) 
    |`Special`| [`📍 LOCATION`](<🤔✏️ Prompt inputs/LOCATION 📍/LOCATION 📍 prompt.md>) [`🗺️ TRACK`](<🤔✏️ Prompt inputs/TRACK 🗺️/TRACK 🗺️ prompt.md>)


    ---
    <br/>


1. **Can Hosts replace sent prompts?**

    Yes, but only temporary [Prompts 🤔](<🤔 Prompt.md>). 
    - If a [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) sends  two consecutive blocking [Prompts 🤔](<🤔 Prompt.md>) while the user has not answered the first, then the first becomes readonly and the second becomes the active input.
    - If the [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) wants a [Prompts 🤔](<🤔 Prompt.md>) to be visually replaced, then they need to use a temporary [Prompts 🤔](<🤔 Prompt.md>), visually represented by an hourglass ⏳ emoji. 
    - This is particularly useful when [preparing food 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/53 🪑 Seat: Change order 🌀.md>), when [waiting food orders 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/82 🧑‍🍳 Chef: Prepare food 🥘.md>), and when reminding users of [upcoming bookings 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>).

    ---
    <br/>

1. **Can users change an answer to an answered prompt?**

    Yes, but that rewinds the flow.

    * [Chats 💬](<../Chats 💬/💬 Chat.md>) are designed to be forward-only workloads managed by a [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) (and not by the user). 
        * This behavior is similar to LLM apps like ChatGPT, Gemini, and others. 
        * Just like in ChatGPT, users to change answers to old [Prompts 🤔](<🤔 Prompt.md>).
        
    * For example:
        * a user can answer A, B, C, D, E; 
        * then go back to B and change the history to A, B, X, Y, Z;
        * as long as there was no [Freeze ❄️](<../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Freeze 🤗⏩❄️/🤗 Freeze ⏩ flow.md>) between B and E.
    
    * However, [Host 🤗 domains](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) can [Freeze ❄️](<../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Freeze 🤗⏩❄️/🤗 Freeze ⏩ flow.md>) a [Chat 💬](<../Chats 💬/💬 Chat.md>) until a certain checkpoint.
        * This blocks the user from changing any [Prompts 🤔](<🤔 Prompt.md>) up to that point.
        * [Hosts 🤗](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) to this when committing a transaction to a database with the inputs collected.
  
    * ⚠️ Note: [`Options`](<🤔⚙️ Prompt features/4 🔘 with Options.md>) with a `§` open a new [Chat 💬](<../Chats 💬/💬 Chat.md>)  and are never frozen.

    ---
    <br/>
    

1. **What are features of Prompts?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<🤔⚙️ Prompt features/4 🔘 with Options.md>)  | Has options for users to select.
    | 📎 [`Appendix`](<🤔⚙️ Prompt features/5 📎 with Appendix.md>)  | Has a PDF, PNG, or JPEG attachment.
    | ⚠️ [` Status`](<🤔⚙️ Prompt features/8 ⚠️ as Status.md>) | Informs and continues the flow.
    | ✏️ [`Input`](<🤔⚙️ Prompt features/9 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>