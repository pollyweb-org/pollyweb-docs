# 🤔🔘 Prompts with `Options`

> Part of [Prompts 🤔](<../../Chats 💬/🤔 Prompt.md>)

## FAQ

1. **What is a prompt with options?**

    Option-enabled prompts 
    * are [Prompts 🤔](<../../Chats 💬/🤔 Prompt.md>)
    * that allow users to select na option.

    ---
    <br/>


1. **Can prompt options be deferred?**
       
    Yes. 
    
    * [Prompt options](<4 🔘 with Options.md>) can be differed with [non-blocking status Prompts 🤔](<8 ⚠️ as Status.md>);
    
        * e.g., [`INFO`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>), [`TEMP`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/TEMP ⏳/TEMP ⏳ prompt.md>), [`SUCCESS`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>), and [`FAILURE`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAILURE ❌/FAILURE ❌ prompt.md>).
  
        * [Host 🤗 domains](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) speed-up [Chats 💬](<../../Chats 💬/💬 Chat.md>) by taking unilateral two-way-door decisions that can be reverted by users even after other [Prompts 🤔](<../../Chats 💬/🤔 Prompt.md>) have been sent.

        * For example, [Host 🤗 domains](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) may assign default values to options to speed up the process (e.g., [navigation options 🤝](<../../../../3 🤝 Use Cases/03 🧳 Travel/01 🧳 Plans trips 🧭/02 🧭 Return @ Destination.md>)), while still allowing users to go back and change those default options.

    
    --- 
    <br/>

1. **Do all prompt options behave the same way?**

    No. 
    * [`Options`](<4 🔘 with Options.md>) with a `§` sign 
        * open a new [Chat 💬](<../../Chats 💬/💬 Chat.md>)
        * even after a [Freeze ❄️](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Freeze 🤗⏩❄️/🤗 Freeze ⏩ flow.md>) command.
    * All others [`Options`](<4 🔘 with Options.md>)
        * continue the [Chat 💬](<../../Chats 💬/💬 Chat.md>)
        * and are disabled with a [Freeze ❄️](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Freeze 🤗⏩❄️/🤗 Freeze ⏩ flow.md>) command.
    
    ---
    <br/>


1. **What are the prompts with options?**

    |Behavior| [Prompt 🤔](<../../Chats 💬/🤔 Prompt.md>) 
    |-|-
    |[`Status`](<8 ⚠️ as Status.md>)| [`ℹ️ INFO`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`⏳ TEMP`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/TEMP ⏳/TEMP ⏳ prompt.md>) [`✅ SUCCESS`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>) [`❌ FAILURE`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAILURE ❌/FAILURE ❌ prompt.md>)
    |[`Inputs`](<9 ✏️ as Input.md>) | [`1️⃣ ONE`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`🔢 MANY`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/MANY 🔠/🔠 MANY ⌘ cmd.md>)  [`🔠 TEXT`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>) 

    ---
    <br/>





