# 🔐 Talker `VERIFY` Domain Signature 🖋️

> About
* Part of the [`VERIFY` ⌘ command](<../🔐 VERIFY ⌘ cmd.md>)

<br/>

## Diagram

![alt text](<🔐 Domain Signature ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .VERIFY-Domain-Signature:
    Data: {...}
    Hash: <base64-hash>
    DKIM: pk1
    Domain: any-domain.dom
    Signature: <base64-signature>    
```

<br/>

## Script 

```yaml
📃 .VERIFY-Domain-Signature:

# Assert the inputs
- ASSERT $.Inputs:
    AllOf: Domain, DKIM, Data, Hash, Signature
    Texts: Domain, DKIM
    
    # Cryptographic assertions
    Hash.IsBase64:       # Base 64 hash
    Hash.Hashes: Data    # Data matches the hash

# Get the public key of the domain from Graph
- GRAPH PublicKey >> $publicKey:
    Domain: $Domain
    DKIM: $DKIM

# Verify the signature
- RUN .VERIFY-Data-Signature:
    Data: $Data
    Hash: $Hash
    Signature: $Signature
    PublicKey: $publicKey
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GRAPH`](<../../GRAPH 🕸/🕸 GRAPH ⌘ cmd.md>) [`VERIFY`](<../🔐 VERIFY ⌘ cmd.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>) [`$.Inputs`](<../../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
|
