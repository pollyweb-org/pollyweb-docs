# 🧑‍💻🚀😃 Placed @ Talker

> Implementation

* Implements [Hoster ☁️ helper domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️ Hoster/☁️🤲 Hoster helper.md>)
* Implemented by the [`Placed` 📃 handler](<😃 Placed 📃 handler.md>)

> Flow
* Part of [Handle @ Talker 😃⏩🧑‍💻](<../../😃⏩ Talker flows/Run Sync Functions 😃⏩📦/😃 Call ⏩ flow.md>) flow
* Paired with [`Place@Talker`](<../Place 🧑‍💻🚀😃/😃 Place 🚀 call.md>) message

> Purpose

* Reads a [Holder 🧠](<../../../Scripts 📃/Holder 🧠.md>)
* The holder [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Chat 💬/💬 $.Chat 🧠 holder.md>) contains [Chat 💬](<../../../Chats 💬/💬 Chat.md>) details.

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-hosted.dom
    To: any-hoster.dom
    Subject: Placed@Talker

Body:
    Hook: <hook-uuid>
    Holder: $p
```


|Object|Property|Type|Description
|-|-|-|-
| Header    |`From`|text| [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name
|           |`To`|text| [Hoster ☁️ domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️ Hoster/☁️🤲 Hoster helper.md>) name
|           | `Subject`     | string    | `Placed@Talker`
| Body      | `Hook`      | uuid      | Hook from [`Handle@Hosted`](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Handle 😃🐌📦/📦 Handle 🐌 msg.md>)
|           | `Holder` | string    | [Holder 🧠](<../../../Scripts 📃/Holder 🧠.md>) name
|

<br/>

## Synchronous Response

```yaml
Value: {...}
```