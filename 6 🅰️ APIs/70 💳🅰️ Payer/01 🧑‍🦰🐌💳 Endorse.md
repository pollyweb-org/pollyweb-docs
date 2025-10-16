<!-- #TODO -->

<!-- https://quip.com/EzmaAjGwmvRq#temp:C:bSR232c2e6eecff4c639e0bf6068 -->

# 🧑‍🦰🐌💳 Endorse @ [Payer](<../../4 ⚙️ Solution/50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>)

> Used in [Charge 💵👉🧑‍🦰](<../../4 ⚙️ Solution/41 🎭 Domain Roles/70 💵 Sellers/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>)

<br/>

## Async Message 🐌

```yaml
Header:
   From: any-broker.com
   To: any-payer.org
   Subject: Endorse@Payer

Body:

   BindID: <bind-uuid>
   Collector: any-collector.org
   Chat: 
      Host: any-seller.org
      Broker: any-broker.com
      Locator: <any-locator>
      ChatID: <session-uuid>
   Charge: { ... }
```



|Property|Type|Description
|-|-|-
| `From` | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) name.
| `To`| string | [Payer 💳 domain](<../../4 ⚙️ Solution/50 🫥 Agent domains/60 💳 Payers/03 💳🎭 Payer role.md>) name.
| `Subject` | string | `Endorse@Payer`
| `Bind`| uuid | [Bind 🔗](<../../4 ⚙️ Solution/30 Data/2 🔗 Binds/🔗 Bind.md>) ID.
| `Collector` | string | [Collector 🏦 domain](<../../4 ⚙️ Solution/45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>) name.
| `Host` | string | [Host 🤗 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) name.
| `Broker` | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) name.
| `Locator` | string | [Locator 🔆](<../../4 ⚙️ Solution/25 Locators/1 🔆 Locators/🔆 Locator.md>).
| `ChatID` | uuid | [Chat 💬](<../../4 ⚙️ Solution/35 Chats/💬 Chats/💬 Chat.md>) ID.
| `Charge` | object | [Charge 💵](<../../4 ⚙️ Solution/41 🎭 Domain Roles/70 💵 Sellers/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>) flow.
|
