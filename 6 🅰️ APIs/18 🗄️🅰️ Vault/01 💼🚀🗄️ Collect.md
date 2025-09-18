<!-- #TODO -->

<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ67394972376e4fb8979d41209 -->


# 💼🚀🗄️ Collect @ Vault


> Tells it to reply with the data [shared](<../05 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>) by the user.



## Sync Request 🚀

|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) name
|| `To`| string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) name
||`Subject` | string | `Collect@Vault`
|Body|`Collection` | UUID | Callback from [Consume@Consumer](<../05 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>)

````yaml
Header:
    From: any-consumer.com
    To: any-vault.com
    Subject: Collect@Vault
    
Body:
    Collection: <collection-uuid> 
````
<br/>
 
## Design decisions

| Type | Decision
|-|-
| `Size`| A synchronous request (instead of an async message) allows Consumers to download data sets from the Vault via HTTPS with no theoretical size limit.
| `Cache` | Consumers expect the response to be cached during [Consume@Consumer](<../05 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>), to allow Vaults to take as much time as necessary to gather the data, while avoiding timeouts when the Consumer calls [Collect@Vault](<01 💼🚀🗄️ Collect.md>).
| `Timeout` | The request is rejected if the TTL of the Vault's cache is exceeded.

