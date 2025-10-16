# 🧑‍🦰🐌🤵 Assess @ Broker

> Used in:
> <br/>• [🧑‍🦰👉🤗 Scan host QR](<../../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in App 🏠/🧑‍🦰🔆🤗 Tap host locator.md>)
> <br/>• [🧑‍🦰👉🤗 Scan printer QR](<../../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in App 🏠/🧑‍🦰🔆🖨️ Tap alias locator.md>)


* Parse the [Locator 🔆](<../../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) in the [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>).
    * If the [Locator 🔆](<../../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) is an [`nlweb.dom/ALIAS 🧩`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>) 
    * then it needs to be be translated 
    * into the final [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>).


<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-id>
    To: any-broker.dom
    Subject: Assess@Broker
    
Body:
    Locator: @ALIAS,any-printer.dom,7V8KD3G
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|uuid | [Wallet 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`To`|string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`Subject`|string|`Assess@Broker`
|Body  |`Locator` |string| [Locator 🔆](<../../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) of types: <br/>- [`.HOST` 🧩](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>) <br/>- [`.ALIAS` 🧩](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
|


<br/>

## Logic

![alt text](<.📎 Assets/⚙️ Assess.png>)


| # | Call | Notes
|-|-|-
| 1 | 
| 2 | [🤵⏩🧑‍🦰 Converse 🔆](<../../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Converse 💬.md>) | Ask [Wallets 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)  to open a chat window
| 3 | [🔎⏩🧑‍🦰 Introduce 🤗](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>) | Ask [Finders 🔎](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) to introduce [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)
||
