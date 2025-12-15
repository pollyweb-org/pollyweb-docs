# 🔐 Talker `VERIFY` Signature 🖋️

> About
* Part of the [`VERIFY` ⌘ command](<../VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)

<br/>

## Diagram

![alt text](<🔐 Signature ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .VERIFY-Signature:
    Data: {...}
    Signature: <base64-signature>    
    PublicKey: <base64-public-key>
```

<br/>

## Script 

```yaml
📃 .VERIFY-Signature:

# Assert the data structure
- ASSERT $.Inputs:
    Error: Invalid signature structure
    
    # Group assertions
    AllOf: Signature, PublicKey, Data
    Texts: Signature, PublicKey

    # Base 64 encryption
    PublicKey.IsBase64:    
    Signature.IsBase64:  

# Assert the PEM public key
- ASSERT $.Inputs:
    Error: Invalid public key PEM
    PublicKey.IsPEM:

# Assert the signature is valid
- ASSERT $.Inputs:
    Error: Signature verification failed
    Signature.Signs:     
        Data: Data
        PublicKey: PublicKey
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`SEND`](<../../SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsBase64`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsBase64 ⓕ.md>)  [`.IsPEM`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsPEM ⓕ.md>) [`.Signs`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/Signs ⓕ.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>) [`$.Inputs`](<../../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>) 
|
