<!-- Docs: https://quip.com/zaYoA4kibXAP/-Broker-Wallets --> 
<!-- Code: -->
<!-- Test: -->


# 🧑‍🦰🚀📣 Onboard @ Notifier

A new [Wallet 🧑‍🦰 apps](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) asks a [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) to onboard.

* Used in [Onboard 🧑‍🦰👉🤵](<../../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet chats/in App 🏠/🧑‍🦰💬🤵 Onboard.md>) to register the channel between the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) and the [Wallet 🧑‍🦰 apps](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) (e.g., sockets). 
 
* Should wait for the notifications to start working before allowing the user to fully use the [Wallet 🧑‍🦰 app](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>).

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: Anonymous
    To: any-notifier.com
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
|       | `PublicKey` | string | For [`Chats@Broker`](<../../../3 🤵 Brokers/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🚀🤵 Chats.md>), etc.
|

<br/>

## Synchronous Response

```yaml
WalletID: <wallet-uuid>
```


|Property|Type|Description
|-|-|-
| `Broker`        | string | [Broker 🤵](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) from [`Onboard@Broker`](<../../../3 🤵 Brokers/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/📣🚀🤵 Onboard.md>)
| `WalletID`      | uuid | [Wallet 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) ID from [`Onboard@Broker`](<../../../3 🤵 Brokers/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/📣🚀🤵 Onboard.md>)
|