<!-- #TODO -->

<!-- https://quip.com/EzmaAjGwmvRq#temp:C:bSR232c2e6eecff4c639e0bf6068 -->

# 🧑‍🦰🐌💳 Endorse @ [Payer](<../../💳🎭 Payer role.md>)

> Used in [Charge 💵👉🧑‍🦰](<../../../Sellers 💵/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>)

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
|`From`|domain| [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/Broker 🤵 helper 🤲.md>) name.
|`To`|domain| [Payer 💳 domain](<../../💳🎭 Payer role.md>) name.
| `Subject` | string | `Endorse@Payer`
| `Bind`| uuid | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) ID.
| `Collector` | string | [Collector 🏦 domain](<../../../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) name.
| `Host` | string | [Host 🤗 domain](<../../../Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name.
| `Broker` | string | [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/Broker 🤵 helper 🤲.md>) name.
| `Locator` | string | [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>).
| `Chat` | uuid | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID.
| `Charge` | object | [Charge 💵](<../../../Sellers 💵/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>) flow.
|
