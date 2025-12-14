# 🔐 Talker `VERIFY` Signature 🖋️

> About
* Part of the [`VERIFY` ⌘ command](<../🔐 VERIFY ⌘ cmd.md>)

<br/>

## Diagram

![alt text](<🔐 Data Signature ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .VERIFY-Signature:
    Data: {...}
    Hash: <base64-hash>
    Signature: <base64-signature>    
    PublicKey: <base64-public-key>
```

<br/>

## Script 

```yaml
📃 .VERIFY-Data-Signature:

# Assert the data structure
- ASSERT $.Inputs:

    # Group assertions
    AllOf: Hash, Signature, PublicKey, Data
    Texts: Hash, Signature, PublicKey

    # Individual assertions
    Hash.IsBase64:       # Base 64 hash
    Signature.IsBase64:  # Base 64 signature
    PublicKey.IsPEM:     # PEM public key
    
    # Cryptographic assertions
    Hash.Hashes: Data    # Data matches the hash
    Signature.Signs:     # Signature is valid
        Data: Data
        PublicKey: PublicKey
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`SEND`](<../../SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsBase64`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsBase64 ⓕ.md>) [`.Hashes`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/Hashes ⓕ.md>) [`.IsPEM`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsPEM ⓕ.md>) [`.Signs`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/Signs ⓕ.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>) [`$.Inputs`](<../../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
|
