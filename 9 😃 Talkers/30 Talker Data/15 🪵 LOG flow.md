# 🪵 Talker `LOG` command

> Part of [Talker 😃](<../../33 😃 Talkers/01 😃 Talker.md>)

<br/>

1. **What is a LOG command?**

    A `LOG` 🪵
    * is a [Command ⌘](<../20 Talker Flows/10 ⌘ Command.md>) 
    * that sends an event 
    * to the log handler of a [Talker 😃](<../../33 😃 Talkers/01 😃 Talker.md>).


    ---
    <br/>


1. **What are example use cases?**

    * Handling the result of a [`RELAY`](<../60 Messages/51 🛰️ RELAY msg.md>) command.
    * The [Talker 😃](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/93 😃 Owner: Talker.md>) at [Vending machines 🏪](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/01 🏪 Index.md>)

    ---
    <br/>
    
1. **What's the syntax?**

    ```yaml
    # Function syntax
    - LOG|{function}

    # String syntax
    - LOG|<string>

    # Object syntax
    - LOG:
        {object}
    ```
    
    
    | Argument| Purpose | Example
    |-|-|-
    | `{function}`| [{Function}](<12 🐍 {Function}.md>) to valuate and log. | `{MyFunction}` | 
    | `<string>` | String to evaluate and log. | `A` `I'm {$name}`
    | `{object}` | Object to evaluate and log. | `{A:1, B:$n}`
    

    ---
    <br/>

1. **How to use it in a Talker?**
   

    ```yaml
    # Strings
    - LOG|An error occurred.

    # Functions
    - LOG|{$event}
    
    # Objects
    - LOG:
        MyMessage: An error occurred.
        MyEvent: {$event}
    ```

    ---
    <br/>
