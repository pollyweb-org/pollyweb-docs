# 😃ⓕ Talker `.IsSigned` function

> About
* Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
* Used by [`VERIFY`](<../../📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)

## FAQ


1. **What is the .IsSigned function?**

    `.IsSigned`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * to validate the signature of a payload with a public key
    * that returns `True` the signature is valid
    * or `False` otherwise.

    ---
    <br/>

1. **What's the syntax of .IsSigned?**

    ```yaml
    $payload.IsSigned:
        Signature: $signature
        PublicKey: $publicKey
    ```

    | Inputs     | Purpose                      | Examples                          |
    |-|-|-
    | `$payload`   | original data to verify  | `Hello!` `{A:1,B2}`
    | `$signature` | base64 signature to validate   | `...`|
    | `$publicKey` | base64 key for verification | `...` |