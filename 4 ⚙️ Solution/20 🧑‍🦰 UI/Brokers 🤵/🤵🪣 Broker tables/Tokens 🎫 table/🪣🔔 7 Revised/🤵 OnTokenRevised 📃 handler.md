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
- SAVE|Broker.Chats:
    Wallet: $Token.Wallet
    Host: $.Hosted.Domain
    Inputs:
        Context: TOKEN.REVISED
        Token: $Token.Token
        Issuer: $Token.Issuer
```