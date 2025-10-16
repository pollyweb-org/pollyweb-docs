🤔 Prompt
===

> Part of a [Chat 💬](<../💬 Chats/💬 Chat.md>) 

<br/>

1. **What is a Prompt?**

    A [Prompt 🤔](<🤔 Prompt.md>) 
    * is a line in [Chat 💬](<../💬 Chats/💬 Chat.md>) 
    * with a question or information to the user
    * sent to a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) 
    * by a [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) 
    * via the [Prompt 🤗⏩🧑‍🦰](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) flow.

    ---
    <br/>



1. **What input formats can Hosts ask Wallets to render?**

    Similar to HTTP, on NLWeb the [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) servers request the [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to render the requested [Prompts 🤔](<🤔 Prompt.md>).

    * The supported [Prompt 🤔](<🤔 Prompt.md>) formats are as follow.

    |Behavior| Format 
    |-|-
    |[`Status`](<1 📘 Prompt features/08 ⚠️ as Status.md>)| [`ℹ️ INFO`](<4 ⚠️ Status prompts/21 ℹ️ INFO prompt.md>) [`⏳ TEMP`](<4 ⚠️ Status prompts/25 ⏳ TEMP prompt.md>) [`✅ SUCCESS`](<4 ⚠️ Status prompts/23 ✅ SUCCESS prompt.md>) [`❌ FAILURE`](<4 ⚠️ Status prompts/24 ❌ FAILURE prompt.md>)
    |[`Inputs`](<1 📘 Prompt features/09 ✏️ as Input.md>)| [`🔢 DIGITS`](<7 ✏️ Input prompts/44 🔢 DIGITS prompt.md>) [`↕️ QUANTITY`](<7 ✏️ Input prompts/42 ↕️ QUANTITY prompt.md>) [`💰 AMOUNT`](<7 ✏️ Input prompts/43 💰 AMOUNT prompt.md>) [`🔑 OTP`](<7 ✏️ Input prompts/57 🔑 OTP prompt.md>) [`⭐ RATE`](<7 ✏️ Input prompts/46 ⭐ RATE prompt.md>) 
    || [`👍 CONFIRM`](<7 ✏️ Input prompts/31 👍 CONFIRM prompt.md>) [`1️⃣ ONE`](<7 ✏️ Input prompts/53 1️⃣ ONE prompt.md>) [`🔢 MANY`](<7 ✏️ Input prompts/54 🔠 MANY prompt.md>) 
    || [`🕓 TIME`](<7 ✏️ Input prompts/62 🕓 TIME prompt.md>) [`📆 DATE`](<7 ✏️ Input prompts/61 📆 DATE prompt.md>) 
    || [`⬆️ UPLOAD`](<7 ✏️ Input prompts/81 ⬆️ UPLOAD prompt.md>)
    || [`🔠 TEXT`](<7 ✏️ Input prompts/32 🔠 TEXT prompt.md>) 
    || [`👤 IDENTIFY`](<7 ✏️ Input prompts/71 👤 IDENTIFY prompt.md>) [`🛒 EAN`](<7 ✏️ Input prompts/74 🛒 EAN prompt.md>) [`🔆 SCAN`](<7 ✏️ Input prompts/72 🔆 SCAN prompt.md>) [`🦋 TOUCH`](<7 ✏️ Input prompts/73 🦋 TOUCH prompt.md>) 
    |`Special`| [`📍 LOCATION`](<7 ✏️ Input prompts/91 📍 LOCATION prompt.md>) [`🗺️ TRACK`](<7 ✏️ Input prompts/92 🗺️ TRACK prompt.md>)


    ---
    <br/>


1. **Can Hosts replace sent prompts?**

    Yes, but only temporary [Prompts 🤔](<🤔 Prompt.md>). 
    - If a [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) sends  two consecutive blocking [Prompts 🤔](<🤔 Prompt.md>) while the user has not answered the first, then the first becomes readonly and the second becomes the active input.
    - If the [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) wants a [Prompts 🤔](<🤔 Prompt.md>) to be visually replaced, then they need to use a temporary [Prompts 🤔](<🤔 Prompt.md>), visually represented by an hourglass ⏳ emoji. 
    - This is particularly useful when [preparing food 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/53 🪑 Seat: Change order 🌀.md>), when [waiting food orders 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/82 🧑‍🍳 Chef: Prepare food 🥘.md>), and when reminding users of [upcoming bookings 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>).

    ---
    <br/>

1. **Can users change an answer to an answered prompt?**

    Yes, but that rewinds the flow.

    * [Chats 💬](<../💬 Chats/💬 Chat.md>) are designed to be forward-only workloads managed by a [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) (and not by the user). 
        * This behavior is similar to LLM apps like ChatGPT, Gemini, and others. 
        * Just like in ChatGPT, users to change answers to old [Prompts 🤔](<🤔 Prompt.md>).
        
    * For example:
        * a user can answer A, B, C, D, E; 
        * then go back to B and change the history to A, B, X, Y, Z;
        * as long as there was no [Freeze ❄️](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Freeze ❄️.md>) between B and E.
    
    * However, [Host 🤗 domains](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) can [Freeze ❄️](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Freeze ❄️.md>) a [Chat 💬](<../💬 Chats/💬 Chat.md>) until a certain checkpoint.
        * This blocks the user from changing any [Prompts 🤔](<🤔 Prompt.md>) up to that point.
        * [Hosts 🤗](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) to this when committing a transaction to a database with the inputs collected.
  
    * ⚠️ Note: [`Options`](<1 📘 Prompt features/04 🔘 with Options.md>) with a `§` open a new [Chat 💬](<../💬 Chats/💬 Chat.md>)  and are never frozen.

    ---
    <br/>
    

1. **What are features of Prompts?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<1 📘 Prompt features/03 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<1 📘 Prompt features/04 🔘 with Options.md>)  | Has options for users to select.
    | 📎 [`Appendix`](<1 📘 Prompt features/05 📎 with Appendix.md>)  | Has a PDF, PNG, or JPEG attachment.
    | ⚠️ [` Status`](<1 📘 Prompt features/08 ⚠️ as Status.md>) | Informs and continues the flow.
    | ✏️ [`Input`](<1 📘 Prompt features/09 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>