# 🤵 OnTokenRevised 📃 handler

<br/>

## Diagram

![alt text](<🤵 OnTokenRevised ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenRevised:

# Assert the inputs
- ASSERT|$Token:
    Texts: Status, Issuer, Token
    UUIDs: Issuer, Token

# Inform the user
- SEND:
    Header:
        To: $Token.Issuer
        Subject: Offered@Issuer
    Body:
        Token: $Token.Token
        Answer: REVISED 
```