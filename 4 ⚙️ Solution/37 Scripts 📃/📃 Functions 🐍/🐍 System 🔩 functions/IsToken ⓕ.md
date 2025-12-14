# 😃ⓕ Talker `.IsToken` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ


1. **What is the .IsToken function?**

    `.IsToken`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns `True` if the input is a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
    * or `False` otherwise.

    ---
    <br/>

1. **What's the syntax of .IsToken?**

    ```yaml
    $holder.IsToken
    ```

    ---
    <br/>

1. **How could it be implemented?**

    ```yaml
    📃 .IsToken:

    # Assert the Token structure
    - ASSERT $Token:

        # Group validations
        AllOf: Issued, Starts, Schema, Issuer, Signature, DKIM
        Times: Issued, Starts, Expires
        Texts: Signature, DKIM
        
        # Field validations
        Schema.IsSchema:
        Issuer.IsDomain:
        Identity.IsDomain:
        Signature.IsBase64:

        # Time validations
        Issued.IsPast:
        Expires.IsAfter: Starts
    ```

    Uses: [`.IsDomain`](<IsDomain ⓕ.md>) [`.IsSchema`](<IsSchema ⓕ.md>) 

    ---
    <br/>