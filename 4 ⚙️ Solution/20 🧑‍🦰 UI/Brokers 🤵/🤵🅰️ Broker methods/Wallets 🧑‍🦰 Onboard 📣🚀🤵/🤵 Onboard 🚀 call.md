<!-- Docs: https://quip.com/zaYoA4kibXAP/-Broker-Wallets#temp:C:DQN1f2d80d98fdd4e69a98a32887 -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/143c4c876bdd0dd8b120bdfecf20ef6b268ad20f/python/roles/broker/BROKER_WALLETS.py#L40 -->

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
|Header|`From`|string| [Notifier 📣 domain](<../../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) name
||`To`|string| [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) name
||`Subject`| string | `Onboard@Broker`
|Body| `Language` | enum | ISO language code.
|| `PublicKey`| string | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) generated public key
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

