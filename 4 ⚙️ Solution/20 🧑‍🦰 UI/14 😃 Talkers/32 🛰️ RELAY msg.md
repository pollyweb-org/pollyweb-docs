# 🛰️ Talker `RELAY` command

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a RELAY item command?**

    A `RELAY` 
    * is a [Command](<10 Command.md>) 
    * that sends messages to physical devices
    * via [Relayer 🛰️ helper domains](<../../60 🧰 Edge/61 🔌 Pluggables/04 🛰️🛠️ Relayer helper.md>).

    ---
    <br/>


1. **What's the syntax?**

    ```yaml
    - RELAY|<pool>|<key> >> <result>
        Message: <message>
        OnFailure: <failure>
        OnSuccess: <success>
    ```

    | Argument| Purpose
    |-|-
    | `<pool>` | Name of device pool in the [Relayer 🛰️](<../../60 🧰 Edge/61 🔌 Pluggables/04 🛰️🛠️ Relayer helper.md>)
    | `<key>`  | Unique device key in the pool
    | `<message>` | Message to send to the device
    | `<result>` | The response returned by the [Relayer 🛰️](<../../60 🧰 Edge/61 🔌 Pluggables/04 🛰️🛠️ Relayer helper.md>)
    | `<failure>` | [Procedure](<12 ⚙️ Procedure.md>) or [Command](<10 Command.md>) to run on failure
    | `<success>` | [Procedure](<12 ⚙️ Procedure.md>) or [Command](<10 Command.md>) to run on success

    ---
    <br/>

2. **What's an example?**

    ```yaml
    Open:
    - RELAY|Machines|{.ChatKey} >> result
        Instructions: Open({$item.Number})
        OnFailure: FAILURE|Error!
        OnSignal: SUCCESS|Done!

    ```

    | Argument| Purpose
    |-|-
    | `<pool>` | Name of resource pool.
    | `<key>`  | Key to look up in the pool.
    | `<item>` | Item to retrieve.

    ---
    <br/>

3. **What are use cases?**

    * [Vending machines 🏪](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/01 🏪 Index.md>)

    ---
    <br/>
