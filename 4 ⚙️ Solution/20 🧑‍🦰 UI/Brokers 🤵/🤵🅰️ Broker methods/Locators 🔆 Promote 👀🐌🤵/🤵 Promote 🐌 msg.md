# 👀🐌🤵 Promote @ Broker
 
> Used in [👀⏩🧑‍🦰 Advertise](<../../../../45 🤲 Helper domains/Advertisers 👀/👀⏩ Advertiser flows/Advertise 👀⏩🧑‍🦰/👀 Advertise ⏩ flow.md>)

* [Advertiser 👀 helper domains](<../../../../45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) 
    * ask [Broker 🤵 domains](<../../🤵🤲 Broker helper.md>) 
    * to check-in into the selected [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>).


<br/>

## Async Message 🐌

```yaml
Header:
    From: any-advertiser.org
    To: any-broker.dom
    Subject: Promote@Broker
    
Body:
    Chat: <chat-uuid>
    Locator: nlweb.dom/LOCATOR:1.0,any-domain.dom,ANY-RESOURCE
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|           | `To`  | string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`Subject` | string | `Promote@Broker`
|Body|`Chat`  | uuid   | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>)  from [`Converse@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>)
||`Locator`  | string  | [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) to promote
|