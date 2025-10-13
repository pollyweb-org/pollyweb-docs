# 🧑‍🦰🐌🤵 Assess @ Broker

> Used in:
> <br/>• [🧑‍🦰👉🤗 Scan host QR](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/01 🧑‍🦰👉🤗 Scan host QR.md>)
> <br/>• [🧑‍🦰👉🤗 Scan printer QR](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>)


* Parse the [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) in the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>).
    * If the [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) is an [`nlweb.org/ALIAS 🧩`](<../../../7 🧩 Codes/$/🧩 Alias.md>) 
    * then it needs to be be translated 
    * into the final [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>).


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
|Header|`From`|uuid | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)  from [`Onboard@Notifier`](<../../65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
||`To`|string| [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) from [`Onboard@Notifier`](<../../65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
||`Subject`|string|`Assess@Broker`
|Body  |`Locator` |string| [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) of types: <br/>- [`.HOST` 🧩](<../../../7 🧩 Codes/HOST/🧩 Host.md>) <br/>- [`.ALIAS` 🧩](<../../../7 🧩 Codes/$/🧩 Alias.md>)
|


<br/>

## Logic

![alt text](<.📎 Assets/⚙️ Assess.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🚀🖨️ `Alias@Printer`](<../../75 🖨️🅰️ Printer/01 👥🚀🖨️ Alias.md>) | Ask [Printers 🖨️](<../../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) to translate [`.ALIAS` 🧩](<../../../7 🧩 Codes/$/🧩 Alias.md>)
| 2 | [🤵⏩🧑‍🦰 Assessed 🔆](<../../../5 ⏩ Flows/10 🤵⏩ Brokers/02 🤵⏩🧑‍🦰 Assessed 🔆.md>) | Ask [Wallets 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)  to open a chat window
| 3 | [🔎⏩🧑‍🦰 Introduce 🤗](<../../../5 ⏩ Flows/40 🔎⏩ Finders/01 🔎⏩🧑‍🦰 Introduce 🤗.md>) | Ask [Finders 🔎](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) to introduce [Hosts 🤗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)
||
