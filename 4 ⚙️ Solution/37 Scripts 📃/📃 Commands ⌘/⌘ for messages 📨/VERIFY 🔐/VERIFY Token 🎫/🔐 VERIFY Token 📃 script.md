# 🔐 Talker `VERIFY` Token 🎫

> About
* Part of the [`VERIFY` ⌘ command](<../🔐 VERIFY ⌘ cmd.md>)

<br/>

## Diagram

![alt text](<🔐 VERIFY Token ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .VERIFY-Token:
    Token: {...}
```

## Script 

```yaml
📃 .VERIFY-Token:

# Assert the data structure
- ASSERT: $Token.IsToken

# Assert that we're in the validity period
- ASSERT $Token:
    Starts.IsPast:      # Is currently activate
    Expires.IsFuture:   # Has not expired

# Get the public key of the issuer from Graph
- GRAPH PublicKey >> $publicKey:
    Domain: $Token.Issuer
    DKIM: $Token.DKIM

# Verify the signature
- VERIFY $Token:
    Data: 
        $Token.Minus: Signature
    Hash: $Token.Hash
    Signature: $Token.Signature
    PublicKey: $publicKey

# Get the schema definition
- VERIFY:
    Data: $Token.Context 
    Schema: $Token.Schema

# Assert that the Token Data matches the Schema definition
- ASSERT:
    $Token.Data.Conforms: $definition
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GRAPH`](<../../GRAPH 🕸/🕸 GRAPH ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsToken`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsToken ⓕ.md>)  [`.IsPast`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsPast ⓕ.md>)  [`.IsFuture`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>)  
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Trusts@Graph` 🚀 call](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>) <br/> [`PublicKey@Graph` 🚀 call](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Public Key/🕸 Public Key 🚀 call.md>)
|
