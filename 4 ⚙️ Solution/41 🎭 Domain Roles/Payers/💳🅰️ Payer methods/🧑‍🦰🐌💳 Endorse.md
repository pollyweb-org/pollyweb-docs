<!-- #TODO -->

<!-- https://quip.com/EzmaAjGwmvRq#temp:C:bSR232c2e6eecff4c639e0bf6068 -->

# 🧑‍🦰🐌💳 Endorse @ [Payer](<../💳🎭 Payer role.md>)

> Used in [Charge 💵👉🧑‍🦰](<../../Sellers 💵/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>)

<br/>

## Async Message 🐌

```yaml
Header:
   From: any-broker.dom
   To: any-payer.dom
   Subject: Endorse@Payer

Body:

   BindID: <bind-uuid>
   Collector: any-collector.dom
   Chat: 
      Host: any-seller.dom
      Broker: any-broker.dom
      Locator: <any-locator>
      ChatID: <session-uuid>
   Charge: { ... }
```



|Property|Type|Description
|-|-|-
| `From` | string | [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) name.
| `To`| string | [Payer 💳 domain](<../💳🎭 Payer role.md>) name.
| `Subject` | string | `Endorse@Payer`
| `Bind`| uuid | [Bind 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) ID.
| `Collector` | string | [Collector 🏦 domain](<../../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) name.
| `Host` | string | [Host 🤗 domain](<../../Hosts 🤗/🤗🎭 Host role.md>) name.
| `Broker` | string | [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) name.
| `Locator` | string | [Locator 🔆](<../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>).
| `ChatID` | uuid | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID.
| `Charge` | object | [Charge 💵](<../../Sellers 💵/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>) flow.
|
