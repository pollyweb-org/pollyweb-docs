# 🔐 Token 📃 script

> About
* Part of the [`VERIFY` ⌘ command](<../VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)

<br/>


## Diagram

![alt text](<🔐 Token ⚙️ uml.png>)

<br/>


## How to call

```yaml
- RUN .VERIFY-Token:
    Token: {...}
```

<br/>

## Script 

```yaml
📃 .VERIFY-Token:

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

# Assert that we're in the validity period
- ASSERT $Token:
    Starts.IsPast:      # Is currently activate
    Expires.IsFuture:   # Has not expired

# Check if the issuer is trusted
- TRUSTS:
    Trusted: $Token.Issuer
    Schema: $Token.Schema
    Role: VAULT

# Verify the domain signature
- RUN .VERIFY-Domain:
    Data: 
        $Token.Minus: Signature
    DKIM: $Token.DKIM
    Domain: $Token.Issuer
    Signature: $Token.Signature

# Verify the schema
- RUN .VERIFY-Schema:
    Data: $Token.Context 
    Schema: $Token.Schema

# Check that the status on the broker
- SEND >> $status:
    Header:
        To: $Token.Broker
        Subject: Status@Broker
    Body:
        Token: $Token.Token
        Issuer: $Token.Issuer
- ASSERT: 
    $status.Status: ACTIVE
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GRAPH`](<../../GRAPH 🕸/🕸 GRAPH ⌘ cmd.md>) [`SEND`](<../../SEND 📬/📬 SEND ⌘ cmd.md>) [`TRUSTS`](<../../TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) |  [`.IsFuture`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>)  [`.Hashes`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/Hashes ⓕ.md>) [`.IsAfter`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsAfter ⓕ.md>) [`.IsBase64`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsBase64 ⓕ.md>)<br/> [`.IsDomain`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsPast`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsPast ⓕ.md>) [`.IsSchema`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>) [`.Minus`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/Minus ⓕ.md>) 
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Status@Broker` 🚀 call](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Status 💼🚀🤵/🤵 Status 🚀 call.md>)
| [Scripts 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`.VERIFY-Domain`](<../VERIFY Domain 👥/🔐 Domain 📃 script.md>) [`.VERIFY-Schema`](<../VERIFY Schema 🧩/🔐 Schema 📃 script.md>)
|
