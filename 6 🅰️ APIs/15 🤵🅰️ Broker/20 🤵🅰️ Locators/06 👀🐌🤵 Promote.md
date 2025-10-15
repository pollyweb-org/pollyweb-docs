# 👀🐌🤵 Promote @ Broker
 
> Used in [👀⏩🧑‍🦰 Advertise](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/12 👀 Advertisers/01 👀⏩🧑‍🦰 Advertise.md>)

* [Advertiser 👀 helper domains](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/12 👀 Advertisers/$ 👀👥 Advertiser helper.md>) 
    * ask [Broker 🤵 domains](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) 
    * to check-in into the selected [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>).


<br/>

## Async Message 🐌

```yaml
Header:
    From: any-advertiser.org
    To: any-broker.com
    Subject: Promote@Broker
    
Body:
    ChatID: <chat-uuid>
    Locator: nlweb.org/LOCATOR:1.0,any-domain.com,ANY-RESOURCE
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)  from [`Onboard@Notifier`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/📣🅰️ Notifier methods/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
|           | `To`  | string| [Broker 🤵](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) from [`Onboard@Notifier`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/📣🅰️ Notifier methods/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
||`Subject` | string | `Promote@Broker`
|Body|`ChatID`  | uuid   | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)  from [`Converse@Notifier`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/📣🅰️ Notifier methods/02 📣💬🅰️ Chats/21 🤵🐌📣 Converse.md>)
||`Locator`  | string  | [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) to promote
|