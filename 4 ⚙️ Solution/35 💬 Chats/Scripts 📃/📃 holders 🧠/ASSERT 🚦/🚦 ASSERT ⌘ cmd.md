# 😃🚦 Talker `ASSERT` command

> Part of [Script 📃](<../../📃 basics/Script 📃.md>)


<br/>



1. **What's the ASSERT command?**

    An `ASSERT`
    * is a handler [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * that verifies data assumptions.
  
    ---
    <br/>

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
    # Value boolean assertions
    ASSERT|{boolean}

    # Object boolean single assertion (string)
    ASSERT|$object:
        {boolean}  
        
    # Object boolean multiple assertions (array)
    ASSERT|$object:
        - {boolean-1}  
        - {boolean-2}  
    ```
    
    | Input| Purpose | Examples
    |-|-|-
    | `$object`| Optional initial context | `$.Msg`
    | `{boolean}` | Value with a [{Function} 🐍](<../../📃 basics/Function 🐍.md>) | `$p.Equals(3)`
    
    ---
    <br/>


1. **What's the syntax or empty or missing assertions?**

    ```yaml
    # Empty or missing assertions
    ASSERT|$object:
        - {value-1}   
        - {value-n}  
    ```

    | Input| Purpose | Examples
    |-|-|-
    | `$object`| Optional initial context | `$.Msg`
    | `{value}` | Checked with [`.IsEmpty`](<../../📃 functions 🐍/🔩 {.IsEmpty}.md>) | `A` `$h` `$h.A`


    ---
    <br/>


1. **What's an alternative syntax?**

    ```yaml
    # Alternative syntax
    ASSERT|$object:
        
        # Only supports similar comparisons 
        {similar-value-A1}: {similar-value-A2} 
        {similar-value-An}: {similar-value-An} 

        # Supports single value assertions
        :{boolean}:
        :{value}:
    ```
    
    Restrictions:
    * Only supports [`.Is`](<../../📃 functions 🐍/🔩 {.Is}.md>) assertions
    * Supports single value assertions surrounded with `:`
    * `{similar-value-A}` cannot be repeated

    ---
    <br/>



1. **How does the `$context` work with Functions?**

    |Situation | Behavior
    |-|-
    | `Comparisons` | The left of the operator maps to the `$object`
    |               | The right side is evaluated with [{Functions} 🐍](<../../📃 basics/Function 🐍.md>)
    | `Single value` | No [{Functions} 🐍](<../../📃 basics/Function 🐍.md>); all is mapped to `$object` 

    ---
    <br/>

1. **How to assert a Message?**

    ```yaml
    📃 Example:

    # Assert a matching pair
    - ASSERT|$.Msg:
        From: any-broker.dom

    # Show success message
    - SUCCESS|Message is from Any Broker
    ```

    Commands: [`$.Msg`](<../$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`ASSERT`](<🚦 ASSERT ⌘ cmd.md>) [`SUCCESS`](<../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)

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

    Commands: [`PARSE`](<../PARSE 🔆/🔆 PARSE ⌘ cmd.md>) [`SUCCESS`](<../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>

1. **What's the syntax for enums?**

    ```yaml
    # Enum assertions
    ASSERT|$holder:
        Enum: {value-1}, {value-2}, ...
    ```
    | Input| Purpose | Examples
    |-|-|-
    | `$object`| Optional initial context | `$.Msg`
    | `Enum` | List of possible values | `A,B` `[A,B]`
    |

    Syntax flexibility:
    * `Enums` (with an `s`) will also work.
    * The `-` is optional if there's no `Enum` property on the object.
    * If there's an `Enum` property on the given context object
        * then a similar `:` comparison is performed.
    
    <br/>
    
    Here's a valid example for a value.

    ```yaml
    📃 Example:
    
    # Assert
    - ASSERT|A:
        Enum: A, B, C

    # Show success
    - SUCCESS|A is in (A, B, C)
    ```

    <br/>
    Here's a valid example for a list of values.


    ```yaml
    📃 Example:
    
    # Assert
    - ASSERT|A,B,B,B:
        Enum: A, B, C

    # Show success
    - SUCCESS|All elements are in (A, B, C)
    ```

    ---
    <br/>

