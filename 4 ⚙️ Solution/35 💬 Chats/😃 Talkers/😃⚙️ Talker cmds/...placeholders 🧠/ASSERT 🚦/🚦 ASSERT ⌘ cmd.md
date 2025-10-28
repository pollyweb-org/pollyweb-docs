# 😃🚦 Talker `ASSERT` command

> Part of [Talker 😃](<../../../😃 Talker role.md>)


<!-- TODO: examples -->
> Used by [`Accepted@Issuer`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>)

<br/>



1. **What's the ASSERT command?**

    An `ASSERT`
    * is a handler [Command ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) 
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
        * then the assessment defaults ti similar `~=` text comparison.

    ---
    <br/>

1. **What's the syntax for comparisons?**

    ```yaml
    # Single comparison (as a string)
    ASSERT|$object:
        {value-A} {comparison} {value-B} 

    # Multiple comparisons (as an array)
    ASSERT|$object:
        - {value-A-1} {comparison} {value-B-1} 
        - {value-A-n} {comparison} {value-B-n} 
    ```
    
    | Input| Purpose | Examples
    |-|-|-
    | `$object`| Optional initial context | `$.Msg` 
    | `{value}` | String or [{Function}](<../../...functions 🐍/{Function} 🐍.md>) evaluated | `A` `{f}` `{$p}`
    || Supports missing `{}`  | `f()` `$p`
    | `{comparison}` | `=` `~=` `!=` `>` `>=` `<` `<=` 
    
    ---
    <br/>


1. **How do equal comparisons work?**

    | | Meaning | Valid results ✅
    |-|-|-
    | `=`  | Same meaning | `a = b` `A = B` 
    |       | Same math | `1 = 1.0` `01 = 1` 
    |       | Same array order | `[1,2] = [1,2]`
    |       | Same object order | `{A:1, B:2} = {A:2, B:1}`

    ---
    <br/>

1. **How do unequal comparisons work?**
   
    | | Meaning | Valid results ✅
    |-|-|-
    | `!=` | Different meaning | `a != b`  
    |       | Different math | `1 != 1.1`
    |       | Different array content | `[1] = [1,2,3]`
    |       | Different object content | `{A:1} = {A:1, B:2, C:3}`
    
    ---
    <br/>

1. **How do similar comparisons work?**

    | | Meaning | Valid results ✅
    |-|-|-
    | `~=` | Same content out of order | `[1,2] = [2,1]`
    |       | Same content out of order | `{A:1, B:2} = {B:2, A:1}`
    |       |Same [Schema 🧩 code](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | `.HOST ~= nlweb.org/HOST:1.0 `|
    |       | Same [domain 👥](<../../../../../40 👥 Domains/👥 Domain.md>) name | `domain.dom ~= DOMAIN.DOM`
    |       | Same [`{.Today}` 🐍](<../../...functions 🐍/{Function} 🐍.md>) date | `~= 2013-04-01T05:00:30.001Z`
    
    

    ---
    <br/>

1. **How do bigger and smaller comparisons work?**

    | Situation | Behavior | Result 
    |-|-|-
    | `math` | Math is math | ✅ `5 > 1.0` 
    | `text` | Text checks length | ✅ `ABC` > 2
    |                               || ✅ `ABC` > `XZ`
    | `empties` | Empties are ignored  | ✅ `$empty > 1`
    ||                   | ✅ `$empty < 1`
    | `arrays` | Arrays check length | ✅ `[A,B] > 1`
    |                               || ✅ `[A,B] > [C]`
    | `objects` | Objects are blocked | ❌ `{A:1} >= 1`
    |                               || ❌ `{A:1} > {A:2}`
    

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
    | `{boolean}` | ✅ Valid for meaningful values | `1` `-1` `True` `A`
    || ❌ Fails on empty meanings | `0` `False` `$p=`
    
    ---
    <br/>


1. **What's the syntax or empty or missing assertions?**

    ```yaml
    # Empty or missing assertions
    ASSERT|$object:
        - {empty-array}   
        - {empty-object}  
    ```

    | Input| Purpose | Examples
    |-|-|-
    | `$object`| Optional initial context | `$.Msg`
    | `{empty-array}` | ✅ Valid for arrays with values | `[0]` `[*]` |
    | | ❌ Fails on empty arrays  | `[]` `$p=`
    | `{empty-object}` | ✅ Valid for objects with values | `{A:0}`
    | | ❌ Fails on empty objects | `{}` `$p=`

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
        :{empty-array}:
        :{empty-object}:  
    ```
    
    Restrictions:
    * Only supports similar comparisons, i.e. `~=`
    * Supports single value assertions surrounded with `:`
    * `{similar-value-A}` cannot be repeated

    ---
    <br/>



1. **How does the `$context` work with Functions?**

    |Situation | Behavior
    |-|-
    | `Comparisons` | The left of the operator maps to the `$object`
    |               | The right side is evaluated with [{Functions} 🐍](<../../...functions 🐍/{Function} 🐍.md>)
    | `Single value` | No [{Functions} 🐍](<../../...functions 🐍/{Function} 🐍.md>); all is mapped to `$object` 

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

    Commands: [`$.Msg`](<../$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`ASSERT`](<🚦 ASSERT ⌘ cmd.md>) [`SUCCESS`](<../../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>


1. **How to assert a Locator?**

    > This uses the syntax of the [`{.Parse}` 🔆 function](<../PARSE 🔆/🔆 PARSE ⌘ cmd.md>).

    ```yaml
    📃 Example:

    # Put the locator in a placeholder
    - PARSE >> $locator:
        nlweb.org/HOST:1.0,any-host.dom,ANY-RESOURCE

    # Assert for equivalence to .HOST
    - ASSERT|$locator:
        Schema: .HOST

    # Show success message.
    - SUCCESS|The schema is equivalent to ./HOST
    ```

    Commands: [`PARSE`](<../PARSE 🔆/🔆 PARSE ⌘ cmd.md>) [`SUCCESS`](<../../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>

1. **What's the syntax for enums?**

    ```yaml
    # Enum assertions
    ASSERT|$placeholder:
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
        * then a similar `~=` comparison is performed.
    
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

