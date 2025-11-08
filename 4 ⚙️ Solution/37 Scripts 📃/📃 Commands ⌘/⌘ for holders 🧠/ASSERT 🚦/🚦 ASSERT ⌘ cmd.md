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
    | [`$.Inputs` 🧠 holder](<../../../📃 Holders 🧠/🧠 System holders/$.Inputs ▶️/▶️ $.Inputs 🧠 holder.md>)      | Assert inputs from [`RUN`](<../../⌘ for control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>) commands
    | [`$.Msg` 🧠 holder](<../../../📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)         | Assert incoming [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)
    | [`List` holders 🧠](<../../../📃 Holders 🧠/🧠 Holder types/List holders.md>)  | Assert items in list [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

    ---
    <br>

1. **What's the syntax for Multi-field assertions?**

    ```yaml
    # Multi-field assertions
    ASSERT|$object:
        - AllOf: <fields> # Required fields
        - AnyOf: <fields> # One or more of these
        - OneOf: <fields> # Only one of these
        - UUIDs: <fields> # UUID fields
        - Texts: <fields> # Text fields
        - Times: <fields> # Time fields
        - Lists: <fields> # List fields
        - Maths: <fields> # Numeric fields
    ```
    
    | Input| Purpose | Examples
    |-|-|-
    | `$object`| Optional initial context | `$.Msg`
    | `AllOf` | All should have values | `A,B` `[A,B]`
    | `AnyOf` | One or more have values | `A,B` `[A,B]`
    | `OneOf` | Only one should have value | `A,B` `[A,B]`
    | `UUIDs` | Must be a UUID fields| `A,B` `[A,B]`
    | `Texts` | Must be a text fields | `A,B` `[A,B]`
    | `Times` | Absolute or relative times | `A,B` `[A,B]`
    | `Lists` | Must be list fields | `A,B` `[A,B]`
    | `Maths` | Must be numeric fields | `A,B` `[A,B]`
    
    <br/>

    **Syntax flexibility:**
    * The `-` is optional 
        * if there's no property in the object context with the same name.
    * If there's a property with the same name in the context object, 
        * then the assessment defaults ti similar `:` text comparison.

    ---
    <br/>


1. **What's the syntax for boolean assertions?**

    ```yaml
    ASSERT|$object:
        - <key>
        - <key>.f(?)
        - <key>: <val>
    ```
    
    | Input| Purpose | Examples
    |-|-|-
    | `$object`| Optional initial context | [`$.Msg`](<../../../📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`.Inputs`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Inputs}.md>)
    | `<key>` | Context property or [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | `From` `$A` [`$list`](<../../../📃 Holders 🧠/🧠 Holder types/List holders.md>)`.A` 
    | | - asserts with [`.IsNotEmpty`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsNotEmpty}.md>) 
    | `.f(?)`| Boolean [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsIn`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsIn}.md>)`(A,B)`
    | | - only asserts if [`.IsNotEmpty`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsNotEmpty}.md>) 
    | `:<val>` | Value to assert with [`.Is`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Is}.md>)  | `:any-domain.dom`
    | | - only asserts if [`.IsNotEmpty`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsNotEmpty}.md>) 
    
    ---
    <br/>




1. **How to assert a Locator?**

    > This uses the syntax of the [`{.Parse}` 🔆 function](<../PARSE 🔆/🔆 PARSE ⌘ cmd.md>).

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

    Commands: [`PARSE`](<../PARSE 🔆/🔆 PARSE ⌘ cmd.md>) [`SUCCESS`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>


1. **How to assert list of objects?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    # Create a list
    EVAL >> $list:
        - {A:10, B:20, C:X}
        - {A:11, B:21, C:Y}

    # Verify the list items.
    ASSERT|$list:
        - AllOf: A, B
        - A.IsBetween(10,19)
        - B.IsBetween(20,29)
        - C.IsIn(X,Y)
    ```
    Uses: [`EVAL`](<../EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`.IsBetween`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsBetween}.md>) [`.IsIn`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsIn}.md>)

    ---
    <br/>