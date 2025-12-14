# 😃ⓕ Talker `.If` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ


1. **What is the .If function?**

    `.If`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that evaluates a 1st boolean input, 
    * then returns of 2nd input if `True` 
    * or else the 3rd input if `False`.

    ---
    <br/>

1. **What's the syntax of .If?**
    
    ```yaml
    # Without context
    .If: 
        .function($context), 
        $true-value, 
        $false-value
    ```

    ```yaml
    # With context
    $context.If: 
        .function, 
        $true-value, 
        $false-value
    ```

    ```yaml
    # Comprehensive syntax
    $context.If: 
        Assert: .function
        Then: $true-value
        Else: $false-value
    ```
    ---
    <br/>