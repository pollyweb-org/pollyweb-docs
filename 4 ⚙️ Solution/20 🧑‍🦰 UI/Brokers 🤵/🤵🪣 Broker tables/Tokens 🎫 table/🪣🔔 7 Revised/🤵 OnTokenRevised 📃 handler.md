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
    AllOf: Token, Issuer, Status, Starts
    UUIDs: Token
    Texts: Status, Issuer
    Times: Starts, Expires



# Inform the user
- SEND:
    Header:
        To: $Token.Issuer
        Subject: Offered@Issuer
    Body:
        Token: $Token.Token
        Answer: REVISED 
```