# 😃🧬 Talker `GROUP` Command

> Part of [Talker 😃](<../../../😃 Talker role.md>)

> Used by [`Chats@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Chats 🧑‍🦰🚀🤵/🤵 Chats 🚀 request.md>)

<br/>


1. **What is a GROUP command?**

    A `GROUP` 🧬
    * is a [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) 
    * that merges too lists or an object with a list
    * by grouping properties.

    ---
    <br/>

1. **What's the syntax of GROUP for distinct values?**

    ```yaml
    # Property from a single list
    GROUP >> $distinct:
        $list.property
    ```
    
    ```yaml
    # Properties from multiple lists
    GROUP >> $distinct
        - $list-1.property-1
        - $list-n.property-n
    ```

    Argument | Purpose 
    |-|-
    | `$list.property`  | Take `property` for every item of `$list`
    | `$distinct`       | Group into the `$distinct` placeholder

    ---
    <br/>

1. **What's the syntax of GROUP for distinct objects?**


    ```yaml
    # Objects from multiple lists
    GROUP >> $distinct:
        - $list-1
        - $list-n
    ```

    Argument | Purpose 
    |-|-
    | `$list`  | Take every item of `$list`
    | `$distinct`       | Group into the `$distinct` placeholder

    ---
    <br/>