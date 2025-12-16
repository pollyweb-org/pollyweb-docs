# 🆔 IDENTIFY ⌘ cmd

> About
* Implemented by the [`IDENTIFY` 📃 script](<🆔 IDENTIFY 📃 script.md>)

## FAQ

1. **How to use IDENTIFY with a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)?**

    ```yaml
    # With a token
    - VERIFY: $token
    - IDENTIFY: $token
    ```

    ---
    <br/>

1. **How to use IDENTIFY with an [Identity 🆔 domain](<../../../../50 🫥 Agent domains/Identities 🆔/🆔 Identity agent/🆔 Identity 🫥 agent.md>) biostamp?**

    ```yaml
    # With identity and biostamp
    - IDENTIFY:
        Identity: any-identity.dom
        Biostamp: <biostamp-uuid>
    ```

    ---
    <br/>