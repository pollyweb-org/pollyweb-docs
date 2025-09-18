<!-- #TODO -->

<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ7c06cfb34057465cadb320937 -->
     

# 🤵🐌🗄️ Unbind @ Vault

> Broker unbinds a wallet user from a vault user.


## Message 🐌

|Property|Type|Description
|-|-|-
| `From` | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
| `To` | string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)
| `Subject` | string | `Unbind@Vault`

```yaml
Header:
    Subject: Unbind@Vault
Body:
    BindID: <bind-uuid>
```

## Design decisions

* Delete from 🪣 Binds