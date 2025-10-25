# 🤔 Prompts with `Options`


> Part of [Prompts 🤔](<../🤔 Prompt.md>)

<br/>

1. **What is a prompt with options?**

    Option-enabled prompts 
    * are [Prompts 🤔](<../🤔 Prompt.md>)
    * that allow users to select na option.

    ---
    <br/>


1. **Can prompt options be deferred?**
       
    Yes. 
    
    * [Prompt options](<4 🔘 with Options.md>) can be differed with [non-blocking status Prompts 🤔](<8 ⚠️ as Status.md>);
    
        * e.g., [`INFO`](<../🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>), [`TEMP`](<../🤔📢 Prompt status/TEMP ⏳/TEMP ⏳ prompt.md>), [`SUCCESS`](<../🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>), and [`FAILURE`](<../🤔📢 Prompt status/FAILURE ❌/FAILURE ❌ prompt.md>).
  
        * [Host 🤗 domains](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) speed-up [Chats 💬](<../../💬 Chats/💬 Chat.md>) by taking unilateral two-way-door decisions that can be reverted by users even after other [Prompts 🤔](<../🤔 Prompt.md>) have been sent.

        * For example, [Host 🤗 domains](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) may assign default values to options to speed up the process (e.g., [navigation options 🤝](<../../../../3 🤝 Use Cases/03 🧳 Travel/01 🧳 Plans trips 🧭/02 🧭 Return @ Destination.md>)), while still allowing users to go back and change those default options.

    
    --- 
    <br/>

1. **Do all prompt options behave the same way?**

    No. 
    * [`Options`](<4 🔘 with Options.md>) with a `§` sign 
        * open a new [Chat 💬](<../../💬 Chats/💬 Chat.md>)
        * even after a [Freeze ❄️](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Freeze ❄️.md>) command.
    * All others [`Options`](<4 🔘 with Options.md>)
        * continue the [Chat 💬](<../../💬 Chats/💬 Chat.md>)
        * and are disabled with a [Freeze ❄️](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Freeze ❄️.md>) command.
    
    ---
    <br/>


1. **What are the prompts with options?**

    |Behavior| [Prompt 🤔](<../🤔 Prompt.md>) 
    |-|-
    |[`Status`](<8 ⚠️ as Status.md>)| [`ℹ️ INFO`](<../🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`⏳ TEMP`](<../🤔📢 Prompt status/TEMP ⏳/TEMP ⏳ prompt.md>) [`✅ SUCCESS`](<../🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>) [`❌ FAILURE`](<../🤔📢 Prompt status/FAILURE ❌/FAILURE ❌ prompt.md>)
    |[`Inputs`](<9 ✏️ as Input.md>) | [`1️⃣ ONE`](<../🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`🔢 MANY`](<../🤔✏️ Prompt inputs/MANY 🔠/MANY 🔠 prompt.md>)  [`🔠 TEXT`](<../🤔✏️ Prompt inputs/TEXT 🔠/TEXT 🔠 prompt.md>) 

    ---
    <br/>





