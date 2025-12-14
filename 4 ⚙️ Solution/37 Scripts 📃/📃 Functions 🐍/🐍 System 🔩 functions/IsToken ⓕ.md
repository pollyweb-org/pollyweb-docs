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
        AllOf: Issued, Starts, Schema, Issuer, Hash, Signature, DKIM
        Times: Issued, Starts, Expires
        Texts: DKIM
        
        # Field validations
        Schema.IsSchema:
        Issuer.IsDomain:
        Identity.IsDomain:

        # Time validations
        Issued.IsPast:
        Expires.IsAfter: Starts

        # Signature validations
        Hash.IsBase64:
        Signature.IsBase64:
        Hash.Hashes: 
            $Token.Minus: Hash, Signature
    ```

    Uses: [`.Hashes`](<Hashes ⓕ.md>) [`.IsAfter`](<IsAfter ⓕ.md>) [`.IsBase64`](<IsBase64 ⓕ.md>) [`.IsDomain`](<IsDomain ⓕ.md>) [`.IsPast`](<IsPast ⓕ.md>) [`.IsSchema`](<IsSchema ⓕ.md>) [`.Minus`](<Minus ⓕ.md>) 

    ---
    <br/>