# 🧠 Time holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ


1. **What are time holders?**

    Time holders 
    * represent specific points in UTC time 
    * e.g. `2024-09-21T12:34:00Z`.

    ---
    <br/>

1. **What are the built-in functions for time?**

    |Group| [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | Returns| Details 
    |-|-|-|-
    |Get    | [`.Now`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>)     |[time](<🧠 Time holders.md>)|What's the current time?
    |       | [`.Today`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Today ⓕ.md>) |[time](<🧠 Time holders.md>)| What's the current date?
    |       | [`.This`](<../../📃 Functions 🐍/🐍 System 🔩 functions/This ⓕ.md>)      |[period](<../🧠 Output holders/Period holders.md>)| What's the given current period? 
    |       | [`.Previous`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Previous ⓕ.md>)  |[period](<../🧠 Output holders/Period holders.md>)| What's the given previous period? 
    |       | [`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Last ⓕ.md>)      |[period](<../🧠 Output holders/Period holders.md>)| What's the given last period?
    |       | [`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Diff ⓕ.md>) |[period](<../🧠 Output holders/Period holders.md>)| How long between two times?
    |Compare| [`.IsBetween`](<../../📃 Functions 🐍/🐍 System 🔩 functions/IsBetween ⓕ any.md>)  |bool| Is it between two given times?
    |       | [`.IsIn`](<../../📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ any.md>)       |bool| Is it in a given [Period 🧠 holder](<../🧠 Output holders/Period holders.md>)?
    |Assess   | [`.IsEmpty`](<../../📃 Functions 🐍/🐍 System 🔩 functions/IsEmpty ⓕ any.md>) |bool| Is it empty, i.e. no time given?
    |         | [`.IsNotEmpty`](<../../📃 Functions 🐍/🐍 System 🔩 functions/IsNotEmpty ⓕ any.md>) |bool| Is it not empty?
    |Change | [`.Advance`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Advance ⓕ time.md>) |[time](<🧠 Time holders.md>)| What if we add time?
    |       | [`.Add`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ any.md>) |[time](<🧠 Time holders.md>)| Same as [`.Advance`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Advance ⓕ time.md>)Time 🧠 functions/🔩 .Advance.md
    |       | [`.Plus`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Plus ⓕ any.md>) |[time](<🧠 Time holders.md>)| Same as [`.Advance`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Advance ⓕ time.md>)Time 🧠 functions/🔩 .Advance.md
    |       | [`.GoBack`](<../../📃 Functions 🐍/🐍 System 🔩 functions/GoBack ⓕ time.md>) |[time](<🧠 Time holders.md>)| What if we remove time?
    |       | [`.Minus`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Minus ⓕ any.md>)|[time](<🧠 Time holders.md>)| Same as [`.GoBack`](<../../📃 Functions 🐍/🐍 System 🔩 functions/GoBack ⓕ time.md>)Time 🧠 functions/🔩 .GoBack.md
  

    ---
    <br/>