1. **What's the format for a [Talker 😃](<../../😃 Talkers/😃 Talker role.md>)?**

    ```yaml
    # Simplest
    <PROMPT>|<statement>|<options>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<PROMPT>` | A [Prompt 🤔](<../🤔 Prompt.md>) format. | [`INFO`](<../🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`TEMP`](<../🤔📢 Prompt status/TEMP ⏳/TEMP ⏳ prompt.md>)
    | `<statement>` |  Message to show to the user. | `Hi!`
    | `<options>` | Comma-separated strings, or | `A,B,C`
    || a comma-separated dictionary | `1:A,2:B`
    
    ```yaml
    # One-line
    <PROMPT>|<statement>|<options> >> $selected
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `$selected` | Placeholder for the selection: | `$answer`
    || for string lists, returns the text | → `A` in `A,B,C`
    || for dictionaries, returns the ID. | → `1` in `{1:A}`
    
    ```yaml
    # Multi-line with a single options string
    <PROMPT> >> $selected:
        Statement: <statement>
        Options: <options>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<statement>` | Also allows interpolated strings. | `Hi {$name}!`
    | `<options>` | Also allows string array functions |`{f}` → `[A,B]`
    |           | and object functions. | `{f}` → `{1:A}`
    
    ```yaml
    # Multi-line with multiple strings
    <PROMPT> >> $selected:
        Statement: <statement>
        Options:
            - <option-1>
            - <option-n>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<option-n>` | Also allows option interpolation |`- Item {$id}`
    || and uses `/` to set Option IDs | `/Close chat`
    || and uses `§` for [Locators 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>). | `Open § {$url}`


    ```yaml
    # Multi-line with a dictionary
    <PROMPT> >> $selected:
        Statement: <statement>
        Options:
            <id-1>: <option-1>
            <id-n>: <option-n>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<id-n>` | Also allows interpolated objects. | `- A: Item {$id}`
    
    
    ---
    <br/>



1. **What's an example in a [Chat 💬](<../../💬 Chats/💬 Chat.md>)?**

    > Note: [non-blocking status prompts ⚠️](<8 ⚠️ as Status.md>) behave slightly differently.

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 What to do? <br>- [ Play ] music <br/>- [ Share ] list | > Play
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ You opted to play.
    |  

    Here's the [Talker 😃](<../../😃 Talkers/😃 Talker role.md>).

    ```yaml
    # 😃 Talker

    # Ask the question.
    - ONE|What to do?:
        Options:
            - /Play music 
            - /Share list

    # Check the answer.
    - CASE: # Default to last input.
        Play : INFO|You opted to play.
        Share: INFO|You choose to share.
    ```

    | [Command ⌘](<../../😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | Purpose
    |-|-
    | 1️⃣ [`ONE`](<../🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>) | To show the options.
    | ⏯️️ [`CASE`](<../../😃 Talkers/😃⚙️ Talker cmds/...control ▶️/CASE ⏯️/CASE ⏯️.md>) | To check the selected option.
    | ℹ️ [`INFO`](<../🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) | To show the result.
    

    <br/> 

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: ONE
    Statement: 😃 What to do?
    Options: 
        - ID: Play
          Title: Play music 
        - ID: Share
          Title: Share list
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: Play
    ```

    ---
    <br/>



1. **What's a Locator example in a [Chat 💬](<../../💬 Chats/💬 Chat.md>)?**

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 What to do?<br>- [ Play ] music <br/>- [ Share ] list <br/> - [ Speak ] with singer 🔆 | > Speak
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ Over to 👨‍🎤 Any Singer.
    | [ new chat ]
    | 🔎 [Finder](<../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) | ⓘ Any Singer (4.4 ⭐) [+]
    | 👨‍🎤 Singer   | ℹ️ Received fan request.
    | 👨‍🎤 Singer  | 😃 Hi! What do you need?
    |

    The option with `§` 
    * opens a new [Chat 💬](<../../💬 Chats/💬 Chat.md>)
    * using the [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) `any-artist.com/FANS`

    <br/>

    Here's the [Talker 😃](<../../😃 Talkers/😃 Talker role.md>).

    
  
    ```yaml
    # 😃 Talker

    # Ask the question.
    - ONE:
        Statement: What to do?
        Options:
            - /Play music 
            - /Share list
            - /Speak with singer § .HOST,any-artist.com,fans

    # Check the answer.
    - CASE: 
        Play : INFO|You opted to play.
        Share: INFO|You choose to share.
        # [Speak] never gets here.
    ```


    | [Command ⌘](<../../😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | Purpose
    |-|-
    | 1️⃣ [`ONE`](<../🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>) | To show the options.
    | ⏯️️ [`CASE`](<../../😃 Talkers/😃⚙️ Talker cmds/...control ▶️/CASE ⏯️/CASE ⏯️.md>) | To check the selected option.
    | ℹ️ [`INFO`](<../🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) | To show the result.
    
    <br/>

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>).
    * The `§` is split into the `Locator` property.
    
    ```yaml
    Format: ONE
    Statement: 😃 What to do?
    Options: 
        - ID: Play
          Title: Play music 
        - ID: Share
          Title: Share list
        - ID: Speak                     
          Title: Speak with singer
          Locator: .HOST,any-artist.com,fans
    ```

    ---
    <br/>