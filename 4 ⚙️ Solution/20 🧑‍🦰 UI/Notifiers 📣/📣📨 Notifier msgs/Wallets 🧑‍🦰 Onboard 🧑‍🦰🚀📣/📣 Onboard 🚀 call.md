# 🧑‍🦰🚀📣 Onboard @ Notifier

> Implementations
* Implements the [Notifier 📣 domain](<../../📣/📣 Notifier 👥 domain.md>)

> Purpose
* A new [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) asks a [Notifier 📣 domain](<../../📣/📣 Notifier 👥 domain.md>) to onboard.

> Used in 
* [Onboard 🧑‍🦰👉🤵](<../../../Wallets 🧑‍🦰/🧑‍🦰✨ Wallet onboard 🤵/...in App/🧑‍🦰 Onboard 💬 flow.md>) to register the channel between the [Notifier 📣 domain](<../../📣/📣 Notifier 👥 domain.md>) and the [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) (e.g., sockets). 
 
> Notes
* Should wait for the notifications to start working before allowing the user to fully use the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: Anonymous
    To: any-notifier.dom
    Subject: Onboard@Notifier
Body:
    Language: en-us
    PublicKey: MIGfMA0GCSqGSI...
```

|Object|Property|Type|Description|Purpose
|-|-|-|-|-
|Header |`From`|text| `Anonymous`
|       |`To`|text| [Notifier 📣](<../../📣/📣 Notifier 👥 domain.md>) name
|       | `Subject`   |text| `Onboard@Notifier`
| Body  | `Language`  | enum   | ISO language code | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|       | `PublicKey` |text| |[`Chats@`](<../../../Brokers 🤵/🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|

<br/>

## Synchronous Response

```yaml
Wallet: <wallet-uuid>
```


|Property|Type|Description
|-|-|-
| `Broker`        |text| [Broker 🤵](<../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) from [`Onboard@Broker`](<../../../Brokers 🤵/🤵📨 Broker msgs/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 call.md>)
| `Wallet`      | uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) ID from [`Onboard@Broker`](<../../../Brokers 🤵/🤵📨 Broker msgs/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 call.md>)
|