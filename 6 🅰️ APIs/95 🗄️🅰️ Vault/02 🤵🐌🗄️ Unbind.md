<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ7c06cfb34057465cadb320937 -->
     

# 🤵🐌🗄️ Unbind @ Vault

> A [Broker 🤵 domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) unbinds a [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)  from a [Vault 🗄️ domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>).

> Part of the [🧑‍🦰👉🗄️ Unbind @ Wallet](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/03 🧑‍🦰👉🗄️ Unbind.md>) flow.


<br/>

## Async Message 🐌


```yaml
Header:
    From: any-broker.com
    To: any-vault.com
    Subject: Unbind@Vault
    
Body:
    BindID: <bind-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From` | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>)
|| `To` | string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>)
|| `Subject` | string | `Unbind@Vault`
|Body| `BindID`| uuid | [Bind 🔗](<../../4 ⚙️ Solution/30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>) ID
|

