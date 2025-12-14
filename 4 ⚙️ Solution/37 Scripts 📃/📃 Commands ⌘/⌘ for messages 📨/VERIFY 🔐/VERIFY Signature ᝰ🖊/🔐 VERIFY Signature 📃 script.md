# 🔐 Talker `VERIFY` Signature 🖋️

> About
* Part of the [`VERIFY` ⌘ command](<../🔐 VERIFY ⌘ cmd.md>)

<br/>

## Diagram

![alt text](<🔐 VERIFY Signature ⚙️ uml.png>)

<br/>

## Script 

```yaml
📃 .VERIFY-Signature:

# Assert the data structure
- ASSERT $Inputs:
    AllOf: Hash, Signature, Key, Data
    Texts: Hash, Signature, Key
    Key.IsPEM:           # PEM public key
    Hash.IsBase64:       # Base 64 hash
    Signature.IsBase64:  # Base 64 signature

# Verify the hash
- ASSERT:
    .IsHashed: $Data, $Hash

# Verify the signature
- ASSERT:
    .IsSigned: $Data, $Key, $Signature
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`SEND`](<../../SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsBase64`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsBase64 ⓕ.md>) [`.IsHashed`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsHashed ⓕ.md>) [`.IsPEM`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsPEM ⓕ.md>) [`.IsSigned`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsSigned ⓕ.md>)
|
