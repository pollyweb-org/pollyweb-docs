# 😃🚦 Talker `ASSERT` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)


<br/>



1. **What's the ASSERT command?**

    An `ASSERT`
    * is a handler [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that verifies data assumptions.
  
    ---
    <br/>

1. **What are examples of ASSERT usage?**

    | Scenario | Purpose
    |-|-
    | [`$.Inputs` 🧠 holder](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)      | Assert inputs from [`RUN`](<../../⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) commands
    | [`$.Msg` 🧠 holder](<../../../📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)         | Assert incoming [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)
    | [`List` holders 🧠](<../../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>)  | Assert items in list [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

    ---
    <br>

1. **What's the syntax for Multi-field assertions?**

    ```yaml
    # Multi-field assertions
    ASSERT|$object:
        AllOf: <fields> # Required fields
        AnyOf: <fields> # One or more of these
        OneOf: <fields> # Only one of these
        UUIDs: <fields> # UUID fields
        Texts: <fields> # Text fields
        Times: <fields> # Time fields
        Lists: <fields> # List fields
        Bools: <fields> # Boolean fields
        Enums: <fields> # Enum fields, i.e. list of texts
        Nums: <fields> # Numeric fields
    ```
    
    | Input| Purpose |  Examples |Behavior
    |-|-|-|-
    | `$object`| Optional initial context | `$.Msg`
    | `AllOf` | All should have values |  `A,B` `[A,B]` | [`.AllOf`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/AllOf ⓕ.md>)
    | `AnyOf` | One or more have values |  `A,B` `[A,B]` | [`.AnyOf`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/AnyOf ⓕ.md>)
    | `OneOf` | Only one should have value | `A,B` `[A,B]` | [`.OneOf`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/OneOf ⓕ.md>)
    | `UUIDs` | Must be a UUID fields| `A,B` `[A,B]`
    | `Texts` | Must be [Text 🧠](<../../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>) fields | `A,B` `[A,B]`
    | `Times` | Absolute or relative [Time 🧠](<../../../📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>) | `A,B` `[A,B]`
    | `Lists` | Must be [Lists 🧠](<../../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) or [Sets 🧠](<../../../📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>) | `A,B` `[A,B]`
    | `Bools` | Must be boolean fields | `A,B` `[A,B]`
    | `Enums` | Must be [Lists 🧠](<../../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) of [Text 🧠](<../../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>) | `A,B` `[A,B]`
    | `Nums` | Must be [Num 🧠](<../../../📃 Holders 🧠/Input holders 📥/🧠 Num holders.md>) fields | `A,B` `[A,B]`
    |
    
    <br/>

    
    ---
    <br/>


1. **What's the syntax for boolean assertions?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

    ```yaml
    ASSERT|$object:
        <key>
        <key>.f: ?
        <key>: <val>
    ```
    
    | Input| Purpose | Examples
    |-|-|-
    | `$object`| Optional initial context | [`$.Msg`](<../../../📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`.Inputs`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Inputs ⓕ.md>)
    | `<key>` | Input to [`.Assert`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | `From` `$A` [`$lst.A`](<../../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>)
    | `.f(?)`| Input to [`.Assert`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) a [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)  | [`.IsIn`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>)`(A,B)`
    | `:<val>` | Input to [`.Assert`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) with  [`.Is`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>) | `:any-domain.dom`
    

    > **Note** 
    * If `AllOf`, `AnyOf`, or `OneOf` are set, 
    * then [`.Assert`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) will only be called if [`.IsNotEmpty`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/IsNotEmpty ⓕ.md>), 
    * to allow optional inputs to be validated only if they have an assigned value.


    ---
    <br/>


1. **What's the simplest syntax?**

    ```yaml
    # Simplest inline
    ASSERT|<assertion>
    ```

    ```yaml
    # Simplest multi-line
    ASSERT:
        <assertion>
    ```


    | Input| Purpose | Examples
    |-|-|-
    | `assertion` | Input to [`.Assert`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) | `aA.Is(7)`
    


    ---
    <br/>


1. **How to assert a [List 🧠](<../../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) of [Maps 🧠](<../../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>)?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    # Create a list
    PUT >> $list:
        - {A:10, B:20, C:X}
        - {A:11, B:21, C:Y}
        - {A:12, B:22}

    # Verify the list items.
    ASSERT|$list:
        AllOf: A, B
        A.IsBetween: 10, 19
        B.IsBetween: 20, 29
        C.IsIn: X,Y
    ```
    Uses: [`PUT`](<../PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`.IsBetween`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/IsBetween ⓕ.md>) [`.IsIn`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>)

    > Note
    * The [`.Assert`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) of `C.IsIn(X,Y)` returns `False` because the property `C` doesn't event exist in the third list item.
    * However, that doesn't break the overall assertion.
    * This is because `AllOf` is set, and it doesn't include `C`, allowing `C` to be asserted only when [`.IsNotEmpty`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/IsNotEmpty ⓕ.md>).

    ---
    <br/>



1. **How to assert a [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)?**

    > This example uses 
    * [`.Parse`](<../PARSE 🔆/🔆 PARSE ⌘ cmd.md>) to break a [`Locator`](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
    *  [`.Is`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>) to compare [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)

    ```yaml
    📃 Example:

    # Put the locator in a holder
    - PARSE >> $locator:
        nlweb.org/HOST:1.0,any-host.dom,ANY-RESOURCE

    # Assert for equivalence to .HOST
    - ASSERT|$locator:
        Schema: .HOST

    # Show success message.
    - SUCCESS|The schema is equivalent to ./HOST
    ```

    Uses: [`PARSE`](<../PARSE 🔆/🔆 PARSE ⌘ cmd.md>) [`SUCCESS`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>
