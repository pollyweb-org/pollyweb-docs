# 😃🚀☁️ Proxy @ Hoster

> Purpose
* A [Hoster ☁️ helper domain](<../../☁️ Hoster helper/☁️🤲 Hoster helper.md>) 
    * proxies [Sync Calls 🚀](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Sync Calls 🚀.md>)
    * from a [Talker 😃 helper domain](<../../../../35 💬 Chats/Talkers 😃/😃 Talker/😃🤲 Talker helper.md>)
    * to other [domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>).


## Flow

![alt text](<☁️ Proxy ⚙️ uml.png>)

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-talker.dom
    To: any-hoster.dom
    Subject: Proxy@Hoster

Body:
    To: any-domain.dom
    Subject: Any@Role
    Body: {...}
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header    |`From`|text| [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃 Talker/😃🤲 Talker helper.md>)
|           |`To`|text| [Hoster ☁️](<../../☁️ Hoster helper/☁️🤲 Hoster helper.md>)
|           | `Subject`|text| `Proxy@Hoster`
| Body      |`To`|text| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
|           | `Subject`|text| Method name
|           | `Body` | any | [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) body
|       

<br/>

## Synchronous Response

```yaml
Status: 200
Body: {...}
```

||Property|Type|Description|Origin
|-|-|-|-|-
|| `Status`| integer  | HTTP status code
|| `Body` | any | HTTP response
|