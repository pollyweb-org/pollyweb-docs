<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ67394972376e4fb8979d41209 -->


# 💼🚀🗄️ Collect @ Vault


> Tells it to reply with the data [shared](<../../Consumers 💼/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>) by the user.

> Used by [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Prompts 🤔/👉💼 Share Bind 🔗.md>)

<br/>

## Sync Request 🚀

````yaml
Header:
    From: any-consumer.dom
    To: any-vault.dom
    Subject: Collect@Vault

Body:
    VaultKey: <callback-uuid> 
````

|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Consumer 💼 domain](<../../Consumers 💼/💼🎭 Consumer role.md>) name
|| `To`| string | [Vault 🗄️ domain](<../🗄️🎭 Vault role.md>) name
||`Subject` | string | `Collect@Vault`
|Body|`VaultKey` | uuid | Callback from [Consume@Consumer](<../../Consumers 💼/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>)
|

<br/>
 
## FAQ

1. **Why a synchronous request?**

    A synchronous request (instead of an async message) allows  [Consumer 💼 domains](<../../Consumers 💼/💼🎭 Consumer role.md>) to download data sets from the [Vault 🗄️ domain](<../🗄️🎭 Vault role.md>) via HTTPS with no theoretical size limit.

    ---
    <br/>