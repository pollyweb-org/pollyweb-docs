# 🔐 Talker `VERIFY` Domain 👥

> About
* Part of the [`VERIFY` ⌘ command](<../VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)

<br/>

## Diagram

![alt text](<🔐 Domain ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .VERIFY-Domain:
    Data: {...}
    DKIM: pk1
    Domain: any-domain.dom
    Signature: <base64-signature>    
```

<br/>

## Script 

```yaml
📃 .VERIFY-Domain:

# Assert the inputs
- ASSERT $.Inputs:
    AllOf: Domain, DKIM, Data, Signature
    Texts: Domain, DKIM
    Signature.IsBase64:

# Get the public key of the domain from Graph
- GRAPH PublicKey >> $publicKey:
    Domain: $Domain
    DKIM: $DKIM

# Verify the signature
- RUN .VERIFY-Signature:
    Data: $Data
    Signature: $Signature
    PublicKey: $publicKey
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GRAPH`](<../../GRAPH 🕸/🕸 GRAPH ⌘ cmd.md>) [`RUN`](<../../../⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsBase64`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsBase64 ⓕ.md>) 
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) |  [`$.Inputs`](<../../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`PublicKey@Graph` 🚀 call](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Public Key/🕸 Public Key 🚀 call.md>)
| [Scripts 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`.VERIFY-Signature` 📃 script](<../VERIFY Signature ᝰ🖊/🔐 Signature 📃 script.md>)
|
