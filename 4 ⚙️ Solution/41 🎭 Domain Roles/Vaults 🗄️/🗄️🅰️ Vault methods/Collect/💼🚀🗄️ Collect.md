<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ67394972376e4fb8979d41209 -->


# 💼🚀🗄️ Collect @ Vault

> Part of the [`Consume flow`](<../../🗄️⏩ Vault flows/🗄️⏩💼 Consume 🔗 flow.md>)

> Purpose

* Tells it to reply with the data [shared](<../../../Consumers 💼/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>) by the user.

> Used by 
* [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉💼 Share Bind 🔗.md>)

> Preceded by [`Consume@Consumer`](<../../../Consumers 💼/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>)

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

|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | string | [Consumer 💼](<../../../Consumers 💼/💼🎭 Consumer role.md>) from [`Consume@Consumer`](<../../../Consumers 💼/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>)
|| `To`| string | [Vault 🗄️](<../../🗄️🎭 Vault role.md>) from [`Consume@Consumer`](<../../../Consumers 💼/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>)
||`Subject` | string | `Collect@Vault`
|Body|`Collect` | uuid | `Collect` from [`Consume@Consumer`](<../../../Consumers 💼/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>)
|

<br/>

 
## FAQ

1. **Why a synchronous request?**

    A synchronous request (instead of an async message) allows  [Consumer 💼 domains](<../../../Consumers 💼/💼🎭 Consumer role.md>) to download data sets from the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>) via HTTPS with no theoretical size limit.

    ---
    <br/>