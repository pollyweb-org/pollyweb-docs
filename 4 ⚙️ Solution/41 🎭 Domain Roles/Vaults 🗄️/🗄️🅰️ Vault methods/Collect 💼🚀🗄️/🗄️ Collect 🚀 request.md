<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ67394972376e4fb8979d41209 -->


# 💼🚀🗄️ Collect @ Vault

> Flow
* Part of the [`Consume flow`](<../../🗄️⏩ Vault flows/Consume 🗄️⏩💼/🗄️ Consume ⏩ flow.md>)
* Preceded by [`Consume@Consumer`](<../../../Consumers 💼/💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>)


> Purpose

* Tells it to reply with the data [shared](<../../../Consumers 💼/💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>) by the user.

> Used by 
* [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>)


<br/>

## Sync Request 🚀

````yaml
Header:
    From: any-consumer.dom
    To: any-vault.dom
    Subject: Collect@Vault

Body:
    Collect: <collect-uuid> 
````

|Object|Property|Type|Description|Origin
|-|-|-|-|-|
|Header|`From`|domain| [Consumer 💼](<../../../Consumers 💼/💼🎭 Consumer role.md>) | [`Consume@`](<../../../Consumers 💼/💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>)
||`To`|domain| [Vault 🗄️](<../../🗄️🎭 Vault role.md>) | [`Consume@`](<../../../Consumers 💼/💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>)
||`Subject` | string | `Collect@Vault`
|Body|`Collect` | uuid | `Collect` | [`Consume@`](<../../../Consumers 💼/💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>)
|

<br/>


## Synchronous Response

```yaml
Schema: airlines.any-igo.dom/SSR/WCH:1    
Data: {...}
```

||Property|Type|Description
|-|-|-|-
|| `Schema`| string |  [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) of the data
|| `Data` | any | Data shared
|
 
## FAQ

1. **Why a synchronous request?**

    A synchronous request (instead of an async message) allows  [Consumer 💼 domains](<../../../Consumers 💼/💼🎭 Consumer role.md>) to download data sets from the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>) via HTTPS with no theoretical size limit.

    ---
    <br/>