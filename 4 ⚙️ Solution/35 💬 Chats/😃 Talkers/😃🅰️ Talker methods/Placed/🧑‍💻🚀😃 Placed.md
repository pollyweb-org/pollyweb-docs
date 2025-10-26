# 🧑‍💻🚀😃 Placed @ Talker

> About

* Implements [Hoster ☁️ helper domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>)
* Implemented by the [`Placed` 📃 handler](<.📎 Assets/Placed 📃 handler.md>)
* Part of [Handle @ Talker 😃⏩🧑‍💻](<../../😃⏩ Talker flows/Eval Functions 😃⏩📦/😃 Eval ⏩ flow.md>) flow
* Paired with [`Place@Talker`](<../Place/🧑‍💻🚀😃 Place.md>) message

> Purpose

* Reads a [Placeholder 🧠](<../../😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>)
* The placeholder [`$.Chat`](<../../😃⚙️ Talker cmds/...placeholders 🧠/$.Chat 💬.md>) contains [Chat 💬](<../../../💬 Chats/💬 Chat.md>) details.

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-hosted.dom
    To: any-hoster.dom
    Subject: Placed@Talker

Body:
    Chat: <chat-uuid>
    Placeholder: $p
```


|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) name
|           | `To`          | string    | [Hoster ☁️ domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) name
|           | `Subject`     | string    | `Placed@Talker`
| Body      | `Chat`      | uuid      | [Chat 💬](<../../../💬 Chats/💬 Chat.md>) ID
|           | `Placeholder` | string    | [Placeholder 🧠](<../../😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) name
|

<br/>

## Synchronous Response

```yaml
{A:1, B:2}
```