1. **What's the syntax for a [Script 📃](<../../Scripts 📃/Script 📃.md>)?**

    ```yaml
    # Simplest
    <PROMPT>|<text>|<options>
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<PROMPT>` | A [Prompt 🤔](<../../Chats 💬/🤔 Prompt.md>) format. | [`INFO`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`TEMP`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/TEMP ⏳/TEMP ⏳ prompt.md>)
    | `<text>` |  Message to show to the user. | `Hi!`
    | `<options>` | Comma-separated strings | `A,B,C`
    || or a comma-sep dictionary  | `1:A,2:B`
    || or a dictionary object  | `{1:A,2:B}`
    || or a list of objects | `{A:1},{A:2}`
    
    ```yaml
    # One-line
    <PROMPT>|<text>|<options> >> $selected
    ```

    | Input| Purpose | Example
    |-|-|-
    | `$selected` | Holder for the selection: | `$answer`
    || for string lists, returns the text | → `A` in `A,B,C`
    || for dictionaries, returns the key | → `1` in `{1:A}`
    || for object lists, the 1st property | → `1` in `[{K:1}]`
    
    ```yaml
    # Multi-line with a single options string
    <PROMPT> >> $selected:
        Text: <text>
        Options: <options>
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<text>` | Also allows interpolated strings. | `Hi {$name}!`
    | `<options>` | Also allows string array functions |`{f}` → `[A,B]`
    |           | and object functions | `{f}` → `{1:A}`
    |           | and object list functions | `{f}` → `[{K:1}]`
    
    ```yaml
    # Multi-line with multiple strings
    <PROMPT> >> $selected:
        Text: <text>
        Options:
            - <option-1>
            - <option-n>
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<option-n>` | Also allows option interpolation |`- Item {$id}`
    || and uses `/` to set Option IDs | `/Close chat`
    || and uses `§` for [Locators 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>). | `Open § {$url}`


    ```yaml
    # Multi-line with a dictionary
    <PROMPT> >> $selected:
        Text: <text>
        Options:
            <id-1>: <option-1>
            <id-n>: <option-n>
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<id-n>` | Also allows interpolated objects. | `- A: Item {$id}`
    
    
    ---
    <br/>



1. **What's an example in a [Chat 💬](<../../Chats 💬/💬 Chat.md>)?**

    > Note: [non-blocking status prompts ⚠️](<8 ⚠️ as Status.md>) behave slightly differently.

    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 What to do? <br>- [ Play ] music <br/>- [ Share ] list | > Play
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ You opted to play.
    |  

    Here's the [Script 📃](<../../Scripts 📃/Script 📃.md>).

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

    | [Command ⌘](<../../Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | 1️⃣ [`ONE`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) | To show the options.
    | ⏯️️ [`CASE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) | To check the selected option.
    | ℹ️ [`INFO`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) | To show the result.
    

    <br/> 

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>).

    ```yaml
    Format: ONE
    Emoji: 😃
    Text: What to do?
    Options: 
        - ID: Play
          Title: Play music 
        - ID: Share
          Title: Share list
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>).

    ```yaml
    Answer: Play
    ```

    ---
    <br/>



1. **What's a Locator example in a [Chat 💬](<../../Chats 💬/💬 Chat.md>)?**

    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 What to do?<br>- [ Play ] music <br/>- [ Share ] list <br/> - [ Speak ] with singer 🔆 | > Speak
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ Over to 👨‍🎤 Any Singer.
    | [ new chat ]
    | 🔎 [Finder](<../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Singer (4.4 ⭐) [+]
    | 👨‍🎤 Singer   | ℹ️ Received fan request.
    | 👨‍🎤 Singer  | 😃 Hi! What do you need?
    |

    The option with `§` 
    * opens a new [Chat 💬](<../../Chats 💬/💬 Chat.md>)
    * using the [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) `any-artist.dom/FANS`

    <br/>

    Here's the [Script 📃](<../../Scripts 📃/Script 📃.md>).

    
  
    ```yaml
    # 😃 Talker

    # Ask the question.
    - ONE:
        Text: What to do?
        Options:
            - /Play music 
            - /Share list
            - /Speak with singer § .HOST,any-artist.dom,fans

    # Check the answer.
    - CASE: 
        Play : INFO|You opted to play.
        Share: INFO|You choose to share.
        # [Speak] never gets here.
    ```


    | [Command ⌘](<../../Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | 1️⃣ [`ONE`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) | To show the options.
    | ⏯️️ [`CASE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) | To check the selected option.
    | ℹ️ [`INFO`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) | To show the result.
    
    <br/>

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>).
    * The `§` is split into the `Locator` property.
    
    ```yaml
    Format: ONE
    Emoji: 😃
    Text: What to do?
    Options: 
        - ID: Play
          Title: Play music 
        - ID: Share
          Title: Share list
        - ID: Speak                     
          Title: Speak with singer
          Locator: .HOST,any-artist.dom,fans
    ```

    ---
    <br/>