# 😃🔩 Talker {.IsSigned} function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ

1. **What is the .IsSigned function?**

    `{.IsSigned}` 
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that when given a {{Holder}}, a public key, and a signature,
    * checks if the content in the {{Holder}} was signed with the private key
    * corresponding to the given public key.

    ---
    <br/>

1. **What's the syntax of .IsSigned?**

    ```r
    .IsSigned(Holder, PublicKey, Signature)
    ```

    | Argument | Purpose |
    |-|-
    | `Holder` | {{Holder}} with the content to verify |
    | `PublicKey` | Public key in [PEM format](<https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail>) |
    | `Signature` | Signature in [Base64 format](<https://en.wikipedia.org/wiki/Base64>) |