<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ7c06cfb34057465cadb320937 -->
     

# 🤵🐌🗄️ Unbound @ Vault

> A [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) unbinds a [Wallet 🧑‍🦰 app](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  from a [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>).

> Part of the [🧑‍🦰👉🗄️ Unbind @ Wallet](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Vaults 🗄️/💬🤵 Unbind 🗄️.md>) flow.


<br/>

## Async Message 🐌


```yaml
Header:
    From: any-broker.dom
    To: any-vault.dom
    Subject: Unbound@Vault
    
Body:
    Bind: <bind-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From` | string | [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) from [`Bound@Vault`](<🤵🐌🗄️ Bound.md>)
|| `To` | string | [Vault 🗄️](<../../🗄️🎭 Vault role.md>) from [`Bound@Vault`](<🤵🐌🗄️ Bound.md>)
|| `Subject` | string | `Unbound@Vault`
|Body| `Bind`| uuid | [Bind 🔗 ID](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)  from [`Bound@Vault`](<🤵🐌🗄️ Bound.md>)
|



<br/>

## Handler

```yaml
- DELETE|Binds@Vault:
    Broker: $Msg.From
    Bind: $bind.Bind
```
