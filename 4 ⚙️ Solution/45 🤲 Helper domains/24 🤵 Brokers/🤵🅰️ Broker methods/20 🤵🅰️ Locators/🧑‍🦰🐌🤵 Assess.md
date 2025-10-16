# 🧑‍🦰🐌🤵 Assess @ Broker

> Used in:
> <br/>• [🧑‍🦰👉🤗 Scan host QR](<../../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/01 🧑‍🦰👉🤗 Scan host QR.md>)
> <br/>• [🧑‍🦰👉🤗 Scan printer QR](<../../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>)


* Parse the [Locator 🔆](<../../../../30 🧩 Data/15 🔆 Locators/$ 🔆 Locator.md>) in the [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>).
    * If the [Locator 🔆](<../../../../30 🧩 Data/15 🔆 Locators/$ 🔆 Locator.md>) is an [`nlweb.org/ALIAS 🧩`](<../../../75 🖨️ Printers/🖨️🧩 Printer schemas/🧩 ALIAS.md>) 
    * then it needs to be be translated 
    * into the final [Host 🤗 domain](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>).


<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-id>
    To: any-broker.com
    Subject: Assess@Broker
    
Body:
    Locator: @ALIAS,any-printer.com,7V8KD3G
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|uuid | [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)  from [`Onboard@Notifier`](<../../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`To`|string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`Subject`|string|`Assess@Broker`
|Body  |`Locator` |string| [Locator 🔆](<../../../../30 🧩 Data/15 🔆 Locators/$ 🔆 Locator.md>) of types: <br/>- [`.HOST` 🧩](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🧩 Host schemas/🧩 HOST.md>) <br/>- [`.ALIAS` 🧩](<../../../75 🖨️ Printers/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
|


<br/>

## Logic

![alt text](<.📎 Assets/⚙️ Assess.png>)


| # | Call | Notes
|-|-|-
| 1 | 
| 2 | [🤵⏩🧑‍🦰 Converse 🔆](<../../../../../5 ⏩ Flows/10 🤵⏩ Brokers/03 🤵⏩🧑‍🦰 Converse 💬.md>) | Ask [Wallets 🧑‍🦰](<../../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)  to open a chat window
| 3 | [🔎⏩🧑‍🦰 Introduce 🤗](<../../../../50 🫥 Agent domains/40 🔎 Finders/🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>) | Ask [Finders 🔎](<../../../../50 🫥 Agent domains/40 🔎 Finders/🔎🫥 Finder agent.md>) to introduce [Hosts 🤗](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>)
||
