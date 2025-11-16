# 🧠 Set holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are Set holders?**

    `Set` holders 
    * are [List 🧠 holders](<../List 📚 holders/🧠 List holders.md>) that contain [Maps 🧠][map]
        * e.g. `[{A:11,B:12}, {A:21,B:22}]`
    * typically representing a collection of similar objects
        * e.g. an [Itemized 🛢 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>), [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)

    ---
    <br/>


1. **What are the built-in functions for Sets?**

    |Group| [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | Returns | Details 
    |-|-|-|-
    |Read | [`.First`][.First] | [set][set], [map][map] | Return the first `n` [Maps 🧠][map] with [`.Filter`][.Filter]
    ||[`.Take`][.Take] | [set][set], [map][map] | Equals [`.First`][.First]
    ||[`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Last}.md>) | [set][set], [map][map] | Return the last `n` [Maps 🧠][map] with [`.Filter`][.Filter]
    ||[`.Filter`][.Filter] | [set][set] | Return [Maps 🧠][map] that match a given filter
    ||[`.Where`](<Where ⓕ set.md>) | [set][set] | Equals [`.Filter`][.Filter]
    |Merge| [`.Cross`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Cross}.md>) | [set][set] | Cross multiple [Set 🧠 holders][set]
    |Change | [`Set.Sort`](<Sort ⓕ set.md>) | [set][set] | Sort [Maps 🧠][map] by key
    || [`.Format`](<Format ⓕ set.md>) | [set][set] | Select and rename [Map 🧠][map] keys
    ||[`.Append`][.Append]     |[set][set]| Add items to the list
    |       | [`.Add`](<../Any 📚 holders/Add ⓕ any.md>) |[set][set]| Same as [`.Append`][.Append]

    ---
    <br/>

[list]: <List holders.md>
[.First]: <../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.First}.md>
[.Take]: <../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Take}.md>
[map]: <Map holders.md>
[.Filter]: <../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Filter}.md>
[set]: <Set holders.md>
[.Append]: <../../📃 Functions 🐍/🐍 System 🔩 functions/Append ⓕ.md>