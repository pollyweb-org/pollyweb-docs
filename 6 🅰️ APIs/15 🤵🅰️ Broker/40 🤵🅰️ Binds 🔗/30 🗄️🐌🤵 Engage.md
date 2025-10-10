# 🗄️🐌🤵 Engage

> Part of [🗄️⏩🧑‍🦰 Engage @ Vault](<../../../5 ⏩ Flows/80 🗄️⏩ Vaults/04 🗄️⏩🧑‍🦰 Engage.md>)

<br/>

## 🐌 Async Message

```yaml
Header:
    From: any-vault.com
    To: any-broker.com
    Subject: Help@Broker

Body:
    Bind: <bind-id>

```
| Object | Property | Type |Description
|-|-|-|-
| Header | `From`    | string | [Vault 🗄️ domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) name
|| `To`      | string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
|| `Subject` | string | `Engage@Broker`
| Body | `BindID`  | uuid   | [Bind 🔗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) of [Host 🧩](<../../../7 🧩 Codes/HOST/🧩 Host.md>)
|