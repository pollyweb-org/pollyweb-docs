# 😃❄️ Talker `FREEZE` command 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)


<br/>


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
    # 😃 Talker 
    💬 Book something:
    
    # Instructions
    - INFORM|Book                           
    
    # Editable inputs
    - ONE|When?|Today,Tomorrow >> $date   # When?
    - SHARE|.PERSONA/BOOKING >> $contacts # Contacts?
    
    # Last chance to change the previous inputs.
    - CONFIRM|Confirm booking?  
    - FREEZE >> $inputs:
        Date: {$date}
        Contacts: {$contacts}

    # Save the booking
    - EVAL|SaveBooking($inputs)
    - SUCCESS|Done.
    - GOODBYE
    ```

    Uses: [`CONFIRM`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`EVAL`](<../../⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`FREEZE`](<❄️ FREEZE ⌘ cmd.md>) [`GOODBYE`](<../GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) [`INFORM`](<../INFORM 📝/📝 INFORM ⌘ cmd.md>) [`ONE`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`SHARE`](<../SHARE 💼/💼 SHARE ⌘ cmd.md>) [`SUCCESS`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>