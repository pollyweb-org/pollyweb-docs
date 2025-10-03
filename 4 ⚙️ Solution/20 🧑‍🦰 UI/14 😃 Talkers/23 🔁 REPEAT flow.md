# 🔁 Talker `REPEAT` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a REPEAT flow?**

    A `REPEAT` is a flow [Command](<10 Command.md>) that repeats it's enclosing [Procedure](<20 ⚙️ Procedure block.md>) if confirmed.

    ---
    <br/>

2. **What's the syntax?**

    ```yaml
    - REPEAT|<message>
    ```

    | Argument| Purpose
    |-|-
    | `<message>`| Optional message for a [CONFIRM 👍 prompt](<../13 🤔 Prompts/24 👍 CONFIRM prompt.md>)
    
    ---
    <br/>


3. **What's an example of a REPEAT with a message?**

    ```yaml
    💬|[Order] a list of items:
    - RUN|AddItems
    - SUCCESS|Order submitted!

    AddItems:
    - INT|What's the item code? >> code
    - REPEAT|Add another?
    ```

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [Order] a list of items | > Order
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the item code?  | 🔢 123
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Add another? [Yes, No] | > Yes
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the item code?  | 🔢 456
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Add another? [Yes, No] | > No
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Order submitted!

    ---
    <br/>

4. **What's an example of a repeat without a message?**



    ---
    <br/>

1. **How to build a simple game?**

    Used commands
    | Commands | Purpose
    |-|-
    | [`EVAL`](<12 🧠 EVAL command.md>)
    | [`CASE`](<22 🔀 CASE flow.md>)
    | [`RETURN`](<23 ⏪ RETURN flow.md>)
    | [`REPEAT`](<this file>)
    | [`SUCCESS`](<../13 🤔 Prompts/13 ✅ SUCCESS prompt.md>)
    | [`FAILURE`](<../13 🤔 Prompts/14 ❌ FAILURE prompt.md>)
    | [`GOODBYE`](<25 🛑 GOODBYE flow.md>)


    ```yaml
    💬 Play guess:                      
    - EVAL|{RandomInt(1,9)} >> target  # Set the target
    - INFO|You have 3 attempts.        # Inform the rules
    - EVAL|3 >> tries                  # Reset the counter
    - RUN|TryLoop >> result            # Run the loop
    - CASE|{$result}:                  # Check the result
        Won: SUCCESS|You won! 🥳
        Lost: FAILURE|You lost! 😮
    - REPEAT|Play again?               # Ask to play again
    - INFO|OK, see you next time!      # Exit the game
    - GOODBYE                          # Show ads

    TryLoop:      

    # Ask for a number between 1 and 9
    - QUANTITY|Say a number from 1 to 9? >> guess:   
        MinValue: 1
        MaxValue: 9

    # Compare the guess with the target
    - CASE|{$guess}:      
        # If matched, the user won.             
        {$target}: RETURN|Won
        # If not matched, then decrease the tries
        *: EVAL|{Subtract($tries, 1)} >> $tries

    # Verify the number of tries.
    - CASE|{$tries}:               
        # If out of tries, the user lost.     
        0: RETURN|Lost
        # Last try.
        1: FAILURE|It's your last try.
        # Otherwise, try again.
        *: FAILURE|You have {$tries} more tries.

    # Try again.
    - REPEAT
    ```

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [ Play ] guess | > Play
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You have 3 attempts.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Say a number from 1 to 9. | 🔄 3
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ❌ You have 2 more tries.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Say a number from 1 to 9. | 🔄 1
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ❌ It's your last try.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Say a number from 1 to 9. | 🔄 7
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ You won! 🥳
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Play again? [Yes, No] | > Yes
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You have 3 attempts.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Say a number from 1 to 9. | ...
    | ...|...|...
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ❌ You lost! 😮
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Play again? [Yes, No] | > No
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ OK, see you next time!
    | ⭐ [Rate](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | ⭐ 5
    | [👀 Ads](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) | ⓘ Explore follow-ups: <br/>- [ 🛍️ Reusable bottles at Greg's ] 
    
    ---
    <br/>
