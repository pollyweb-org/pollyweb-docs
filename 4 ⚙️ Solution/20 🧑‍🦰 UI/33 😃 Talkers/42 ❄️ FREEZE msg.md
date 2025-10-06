# ❄️ Talker `FREEZE` command 

> Part of [Talker 😃](<01 😃 Talker.md>)

> Related to [🤗⏩🧑‍🦰 Freeze ❄️](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/06 🤗⏩🧑‍🦰 Freeze ❄️.md>) flow

<br/>


1. **What is a FREEZE command?**

    A `FREEZE` ❄️
    * is a flow [Command ⌘](<10 ⌘ Command.md>) 
    * that freezes all previous [non-blocking Prompts 🤔](<../31 🤔 Prompts/08 🤔✨ with Status behavior.md>).

    ---
    <br/>

1. **What's a use-case for FREEZE?**

    * [Book a table at a restaurant 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    
    ---
    <br/>

1. **What's the syntax of a FREEZE?**
   
    ```yaml
    - FREEZE >> $inputs: 
        {inputs}
    ```


    | Argument| Purpose
    |-|-
    | `{inputs}` | Object with the inputs to store.
    | `$inputs` | Placeholder with aggregated inputs.
    
    ---
    <br/>

1. **What's an example for FREEZE?**

    ```yaml
    # 😃 Talker 
    💬 Book something:
    
    # Instructions
    - FORM|Book                           
    
    # Editable inputs
    - ONE|When?|Today,Tomorrow >> $date   # When?
    - SHARE|@PERSONA/BOOKING >> $contacts # Contacts?
    
    # Last chance to change the previous inputs.
    - CONFIRM|Confirm booking?  
    - FREEZE >> $inputs:
        Date: $date
        Contacts: $contacts

    # Save the booking
    - EVAL|{SaveBooking($inputs)}
    - SUCCESS|Done.
    - GOODBYE
    ```


    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | 📝 [`FORM`](<41 📝 FORM msg.md>) | Show user instructions and allow inputs.
    | 1️⃣ [`ONE`](<../31 🤔 Prompts/25 1️⃣ ONE prompt.md>) | Select an option, the day in this case.
    | 💼 [`SHARE`](<45 💼 SHARE msg.md>) | Get the user's booking contacts.
    | 👍 [`CONFIRM`](<../31 🤔 Prompts/10 👍 CONFIRM prompt.md>) | Pause to allow changing previous inputs.
    | ⬇️ [`EVAL`](<20 ⬇️ EVAL flow.md>) | Save the booking.

    ---
    <br/>