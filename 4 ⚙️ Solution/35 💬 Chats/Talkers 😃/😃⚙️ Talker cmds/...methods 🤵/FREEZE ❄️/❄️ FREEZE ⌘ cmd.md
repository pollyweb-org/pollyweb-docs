# 😃❄️ Talker `FREEZE` command 

> Part of [Talker 😃](<../../../😃 Talker role.md>)


<br/>


1. **What is a FREEZE command?**

    A `FREEZE` ❄️
    * is a flow [Command ⌘](<../../../../Scripts 📃/...commands ⌘/Command ⌘/⌘ Command.md>) 
    * that freezes all previous [non-blocking Prompts 🤔](<../../../../Prompts 🤔/🤔⚙️ Prompt features/8 ⚠️ as Status.md>)
    * as described in the [Freeze ⏩ flow](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Freeze 🤗⏩❄️/🤗 Freeze ⏩ flow.md>).

    ---
    <br/>

1. **What's a use-case for FREEZE?**

    * [Book a table at a restaurant 🍽️](<../../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    
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

    Commands: [`CONFIRM`](<../../../../Prompts 🤔/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`EVAL`](<../../...holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`FREEZE`](<❄️ FREEZE ⌘ cmd.md>) [`GOODBYE`](<../GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) [`INFORM`](<../INFORM 📝/📝 INFORM ⌘ cmd.md>) [`ONE`](<../../../../Prompts 🤔/🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`SHARE`](<../SHARE 💼/💼 SHARE ⌘ cmd.md>) [`SUCCESS`](<../../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>