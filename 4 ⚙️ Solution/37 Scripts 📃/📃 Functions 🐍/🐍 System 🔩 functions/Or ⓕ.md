# 😃ⓕ Talker `{.Or}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ


1. **What is the .Or function?**

    `{.Or}`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns True if the result of one of two functions is True
    * or false otherwise.

    ---
    <br/>

1. **What is the .Or syntax?**

    ```yaml
    $holder.<func1>.Or.<func2>
    ```

    | Input | Purpose | Examples
    |-|-|-
    | `$holder` | Any [Holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | `$p` `$user`
    | `func1` | 1st function to evaluate on `$holder` | `.IsEmpty` `.IsPast`
    | `func2` | 2nd function to evaluate on `$holder` | `.IsFuture` `.Is(X)`

    ---
    <br/>

1. **What's an example of the .Or function?**

    ```yaml
    $p.IsEmpty.Or.IsPast
    ```

    The above example:
    * evaluates if the `$p` [Holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) is empty
    * or if it is a past [Time 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>)
    * returning `True` if one of the two conditions is met
    * or `False` otherwise.

    ---
    <br/>