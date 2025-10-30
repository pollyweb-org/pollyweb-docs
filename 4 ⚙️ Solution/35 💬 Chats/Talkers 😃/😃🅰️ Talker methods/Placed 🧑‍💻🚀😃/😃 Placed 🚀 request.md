# 🧑‍💻🚀😃 Placed @ Talker

> Implementation

* Implements [Hoster ☁️ helper domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>)
* Implemented by the [`Placed` 📃 handler](<😃 Placed 📃 handler.md>)

> Flow
* Part of [Handle @ Talker 😃⏩🧑‍💻](<../../😃⏩ Talker flows/Run Sync Functions 😃⏩📦/😃 Eval ⏩ flow.md>) flow
* Paired with [`Place@Talker`](<../Place 🧑‍💻🚀😃/😃 Place 🚀 request.md>) message

> Purpose

* Reads a [Holder 🧠](<../../../Scripts 📃/📃 basics/Holder 🧠.md>)
* The holder [`$.Chat`](<../../../Scripts 📃/📃 holders 🧠/$.Chat 💬/💬 $.Chat 🧠 holder.md>) contains [Chat 💬](<../../../Chats 💬/💬 Chat.md>) details.

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-hosted.dom
    To: any-hoster.dom
    Subject: Placed@Talker

Body:
    Chat: <chat-uuid>
    Holder: $p
```


|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) name
|           | `To`          | string    | [Hoster ☁️ domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) name
|           | `Subject`     | string    | `Placed@Talker`
| Body      | `Chat`      | uuid      | [Chat 💬](<../../../Chats 💬/💬 Chat.md>) ID
|           | `Holder` | string    | [Holder 🧠](<../../../Scripts 📃/📃 basics/Holder 🧠.md>) name
|

<br/>

## Synchronous Response

```yaml
Value: {...}
```