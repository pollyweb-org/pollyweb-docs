# 🔐 Talker `VERIFY` Token 🎫

> About
* Part of the [`VERIFY` ⌘ command](<../VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
* Implemented by the [`VERIFY-Token` 📃 script](<🔐 Token 📃 script.md>)

## FAQ

1. **What's the syntax for [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)?**

    ```yaml
    # Blocker version (raises error if invalid)
    - VERIFY $token 
    
    # Safe version (stores result in $isValid)
    - VERIFY $token >> $isValid
    ```

    | Input| Purpose |
    |-|-
    | `$token`| [Holder 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
    | `$isValid`| [Holder 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) that will store `true`/`false`.


    ---
    <br/>


