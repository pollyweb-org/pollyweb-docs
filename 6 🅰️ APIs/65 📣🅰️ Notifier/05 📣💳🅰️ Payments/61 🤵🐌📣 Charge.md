<!-- #TODO -->

<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->


# 🤵🐌📣 Charge @ [Notifier](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>)


> Used in [💵⏩🧑‍🦰 Charge](<../../../5 ⏩ Flows/75 💵⏩ Sellers/02 💵⏩🧑‍🦰 Charge.md>)

<br/>

## 🐌 Async Message

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