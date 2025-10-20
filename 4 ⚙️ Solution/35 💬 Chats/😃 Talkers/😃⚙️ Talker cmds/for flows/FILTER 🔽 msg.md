# 👋 Talker `FILTER` command


> Part of [Talker 😃](<../../😃 Talker.md>)

<br/>

1. **What's a FILTER command?**

    A `FILTER`
    * is a message [Command ⌘](<../for control/⌘ Command.md>) 
    * that calls [`MANY` 🔠 prompt](<🤔✏️ Prompt inputs/54 🔠 MANY prompt.md>)
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

    Here's a [Chat 💬](<../../../4 ⚙️ Solution/35 💬 Chats/💬 Chats/💬 Chat.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🤗 [Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Which options? [All, No] <br/> - [ ] Some option <br/> - [ ] Another option | > All
    ||

    <br/>

    Here's the [Talker 😃](<../../😃 Talker.md>).

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


1. **How does it work internally?**

    ```yaml
    FILTER_IMPLEMENTATION:

    # Format the options into {ID,Title}
    - EVAL|$1.Options >> $options:
        ID: {$1.ID}
        Title: {$1.Title}

    # Ask the user to select
    - MANY|$1.Statement >> $result:
        Options: $options

    # Match the selected options.
    - MERGE >> $selected:
        Lists:
            ORIGINAL: $1.Options
            RESULT: $result
        Match:
            ORIGINAL.{$1.ID}: RESULT.ID 
        Output:
            :ORIGINAL:

    # Return the list of items selected.
    - RETURN|$selected
    ```


    | [Command ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
    |-|-
    | ⬇️ [`EVAL`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/EVAL ⬇️ flow.md>) | Format the options
    | 🔠 [`MANY`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/54 🔠 MANY prompt.md>) | Ask the user to select
    | 🧬 [`MERGE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/MERGE 🧬 lists.md>) | Merge the results
    | ↩️ [`RETURN`](<RETURN ↩️.md>) | Return the selection
        
    

    ---
    <br/>