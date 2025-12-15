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

<br/>

## Script 

```yaml
📃 .VERIFY-Token:

# Assert the data structure
- ASSERT: $Token.IsToken

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
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GRAPH`](<../../GRAPH 🕸/🕸 GRAPH ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsToken`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsToken ⓕ.md>)  [`.IsPast`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsPast ⓕ.md>)  [`.IsFuture`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>)  
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Trusts@Graph` 🚀 call](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>) 
|
