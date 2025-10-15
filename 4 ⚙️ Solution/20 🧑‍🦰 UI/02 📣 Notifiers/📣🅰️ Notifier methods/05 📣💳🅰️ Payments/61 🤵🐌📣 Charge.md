<!-- #TODO -->

<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->


# 🤵🐌📣 Charge @ [Notifier](<../../📣 Notifier domain.md>)


> Used in [💵⏩🧑‍🦰 Charge](<../../../../41 🎭 Domain Roles/70 💵 Sellers/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.com
    To: any-notifier.com
    Subject: Charge@Notifier
    
Body:
    WalletID: <wallet-uuid>
    ChatID: <chat-uuid>
    Amount: <amount>
    Currency: <currency>
    Reason: <reason>
```