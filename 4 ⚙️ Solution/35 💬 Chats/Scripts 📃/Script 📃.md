# 😃📃 Talker `Script`

> Part of [Talker 😃](<../Talkers 😃/😃🤲 Talker helper.md>)

<br/>

1. **What's a Talker Script?**

    A [Script 📃]() 
    
    * is a set of [Commands ⌘](<Command ⌘.md>) 
    * specified in a [static YAML 📄](<../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Static YAML 📄.md>) resource
    * referencing [{Functions} 🐍](<Function 🐍.md>) evaluated by [Hosted 📦 domains](<../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>)
    * and implemented by [Hoster ☁️ helper domains](<../../45 🤲 Helper domains/Hosters ☁️/☁️ Hoster helper/☁️🤲 Hoster helper.md>).
    * for the purpose of rendering dialogs in a [💬 Chat](<../Chats 💬/💬 Chat.md>)

    ---
    <br/>

1. **What's the syntax of a Script?**
   
    ```yaml
    📃 <script>:
    - <command-1>
    - <command-n>
    ```

    | Input| Purpose
    |-|-
    | `📃 <script>` | The name of the [Script 📃](<Script 📃.md>).
    |            | The 📃 emoji is optional, and will be ignored.
    | `<command-n>` | A [Command ⌘](<Command ⌘.md>)  to be executed.
    
    ```yaml
    📃 TestScript:
    - INFO|Hi!
    - CONFIRM|Are you OK? >> $answer
    ```
    
    ---
    <br/>


1. **How to invoke a Script?**

    |Context|Syntax
    |-|-
    |▶️ [`RUN`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)| Calls a [Script 📃](<Script 📃.md>) by name, then returns.
    |⤵️ [`IF`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) | Runs [Scripts 📃](<Script 📃.md>) for `True` and `False` evaluations.
    | ⏯️️ [`CASE`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) | Runs [Scripts 📃](<Script 📃.md>) for matching evaluations.
    | 🧘 [`WAIT`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>) | Runs [Scripts 📃](<Script 📃.md>) on signalled and timed out.

    ---
    <br/>

1. **What's the syntax of a Script name?**

    No emojis nor special characters except dashes `-`, underscores `_`, and spaces ` `.
    * Emojis and special characters are reserved for current and future use.
    * Spaces are OK because only commas and pipes are used as separators.

    |Type|Example|
    |-|-
    |✅ Valid | `MyP` `My P` `myP` `my-p` `p2` `my_p`  `my--p` 
    |❌ Invalid | `{p}` `my$p` `$` `my-p!` `my/p` `my\|p` `my>p` `my,p` `👋`

    ---
    <br/>
