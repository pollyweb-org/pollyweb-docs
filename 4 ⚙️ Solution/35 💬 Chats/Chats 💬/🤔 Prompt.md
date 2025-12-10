🤔 Prompt
===

> Part of a [Chat 💬](<../Chats 💬/💬 Chat.md>) 

## FAQ

1. **What is a Prompt?**

    A [Prompt 🤔](<🤔 Prompt.md>) 
    * is a line in [Chat 💬](<../Chats 💬/💬 Chat.md>) 
    * with a question or information to the user
    * sent to a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
    * by a [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) 
    * with the [`Prompted@Host` 🚀 call](<../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>)
    * within the [Prompt 🤗⏩🧑‍🦰](<../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) flow.

    ---
    <br/>



1. **What input formats can Hosts ask Wallets to render?**

    Similar to HTTP, on NLWeb the [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) servers request the [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to render the requested [Prompts 🤔](<🤔 Prompt.md>).

    * The supported [Prompt 🤔](<🤔 Prompt.md>) formats are as follow.

    |Behavior| Format 
    |-|-
    |[`Status`](<../Prompts 🤔/🤔⚙️ Prompt features/8 ⚠️ as Status.md>)| [`ℹ️ INFO`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`⏳ TEMP`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/TEMP ⏳/TEMP ⏳ prompt.md>) [`✅ DONE`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`❌ FAIL`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>)
    |[`Inputs`](<../Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>)| [`🔢 DIGITS`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/DIGITS 🔢/🔢 DIGITS ⌘ cmd.md>) [`↕️ QUANTITY`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/QUANTITY ↕️/↕️ QUANTITY ⌘ cmd.md>) [`💰 AMOUNT`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/AMOUNT 💰/💰 AMOUNT ⌘ cmd.md>) [`🔑 OTP`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/OTP 🔑/🔑 OTP ⌘ cmd.md>) [`⭐ RATE`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/RATE ⭐/⭐ RATE ⌘ cmd.md>) 
    || [`👍 CONFIRM`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>) [`1️⃣ ONE`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/1️⃣ ONE ⌘ cmd.md>) [`🔢 MANY`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/MANY 🔠/🔠 MANY ⌘ cmd.md>) 
    || [`🕓 TIME`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TIME 🕓/🕓 TIME ⌘ cmd.md>) [`📆 DATE`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/DATE 📆/📆 DATE ⌘ cmd.md>) 
    || [`⬆️ UPLOAD`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/UPLOAD ⬆️/⬆️ UPLOAD ⌘ cmd.md>)
    || [`🔠 TEXT`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 💭/💭 TEXT ⌘ cmd.md>) 
    || [`👤 IDENTIFY`](<../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/IDENTIFY 🆔/🆔 IDENTIFY ⌘ cmd.md>) [`🛒 EAN`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/EAN 🛒/🛒 EAN ⌘ cmd.md>) [`🔆 SCAN`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/SCAN 🔆/🔆 SCAN ⌘ cmd.md>) [`🦋 TOUCH`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TOUCH 🦋/🦋 TOUCH ⌘ cmd.md>) 
    |`Special`| [`📍 LOCATION`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/LOCATION 📍/📍 LOCATION ⌘ cmd.md>) [`🗺️ TRACK`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TRACK 🗺️/🗺️ TRACK ⌘ cmd.md>)


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
  
    * ⚠️ Note: [`Options`](<../Prompts 🤔/🤔⚙️ Prompt features/4 🔘 with Options.md>) with a `§` open a new [Chat 💬](<../Chats 💬/💬 Chat.md>)  and are never frozen.

    ---
    <br/>
    

1. **What are features of Prompts?**

    | Feature | Details
    |-|-
    | 🪧 [`Text`](<../Prompts 🤔/🤔⚙️ Prompt features/2 🪧 Text.md>) | Mandatory prompt message
    | ⊕ [`Details`](<../Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details
    | 🔘 [`Options`](<../Prompts 🤔/🤔⚙️ Prompt features/4 🔘 with Options.md>)  | Has options for users to select
    | 🧡 [`Default`](<../Prompts 🤔/🤔⚙️ Prompt features/5 🧡 with Default.md>) | Pre-filled answer or highlighted [option](<../Prompts 🤔/🤔⚙️ Prompt features/4 🔘 with Options.md>)
    | 📎 [`Appendix`](<../Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>)  | Has a PDF, PNG, or JPEG attachment
    | ⚠️ [` Status`](<../Prompts 🤔/🤔⚙️ Prompt features/8 ⚠️ as Status.md>) | Informs and continues the flow
    | ✏️ [`Input`](<../Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>) | Waits for an answer from users
    
    ---
    <br/>