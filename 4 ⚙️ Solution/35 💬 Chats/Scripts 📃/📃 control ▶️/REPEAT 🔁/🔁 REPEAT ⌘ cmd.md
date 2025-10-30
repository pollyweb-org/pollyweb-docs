# 😃🔁 Talker `REPEAT` flow 

> Part of [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>)

<br/>


1. **What's a REPEAT flow?**

    A `REPEAT` 🔁
    * is a flow [Command ⌘](<../../📃 basics/Command ⌘/⌘ Command.md>) 
    * that repeats it's enclosing [Script 📃](<../../📃 commands ⌘/Script 📃/📃 Script.md>) 
    * either always or only when confirmed.

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    - REPEAT|<statement>
    ```

    | Input| Purpose
    |-|-
    | `<statement>`| Optional message for a [CONFIRM 👍 prompt](<../../../Prompts 🤔/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>)
    
    ---
    <br/>


1. **What's an example of a REPEAT with a message?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🕙 Clock | ✅ The time is 09:01:26Z
    | 🕙 Clock | 😃 Check again? [Yes, No] | > Yes
    | 🕙 Clock | ✅ The time is 09:02:58Z
    | 🕙 Clock | 😃 Check again? [Yes, No] 
    |

    Here's the [Script 📃](<../../📃 commands ⌘/Script 📃/📃 Script.md>).


    ```yaml
    💬|Show time:
    - SUCCESS|The time is {.Now}.
    - REPEAT|Check again?
    ```

    Commands: [`.Now`](<../../📃 functions 🐍/🔩 {.Now}.md>) [`SUCCESS`](<../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>) [`REPEAT`](<🔁 REPEAT ⌘ cmd.md>)

    ---
    <br/>

1. **What's an example of a repeat without a message?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🕙 Clock | 😃 Want to know the time? [Yes, No] | > Yes
    | 🕙 Clock | ✅ The time is 09:01:26Z
    | 🕙 Clock | 😃 Want to know the time? [Yes, No] | > Yes
    | 🕙 Clock | ✅ The time is 09:02:58Z
    | 🕙 Clock | 😃 Want to know the time? [Yes, No] 
    |

    Here's the [Script 📃](<../../📃 commands ⌘/Script 📃/📃 Script.md>).

    ```yaml
    💬|Show time:
    - CONFIRM|Want to know the time? 
    - SUCCESS|The time is {.Now}.
    - REPEAT
    ```
    Commands: [`QUANTITY`](<../../../Prompts 🤔/🤔✏️ Prompt inputs/QUANTITY ↕️/QUANTITY ↕️ prompt.md>) [`SUCCESS`](<../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>) [`REPEAT`](<🔁 REPEAT ⌘ cmd.md>)
    
    ---
    <br/>



1. **How to build a simple shopping basket?**

    
    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [Order] a list of items | > Order
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 What's the item code?  | 🔢 123
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Added `Flower vase`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Add another? [Yes, No] | > Yes
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 What's the item code?  | 🔢 456
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Added `Safety box`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Add another? [Yes, No] | > No
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Here's your basket:<br/>- Flower vase <br>- Safety box
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Submit order? [Yes, No] | > Yes
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ Order submitted!
    |

    Here's the [Script 📃](<../../📃 commands ⌘/Script 📃/📃 Script.md>).


    ```yaml
    💬|[Order] a list of items:

    # Call the AddItems procedure
    - RUN|AddItems

    # Show the order summary
    - INFO|{OrderSummary}

    # Ask the user to confirm the submission
    - CONFIRM|Submit order?

    # Call the custom function 
    #   to pending submit the order 
    - EVAL|Submit 

    # Show the successful submission
    - SUCCESS|Order submitted!
    ````
    Commands: [`CONFIRM`](<../../../Prompts 🤔/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>)  [`INFO`](<../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)  [`RUN`](<../RUN ▶️/▶️ RUN ⌘ cmd.md>) [`SUCCESS`](<../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ```yaml
    📃 AddItems:

    # Ask the ser for a code
    - DIGITS| What's the item code? >> $code:
        
    # Call the custom function 
    #    to add it to the ERP 
    #    and get the description
    - EVAL| AddItem($code) >> $description:

    # Show the description to the user
    - INFO| Added `{$description}`

    # Repeat after the user confirms
    - REPEAT|Add another?
    ```
    Commands:  [`DIGITS`](<../../../Prompts 🤔/🤔✏️ Prompt inputs/DIGITS 🔢/DIGITS 🔢 prompt.md>) [`EVAL`](<../../📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`INFO`](<../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`REPEAT`](<🔁 REPEAT ⌘ cmd.md>) 

    ---
    <br/>

1. **How to build a simple game?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [ Play ] guess | > Play
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ You have 3 attempts.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Say a number from 1 to 9. | ↕️ 3
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ❌ You have 2 more tries.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Say a number from 1 to 9. | ↕️ 1
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ❌ It's your last try.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Say a number from 1 to 9. | ↕️ 7
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ You won! 🥳
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Play again? [Yes, No] | > Yes
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ You have 3 attempts.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Say a number from 1 to 9. | ...
    | ...|...|...
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ❌ You lost! 😮
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Play again? [Yes, No] | > No
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ OK, see you next time!
    | ⭐ [Rate](<../../../../50 🫥 Agent domains/Reviewers ⭐/⭐🫥 Reviewer agent.md>) | 🫥 Experience feedback? | ⭐ 5
    | [👀 Ads](<../../../../45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) | ⓘ Explore follow-ups: <br/>- [ #️⃣ Play Tic-Tac-Toe ] 
    |

    Here's the [Script 📃](<../../📃 commands ⌘/Script 📃/📃 Script.md>).

    ```yaml
    💬 Play guess:                      
    - EVAL|.Random(1,9) >> $target       # Set the target
    - INFO|You have 3 attempts.          # Inform the rules
    - EVAL >> $tries:                    # Reset the counter
        3
    - RUN|TryLoop >> $result             # Run the loop
    - CASE|$result:                      # Check the result
        Won: SUCCESS|You won! 🥳
        Lost: FAILURE|You lost! 😮
    - REPEAT|Play again?                 # Ask to play again
    - INFO|OK, see you next time!        # Exit the game
    - GOODBYE                            # Show ads

    TryLoop:      

    # Ask for a number between 1 and 9
    - QUANTITY >> $guess:
        Text: : Say a number from 1 to 9.   
        MinValue: 1
        MaxValue: 9

    # Compare the guess with the target
    - CASE|$guess:      
        # If matched, the user won.             
        $target: RETURN|Won
        # If not matched, then decrease the tries
        $: EVAL|{.Add($tries, -1)} >> $tries

    # Verify the number of tries.
    - CASE|$tries:               
        # If out of tries, the user lost.     
        0: RETURN|Lost
        # Last try.
        1: FAILURE|It's your last try.
        # Otherwise, try again.
        $: FAILURE|You have {$tries} more tries.

    # Try again.
    - REPEAT
    ```

    Commands: [`EVAL`](<../../📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`QUANTITY`](<../../../Prompts 🤔/🤔✏️ Prompt inputs/QUANTITY ↕️/QUANTITY ↕️ prompt.md>) [`REPEAT`](<🔁 REPEAT ⌘ cmd.md>) [`RETURN`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`CASE`](<../CASE ⏯️/⏯️ CASE ⌘ cmd.md>) 


    ---
    <br/>
