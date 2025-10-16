<!-- #TODO -->

<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->


# 🤵🐌📣 Charge @ [Notifier](<../../📣👥 Notifier domain.md>)


> Used in [💵⏩🧑‍🦰 Charge](<../../../../41 🎭 Domain Roles/Sellers 💵/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Charge@Notifier
    
Body:
    WalletID: <wallet-uuid>
    ChatID: <chat-uuid>
    Amount: <amount>
    Currency: <currency>
    Reason: <reason>
```