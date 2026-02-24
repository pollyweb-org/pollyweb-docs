<!-- #TODO -->
# 🧑‍🦰🐌💳 Endorse @ [Payer](<../../💳🎭 Payer role.md>)

> Used in [Charge 💵👉🧑‍🦰](<../../../Sellers 💵/💵⏩ Seller flows/Charge 💵⏩🧑‍🦰/💵 Charge ⏩ flow.md>)

<br/>

## Async Message 🐌

```yaml
Header:
   From: any-broker.dom
   To: any-payer.dom
   Subject: Endorse@Payer

Body:

   Bind: <bind-uuid>
   Collector: any-collector.dom
   Chat: 
      Host: any-seller.dom
      Broker: any-broker.dom
      Locator: <any-locator>
      Chat: <session-uuid>
   Charge: { ... }
```



|Property|Type|Description
|-|-|-
|`From`|text| [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) name.
|`To`|text| [Payer 💳 domain](<../../💳🎭 Payer role.md>) name.
| `Subject` |text| `Endorse@Payer`
| `Bind`| uuid | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) ID.
| `Collector` |text| [Collector 🏦 domain](<../../../../45 🤲 Helper domains/Collectors 🏦/🏦 Collector/🏦🤲 Collector helper.md>) name.
| `Host` |text| [Host 🤗 domain](<../../../Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name.
| `Broker` |text| [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) name.
| `Locator` |text| [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>).
| `Chat` | uuid | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID.
| `Charge` | object | [Charge 💵](<../../../Sellers 💵/💵⏩ Seller flows/Charge 💵⏩🧑‍🦰/💵 Charge ⏩ flow.md>) flow.
|
