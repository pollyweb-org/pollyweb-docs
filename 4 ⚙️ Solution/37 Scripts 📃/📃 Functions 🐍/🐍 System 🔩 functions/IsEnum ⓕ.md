# 😃ⓕ Talker `.IsEnum` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ


1. **What is the .IsEnum function?**

    `.IsEnum`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns `True` if a given holder is an [Enum 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Enum holders.md>)
    * and returns `True` if the all listed properties of a [Set 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>) are [Enum 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Enum holders.md>) holders
    * and returns `False` otherwise.

    ---
    <br/>

1. **What are examples of .IsEnum usage on a value [Holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)?**

    |||
    |-|-
    | Success | `A` `A,B` 
    | Failure | `1` `1,2` `{A:1}` `True`

    ---
    <br/>

1. **What are examples of .IsEnum usage on a [Set 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>)?**

    |Input #1|Input 2|Result
    |-|-|-
    | `{A:1}`|`A`|False
    | `{A:B}`|`A`|True
    | `{A:B,C:3}`|`A,C`|False
    | `{A:B,C:D}`|`A,C`|True

    ---
    <br/>

1. **What's the syntax of .IsEnum?**

    ```yaml
    $holder.IsEnum
    ```