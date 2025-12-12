# 😃❄️ Talker `FREEZE` command 

> About
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ

1. **What is a FREEZE command?**

    A `FREEZE` ❄️
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that freezes all previous [non-blocking Prompts 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/8 ⚠️ as Status.md>)
    * as described in the [Freeze ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Freeze 🤗⏩❄️/🤗 Freeze ⏩ flow.md>).

    ---
    <br/>

1. **What's a use-case for FREEZE?**

    * [Book a table at a restaurant 🍽️](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    
    ---
    <br/>

1. **What's the syntax of a FREEZE?**

    ```yaml
    # Simplest
    - FREEZE
    ```

    ```yaml
    # Comprehensive
    - FREEZE >> $inputs: 
        {inputs}
    ```

    | Input| Purpose
    |-|-
    | `{inputs}` | Object with the inputs to store.
    | `$inputs` | Holder with aggregated inputs.
    
    ---
    <br/>

1. **What's an example of FREEZE?**

    ```yaml
    💬 Book something:
    
    # Instructions
    - INFORM Book                           
    
    # Editable inputs
    - ONE When?|Today,Tomorrow >> $date   # When?
    - SHARE .PERSONA/BOOKING >> $contacts # Contacts?
    
    # Last chance to change the previous inputs.
    - CONFIRM Confirm booking?  
    - FREEZE >> $inputs:
        Date: {$date}
        Contacts: {$contacts}

    # Save the booking
    - CALL SaveBooking($inputs)
    - DONE: Done.
    - GOODBYE
    ```

    Uses: [`CONFIRM`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>) [`CALL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`FREEZE`](<❄️ FREEZE ⌘ cmd.md>) [`GOODBYE`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) [`INFORM`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) [`ONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/1️⃣ ONE ⌘ cmd.md>) [`SHARE`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/SHARE 💼/💼 SHARE ⌘ cmd.md>) [`DONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)

    ---
    <br/>