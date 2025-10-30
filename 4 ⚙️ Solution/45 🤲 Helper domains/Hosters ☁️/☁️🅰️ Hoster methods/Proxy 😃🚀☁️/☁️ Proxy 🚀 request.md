# 😃🚀☁️ Proxy @ Hoster

<!-- TODO -->

> Purpose
* A [Hoster ☁️ helper domain](<../../☁️🤲 Hoster helper.md>) 
    * proxies a synchronous [Request 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
    * from a [Talker 😃 helper domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>).


## Flow

![alt text](<☁️ Proxy ⚙️ uml.png>)

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-talker.dom
    To: any-hoster.dom
    Subject: Proxy@Hoster

Body:
    To: any-domain.com
    Subject: Any@Role
    Body: {...}
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header    | `From`| string    | [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)
|           | `To`  | string    | [Hoster ☁️](<../../☁️🤲 Hoster helper.md>)
|           | `Subject`| string | `Proxy@Hoster`
| Body      | `To`  | string | [domain 👥](<../../../../40 👥 Domains/👥 Domain.md>) name
|           | `Subject`| string | Method name
|           | `Body` | any | [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) body
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