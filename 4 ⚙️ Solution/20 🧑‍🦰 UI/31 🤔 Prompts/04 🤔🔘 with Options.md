# 🤔 Prompts with `Options`


> Part of [Prompts 🤔](<01 🤔 Prompt.md>)

<br/>

1. **What is a prompt with options?**

    Option-enabled prompts 
    * are [Prompts 🤔](<01 🤔 Prompt.md>)
    * that allow users to select na option.

    ---
    <br/>


1. **Can prompt options be deferred?**
       
    Yes. 
    
    * [Prompt options](<04 🤔🔘 with Options.md>) can be differed with [non-blocking status Prompts 🤔](<08 🤔⚠️ with Status behavior.md>);
    
        * e.g., [`INFO`](<21 ℹ️ INFO prompt.md>), [`TEMP`](<22 ⏳ TEMP prompt.md>), [`SUCCESS`](<23 ✅ SUCCESS prompt.md>), and [`FAILURE`](<24 ❌ FAILURE prompt.md>).
  
        * [Host 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) speed-up [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) by taking unilateral two-way-door decisions that can be reverted by users even after other [Prompts 🤔](<01 🤔 Prompt.md>) have been sent.

        * For example, [Host 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) may assign default values to options to speed up the process (e.g., [navigation options 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/01 🧳 Plans trips 🧭/02 🧭 Return @ Destination.md>)), while still allowing users to go back and change those default options.

    
    --- 
    <br/>

1. **Do all prompt options behave the same way?**

    No. 
    * [`Options`](<04 🤔🔘 with Options.md>) with a `§` sign 
        * open a new [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)
        * even after a [Freeze ❄️](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/06 🤗⏩🧑‍🦰 Freeze ❄️.md>) command.
    * All others [`Options`](<04 🤔🔘 with Options.md>)
        * continue the [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)
        * and are disabled with a [Freeze ❄️](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/06 🤗⏩🧑‍🦰 Freeze ❄️.md>) command.
    
    ---
    <br/>


1. **What are the prompts with options?**

    |Behavior| [Prompt 🤔](<01 🤔 Prompt.md>) 
    |-|-
    |[`Status`](<08 🤔⚠️ with Status behavior.md>)| [`ℹ️ INFO`](<21 ℹ️ INFO prompt.md>) [`⏳ TEMP`](<22 ⏳ TEMP prompt.md>) [`✅ SUCCESS`](<23 ✅ SUCCESS prompt.md>) [`❌ FAILURE`](<24 ❌ FAILURE prompt.md>)
    |[`Inputs`](<11 ✏️ Input behavior.md>) | [`1️⃣ ONE`](<55 1️⃣ ONE prompt.md>) [`🔢 MANY`](<54 🔠 MANY prompt.md>)  [`🔠 TEXT`](<32 🔠 TEXT prompt.md>) 

    ---
    <br/>





1. **What's the format for a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    # One-line
    <PROMPT>|<message>|<options> >> $selected
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<PROMPT>` | A [Prompt 🤔](<01 🤔 Prompt.md>) format. | [`INFO`](<21 ℹ️ INFO prompt.md>) [`TEMP`](<22 ⏳ TEMP prompt.md>)
    | `<message>` |  Message to show to the user. | `Hi!`
    | `<options>` | Comma-separated strings | `A,B,C`
    || or comma-separated dictionary. | `1:A,2:B`
    | `$selected` | Placeholder for the selected option: | `$answer`
    || for string lists, returns the text | → `A` in `A,B,C`
    || for dictionaries, returns the ID. | → `1` in `{1:A}`
    
    ```yaml
    # Multi-line with a single options string
    <PROMPT> >> $selected:
        Message: <message>
        Options: <options>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<message>` | Also allows interpolated strings. | `Hi {$name}!`
    | `<options>` | Also allows string array functions |`{f}` → `[A,B]`
    |           | and object functions. | `{f}` → `{1:A}`
    
    ```yaml
    # Multi-line with multiple strings
    <PROMPT> >> $selected:
        Message: <message>
        Options:
            - <option-1>
            - <option-n>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<option-n>` | Also allows option interpolation |`- Item {$id}`
    || and uses `[]` to highlight words | `[Close] chat`
    || and uses `§` for [Locators 🔆](<../11 🔆 Locators/01 🔆 Locator.md>). | `Open § {$url}`


    ```yaml
    # Multi-line with a dictionary
    <PROMPT> >> $selected:
        Message: <message>
        Options:
            <id-1>: <option-1>
            <id-n>: <option-n>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<id-n>` | Also allows interpolated objects. | `- A: Item {$id}`
    
    
    ---
    <br/>



1. **What's an example in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What to do? <br>- [ Play ] music <br/>- [ Share ] list | > Play
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You opted to play.
    |  

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).

    ```yaml
    # 😃 Talker

    # Ask the question.
    ONE|What to do? >> $answer:
        Options:
            - [Play] music 
            - [Share] list

    # Check the answer.
    CASE|$answer:
        Play : INFO|You opted to play.
        Share: INFO|You choose to share.
    ```


    <br/> 

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) response.

    ```yaml
    Format: ONE
    Message: 😃 What to do?
    Options: 
        - ID: Play
          Translation: Play music 
        - ID: Share
          Translation: Share list
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: Play
    ```

    ---
    <br/>



1. **What's a Locator example in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What to do?<br>- [ Play ] music <br/>- [ Share ] list <br/> - [ Speak ] with singer 🔆 | > Speak
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Over to 👨‍🎤 Any Singer.
    | [ new chat ]
    | 🔎 [Finder](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Singer (4.4 ⭐) [+]
    | 👨‍🎤 Singer   | ℹ️ Received fan request.
    | 👨‍🎤 Singer  | 😃 Hi! What do you need?
    |

    The option with `§` 
    * opens a new [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)
    * using the [Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>) `any-artist.com/FANS`

    <br/>

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).

    
  
    ```yaml
    # 😃 Talker

    # Ask the question.
    ONE|What to do? >> $answer:
        Options:
            - [Play] music 
            - [Share] list
            - [Speak] with singer § any-artist.com/FANS

    # Check the answer.
    CASE|$answer:
        Play : INFO|You opted to play.
        Share: INFO|You choose to share.
        # [Speak] never gets here.
    ```

    


    ---
    <br/>