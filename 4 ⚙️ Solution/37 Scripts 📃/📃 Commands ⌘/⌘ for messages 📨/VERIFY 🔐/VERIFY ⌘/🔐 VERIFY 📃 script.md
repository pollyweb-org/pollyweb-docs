# 🔐 VERIFY 📃 script

> About
* Implements the [`VERIFY` ⌘ command](<🔐 VERIFY ⌘ cmd.md>)

<br/>


## Script 

```yaml
📃 .VERIFY:

# Check if it is a Schema
# ------------------------------
- IF .AllOf:
    $Data,
    $Schema
- THEN:
    - RUN .VERIFY-Schema:
        Data: $Data
        Schema: $Schema
    - RETURN

# Check if it is a Message
# ------------------------------
- IF .AnyOf:
    $Data.Header,
    $Message
- THEN:
    - RUN .VERIFY-Message:
        PublicKey: $PublicKey
        Message: 
            $Message.Default: $Data
    - RETURN

# Check if it is a Token
# ------------------------------
- IF .AnyOf:
    $Data.Issuer,
    $Token
- THEN:
    - RUN .VERIFY-Token:
        Token: 
            $Token.Default: $Data
    - RETURN

# Invalid input if none matched
# ------------------------------
- HTTP: 400|Invalid input
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`HTTP`](<../../../⌘ for control ▶️/HTTP 💥/💥 HTTP ⌘ cmd.md>) [`IF`](<../../../⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RETURN`](<../../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../../⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`THEN`](<../../../⌘ for control ▶️/THEN ⤵️/⤵️ THEN ⌘ cmd.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.AllOF`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/AllOf ⓕ.md>) [`.AnyOf`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/AnyOf ⓕ.md>)
| [Scripts 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`.VERIFY-Message`](<../VERIFY Message 📨/🔐 Message 📃 script.md>) [`.VERIFY-Schema`](<../VERIFY Schema 🧩/🔐 Schema 📃 script.md>) [`.VERIFY-Token`](<../VERIFY Token 🎫/🔐 Token 📃 script.md>)
|
