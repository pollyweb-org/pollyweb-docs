# 🔐 Talker `VERIFY` Schema 🧩

> About
* Part of the [`VERIFY` ⌘ command](<../VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
* Implemented by the [`.VERIFY-Schema` 📃 script](<🔐 Schema 📃 script.md>)

## FAQ


1. **What's the syntax for Schema validation?**

    ```yaml
    # Blocker version (raises error if invalid)
    - VERIFY:
        Data: $data
        Schema: $schema
    
    # Safe version (stores result in $isValid)
    - VERIFY >> $isValid:
        Data: $data
        Schema: <schema>
    ```

    | Input| Purpose |
    |-|-
    | `$data`| [Holder 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with data to be validated
    | `$isValid`| [Holder 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) that will store `True` or `False`
    | `<schema>`| [Schema Code 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to validate the data against


    ---
    <br/>

1. **What's an example of a call?**

    ```yaml
    📃 Example:
    - VERIFY:
        Data: {...}
        Schema: any-authority.dom/ANY/SCHEMA:1.0.0
    ```