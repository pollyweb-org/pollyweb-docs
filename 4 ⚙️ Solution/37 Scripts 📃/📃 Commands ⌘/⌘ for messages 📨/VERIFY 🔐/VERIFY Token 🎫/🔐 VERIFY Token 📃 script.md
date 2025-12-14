# 🔐 Talker `VERIFY` Token 🎫

> About
* Part of the [`VERIFY` ⌘ command](<../🔐 VERIFY ⌘ cmd.md>)

<br/>

## Diagram

![alt text](<🔐 VERIFY Token ⚙️ uml.png>)

<br/>

## Script 

```yaml
📃 .VERIFY-Token:

# Assert the data structure
- ASSERT $Token:
    AllOf: Issued, Starts, Schema, Issuer, Signature, DKIM
    Times: Issued, Starts, Expires
    Texts: Signature, DKIM
    Issuer.IsDomain:    # Valid domain name
    Schema.IsSchema:    # Valid schema code
    Issued.IsPast:      # Issued is in the past
    Starts.IsPast:      # Is currently activate
    Expires.IsFuture:   # Has not expired

# Get the public key of the issuer from Graph
- SEND >> $schema:
    Header: 
        To: $.Hosted.Graph
        Subject: PublicKey@Graph
    Body:
        Issuer: $Token.Issuer
        DKIM: $Token.DKIM

- ASSERT:
    
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`SEND`](<../../SEND 📬/📬 SEND ⌘ cmd.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>) [`$.Inputs`](<../../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Trusts@Graph` 🚀 call](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>) <br/> [`PublicKey@Graph` 🚀 call](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Public Key/🕸 Public Key 🚀 call.md>)
|
