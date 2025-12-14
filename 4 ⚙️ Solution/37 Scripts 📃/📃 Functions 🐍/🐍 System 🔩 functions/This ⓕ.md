# 😃ⓕ Talker `{.This}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ

1. **What is the .This function?**

    `{.This}` 
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns a [Period 🧠 holder](<../../📃 Holders 🧠/Output holders 📤/Period holders.md>)
    * to be used with the [`.IsIn` function](<IsIn ⓕ.md>).

    ---
    <br/>

1. **What't the syntax of .This?**

    ```yaml
    .This(period)
    ```

    Input | Purpose | Example
    |-|-|-
    |`period` | Textual period | `year`

    ---
    <br/>


1. **What are examples of .This?**

    | Example | Returns
    |-|-
    | `.This(hour)`    | From 1st to last seconds of the current hour
    | `.This(day)`    | From 1st to last seconds of the current day
    | `.This(month)`    | From 1st to last seconds of the current month
    | `.This(quarter)`    | From 1st to last seconds of the current quarter
    | `.This(year)`    | From 1st to last seconds of the current year

    ---
    <br/>

1. **How to use .This in a Script?**

    Here's a [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that asserts if a date is from the current year.

    ```yaml
    📃 Example:
    - ASSERT:
        $date.IsIn(.This(year))
    ```
    Uses: [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`.IsIn`](<IsIn ⓕ.md>)

    ---
    <br/>
