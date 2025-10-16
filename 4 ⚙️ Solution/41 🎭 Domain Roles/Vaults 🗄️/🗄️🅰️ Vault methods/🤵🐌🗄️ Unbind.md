<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ7c06cfb34057465cadb320937 -->
     

# 🤵🐌🗄️ Unbind @ Vault

> A [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) unbinds a [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)  from a [Vault 🗄️ domain](<../🗄️🎭 Vault role.md>).

> Part of the [🧑‍🦰👉🗄️ Unbind @ Wallet](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Vaults 🗄️/💬🤵 Unbind 🗄️.md>) flow.


<br/>

## Async Message 🐌


```yaml
Header:
    From: any-broker.dom
    To: any-vault.dom
    Subject: Unbind@Vault
    
Body:
    BindID: <bind-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From` | string | [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>)
|| `To` | string | [Vault 🗄️ domain](<../🗄️🎭 Vault role.md>)
|| `Subject` | string | `Unbind@Vault`
|Body| `BindID`| uuid | [Bind 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) ID
|

