# 😃🔽 Talker `FILTER` command

> Part of [Script 📃](<../../📃 basics/Script 📃.md>)

> Implemented by the [`.FILTER` 📃 script](<🔽 FILTER 📃 script.md>)

<br/>

1. **What's a FILTER command?**

    A `FILTER`
    * is a message [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * that calls [`MANY` 🔠 prompt](<../../../Prompts 🤔/🤔✏️ Prompt inputs/MANY 🔠/🔠 MANY ⌘ cmd.md>)
    * to return only the user-selected items of a list.


    ---
    <br/>

1. **What's the FILTER syntax?**

    ```yaml
    FILTER|<text> >> $filtered:
        Text: <text>
        Options: $list
        ID: <ID property>
        Title: <Title property>
    ```

    | Input| Purpose | Example
    |-|-|-
    | `Text` | Prompt question | `Which ones?`
    | `Options`  | Array of items to filter | `[{A:1,B:2,C:3},{...}]`
    | `ID`       | ID property name | `A`
    | `Title`    | Title property name | `B`
    | `$filtered`| Array of filtered items | `[{A:1,B:2,C:3}]`
    
    
    ---
    <br/>

1. **What's an example of a FILTER?**

    Here's a [Chat 💬](<../../../Chats 💬/💬 Chat.md>).

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | 🤗 [Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Which options? [All, No] <br/> - [ ] Some option <br/> - [ ] Another option | > All
    ||

    <br/>

    Here's the [Script 📃](<../../📃 basics/Script 📃.md>).

    ```yaml
    # Create a dummy list
    EVAL >> $list:
        - A: 1
          B: Some Option
        - A: 2
          B: Another Option

    # Filter the list
    FILTER >> $filtered:
        Text: Which options?
        Options: $list
        ID: A
        Title: B
    ```

    The user selected `All`, so `$filtered` equals `$list`.

    ---
    <br/>

