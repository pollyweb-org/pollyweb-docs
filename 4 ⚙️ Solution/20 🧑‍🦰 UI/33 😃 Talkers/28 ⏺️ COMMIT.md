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


1. **What's an example for COMMIT?**

    ```yaml
    # Get the booking.
    - SHARE|nlweb.org/SCHEDULER/BOOK >> $b
        Context: 
            About: {/info/{$r.ID}.md} # Get the file.
            Slots: {Slots($r.ID)}     # From the ERP.

    # Get Contacts.
    - SHARE|nlweb.org/PERSONA/BOOKING >> $c

    # Get preferences
    - SHARE|nlweb.org/PERSONA/SEAT/PREFERENCES >> $p

    # Commit the booking
    - CONFIRM|Confirm booking?
    - COMMIT|{Confirm} >> $committed: 
        Input: 
            Restaurant: $r
            Booking: $b
            Contacts: $c
            Preferences: $p
        OnFailure: Failure
        OnSuccess: Success

    Failure:
    - FAILURE|An error occurred.
        
    Success:
    # Issue token
    - OFFER|{$committed.token}
    - SUCCESS|Done. See you then!
    - GOODBYE
    ```

    ---
    <br/>