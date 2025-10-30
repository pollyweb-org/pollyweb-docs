# 😃🐌☁️ Forward @ Hoster

> Purpose
* A [Hoster ☁️ helper domain](<../../☁️🤲 Hoster helper.md>) 
    * forwards [Async Messages 🐌](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Async Messages 🐌.md>)
    * from a [Talker 😃 helper domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)
    * to other [domains 👥](<../../../../40 👥 Domains/👥 Domain.md>).

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
    To: any-domain.com
    Subject: Any@Role
    Body: {...}
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header    | `From`| string    | [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)
|           | `To`  | string    | [Hoster ☁️](<../../☁️🤲 Hoster helper.md>)
|           | `Subject`| string | `Forward@Hoster`
| Body      | `To`  | string | [domain 👥](<../../../../40 👥 Domains/👥 Domain.md>) name
|           | `Subject`| string | Method name
|           | `Body` | any | [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) body
|       