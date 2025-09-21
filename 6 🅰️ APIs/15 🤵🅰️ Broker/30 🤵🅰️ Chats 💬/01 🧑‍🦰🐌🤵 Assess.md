# 🧑‍🦰🐌🤵 Assess @ Broker

> Parse the [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) in the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>).

> If the [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) is from a [Printer 🖨️ helper domain](<../../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) then it needs to be be translated into the final [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>).
|

> Used in:
> <br/>• [🧑‍🦰👉🤗 Scan host QR](<../../../5 ⏩ Flows/02 🧑‍🦰👉 Wallets/15 👉🔆 Locators/01 🧑‍🦰👉🤗 Scan host QR.md>)
> <br/>• [🧑‍🦰👉🤗 Scan printer QR](<../../../5 ⏩ Flows/02 🧑‍🦰👉 Wallets/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-id>
    To: any-broker.com
    Subject: Assess@Broker
Body:
    Locator: nlweb.org/QR,1,any-printer.com,7V8KD3G
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|UUID | [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) ID
||`To`|string| [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`Subject`|string|`Assess@Broker`
|Body  |`Locator` |string| QR [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) 
|

