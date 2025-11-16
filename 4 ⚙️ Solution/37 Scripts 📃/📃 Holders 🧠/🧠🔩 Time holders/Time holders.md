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
    |Get    | [`.Now`](<../../📃 Functions 🐍/🐍 System 🔩 functions/time/🔩 Now.md>)     |[time](<Time holders.md>)|What's the current time?
    |       | [`.Today`](<../../📃 Functions 🐍/🐍 System 🔩 functions/time/🔩 Today.md>) |[time](<Time holders.md>)| What's the current date?
    |       | [`.This`](<../../📃 Functions 🐍/🐍 System 🔩 functions/time/🔩 This.md>)      |[period](<../🧠 Output holders/Period holders.md>)| What's the given current period? 
    |       | [`.Previous`](<../../📃 Functions 🐍/🐍 System 🔩 functions/time/🔩 Previous.md>)  |[period](<../🧠 Output holders/Period holders.md>)| What's the given previous period? 
    |       | [`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Last}.md>)      |[period](<../🧠 Output holders/Period holders.md>)| What's the given last period?
    |       | [`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>) |[period](<../🧠 Output holders/Period holders.md>)| How long between two times?
    |Compare| [`.IsBetween`](<../🧠🔩 Any holders/.IsBetween 🔩 any.md>)  |bool| Is it between two given times?
    |       | [`.IsIn`](<../🧠🔩 Any holders/🔩 {.IsIn}.md>)       |bool| Is it in a given [Period 🧠 holder](<../🧠 Output holders/Period holders.md>)?
    |Assess   | [`.IsEmpty`](<../🧠🔩 Any holders/any.IsEmpty 🔩 ext.md>) |bool| Is it empty, i.e. no time given?
    |         | [`.IsNotEmpty`](<../🧠🔩 Any holders/any.IsNotEmpty 🔩 ext.md>) |bool| Is it not empty?
    |Change | [`.Advance`](<time.Advance 🔩 ext.md>) |[time](<Time holders.md>)| What if we add time?
    |       | [`.Add`](<../🧠🔩 Any holders/.Add 🔩 any.md>) |[time](<Time holders.md>)| Same as [`.Advance`](<time.Advance 🔩 ext.md>)Time 🧠 functions/🔩 .Advance.md
    |       | [`.Plus`](<../🧠🔩 Any holders/any.Plus 🔩 ext.md>) |[time](<Time holders.md>)| Same as [`.Advance`](<time.Advance 🔩 ext.md>)Time 🧠 functions/🔩 .Advance.md
    |       | [`.GoBack`](<time.GoBack 🔩 ext.md>) |[time](<Time holders.md>)| What if we remove time?
    |       | [`.Minus`](<../🧠🔩 Any holders/any.Minus 🔩 ext.md>)|[time](<Time holders.md>)| Same as [`.GoBack`](<time.GoBack 🔩 ext.md>)Time 🧠 functions/🔩 .GoBack.md
  

    ---
    <br/>