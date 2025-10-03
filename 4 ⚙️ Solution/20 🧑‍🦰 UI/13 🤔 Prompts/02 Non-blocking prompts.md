# Non-blocking status prompts 🤔

> Part of [Prompts 🤔](<01 🤔 Prompt.md>)

<br/> 

1. **What are non-blocking status prompts?**

    These are [Prompts 🤔](<01 🤔 Prompt.md>) that don't wait for user input.

    ---
    <br/>

2. **What non-blocking prompts exist?**
   
    || Format | Description
    |-|-|-
    || [ℹ️&nbsp;INFO](<11 ℹ️ INFO prompt.md>) | General information.
    || [⏳&nbsp;TEMP](<12 ⏳ TEMP prompt.md>)| Temporary message.
    || [✅&nbsp;SUCCESS](<13 ✅ SUCCESS prompt.md>) | Success message.
    || [❌&nbsp;FAILURE](<14 ❌ FAILURE prompt.md>) | Failure message.
    
    ---
    <br/>

3. **How do non-blocking options work?**
   
    Non-blocking prompts support [ONE 1️⃣ prompt](<25 1️⃣ ONE prompt.md>) options.
    - If it contains options, then the user may click an option any time before or after the [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) sends other subsequent [Prompts 🤔](<01 🤔 Prompt.md>).
    - See a full example at [Driver pick-up on pizza delivery 🛵](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/82 🛵 Driver: Pick-up.md>).

    ---
    <br/>


4. **What's an example of non-blocking options?**

    ```yaml
    INFO|With options|[Cancel] later, [Play] music >> answer
    ```

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ With options:<br/>- [ Cancel ] later <br>- [ Play ] music | > Cancel
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 I'm blocking, but  did <br/>   you that you can still<br/>   go back and cancel? <br/> - [ Yes, I did ] <br/> - [ No, I didn't ]

    

    ---
    <br/>