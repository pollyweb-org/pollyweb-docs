# 🧑‍🦰🐌🤵 Assess @ Broker

> Parse the [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) in the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>).

> If the [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) is an [`nlweb.org/ALIAS 🧩`](<../../../7 🧩 Codes/🧩 Alias.md>) 
> <br/>• then it needs to be be translated into the final [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>).

> Used in:
> <br/>• [🧑‍🦰👉🤗 Scan host QR](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/01 🧑‍🦰👉🤗 Scan host QR.md>)
> <br/>• [🧑‍🦰👉🤗 Scan printer QR](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>)

<br/>

## 🐌 Async Message

```yaml
Header:
    From: <wallet-id>
    To: any-broker.com
    Subject: Assess@Broker
Body:
    Locator: nlweb.org/ALIAS:1.0,any-printer.com,7V8KD3G
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|uuid | [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) ID
||`To`|string| [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`Subject`|string|`Assess@Broker`
|Body  |`Locator` |string| [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) of types: <br/>- [`nlweb.org/HOST` 🧩](<../../../7 🧩 Codes/HOST/🧩 Host.md>) <br/>- [`nlweb.org/ALIAS` 🧩](<../../../7 🧩 Codes/🧩 Alias.md>)
|

