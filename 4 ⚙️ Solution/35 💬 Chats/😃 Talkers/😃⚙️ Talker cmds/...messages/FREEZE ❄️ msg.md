# 😃❄️ Talker `FREEZE` command 

> Part of [Talker 😃](<../../😃 Talker role.md>)


<br/>


1. **What is a FREEZE command?**

    A `FREEZE` ❄️
    * is a flow [Command ⌘](<../...commands/⌘ Command.md>) 
    * that freezes all previous [non-blocking Prompts 🤔](<../../../🤔 Prompts/🤔⚙️ Prompt features/8 ⚠️ as Status.md>)
    * as described in the [Freeze ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Freeze ❄️.md>).

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

    Commands: [`CONFIRM`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>) [`EVAL`](<../...placeholders/EVAL ⬇️ flow.md>) [`FREEZE`](<FREEZE ❄️ msg.md>) [`GOODBYE`](<GOODBYE 👋 msg.md>) [`INFORM`](<INFORM 📝 msg.md>) [`ONE`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/53 1️⃣ ONE prompt.md>) [`SHARE`](<SHARE 💼 msg.md>) [`SUCCESS`](<../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>)

    ---
    <br/>