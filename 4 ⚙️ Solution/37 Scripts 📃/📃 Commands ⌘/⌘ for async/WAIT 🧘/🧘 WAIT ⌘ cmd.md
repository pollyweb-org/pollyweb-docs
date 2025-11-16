# 😃🧘 Talker `WAIT` flow 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

> Used by
* [`Async` ⏩ flow](<../../../../35 💬 Chats/Talkers 😃/😃⏩ Talker flows/Run Async Tasks 😃⏩📦/😃 Async ⏩ flow.md>)

<br/>

## FAQ

1. **What's a WAIT flow command?**

    A [`WAIT` 🧘](<🧘 WAIT ⌘ cmd.md>)
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that pauses the flow for a period of time 
    * or until triggered by the [`REEL` 🎣 command](<../../⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>)
    * or by the [`Handled@Talker` 🅰️ method](<../../../../35 💬 Chats/Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>).

    ---
    <br/>


1. **What's the WAIT syntax?**

    
    ```yaml
    # Listen to two triggers in parallel: 
    #   a signal to a hook, or a timeout.

    - WAIT >> $response:
        Hook: $hook
        Timeout: <period>
    ```

    | Input| Purpose
    |-|-
    | `Timeout`  | Time to wait, evaluated by the [`.Add`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>) function
    | `Hook`   | For [`REEL` 🎣](<../../⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>) and [`Handled@Talker` 🅰️](<../../../../35 💬 Chats/Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>)
    | `$response` | Response from [`REEL` 🎣](<../../⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>) or [`Handled@Talker` 🅰️](<../../../../35 💬 Chats/Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>)

    ```yaml
    # Listen to only one trigger:
    #   either a timeout or a hook.

    - WAIT|<something> >> $result
    ```

    | Input| Purpose 
    |-|-
    | `<something>` | Either a `Timeout` or a `Hook`

    ---
    <br/>

1. **How to build a clock?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | 🕙 Clock | ⏳ It's 17:01
    | 🕙 Clock | ⏳ It's 17:02

    ```yaml
    # 😃 Talker 
    💬 Clock:
    - TEMP|It's {.Now}
    - WAIT|00:00:01 
    - REPEAT
    ```

    Uses: [`.Now`](<../../../📃 Holders 🧠/🧠 Input holders/Time/🧠🔩 .Now.md>) [`REPEAT`](<../../⌘ for control ▶️/REPEAT 🔁/🔁 REPEAT ⌘ cmd.md>) [`TEMP`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/TEMP ⏳/TEMP ⏳ prompt.md>) [`WAIT`](<🧘 WAIT ⌘ cmd.md>)
    

    
    ---
    <br/>



1. **How to wait for a task to complete?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | 🍕 Pizza | ℹ️ Order submitted 
    | 🍕 Pizza | ⏳ Step `1/3` Order in the queue...
    | 🍕 Pizza | ⏳ Step `2/3` Order being cooked...
    | 🍕 Pizza | ⏳ Step `3/3` Just finishing up...
    | 🍕 Pizza | ✅ Order ready!
    |

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    💬 Test:

    # Submit an async task
    - ASYNC|Submit >> $hook      

    # Inform the user about the submission
    - INFO|Order submitted       

    # Show the wait status
    - RUN|WaitForReady           

    # Inform the user that it's done
    - SUCCESS|Order ready!       
    ```
    Uses: [`ASYNC`](<../../⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>) [`RUN`](<../../⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`SUCCESS`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>) 
  
    ```yaml
    📃 WaitForReady:

    # Wait for the hook response
    - WAIT >> $status:           
        Hook: $hook

    # Check the response
    - IF|$status.Ready:          
        # End if ready
        Then: RETURN             
        
        # Show status otherwise
        Else: TEMP|$status.Message    

    # Repeat the script
    - REPEAT                     
    ```
    Uses: [`IF`](<../../⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`REPEAT`](<../../⌘ for control ▶️/REPEAT 🔁/🔁 REPEAT ⌘ cmd.md>) 
    [`TEMP`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/TEMP ⏳/TEMP ⏳ prompt.md>) [`WAIT`](<🧘 WAIT ⌘ cmd.md>)

    ---
    <br/>


1. **How to wait in a queue?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | 🏦 Bank | ⏳ There are 21 people ahead of you.
    | 🏦 Bank | ⏳ There are 7 people ahead of you.
    | 🏦 Bank | ⏳ You're next, get ready!
    | 🏦 Bank | 💬 What do you need? | `I need...`
    |

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    💬 Check-in:

    # Add the person to a waiting line
    - ASYNC|AddToLine >> $hook

    # Show line updates
    - RUN|WaitInLine

    # Finally, help the person
    - TEXT|What do you need?
    ```
    Uses: [`ASYNC`](<../../⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>) [`RUN`](<../../⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`TEXT`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>) 

    ```yaml
    📃 WaitInLine:

    # Check the status of the queue.
    - READ >> $len:
        Set: Queues
        Key: MyQueue

    # Show the status in a human-friendly wait.
    - CASE|$len:
        $: TEMP|There are {$len} people ahead of you.
        1: TEMP|You're next, get ready!
        0: RETURN
    
    # Wait 1 minute or until signalled.
    - WAIT >> $ready:
        Hook: $hook
        Timeout: 00:01:00

    # Jump off if signalled.
    - IF|$ready:
        RETURN

    # Check the queue length again.
    - REPEAT
    ```
    Uses: [`CASE`](<../../⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`READ`](<../../⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`IF`](<../../⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`REPEAT`](<../../⌘ for control ▶️/REPEAT 🔁/🔁 REPEAT ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/REPEAT 🔁/🔁 REPEAT ⌘ cmd.md>) [`TEMP`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/TEMP ⏳/TEMP ⏳ prompt.md>) [`WAIT`](<🧘 WAIT ⌘ cmd.md>)

    ---
    <br/>
