# 😃 Talker `TALK` command

> About
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* Works with the [`REGISTER`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/REGISTER 🔆/🔆 REGISTER ⌘ cmd.md>) and [`CHAT`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) commands
* Implemented by the [`TALK` 📃 script](<😃 TALK 📃 script.md>)

## FAQ

1. **What is the TALK command?**

    `TALK` 🔆
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that runs a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) registered on the [`Host.Talkers` 🪣 table](<../../🤗🪣 Host tables/Talkers 😃 table/Talkers 🪣/😃 Host.Talkers 🪣 table.md>)
    * to handle the [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) key in the [`$.Chat` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>)
    * after the invocation of the [`CHAT`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) command.

    ---
    <br/>

1. **What's the TALK syntax?**

    ```yaml
    # Comprehensive syntax
    TALK:
        Name: <name>
        Inputs: {inputs} 
    ```

    ```yaml
    # Simplified syntax
    TALK|<name>:
        {inputs} 
    ```
    
    |Input|Description|
    |-|-|
    | `Name` | Optional name of the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)
    | | Defaults to [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>).`Key`
    | | If omitted and [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`.IsEmpty`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsEmpty ⓕ.md>) then an error is raised
    | `Inputs` | Optional [Map 🧠](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) to pass to the [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) command

    ---
    <br/>