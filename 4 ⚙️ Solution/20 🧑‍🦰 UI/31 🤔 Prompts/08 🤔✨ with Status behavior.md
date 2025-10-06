# 🤔 Non-blocking status prompts 

> Part of [Prompts 🤔](<01 🤔 Prompt.md>)

<br/> 

1. **What are non-blocking status prompts?**

    These are [Prompts 🤔](<01 🤔 Prompt.md>) that don't wait for user input.

    ---
    <br/>

1. **What prompts are non-blocking?**
   
    | Format | Description
    |-|-
    | ℹ️ [`INFO`](<11 ℹ️ INFO prompt.md>) | General information.
    | ⏳ [`TEMP`](<12 ⏳ TEMP prompt.md>)| Temporary message.
    | ✅ [`SUCCESS`](<13 ✅ SUCCESS prompt.md>) | Success message.
    | ❌ [`FAILURE`](<14 ❌ FAILURE prompt.md>) | Failure message.
    
    ---
    <br/>



1. **What's an example of non-blocking prompts?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Any non-blocking status.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 I'm blocking input, OK? [ Yes, No ] | > Yes
    |

    The related [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) is as follows.
    
    ```yaml
    INFO|Any non-blocking status.
    CONFIRM|I'm blocking input, OK?
    ```

    ---
    <br/>

1. **How do non-blocking options work?**
   
    Non-blocking status prompts support [`Options`](<04 🤔✨ with Options.md>).
    - If it contains [`Options`](<04 🤔✨ with Options.md>), then the user may click an option any time before or after the [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) sends other subsequent [Prompts 🤔](<01 🤔 Prompt.md>).
    - See a full example at [Driver pick-up on pizza delivery 🛵](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/82 🛵 Driver: Pick-up.md>).
    
    These options are not disabled with a [Freeze ❄️](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/06 🤗⏩🧑‍🦰 Freeze ❄️.md>) flow, and will continue to work.
    - This allows users to continue to retrieve outputs from previous transactions, like the details of a payment.
    - Thus, [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) should validate their replies with optimistic concurrency when necessary.

    Also, these non-blocking [`Options`](<04 🤔✨ with Options.md>) don't return from their [Procedure ⚙️](<../33 😃 Talkers/11 ⚙️ Procedure.md>) in a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    * This is because they have an independent workflow.
    * And because their parent workflow might have already ended.

    ---
    <br/>


1. **What's an example of non-blocking options?**


    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ With options:<br/>- [ Cancel ] later <br>- [ Play ] music | > Cancel
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 I'm blocking, but  did <br/>   you know that you can still<br/>   go back and cancel? <br/> - [ Yes, I did ] <br/> - [ No, I didn't ]
    |

    The related [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) is as follows.
    
    ```yaml
    # Non-blocking
    INFO|With options >> $input$:
        Options: 
            - [Cancel] later
            - [Play] music 

    # Blocking
    ONE: 
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