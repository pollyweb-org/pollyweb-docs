# 😃ⓕ Talker `.Signs` function

> About
* Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
* Used by [`VERIFY`](<../../📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)

## FAQ


1. **What is the .Signs function?**

    `.Signs`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * to validate the signature of a payload with a public key
    * that returns `True` the signature is valid
    * or `False` otherwise.

    ---
    <br/>

1. **What's the syntax of .Signs?**

    ```yaml
    $signature.Signs:
        Data: $data
        PublicKey: $publicKey
    ```

    | Inputs     | Purpose                      | Examples                          |
    |-|-|-
    | `$data`   | original data to verify  | `Hello!` `{A:1,B2}`
    | `$signature` | base64 signature to validate   | `...`|
    | `$publicKey` | base64 key for verification | `...` |