🤔 Prompt FAQ
===

> Part of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) 

<br/>

1. **What is a Prompt?**

    A [Prompt 🤔](<01 🤔 Prompt.md>) 
    * is a line in [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) 
    * with a question or information to the user
    * sent to a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) 
    * by a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) 
    * via the [Prompt 🤗⏩🧑‍🦰](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) flow.

    ---
    <br/>



1. **What input formats can Hosts ask Wallets to render?**

    Similar to HTTP, on NLWeb the [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) servers request the [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to render the requested [Prompts 🤔](<01 🤔 Prompt.md>).

    * The supported [Prompt 🤔](<01 🤔 Prompt.md>) formats are as follow.

    |Behavior| Format 
    |-|-
    |[`Status`](<08 🤔✨ with Status behavior.md>)| [`ℹ️ INFO`](<11 ℹ️ INFO prompt.md>) [`⏳ TEMP`](<12 ⏳ TEMP prompt.md>) [`✅ SUCCESS`](<13 ✅ SUCCESS prompt.md>) [`❌ FAILURE`](<14 ❌ FAILURE prompt.md>)
    |[`Inputs`](<09 🤔✨ with Input behavior.md>)| [`🔢 INT`](<21 🔢 INT prompt.md>) [`🔄 QUANTITY`](<21 🔄 QUANTITY prompt.md>) [`💰 AMOUNT`](<22 💰 AMOUNT prompt.md>) [`🔑 OTP`](<21 🔑 OTP prompt.md>) [`⭐ RATE`](<26 ⭐ RATE prompt.md>) 
    || [`👍 CONFIRM`](<10 👍 CONFIRM prompt.md>) [`1️⃣ ONE`](<25 1️⃣ ONE prompt.md>) [`🔢 MANY`](<25 🔠 MANY prompt.md>) 
    || [`🕓 TIME`](<27 🕓 TIME prompt.md>) [`📆 DATE`](<27 📆 DATE prompt.md>) 
    || [`⬆️ UPLOAD`](<51 ⬆️ UPLOAD prompt.md>)
    || [`🔠 TEXT`](<20 🔠 TEXT prompt.md>) 
    || [`👤 IDENTIFY`](<41 👤 IDENTIFY prompt.md>) [`🛒 EAN`](<44 🛒 EAN prompt.md>) [`🔆 SCAN`](<42 🔆 SCAN prompt.md>) [`🦋 TOUCH`](<43 🦋 TOUCH prompt.md>) 
    |`Special`| [`📍 LOCATION`](<61 📍 LOCATION prompt.md>) [`🗺️ TRACK`](<62 🗺️ TRACK prompt.md>)


    ---
    <br/>


1. **Can Hosts replace sent prompts?**

    Yes, but only temporary [Prompts 🤔](<01 🤔 Prompt.md>). 
    - If a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) sends  two consecutive blocking [Prompts 🤔](<01 🤔 Prompt.md>) while the user has not answered the first, then the first becomes readonly and the second becomes the active input.
    - If the [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) wants a [Prompts 🤔](<01 🤔 Prompt.md>) to be visually replaced, then they need to use a temporary [Prompts 🤔](<01 🤔 Prompt.md>), visually represented by an hourglass ⏳ emoji. 
    - This is particularly useful when [preparing food 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/53 🪑 Seat: Change order 🌀.md>), when [waiting food orders 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/82 🧑‍🍳 Chef: Prepare food 🥘.md>), and when reminding users of [upcoming bookings 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>).

    ---
    <br/>

1. **Can users change an answer to an answered prompt?**

    Yes, but that rewinds the flow.

    * [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) are designed to be forward-only workloads managed by a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) (and not by the user). 
        * This behavior is similar to LLM apps like ChatGPT, Gemini, and others. 
        * Just like in ChatGPT, users to change answers to old [Prompts 🤔](<01 🤔 Prompt.md>).
        
    * For example:
        * a user can answer A, B, C, D, E; 
        * then go back to B and change the history to A, B, X, Y, Z;
        * as long as there was no [Freeze ❄️](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/06 🤗⏩🧑‍🦰 Freeze ❄️.md>) between B and E.
    
    * However, [Host 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) can [Freeze ❄️](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/06 🤗⏩🧑‍🦰 Freeze ❄️.md>) a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) until a certain checkpoint.
        * This blocks the user from changing any [Prompts 🤔](<01 🤔 Prompt.md>) up to that point.
        * [Hosts 🤗](<../12 💬 Chats/04 🤗🎭 Host role.md>) to this when committing a transaction to a database with the inputs collected.
  
    * ⚠️ Note: [`Options`](<04 🤔✨ with Options.md>) with a `§` open a new [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)  and are never frozen.

    ---
    <br/>
    

1. **What are features of Prompts?**

    | Feature | Details
    |-|-
    | [`Details`](<03 🤔✨ with Details.md>) | Has expandable [+] details.
    | [`Options`](<04 🤔✨ with Options.md>) | Has options for users to select.
    | [`Attachment 📎`](<05 🤔📎 with Attachments.md>) | Has a PDF, PNG, or JPEG attachment.
    | [`Status` behavior](<08 🤔✨ with Status behavior.md>) | Informs and continues the flow.
    | [`Input` behavior](<09 🤔✨ with Input behavior.md>) | Waits for an answer from users.
    
    ---
    <br/>