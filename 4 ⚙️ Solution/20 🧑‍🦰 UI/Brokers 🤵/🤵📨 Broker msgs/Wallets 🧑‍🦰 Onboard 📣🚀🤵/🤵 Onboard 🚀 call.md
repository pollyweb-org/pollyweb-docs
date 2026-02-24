<!-- TODO: add a script diagram -->

# 📣🚀🤵 Onboard @ Broker


> Used in [Onboard 👉](<../../../Wallets 🧑‍🦰/🧑‍🦰✨ Wallet onboard 🤵/...in App/🧑‍🦰 Onboard 💬 flow.md>)
> 
<br/>

## Synchronous Call 🚀


```yaml
Header:
    From: any-notifier.dom
    To: any-broker.dom
    Subject: Onboard@Broker

Body:
    Language: en-us
    PublicKey: MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDH+wPr...
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|text| [Notifier 📣 domain](<../../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) name
||`To`|text| [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) name
||`Subject`|text| `Onboard@Broker`
|Body| `Language` | enum | ISO language code.
|| `PublicKey`|text| [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) generated public key
|

<br/>


## Sync Response

```yaml
Wallet: <wallet-uuid>
```

|Property|Type|Description
|-|-|-
| `Wallet` | uuid | The newly generated Wallet ID.
|

