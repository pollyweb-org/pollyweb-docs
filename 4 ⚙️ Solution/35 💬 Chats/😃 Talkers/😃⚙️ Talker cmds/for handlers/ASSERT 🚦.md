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
    ASSERT|<hint>:
        {evaluate-1}: {expect-1}
        {evaluate-N}: {expect-N}
    ```
    
    | Argument| Purpose | Examples
    |-|-|-
    | `<hint>` | Optional hint about the structure | `$locator`
    | `{evaluate}` | String or [{Function}](<../for data/{Function} 🐍.md>) to be evaluated | `A` `{f}` `{$p}`
    || Supports missing `{}` in functions | `f()` `$p`
    | `{expect}` | String or [{Function}](<../for data/{Function} 🐍.md>) of expectation  | (same)

    ---
    <br/>


1. **How to assert a Message?**

    ```yaml
    # Assert a matching pair.
    - ASSERT:
        $.Msg.From: any-broker.dom

    # Show success message.
    - SUCCESS|Message is from Any Broker
    ```

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
        Schema: .HOST

    # Show success message.
    - SUCCESS|The schema is equivalent to ./HOST
    ```

    ---
    <br/>
