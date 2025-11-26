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
    AllOf: Token, Issuer, Status, Starts, Wallet
    UUIDs: Token, Wallet
    Texts: Status, Issuer
    Times: Starts, Expires

# Open a Pop to inform the user
- SAVE|Broker.Pops:
    Wallet: $Token.Wallet
    Context: TOKEN.REVISED
    Key: 
        Token: $Token.Token
        Issuer: $Token.Issuer
```