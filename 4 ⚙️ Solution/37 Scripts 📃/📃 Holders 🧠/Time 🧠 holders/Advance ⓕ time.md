# 😃🔩 Talker `{$time.Advance}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Used by [`.Add`](<../Any 🧠 holders/Add ⓕ any.md>) [`.Plus`](<../Any 🧠 holders/.Plus 🔩 any.md>)

## FAQ

1. **What is the .Advance function?**

    `{.Advance}` 
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that advances a period from a given [Time 🧠 holder](<🧠 Time holders.md>)
    * as opposed to [`.GoBack`](<GoBack ⓕ time.md>).

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    .Advance(time, period)
    ```

    Input|Purpose|Example
    |-|-|-
    | `time` | Original time as a function, | [`.Now`](<../../📃 Functions 🐍/🐍 System 🔩 functions/time/🔩 Now.md>) [`.Today`](<../../📃 Functions 🐍/🐍 System 🔩 functions/time/🔩 Today.md>) 
    || or as a [Time 🧠 holder](<🧠 Time holders.md>) | [`$time`](<🧠 Time holders.md>) 
    | `period` | Textual period to advance, | `3 hours` 
    || or timestamp-like period, | `3:29:47` |
    || or an exact [Time 🧠 holder](<🧠 Time holders.md>) | [`$time2`](<🧠 Time holders.md>) 
   
    ---
    <br/>


1. **How to define textual periods?**

    A textual period is a number followed by:
    * second, seconds, minute, minutes, hour, hours
    * day, days, month, months, year, or years.
  
    ---
    <br/>

1. **How to define a timestamp-like period?**

    A timestamp-like period is a string formatted in `HH:MI:SS` - e.g.:
    * `1:23:45` for 1 hour, 23 minutes, and 45 seconds
    * `1:23` for 1 minute and 23 seconds
    * `1` for 1 second.

    ---
    <br/>

1. **What happens when passing a time holder to the period?**

    A [Time 🧠 holder](<🧠 Time holders.md>) passed in the `period` input 
    * always outputs that holder,
    * allowing to use `.Advance($time, $any)` 
    * where `$any` is either an absolute [Time 🧠](<🧠 Time holders.md>) 
    * or a relative period like `1 day ago`.
  

    ---
    <br/>