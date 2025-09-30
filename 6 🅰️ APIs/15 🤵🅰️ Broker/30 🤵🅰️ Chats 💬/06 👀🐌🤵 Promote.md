<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->


# 👀🐌🤵 Promote @ Broker

> Ask the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) to check-in into the selected [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>).

> Used in [👀⏩🧑‍🦰 Advertise](<../../../5 ⏩ Flows/05 👀⏩ Advertisers/01 👀⏩🧑‍🦰 Advertise.md>)

<br/>

## 🐌 Async Message

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
|Header|`From`     | string  | [Advertiser 👀 domain](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>)
||`To`       | string  | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
||`Subject` | string | `Promote@Broker`
|Body|`ChatID`        | uuid    | ID of the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
||`Locator`  | string  | [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) to promote
|