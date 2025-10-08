# 🤔 Non-blocking status prompts 

> Part of [Prompts 🤔](<01 🤔 Prompt.md>)

> Changes the default behavior of [Prompt with Options 🔘](<../../../9 😃 Talkers/Prompts/10 Prompt definitions/04 🤔🔘 with Options.md>)

<br/> 

1. **What are non-blocking status prompts?**

    These are [Prompts 🤔](<01 🤔 Prompt.md>) that don't wait for user input.

    ---
    <br/>

1. **What prompts are non-blocking?**
   
    | Format | Description
    |-|-
    | ℹ️ [`INFO`](<../../../9 😃 Talkers/Prompts/20 Status prompts/21 ℹ️ INFO prompt.md>) | General information.
    | ✅ [`SUCCESS`](<../../../9 😃 Talkers/Prompts/20 Status prompts/23 ✅ SUCCESS prompt.md>) | Success message.
    | ❌ [`FAILURE`](<24 ❌ FAILURE prompt.md>) | Failure message.
    
    ---
    <br/>



1. **What's an example of non-blocking prompts?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Any non-blocking status.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 I'm blocking inputs, OK? [ Yes, No ] | > Yes
    |

    Here's the [Talker 😃](<../../../9 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    # 😃 Talker 
    - INFO|Any non-blocking status.
    - CONFIRM|I'm blocking inputs, OK?
    ```

    ---
    <br/>

1. **How do non-blocking options work?**
   
    Non-blocking status prompts support [`Options`](<../../../9 😃 Talkers/Prompts/10 Prompt definitions/04 🤔🔘 with Options.md>).
    - If it contains [`Options`](<../../../9 😃 Talkers/Prompts/10 Prompt definitions/04 🤔🔘 with Options.md>), then the user may click an option any time before or after the [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) sends other subsequent [Prompts 🤔](<01 🤔 Prompt.md>).
    - See a full example at [Driver pick-up on pizza delivery 🛵](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/82 🛵 Driver: Pick-up.md>).
    
    ---
    <br/>


1. **What's an example of non-blocking options?**


    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ With options:<br/>- [ Cancel ] later <br>- [ Play ] music | > Cancel
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 I'm blocking, but  did <br/>   you know that you can still<br/>   go back and cancel? <br/> - [ Yes, I did ] <br/> - [ No, I didn't ]
    |

    Here's the [Talker 😃](<../../../9 😃 Talkers/01 😃 Talker.md>).
    
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
        Message: 
            I'm blocking, but did you 
            know that you can still go back 
            and cancel?
        Options:
            - Yes, I did
            - No, I didn't
    ```

    ---
    <br/>