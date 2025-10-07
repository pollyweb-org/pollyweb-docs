# 🔁 Talker `REPEAT` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a REPEAT flow?**

    A `REPEAT` 🔁
    * is a flow [Command ⌘](<10 ⌘ Command.md>) 
    * that repeats it's enclosing [Procedure ⚙️](<11 ⚙️ Procedure.md>) 
    * either always or only when confirmed.

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    - REPEAT|<message>
    ```

    | Argument| Purpose
    |-|-
    | `<message>`| Optional message for a [CONFIRM 👍 prompt](<../31 🤔 Prompts/31 👍 CONFIRM prompt.md>)
    
    ---
    <br/>


1. **What's an example of a REPEAT with a message?**


    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🕙 Clock | ✅ The time is 09:01:26Z
    | 🕙 Clock | 😃 Check again? [Yes, No] | > Yes
    | 🕙 Clock | ✅ The time is 09:02:58Z
    | 🕙 Clock | 😃 Check again? [Yes, No] 
    |

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).


    ```yaml
    💬|Show time:
    - SUCCESS|The time is {.Time}.
    - REPEAT|Check again?
    ```

    ---
    <br/>

1. **What's an example of a repeat without a message?**


    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🕙 Clock | 😃 Want to know the time? [Yes, No] | > Yes
    | 🕙 Clock | ✅ The time is 09:01:26Z
    | 🕙 Clock | 😃 Want to know the time? [Yes, No] | > Yes
    | 🕙 Clock | ✅ The time is 09:02:58Z
    | 🕙 Clock | 😃 Want to know the time? [Yes, No] 
    |

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).

    ```yaml
    💬|Show time:
    - CONFIRM|Want to know the time? 
    - SUCCESS|The time is {.Time}.
    - REPEAT
    ```

    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | 🔄 [`QUANTITY`](<../31 🤔 Prompts/42 🔄 QUANTITY prompt.md>) | To wait for user input.
    
    ---
    <br/>



1. **How to build a simple shopping basket?**

    
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [Order] a list of items | > Order
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the item code?  | 🔢 123
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Added `Flower vase`
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Add another? [Yes, No] | > Yes
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the item code?  | 🔢 456
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Added `Safety box`
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Add another? [Yes, No] | > No
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Here's your basket:<br/>- Flower vase <br>- Safety box
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Submit order? [Yes, No] | > Yes
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Order submitted!
    |

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).


    ```yaml
    💬|[Order] a list of items:
    - RUN|AddItems
    - INFO|{OrderSummary}
    - CONFIRM|Submit order?
    - SUCCESS|Order submitted!

    AddItems:
    - DIGITS|What's the item code? >> $code
    - EVAL|{AddItem($code)} >> $description
    - INFO|Added `{$description}`
    - REPEAT|Add another?
    ```


    Here's a list of flow commands used in the example.

    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | 👍 [`CONFIRM`](<../31 🤔 Prompts/31 👍 CONFIRM prompt.md>) | To wait for user confirmation.
    | ⬇️ [`EVAL`](<20 ⬇️ EVAL flow.md>) | To add an item to the database.

    ---
    <br/>

1. **How to build a simple game?**


    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
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
    | [👀 Ads](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) | ⓘ Explore follow-ups: <br/>- [ #️⃣ Play Tic-Tac-Toe ] 
    |

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).

    ```yaml
    💬 Play guess:                      
    - EVAL|{.RandomInt(1,9)} >> $target  # Set the target
    - INFO|You have 3 attempts.          # Inform the rules
    - EVAL|3 >> $tries                   # Reset the counter
    - RUN|TryLoop >> $result             # Run the loop
    - CASE|{$result}:                    # Check the result
        Won: SUCCESS|You won! 🥳
        Lost: FAILURE|You lost! 😮
    - REPEAT|Play again?                 # Ask to play again
    - INFO|OK, see you next time!        # Exit the game
    - GOODBYE                            # Show ads

    TryLoop:      

    # Ask for a number between 1 and 9
    - QUANTITY|Say a number from 1 to 9? >> $guess:   
        MinValue: 1
        MaxValue: 9

    # Compare the guess with the target
    - CASE|{$guess}:      
        # If matched, the user won.             
        {$target}: RETURN|Won
        # If not matched, then decrease the tries
        $: EVAL|{.Subtract($tries, 1)} >> $tries

    # Verify the number of tries.
    - CASE|{$tries}:               
        # If out of tries, the user lost.     
        0: RETURN|Lost
        # Last try.
        1: FAILURE|It's your last try.
        # Otherwise, try again.
        $: FAILURE|You have {$tries} more tries.

    # Try again.
    - REPEAT
    ```

    Here's a list of flow commands used in the example.

    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | ⬇️ [`EVAL`](<20 ⬇️ EVAL flow.md>) | To generate a random number a subtract tries.
    | 🔄 [`QUANTITY`](<../31 🤔 Prompts/42 🔄 QUANTITY prompt.md>) | To collect the number input.
    | 🔁 [`REPEAT`](<23 🔁 REPEAT flow.md>) | To allow for additional tries.
    | ↩️ [`RETURN`](<25 ↩️ RETURN flow.md>) | To return the result from the loop.
    | 🔀 [`CASE`](<22 🔀 CASE flow.md>) | To check the if the user won or lost.    


    ---
    <br/>
