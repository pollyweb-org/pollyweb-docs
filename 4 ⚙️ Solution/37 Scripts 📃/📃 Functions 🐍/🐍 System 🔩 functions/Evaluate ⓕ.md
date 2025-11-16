# 😃🔩 Talker `{.Evaluate}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ

1. **What is the .Evaluate function?**

    `{.Evaluate}`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that extends the YAML syntax
    * allowing for additional ways to merge YAML lists and objects
    * when passing YAML inputs to [Commands ⌘](<../../../35 💬 Chats/Scripts 📃/Command ⌘.md>).

    ---
    <br/>

1. **What is the .Evaluate syntax?**

    ```yaml
    .Evaluate(context={}, inputs...)
    ```

    Input | Purpose
    |-|-
    |`context`| Optional parent [Holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    |`inputs...` | Inputs to evaluate

    ---
    <br/>

1. **What are the relevant YAML syntaxes?**

    |Type| Variation | Syntax|
    |-|-|-
    | [`Strings`](<../../📃 Holders 🧠/Text 📚 holders/🧠 Text holders.md>)  | single line | May or not be surrounded by `"` or `'`.
    |           | multi line | Multi line strings behaves like a single line
    |           | line breaks | Line breaks are supported with `\|` or `>`
    | [`Arrays`](<../../📃 Holders 🧠/List 📚 holders/🧠 List holders.md>) | single line  | Are represented with `[]`
    |           | multi line  | Are represented with `-` for each item
    | [`Objects`](<../../📃 Holders 🧠/Map 📚 holders/🧠 Map holders.md>)  | single line  | Are represented with `{}`
    | | multi line  | Appear as `key:` for each property

    ---
    <br/>


1. **How does .Evaluate work with interpolation?**

    Values inside `{}` are evaluated first, as in the following [`PUT`](<../../📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) example.

    ```yaml
    PUT|1 >> $a
    PUT|a >> $b
    ```
    
    |Input |Output| Same as | Same as | 
    |-|-|-|-
    | `$a` | `1` | `${a}` | `${$b}`
    | `$b` | `a` | `${b}` |
    | `txt {$a}` | `txt 1` | `txt {${a}}` | `txt {${$b}}`

    ---
    <br/>



1. **How does .Evaluate work with CSV?**

    Single-line comma-separated values (CSV) are converted to YAML [arrays](<../../📃 Holders 🧠/List 📚 holders/🧠 List holders.md>), as in the following [`PUT`](<../../📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) example.

    ```yaml
    PUT| A,B,C  >> $l1
    PUT|[A,B,C] >> $l2
    ```
    
    |Input |Output| 
    |-|-
    | `$l1` | `[A,B,C]` | 
    | `$l2` | `[A,B,C]` | 
    | `A,B,C` | `[A,B,C]` | 
    | `[A,B,C]` | `[A,B,C]` | 
    
    ---
    <br/>

1. **How does .Evaluate work with YAML arrays?**

    Arrays are merged with the [`.Append`](<../../📃 Holders 🧠/List 📚 holders/Append ⓕ list.md>) function, as in the following [`PUT`](<../../📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) example.

    ```yaml
    PUT|[1,2] >> $l1
    PUT|[3,4] >> $l2
    ```

    |Input<br/>lines |Function<br/>output| Same with <br>CSV input | Same with <br> Array input | Same with <br>Object input
    |-|-|-|-|-
    | `$l1` | `[1,2]` | | `[$l1]` | `{$l1:}`
    | `$l1 $l2` | `[1,2,3,4]` | `$l1,$l2` | `[$l1,$l2]` | `{$l1:,$l2:}`

    ---
    <br/>

1. **How does .Evaluate work with YAML objects?**

    Properties are named if more than one, as in the following [`PUT`](<../../📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) example.

    ```yaml
    PUT|{A:1,B:2:C:3} >> $x
    ```
    
    |Input<br/>lines |Function<br/>output| Same with <br> Array input | Same with <br>Object input 
    |-|-|-|-
    | `$x` | `{A:1,B:2:C:3}` | `[$x]` | `{$x:}`
    | `$x.A` | `1` | `[$x.A]` | `{$x.A:}`
    | `$x.A`[`.Add`](<../../📃 Holders 🧠/Any 📚 holders/Add ⓕ any.md>)`(7)` | `8` | `[$x.A.Add(7)]` | `{$x.A.Add(7):}` 
    | `M: $x.A` | `{M:1}` | `[{M:$x.A}]` | `{M:$x.A}`
    | `M: $x.A`[`.Add`](<../../📃 Holders 🧠/Any 📚 holders/Add ⓕ any.md>)`(7)` | `{M:8}` | `[$x.A.Add(7)]` | `{M:$x.A.Add(7)}`
    | `$x.A` `$x.B` | `{A:1,B:2}` | `[$x.A,$x.B]` | `$x.A,$x.B`
    | `M: $x.A` `$x.B:` | `{M:1,B:2}` | `[M:$x.A,$x.B]` | `[{M:$x.A},$x.B]`
    
    ---
    <br/>

1. **How does .Evaluate work with multiple YAML objects?**

    See the following [`PUT`](<../../📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) example.

    ```yaml
    PUT|{D:4, E:5} >> $y
    ```
    
    |Input<br/>lines |Function<br/>output| Same with <br>CSV input | Same with <br> Array input | Same with <br>Object input
    |-|-|-|-|-
    | `$x.A` `$y` | `{A:1,D:4,E:5}` | `$x.A,$y` |`[$x.A,$y]`| `{$x.A:,$y:}`
    | `M: $x.A` `$y:` | `{M:1,D:4,E:5}` | |`[$x.A,$y]`| `{M:$x.A,$y:}`
    
    ---
    <br/>

1. **How does .Evaluate work with YAML objects inside other objects?**

    See the following [`PUT`](<../../📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) example.

    ```yaml
    PUT|{F:{G:6}} >> $z
    ```

    |Input<br/>lines |Function<br/>output| Same with <br>CSV input | Same with <br> Array input | Same with <br>Object input
    |-|-|-|-|-
    | `$z` | `{F:{G:6}}` | | `[$z]` | `{$z:}`
    | `$z.F` | `{G:6}` | | `[$z.F]` | `{$z.F:}`
    | `$x.A` `$z` | `{A:1,F:{G:6}}` | `$x.A,$z` | `[$x.A,$z]` | `{$x.A:,$z:}`
    | `M: $x.A` `$z:` | `{M:1,F:{G:6}}` |  | `[$x.A,$z]` |  `{M:$x.A,$z:}`

    ---
    <br/>

