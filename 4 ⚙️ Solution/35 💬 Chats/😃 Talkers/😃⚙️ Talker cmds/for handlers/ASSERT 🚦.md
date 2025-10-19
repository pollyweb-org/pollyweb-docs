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
    ASSERT:
        {evaluate-1}: {expect-1}
        {evaluate-N}: {expect-N}
    ```
    
    | Argument| Purpose | Examples
    |-|-|-
    | `{evaluate}` | String or [{Function}](<../for data/{Function} 🐍.md>) to be evaluated | `A` `{f}` `{$p}`
    || Supports missing `{}` in functions | `f()` `$p`
    | `{expect}` | String or [{Function}](<../for data/{Function} 🐍.md>) of expectation  | (same)

    ---
    <br/>


1. **What's an example of ASSERT?**

    ```yaml
    - ASSERT:
        $.Msg.From: $broker
    - SUCCESS|Message is from the broker.
    ```

    ---
    <br/>
