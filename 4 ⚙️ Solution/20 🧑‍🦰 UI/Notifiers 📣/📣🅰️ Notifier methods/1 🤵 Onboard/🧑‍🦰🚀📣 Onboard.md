<!-- Docs: https://quip.com/zaYoA4kibXAP/-Broker-Wallets --> 
<!-- Source: -->
<!-- Test: -->


# 🧑‍🦰🚀📣 Onboard @ Notifier

> Implements the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>)

> Purpose

* A new [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) asks a [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) to onboard.

> Used in 
* [Onboard 🧑‍🦰👉🤵](<../../../Wallets 🧑‍🦰/🧑‍🦰✨ Wallet onboard/💬🤵 Onboard.md>) to register the channel between the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) and the [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) (e.g., sockets). 
 
> Notes
* Should wait for the notifications to start working before allowing the user to fully use the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: Anonymous
    To: any-notifier.dom
    Subject: Onboard@Notifier
Body:
    Language: en-us
    PublicKey: MIGfMA0GCSqGSI...
```

|Object|Property|Type|Description
|-|-|-|-
|Header | `From`      | string | `Anonymous`
|       | `To`        | string | [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) name
|       | `Subject`   | string | `Onboard@Notifier`
| Body  | `Language`  | enum   | ISO language code
|       | `PublicKey` | string | For [`Chats@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/...for Chats 💬/Chats 🧑‍🦰🚀🤵/Chats 🚀 request.md>), etc.
|

<br/>

## Synchronous Response

```yaml
Wallet: <wallet-uuid>
```


|Property|Type|Description
|-|-|-
| `Broker`        | string | [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) from [`Onboard@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/...for Wallets 🧑‍🦰/Onboard 📣🚀🤵/Onboard 🚀 request.md>)
| `Wallet`      | uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) ID from [`Onboard@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/...for Wallets 🧑‍🦰/Onboard 📣🚀🤵/Onboard 🚀 request.md>)
|