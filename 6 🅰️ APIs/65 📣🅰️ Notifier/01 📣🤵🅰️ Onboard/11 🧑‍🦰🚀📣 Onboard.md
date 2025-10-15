<!-- Docs: https://quip.com/zaYoA4kibXAP/-Broker-Wallets --> 
<!-- Code: -->
<!-- Test: -->


# 🧑‍🦰🚀📣 Onboard @ Notifier

A new [Wallet 🧑‍🦰 apps](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) asks a [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/$ 📣 Notifier domain.md>) to onboard.

* Used in [Onboard 🧑‍🦰👉🤵](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/11 🧑‍🦰👉🤵 Onboard.md>) to register the channel between the [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/$ 📣 Notifier domain.md>) and the [Wallet 🧑‍🦰 apps](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) (e.g., sockets). 
 
* Should wait for the notifications to start working before allowing the user to fully use the [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>).

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
|       | `To`        | string | [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/$ 📣 Notifier domain.md>) name
|       | `Subject`   | string | `Onboard@Notifier`
| Body  | `Language`  | enum   | ISO language code
|       | `PublicKey` | string | For [`Chats@Broker`](<../../15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/02 🧑‍🦰🚀🤵 Chats.md>), etc.
|

<br/>

## Synchronous Response

```yaml
WalletID: <wallet-uuid>
```


|Property|Type|Description
|-|-|-
| `Broker`        | string | [Broker 🤵](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) from [`Onboard@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/10 🤵🅰️ Wallets 🧑‍🦰/11 📣🚀🤵 Onboard.md>)
| `WalletID`      | uuid | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) ID from [`Onboard@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/10 🤵🅰️ Wallets 🧑‍🦰/11 📣🚀🤵 Onboard.md>)
|