# 😃🐌☁️ Forward @ Hoster

> Purpose
* A [Hoster ☁️ helper domain](<../../☁️ Hoster/☁️🤲 Hoster helper.md>) 
    * forwards [Async Messages 🐌](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Async Messages 🐌.md>)
    * from a [Talker 😃 helper domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)
    * to other [domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>).

<br/>

## Flow

![alt text](<☁️ Forward ⚙️ uml.png>)

## Async Message 🐌

```yaml
Header:
    From: any-talker.dom
    To: any-hoster.dom
    Subject: Forward@Hoster

Body:
    To: any-domain.dom
    Subject: Any@Role
    Body: {...}
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header    |`From`|text| [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)
|           |`To`|text| [Hoster ☁️](<../../☁️ Hoster/☁️🤲 Hoster helper.md>)
|           | `Subject`|text| `Forward@Hoster`
| Body      |`To`|text| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
|           | `Subject`|text| Method name
|           | `Body` | any | [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) body
|       