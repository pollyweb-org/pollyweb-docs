<!-- #TODO -->

<!-- Docs: https://quip.com/zaYoA4kibXAP/-Broker-Wallets#temp:C:DQN0cc419509625497ea39fa08e9 -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/143c4c876bdd0dd8b120bdfecf20ef6b268ad20f/python/roles/broker/BROKER_WALLETS.py#L76 -->


# 🧑‍🦰🐌🤵 Translate @ [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)

## Async Message 🐌


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | UUID | ID of the [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) on the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>).
||`To`| string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`Subject`| string | `Translate@Broker`
|Body|`Language`| string | ISO language code.
|

```yaml
Header: 
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Translate@Broker

Body:
    Language: en-us
```