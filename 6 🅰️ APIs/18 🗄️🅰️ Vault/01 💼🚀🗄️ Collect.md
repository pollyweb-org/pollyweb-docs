<!-- #TODO -->

<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ67394972376e4fb8979d41209 -->


# 💼🚀🗄️ Collect @ [Vault](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)






## Request 🚀

|Property|Type|Description
|-|-|-
|`From` | string | [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>)
| `To`| string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)
|`Subject` | string | `Collect@Vault`
|`Collection` | UUID | ID from [Consume@Consumer](<../05 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>)

````yaml
Header:
    From: any-consumer.com
    Subject: Collect@Vault
Body:
    Collection: <collection-uuid> 
````

## Behavior

- Synchronous request sent from a [Consumer 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) to a [Vault 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)
- Tells it to reply with the data [shared](<../05 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>) by the user.
- Allows HTTP responses with no theoretical size limit.
- Callers expect the response to be cached during [Consume 🐌 ](<../05 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>)
- The message is rejected if the TTL is exceeded.
  
