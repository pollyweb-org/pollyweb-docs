# 🤔 Prompts with `Options`


> Part of [Prompts 🤔](<01 🤔 Prompt.md>)

<br/>

1. **What is a prompt with options?**

    Option-enabled prompts 
    * are [Prompts 🤔](<01 🤔 Prompt.md>)
    * that allow users to select na option.

    ---
    <br/>

1. **What are the prompts with options?**

    |Behavior| [Prompt 🤔](<01 🤔 Prompt.md>) 
    |-|-
    |[`Status`](<08 🤔 with Status behaviour.md>)| [`ℹ️ INFO`](<11 ℹ️ INFO prompt.md>) [`⏳ TEMP`](<12 ⏳ TEMP prompt.md>) [`✅ SUCCESS`](<13 ✅ SUCCESS prompt.md>) [`❌ FAILURE`](<14 ❌ FAILURE prompt.md>)
    |[`Inputs`](<09 🤔 with Input behaviour.md>) | [`1️⃣ ONE`](<25 1️⃣ ONE prompt.md>) [`🔢 MANY`](<25 🔠 MANY prompt.md>)  [`🔠 TEXT`](<20 🔠 TEXT prompt.md>) 

    ---
    <br/>





1. **What's the format for a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    # Inline
    <PROMPT>|<message>|<options> >> $selected

    # Multi-line with strings
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