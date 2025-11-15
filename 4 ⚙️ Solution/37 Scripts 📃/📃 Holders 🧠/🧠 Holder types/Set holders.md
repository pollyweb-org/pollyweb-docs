<!-- TODO -->

# 🧠 Set holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are Set holders?**

    `Set` holders 
    * are [List 🧠 holders](<List holders.md>) that contain [Maps 🧠][Map]
        * e.g. `[{A:11,B:12}, {A:21,B:22}]`
    * typically representing a collection of similar objects
        * e.g. an [Itemized 🛢 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>), [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)

    ---
    <br/>


1. **What are the built-in functions for Sets?**

    |Group| [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | Returns | Details 
    |-|-|-|-
    |Read | [`.First`][.First] | [Set][Set], [Map][Map] | Return the first `n` [Maps 🧠][Map] with [`.Filter`][.Filter]
    ||[`.Take`][.Take] | [Set][Set], [Map][Map] | Equals [`.First`][.First]
    ||[`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Last}.md>) | [Set][Set], [Map][Map] | Return the last `n` [Maps 🧠][Map] with [`.Filter`][.Filter]
    ||[`.Filter`][.Filter] | [Set][Set] | Return [Maps 🧠][Map] that match a given filter
    ||[`.Where`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Where}.md>) | [Set][Set] | Equals [`.Filter`][.Filter]
    |Merge| [`.Cross`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Cross}.md>) | [Set][Set] | Cross multiple [Set 🧠 holders][Set]
    |Change | [`.Sort`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Sort}.md>) | [Set][Set] | Sort [Maps 🧠][Map] by key
    || [`.Format`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Format}.md>) | [Set][Set] | Select and rename [Map 🧠][Map] keys

    ---
    <br/>

[.First]: <../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.First}.md>
[.Take]: <../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Take}.md>
[Map]: <Map holders.md>
[.Filter]: <../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Filter}.md>
[Set]: <Set holders.md>