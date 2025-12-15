<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ7c06cfb34057465cadb320937 -->
     

# 🤵🐌🗄️ Unbound @ Vault

> Part of the [🧑‍🦰👉🗄️ Unbind @ Wallet](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/Unbind 💬🗄️🤵 /🧑‍🦰 Unbind vault ⏩ flow.md>) flow.

* Implemented by the [`Unbound` 📃 handler](<🗄️ Unbound 📃 handler.md>)

> Purpose

* A [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * unbinds a [Wallet 🧑‍🦰 app](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  
    * from a [Vault 🗄️ domain](<../../🗄️ Vault/🗄️🎭 Vault role.md>).



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

|Object|Property|Type|Description|Origin
|-|-|-|-|-
|Header|`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Bound@`](<../Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
||`To`|text| [Vault 🗄️](<../../🗄️ Vault/🗄️🎭 Vault role.md>) | [`Bound@`](<../Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|| `Subject` |text| `Unbound@vault`
|Body| `Bind`| uuid | [Bind 🔗 ID](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)  | [`Bound@`](<../Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|

