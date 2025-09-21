<!-- #TODO -->

<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->


# 🤵🐌📣 Updated @ [Notifier](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>)

> The Broker domain tells the [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) that there was an update and they need to refresh the user experience.

> Used in:
> <br/>• [🧑‍🦰👉🤵 List chats](<../../../5 ⏩ Flows/02 🧑‍🦰👉 Wallets/20 👉💬 Chats/01 🧑‍🦰👉🤵 List chats.md>)
> <br/>• [🧑‍🦰👉🤵 List binds](<../../../5 ⏩ Flows/02 🧑‍🦰👉 Wallets/30 👉🔗 Binds/01 🧑‍🦰👉🤵 List binds.md>)
> <br/>• [🤵⏩🧑‍🦰 Update binds](<../../../5 ⏩ Flows/08 🤵⏩ Brokers/03 🤵⏩🧑‍🦰 Update binds.md>)
> <br/>• [🤵⏩🧑‍🦰 Update tokens](<../../../5 ⏩ Flows/08 🤵⏩ Brokers/04 🤵⏩🧑‍🦰 Update tokens.md>)
> <br/>• [🤵⏩🧑‍🦰 Update chats](<../../../5 ⏩ Flows/08 🤵⏩ Brokers/05 🤵⏩🧑‍🦰 Update chats.md>)

<br/>

## Async Message 🐌

```yaml

Header:
    From: any-broker.com
    To: any-notifier.com
    Subject: Updated@Notifier
Body:
    WalletID: <wallet-uuid>
    Update: Chats | Binds | Tokens
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | Broker domain name
||`To`|string| [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) name
||`Subject`|string|`Updated@Notifier`
|Body  |`WalletID` |UUID  | Wallet ID on the Broker domain
|      |`Update`   |enum[]  | Enum: CHATS
