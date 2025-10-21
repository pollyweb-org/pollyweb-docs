# 🚦 Talker `ASSERT` command

> Part of [Talker 😃](<../../😃 Talker.md>)


<!-- TODO: examples -->
> Used by [`Accepted@Issuer`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🤵🐌🎴 Accepted.md>)

<br/>

1. **What's the ASSERT command?**

    An `ASSERT`
    * is a handler [Command ⌘](<../for control/⌘ Command.md>) 
    * that verifies data assumptions.
  
    ---
    <br/>

1. **What's the syntax of ASSERT?**

    ```yaml
    ASSERT|$object:

        # Comparisons
        - {value-1} {comparison} {value-2} 

        # Boolean assertions
        - {boolean-value}       
        
        # Empty or missing assertions
        - {empty-value}   
        - {empty-array-value}   
        - {empty-object-value}  
    ```
    
    | Argument| Purpose | Examples
    |-|-|-
    | `$object`| Optional initial context | `$.Msg` `$1`
    | `{value}` | String or [{Function}](<../for data/{Function} 🐍.md>) evaluated | `A` `{f}` `{$p}`
    || Supports missing `{}`  | `f()` `$p`
    | `{comparison}` | `=` `~=` `!=` `>` `>=` `<` `<=` 
    | `{boolean}` | ✅ Valid for meaningful values | `1` `-1` `True` `A`
    || ❌ Fails on empty meanings | `0` `False` `$p=`
    | `{empty-array}` | ✅ Valid for arrays with values | `[0]` `[*]` |
    | | ❌ Fails on empty arrays  | `[]` `$p=`
    | `{empty-object}` | ✅ Valid for objects with values | `{A:0}`
    | | ❌ Fails on empty objects | `{}` `$p=`

    ---
    <br/>

1. **How does the `$context` work with Functions?**

    |Situation | Behavior
    |-|-
    | `Comparisons` | The left of the operator maps to the `$object`
    |               | The right side is evaluated with [{Functions} 🐍](<{Function} 🐍.md>)
    | `Single value` | No [{Functions} 🐍](<{Function} 🐍.md>); all is mapped to `$object` 

    ---
    <br/>

1. **What's the meaning of equal comparisons?**

    | | Meaning | Valid results ✅
    |-|-|-
    | `=`  | Same meaning | `a = b` `A = B` 
    |       | Same math | `1 = 1.0` `01 = 1` 
    |       | Same array order | `[1,2] = [1,2]`
    |       | Same object order | `{A:1, B:2} = {A:2, B:1}`
    | `!=` | Different meaning | `a != b`  
    |       | Different math | `1 != 1.1`
    |       | Different array content | `[1] = [1,2,3]`
    |       | Different object content | `{A:1} = {A:1, B:2, C:3}`
    | `~=` | Same content out of order | `[1,2] = [2,1]`
    |       | Same content out of order | `{A:1, B:2} = {B:2, A:1}`
    |       |Same [Schema 🧩 code](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | `.HOST ~= nlweb.org/HOST:1.0 `|
    |       | Same [domain 👥](<../../../../40 👥 Domains/👥 Domain.md>) name | `domain.dom ~= DOMAIN.DOM`
    |       | Same [`{.Today}` 🐍](<../for data/{Function} 🐍.md>) date | `~= 2013-04-01T05:00:30.001Z`
    
    

    ---
    <br/>

1. **How to assert a Message?**

    ```yaml
    # Assert a matching pair
    - ASSERT|$.Msg:
        - From ~= any-broker.dom

    # Show success message
    - SUCCESS|Message is from Any Broker
    ```

    Commands: [`$.Msg`](<$.Msg 📨.md>) [`ASSERT`](<ASSERT 🚦.md>) [`SUCCESS`](<../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>)

    ---
    <br/>


1. **How to assert a Locator?**

    > This uses the syntax of the [`{.Parse}` 🔆 function](<PARSE 🔆.md>).

    ```yaml
    # Put the locator in a placeholder
    - EVAL >> $locator:
        nlweb.org/HOST:1.0,any-host.dom,ANY-RESOURCE

    # Assert for equivalence to .HOST
    - ASSERT|$locator:
        - Schema ~= .HOST

    # Show success message.
    - SUCCESS|The schema is equivalent to ./HOST
    ```

    Commands: [`EVAL`](<../for data/EVAL ⬇️ flow.md>) [`SUCCESS`](<../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>)

    ---
    <br/>
