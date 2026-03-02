<!-- TODO: add the code -->
<!-- TODO: add a script diagram -->

# 👀🐌🤵 Promote @ Broker
 
> Used in [👀⏩🧑‍🦰 Advertise](<../../../../45 🤲 Helper domains/Advertisers 👀/👀⏩ Advertiser flows/Advertise 👀⏩🧑‍🦰/👀 Advertise ⏩ flow.md>)

* [Advertiser 👀 helper domains](<../../../../45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) 
    * ask [Broker 🤵 domains](<../../🤵/🤵 Broker 🤲 helper.md>) 
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
    Locator: pollyweb.org/LOCATOR:1.0,any-domain.dom,ANY-RESOURCE
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header    |`From`| uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
|           |`To`|text| [Broker 🤵](<../../🤵/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`Subject` |text| `Promote@Broker`
|Body|`Chat`  | uuid   | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)  | [`Open@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
||`Locator`  | string  | [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) to promote
|