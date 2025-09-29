<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ67394972376e4fb8979d41209 -->


# 💼🚀🗄️ Collect @ Vault


> Tells it to reply with the data [shared](<../30 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>) by the user.

> Used by [💼⏩🧑‍🦰 Query vault @ Consumer](<../../5 ⏩ Flows/20 💼⏩ Consumers/02 💼⏩🧑‍🦰 Query Vault.md>)

<br/>

## Sync Request 🚀

````yaml
Header:
    From: any-consumer.com
    To: any-vault.com
    Subject: Collect@Vault

Body:
    Collection: <collection-uuid> 
````

|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) name
|| `To`| string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) name
||`Subject` | string | `Collect@Vault`
|Body|`Collection` | uuid | Callback from [Consume@Consumer](<../30 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>)
|

<br/>
 
## FAQ

1. **Why a synchronous request?**

    A synchronous request (instead of an async message) allows  [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) to download data sets from the [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) via HTTPS with no theoretical size limit.

    ---
    <br/>