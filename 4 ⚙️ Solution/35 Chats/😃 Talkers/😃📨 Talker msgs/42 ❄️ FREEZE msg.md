# ❄️ Talker `FREEZE` command 

> Part of [Talker 😃](<../😃 Talker.md>)


<br/>


1. **What is a FREEZE command?**

    A `FREEZE` ❄️
    * is a flow [Command ⌘](<../😃🌊 Talker flow/10 ⌘ Command.md>) 
    * that freezes all previous [non-blocking Prompts 🤔](<../../🤔 Prompts/🤔📘 Prompt features/08 ⚠️ as Status.md>)
    * as described in the [Freeze ⏩ flow](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Freeze ❄️.md>).

    ---
    <br/>

1. **What's a use-case for FREEZE?**

    * [Book a table at a restaurant 🍽️](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    
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

    | Argument| Purpose
    |-|-
    | `{inputs}` | Object with the inputs to store.
    | `$inputs` | Placeholder with aggregated inputs.
    
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


    | [Command ⌘](<../😃🌊 Talker flow/10 ⌘ Command.md>) | Purpose
    |-|-
    | 📝 [`INFORM`](<41 📝 INFORM msg.md>) | Show user instructions and allow inputs.
    | 1️⃣ [`ONE`](<../../🤔 Prompts/7 ✏️ Input prompts/53 1️⃣ ONE prompt.md>) | Select an option, the day in this case.
    | 💼 [`SHARE`](<45 💼 SHARE msg.md>) | Get the user's booking contacts.
    | 👍 [`CONFIRM`](<../../🤔 Prompts/7 ✏️ Input prompts/31 👍 CONFIRM prompt.md>) | Pause to allow changing previous inputs.
    | ⬇️ [`EVAL`](<../😃🗃️ Talker data/20 ⬇️ EVAL flow.md>) | Save the booking.

    ---
    <br/>