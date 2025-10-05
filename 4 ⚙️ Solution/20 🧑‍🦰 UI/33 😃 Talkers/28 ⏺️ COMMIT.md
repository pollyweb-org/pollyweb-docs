# ⏺️ Talker `COMMIT` command 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What is a COMMIT command?**

    A `COMMIT` ⏺️
    * is a flow [Command ⌘](<10 ⌘ Command.md>) 
    * that freezes all previous [non-blocking Prompts 🤔](<../31 🤔 Prompts/02 Non-blocking prompts.md>),
    * evaluates a [{Function}](<12 🐍 {Function}.md>) to save the inputs,
    * and runs a follow-up [Procedure ⚙️](<11 ⚙️ Procedure.md>) when evaluated.

    ---
    <br/>

1. **What's a use-case for COMMIT?**

    * [Book a table at a restaurant 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    
    ---
    <br/>

1. **What's the syntax of a COMMIT?**
   
    ```yaml
    - COMMIT|{function} >> $result: 
        Input: 
            {input-obj}
        OnFailure: <on-failure>
        OnSuccess: <on-success>
    ```


    | Argument| Purpose
    |-|-
    | `{function}`| [{Function}](<12 🐍 {Function}.md>) to be evaluated.
    | `{input-obj}` | Object with the inputs arguments to the function.
    | `$result` | Function output stored into a placeholder.
    | `<on-failure>`        | Run [Procedure ⚙️](<11 ⚙️ Procedure.md>) or [Command ⌘](<10 ⌘ Command.md>) on failure.
    | `<on-success>`        | Run [Procedure ⚙️](<11 ⚙️ Procedure.md>) or [Command ⌘](<10 ⌘ Command.md>) on success.

    ---
    <br/>

1. **What's an example for COMMIT?**

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

    # Freeze all previous inputs from here on.
    - COMMIT|{SaveBooking} >> $committed: 
        Input: 
            Date: $date
            Contacts: $contacts
        OnFailure: 
            - FAILURE|An error occurred.
        OnSuccess: 
            - SUCCESS|Done.
            - GOODBYE
    ```


    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | 📝 [`FORM`](<41 📝 FORM msg.md>) | Show user instructions and allow inputs.
    | 1️⃣ [`ONE`](<../31 🤔 Prompts/25 1️⃣ ONE prompt.md>) | Select an option, the day in this case.
    | 💼 [`SHARE`](<46 💼 SHARE msg.md>) | Get the user's booking contacts.
    | 👍 [`CONFIRM`](<../31 🤔 Prompts/24 👍 CONFIRM prompt.md>) | Pause to allow changing previous inputs.

    ---
    <br/>