# 😃🔽 Talker `FILTER` command

> Part of [Talker 😃](<../../../😃 Talker role.md>)

> Implemented by the [`.FILTER` 📃 script](<😃📃 .FILTER 🔽 script.md>)

<br/>

1. **What's a FILTER command?**

    A `FILTER`
    * is a message [Command ⌘](<../../...commands ⌘/⌘ Command.md>) 
    * that calls [`MANY` 🔠 prompt](<../../../../🤔 Prompts/🤔✏️ Prompt inputs/54 🔠 MANY prompt.md>)
    * to return only the user-selected items of a list.


    ---
    <br/>

1. **What's the FILTER syntax?**

    ```yaml
    FILTER|<statement> >> $filtered:
        Statement: <statement>
        Options: $list
        ID: <ID property>
        Title: <Title property>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `Statement` | Prompt question | `Which ones?`
    | `Options`  | Array of items to filter | `[{A:1,B:2,C:3},{...}]`
    | `ID`       | ID property name | `A`
    | `Title`    | Title property name | `B`
    | `$filtered`| Array of filtered items | `[{A:1,B:2,C:3}]`
    
    
    ---
    <br/>

1. **What's an example of a FILTER?**

    Here's a [Chat 💬](<../../../../💬 Chats/💬 Chat.md>).

    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🤗 [Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Which options? [All, No] <br/> - [ ] Some option <br/> - [ ] Another option | > All
    ||

    <br/>

    Here's the [Script 📃](<../../...commands ⌘/📃 Script.md>).

    ```yaml
    # Create a dummy list
    EVAL >> $list:
        - A: 1
          B: Some Option
        - A: 2
          B: Another Option

    # Filter the list
    FILTER >> $filtered:
        Statement: Which options?
        Options: $list
        ID: A
        Title: B
    ```

    The user selected `All`, so `$filtered` equals `$list`.

    ---
    <br/>

