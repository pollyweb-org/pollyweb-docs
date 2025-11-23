# 🧠 Set holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are Set holders?**

    `Set` holders 
    * are [List 🧠 holders](<🧠 List holders.md>) that contain [Maps 🧠](<🧠 Map holders.md>)
        * e.g. `[{A:11,B:12}, {A:21,B:22}]`
    * typically representing a collection of similar objects
        * e.g. an [Itemized 🛢 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>), [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)

    ---
    <br/>


1. **What are the built-in functions for Sets?**

    |Group| [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | Returns | Details 
    |-|-|-|-
    |Read | [`.First`](<../Set 📚 holders/First ⓕ set.md>) | [set](<🧠 Set holders.md>), [map](<🧠 Map holders.md>) | Return the first `n` [Maps 🧠](<🧠 Map holders.md>) with [`.Filter`](<../Set 📚 holders/Filter ⓕ set.md>)
    ||[`.Take`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Take ⓕ.md>) | [set](<🧠 Set holders.md>), [map](<🧠 Map holders.md>) | Equals [`.First`](<../Set 📚 holders/First ⓕ set.md>)
    ||[`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Last ⓕ.md>) | [set](<🧠 Set holders.md>), [map](<🧠 Map holders.md>) | Return the last `n` [Maps 🧠](<🧠 Map holders.md>) with [`.Filter`](<../Set 📚 holders/Filter ⓕ set.md>)
    ||[`.Filter`](<../Set 📚 holders/Filter ⓕ set.md>) | [set](<🧠 Set holders.md>) | Return [Maps 🧠](<🧠 Map holders.md>) that match a given filter
    ||[`.Where`](<../Set 📚 holders/Where ⓕ set.md>) | [set](<🧠 Set holders.md>) | Equals [`.Filter`](<../Set 📚 holders/Filter ⓕ set.md>)
    |Merge| [`.Cross`](<../Set 📚 holders/Cross ⓕ.md>) | [set](<🧠 Set holders.md>) | Cross multiple [Set 🧠 holders](<🧠 Set holders.md>)
    |Change | [`Set.Sort`](<../Set 📚 holders/Sort ⓕ set.md>) | [set](<🧠 Set holders.md>) | Sort [Maps 🧠](<🧠 Map holders.md>) by key
    || [`.Format`](<../Set 📚 holders/Format ⓕ set.md>) | [set](<🧠 Set holders.md>) | Select and rename [Map 🧠](<🧠 Map holders.md>) keys
    ||[`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Append ⓕ list.md>)     |[set](<🧠 Set holders.md>)| Add items to the list
    |       | [`.Add`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ any.md>) |[set](<🧠 Set holders.md>)| Same as [`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Append ⓕ list.md>)

    ---
    <br/>