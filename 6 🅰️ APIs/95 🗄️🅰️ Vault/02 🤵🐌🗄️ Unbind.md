<!-- #TODO -->

<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ7c06cfb34057465cadb320937 -->
     

# 🤵🐌🗄️ Unbind @ Vault

> A Broker unbinds a wallet user from a Vault.


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
|Header| `From` | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
|| `To` | string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)
|| `Subject` | string | `Unbind@Vault`
|Body| `BindID`| uuid | [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) ID

<br/>

## Steps

* Delete from 🪣 Binds
 
---