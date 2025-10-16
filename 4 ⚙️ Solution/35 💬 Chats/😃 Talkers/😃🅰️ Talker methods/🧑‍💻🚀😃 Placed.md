# 🧑‍💻🚀☁️ Placed @ Hoster

> Implements [Hoster ☁️ helper domain](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>)

> Part of [Handle @ Talker 😃⏩🧑‍💻](<../😃⏩ Talker flows/😃⏩🧑‍💻 Handle 🐍.md>) flow

> Paired with [`Place@Talker`](<🧑‍💻🐌😃 Place.md>) message

* Reads a [$Placeholder 💾](<../😃💾 Talker data/10 💾 $Placeholder.md>)
* The placeholder [`$.Chat`](<../😃💾 Talker data/11 💬 $.Chat holder.md>) contains [Chat 💬](<../../💬 Chats/💬 Chat.md>) details.

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-host.dom
    To: any-hoster.dom
    Subject: Placed@Talker

Body:
    ChatID: <chat-uuid>
    Placeholder: $p
```


|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) name
|           | `To`          | string    | [Hoster ☁️ domain](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) name
|           | `Subject`     | string    | `Placed@Talker`
| Body      | `ChatID`      | uuid      | [Chat 💬](<../../💬 Chats/💬 Chat.md>) ID
|           | `Placeholder` | string    | [$Placeholder 💾](<../😃💾 Talker data/10 💾 $Placeholder.md>) name
|

<br/>

## Synchronous Response

```yaml
{A:1, B:2}
```