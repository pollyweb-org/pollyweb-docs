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
       
    Yes, [prompt options](<04 🤔✨ with Options.md>) can be differed with [non-blocking status Prompts 🤔](<08 🤔✨ with Status behavior.md>).
    
    * [Host 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) can speed-up [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) by taking unilateral two-way-door decisions that can be reverted by users even after other [Prompts 🤔](<01 🤔 Prompt.md>) have been sent.

    * For example, [Host 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) may assign default values to options to speed up the process (e.g., [navigation options 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/01 🧳 Plans trips 🧭/02 🧭 Return @ Destination.md>)), while still allowing users to go back and change those default options.

    * [Hosts 🤗](<../12 💬 Chats/04 🤗🎭 Host role.md>) enable it with [non-blocking Prompts 🤔](<08 🤔✨ with Status behavior.md>) - e.g., [`INFO`](<11 ℹ️ INFO prompt.md>), [`TEMP`](<12 ⏳ TEMP prompt.md>), [`SUCCESS`](<13 ✅ SUCCESS prompt.md>), and [`FAILURE`](<14 ❌ FAILURE prompt.md>).
    
    * [Hosts 🤗](<../12 💬 Chats/04 🤗🎭 Host role.md>) disabled it with a [Freeze ❄️](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/06 🤗⏩🧑‍🦰 Freeze ❄️.md>) flow.
    
    ---
    <br/>


1. **What are the prompts with options?**

    |Behavior| [Prompt 🤔](<01 🤔 Prompt.md>) 
    |-|-
    |[`Status`](<08 🤔✨ with Status behavior.md>)| [`ℹ️ INFO`](<11 ℹ️ INFO prompt.md>) [`⏳ TEMP`](<12 ⏳ TEMP prompt.md>) [`✅ SUCCESS`](<13 ✅ SUCCESS prompt.md>) [`❌ FAILURE`](<14 ❌ FAILURE prompt.md>)
    |[`Inputs`](<09 🤔✨ with Input behavior.md>) | [`1️⃣ ONE`](<25 1️⃣ ONE prompt.md>) [`🔢 MANY`](<25 🔠 MANY prompt.md>)  [`🔠 TEXT`](<20 🔠 TEXT prompt.md>) 

    ---
    <br/>





1. **What's the format for a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    # One-line
    <PROMPT>|<message>|<options> >> $selected

    # Multi-line with a single options string
    <PROMPT> >> $selected:
        Message: <message>
        Options: <options>

    # Multi-line with multiple strings
    <PROMPT> >> $selected:
        Message: <message>
        Options:
            - <string-1>
            - <option-n>

    # Multi-line with a dictionary
    <PROMPT> >> $selected:
        Message: <message>
        Options:
            <id-1>: <option-1>
            <id-n>: <option-n>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<PROMPT>` | A [Prompt 🤔](<01 🤔 Prompt.md>) format. | `INFO` `TEMP`
    | `<message>` |  Message to show to the user. | `Hi!`
    | `<options>` | Optional comma-separated options. | `A,B,C`
    | `<option-n>` | Option text in lists and dictionaries. | `Bla`
    | `<id-n>` | Optional ID in an option dictionary. | `#1`
    | `$selected` | Placeholder for the selected option: <br> - for text lists, returns the text; <br/>- for dictionaries, returns the ID. | `$answer`
    
    
    ---
    <br/>



1. **What's an example in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ With options:<br/>- [ Cancel ] later <br>- [ Play ] music | > Cancel

    The related [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) is as follows.

    ```yaml
    # 😃 Talker
    INFO|With options >> $answer:
        Options:
            - [Cancel] later
            - [Play] music 
    ```


    ---
    <br/>


1. **What's the response in the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: <PROMPT>
    Message: <message>
    Options: <options>
    ```

    ---
    <br/>

1. **What's the Answer in the [`Reply@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    Answer: $selected # if any
    ```

    ---
    <br/>