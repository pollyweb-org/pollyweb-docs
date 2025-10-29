# 🤔 Non-blocking status prompts 

> Part of [Prompts 🤔](<../🤔 Prompt.md>)

> Changes the default behavior of [Prompt with Options 🔘](<4 🔘 with Options.md>)

<br/> 

1. **What are non-blocking status prompts?**

    These are [Prompts 🤔](<../🤔 Prompt.md>) that don't wait for user input.

    ---
    <br/>

1. **What prompts are non-blocking?**
   
    | Format | Description
    |-|-
    | ℹ️ [`INFO`](<../🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) | General information.
    | ✅ [`SUCCESS`](<../🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>) | Success message.
    | ❌ [`FAILURE`](<../🤔📢 Prompt status/FAILURE ❌/FAILURE ❌ prompt.md>) | Failure message.
    
    ---
    <br/>



1. **What's an example of non-blocking prompts?**

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Any non-blocking status.
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 I'm blocking inputs, OK? [ Yes, No ] | > Yes
    |

    Here's the [Script 📃](<../../Talkers 😃/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>).
    
    ```yaml
    # 😃 Talker 
    - INFO|Any non-blocking status.
    - CONFIRM|I'm blocking inputs, OK?
    ```

    ---
    <br/>

1. **How do non-blocking options work?**
   
    Non-blocking status prompts support [`Options`](<4 🔘 with Options.md>).
    - If it contains [`Options`](<4 🔘 with Options.md>), then the user may click an option any time before or after the [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) sends other subsequent [Prompts 🤔](<../🤔 Prompt.md>).
    - See a full example at [Driver pick-up on pizza delivery 🛵](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/82 🛵 Driver: Pick-up.md>).
    
    ---
    <br/>


1. **What's an example of non-blocking options?**


    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ With options:<br/>- [ Cancel ] later <br>- [ Play ] music | > Cancel
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 I'm blocking, but  did <br/>   you know that you can still<br/>   go back and cancel? <br/> - [ Yes, I did ] <br/> - [ No, I didn't ]
    |

    Here's the [Script 📃](<../../Talkers 😃/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>).
    
    ```yaml
    # 😃 Talker

    💬 Example:
    # Non-blocking
    - INFO|With options >> $selected:
        Options: 
          - "[Cancel] later"
          - "[Play] music"

    # Deferred decision tree
    - CASE|{$selected}:
        $: ContinueProc
        Cancel: CancelProc
        Play: PlayProc

    ContinueProc:
    # Blocking
    - ONE: 
        Text: 
            I'm blocking, but did you 
            know that you can still go back 
            and cancel?
        Options:
            - Yes, I did
            - No, I didn't
    ```

    ---
    <br/>