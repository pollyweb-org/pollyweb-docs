# 🔑 Talker `KEYS` command

> Part of [Talker 😃](<../../😃 Talker role.md>)

> Used by [🤵⏩🧑‍🦰 Converse 💬](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵⏩ Broker flows/Converse 🤵⏩💬/🤵⏩🧑‍🦰 Converse 💬.md>)

<br/>

1. **What's a KEYS command?**
   
   A `KEYS` 
   * is a handler [Command ⌘](<../...commands ⌘/Command ⌘/Command ⌘.md>) 
   * that generates a new asymmetric key pair.

    ---
    <br/>


1. **How to use a PARSE?**

    Here's the [Script 📃](<../...commands ⌘/Script 📃/📃 Script.md>).

    ```yaml
    - KEYS >> $keys
    ```

    Here's the properties returned by `$keys`.

    | Expression| Result
    |-|-
    | `PrivateKey`| Private key to sign content 
    | `PublicKey`| Public key to verify the signature

    ---
    <br/>

