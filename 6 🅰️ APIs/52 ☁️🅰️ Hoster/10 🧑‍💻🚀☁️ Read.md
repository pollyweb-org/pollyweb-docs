# 🧑‍💻🚀☁️ Read @ Hoster

> Paired with [Write@Hoster](<20 🧑‍💻🐌☁️ Write.md>)

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-host.com
    To: any-hoster.com
    Subject: Read@Hoster

Body:
    ChatID: <chat-uuid>
    Placeholder: $p
```


|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) name
|           | `To`          | string    | [Talker 😃 domain](<../../9 😃 Talkers/10 📘 Talker specs/02 😃🛠️ Talker helper.md>) name
|           | `Subject`     | string    | `Read@Talker`
| Body      | `ChatID`      | uuid      | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID
|           | `Placeholder` | string    | [$Placeholder 💾](<../../9 😃 Talkers/30 🗃️ Talker data/10 💾 $Placeholder.md>) name
|

<br/>

## Synchronous Response

```yaml
{A:1, B:2}
```