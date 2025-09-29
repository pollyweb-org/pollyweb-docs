<!-- #TODO -->

<!-- https://quip.com/EzmaAjGwmvRq#temp:C:bSR232c2e6eecff4c639e0bf6068 -->

# 🧑‍🦰🐌💳 Endorse @ [Payer](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>)

> Used in [Charge 💵👉🧑‍🦰](<../../5 ⏩ Flows/75 💵⏩ Sellers/02 💵⏩🧑‍🦰 Charge.md>)

<br/>

## Async Message 🐌

```yaml
Header:
   From: any-broker.org
   To: any-payer.org
   Subject: Endorse@Payer

Body:

   BindID: <bind-uuid>
   Collector: any-collector.org
   Chat: 
      Host: any-seller.org
      Broker: any-broker.org
      Locator: <any-locator>
      ChatID: <session-uuid>
   Charge: { ... }
```



|Property|Type|Description
|-|-|-
| `From` | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name.
| `To`| string | [Payer 💳 domain](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) name.
| `Subject` | string | `Endorse@Payer`
| `Bind`| uuid | [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) ID.
| `Collector` | string | [Collector 🏦 domain](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) name.
| `Host` | string | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) name.
| `Broker` | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name.
| `Locator` | string | [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>).
| `ChatID` | uuid | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID.
| `Charge` | object | [Charge 💵](<../../5 ⏩ Flows/75 💵⏩ Sellers/02 💵⏩🧑‍🦰 Charge.md>) flow.
|
