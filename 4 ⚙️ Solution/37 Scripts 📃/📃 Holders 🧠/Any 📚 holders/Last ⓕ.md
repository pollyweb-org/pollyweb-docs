# 😃🔩 Talker `{.Last}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Purpose
* Counts back from a starting point.
* For [List 🧠 holders](<../../📃 Holders 🧠/List 📚 holders/🧠 List holders.md>), it's the opposite of [`.First`](<First ⓕ.md>)
* For [Period 🧠 holders](<../../📃 Holders 🧠/🧠 Output holders/Period holders.md>), it's similar but not the same as [`.This`](<../Time 📚 holders/This ⓕ.md>) and [`.Previous`](<../Time 📚 holders/Previous ⓕ.md>)

> Used by [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)

## FAQ

1. **How to use .Last for time validation?**

    Here's a [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    ```yaml
    📃 Example
    - ASSERT:
        - $date.IsIn(.Last(2 months))
    ```

    ---
    <br/>


1. **What's the behavior of .Last?**

    |Input|Behavior
    |-|-
    |`.Last(period)` | Returns a [Period 🧠 holder](<../../📃 Holders 🧠/🧠 Output holders/Period holders.md>)
    |[`$txt`](<../../📃 Holders 🧠/Text 📚 holders/🧠 Text holders.md>)`.Last(n)`| Returns the last `n` characters of a [Text 🧠 holder](<../../📃 Holders 🧠/Text 📚 holders/🧠 Text holders.md>)
    |               |If `n` exceeds [`.Length`](<Length ⓕ.md>), returns the [Text 🧠 holder](<../../📃 Holders 🧠/Text 📚 holders/🧠 Text holders.md>)
    |[`$txt`](<../../📃 Holders 🧠/Text 📚 holders/🧠 Text holders.md>)`.Last` | Equals `$txt.Last(1)`
    |[`$lst`](<../../📃 Holders 🧠/List 📚 holders/🧠 List holders.md>)`.Last(n)`| Returns the last `n` items of a [List 🧠 holder](<../../📃 Holders 🧠/List 📚 holders/🧠 List holders.md>)
    |               |If `n` exceeds [`.Length`](<Length ⓕ.md>), returns the [List 🧠 holder](<../../📃 Holders 🧠/List 📚 holders/🧠 List holders.md>)
    |[`$lst`](<../../📃 Holders 🧠/List 📚 holders/🧠 List holders.md>)`.Last` | Equals `$lst.Last(1)`
    |[`$mapList`](<../../📃 Holders 🧠/Map 📚 holders/🧠 Map holders.md>)`.Last({A:1},n)`| Applies [`.Filter`](<../../📃 Holders 🧠/Set 📚 holders/Filter ⓕ set.md>) then `.Last(n)`
    |[`$mapList`](<../../📃 Holders 🧠/Map 📚 holders/🧠 Map holders.md>)`.Last({A:1})` | Equals `$mapList.Last({A:1},1)`
    ---
    <br/>


1. **What are examples of .Last for times?**

    For time related strings, [`.Last`](<Last ⓕ.md>) returns a [Period 🧠 holder](<../../📃 Holders 🧠/🧠 Output holders/Period holders.md>) for [`.IsIn`](<../../📃 Holders 🧠/Any 📚 holders/IsIn ⓕ any.md>) and [`.IsBetween`](<../../📃 Holders 🧠/Any 📚 holders/IsBetween ⓕ any.md>).

    | Example | Returns
    |-|-
    | `.Last(60 minutes)` | From [`.Now`](<../Time 📚 holders/Now ⓕ.md>)[`.Minus`](<../../📃 Holders 🧠/Any 📚 holders/Minus ⓕ any.md>)`(60 minutes)` to [`.Now`](<../Time 📚 holders/Now ⓕ.md>)
    | `.Last(hour)` | `.Last(60 minutes)`
    | `.Last(2 hours)` | `.Last(120 minutes)`
    | `.Last(day)` | `.Last(24 hours)`
    | `.Last(2 days)` | `.Last(48 hours)`
    | `.Last(1 month)` | From [`.Now`](<../Time 📚 holders/Now ⓕ.md>)[`.Minus`](<../../📃 Holders 🧠/Any 📚 holders/Minus ⓕ any.md>)`(1 month)` to [`.Now`](<../Time 📚 holders/Now ⓕ.md>)
    | `.Last(month)` | `.Last(1 month)`
    | `.Last(2 months)` | `.Last(2 months)`
    | `.Last(quarter)` | `.Last(3 months)`
    | `.Last(year)` | `.Last(12 months)`

    ---
    <br/>