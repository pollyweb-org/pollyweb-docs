# Item 🛢 Views

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ

1. **What are Views?**

    Views are filtered lists of [Item 🛢 Children](<Item 🛢 Children.md>).

    ---
    <br/>

1. **Why are Views important?**

    Views 
    * allow [Scripts 📃](<../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) to be simpler, 
    * by moving the filtering logic to an [Itemizer 🛢 helper domain](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🤲 Itemizer helper.md>).

    ---
    <br/>

1. **Whats the syntax for child views?**    
   
    ```yaml
    # With children
    Table: <name>

    Views:
        <alias>: 
            - <filter>
    ```

    |Input|Details|Example
    |-|-|-
    | `<alias>`  | View name  | `RETURNS`
    | `<filter>` | Comparisons like [`ASSERT`](<../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) | `PRICE < 0`

    ---
    <br/>

1. **What's an example?**
   
    Here's an example.

    ```yaml
    # Example
    Table: ORDER_LINES

    Views:
        RETURNS:
            - PRICE < 0
    ```

    ---
    <br/>

1. **How to use it?**

    Here's a [Script 📃](<../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>)
    ```yaml
    # Example usage of Views
    - INFO:
        Text: | 
            Here's your order.
            Lines: 
                {$order.LINES}
            Returns: 
                {$order.LINES.RETURNS}
    ```
    Commands: [`INFO`](<../../../35 💬 Chats/Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>
