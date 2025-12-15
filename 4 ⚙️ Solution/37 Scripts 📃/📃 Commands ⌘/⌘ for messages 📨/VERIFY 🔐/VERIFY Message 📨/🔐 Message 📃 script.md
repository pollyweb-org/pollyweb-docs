# 🔐 Message 📃 script

> About
* Part of the [`VERIFY` ⌘ command](<../VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)

<br/>

## Diagram

![alt text](<🔐 Message ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .VERIFY-Message:
    Message: {...}
    Key: <public-key>  # Optional
```

## Script 

```yaml
📃 .VERIFY-Message:

# Assert the data structure
- ASSERT $Message:
    AllOf: Hash, Signature, From, DKIM
    Texts: DKIM
    From.IsDomain:
    Signature.IsBase64:
    Hash.IsBase64:
    Hash.Hashes: 
        $Token.Minus: Hash, Signature

- IF $Key:
    # Verify the signature using the provided public key
    - RUN .VERIFY-Signature:
        Signature: Message.Signature
        PublicKey: $Key
        Data: 
            $Message.Minus: Signature
- ELSE:
    # Verify the domain's public key
    - RUN .VERIFY-Domain:
        Signature: $Message.Signature
        Domain: $Message.From
        DKIM: $Message.DKIM
        Data: 
            $Message.Minus: Signature
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`ELSE`](<../../../⌘ for control ▶️/ELSE ⤵️/⤵️ ELSE ⌘ cmd.md>) [`IF`](<../../../⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RUN`](<../../../⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Hashes`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/Hashes ⓕ.md>) [`.IsBase64`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsBase64 ⓕ.md>) [`.IsDomain`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.Minus`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/Minus ⓕ.md>)
