# 🧑‍💻🚀☁️ Placed @ Hoster

> Implements [Hoster ☁️ helper domain](<../../4 ⚙️ Solution/45 🤲 Helper domains/55 ☁️ Hosters/☁️🤲 Hoster helper.md>)

> Part of [Handle @ Talker 😃⏩🧑‍💻](<../../4 ⚙️ Solution/35 Chats/😃 Talkers/😃⏩ Talker flows/20 😃⏩🧑‍💻 Handle 🐍.md>) flow

> Paired with [`Place@Talker`](<20 🧑‍💻🐌😃 Place.md>) message

* Reads a [$Placeholder 💾](<../../4 ⚙️ Solution/35 Chats/😃 Talkers/😃💾 Talker data/10 💾 $Placeholder.md>)
* The placeholder [`$.Chat`](<../../4 ⚙️ Solution/35 Chats/😃 Talkers/😃💾 Talker data/11 💬 $.Chat holder.md>) contains [Chat 💬](<../../4 ⚙️ Solution/35 Chats/💬 Chats/💬 Chat.md>) details.

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-host.com
    To: any-hoster.com
    Subject: Placed@Talker

Body:
    ChatID: <chat-uuid>
    Placeholder: $p
```


|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) name
|           | `To`          | string    | [Hoster ☁️ domain](<../../4 ⚙️ Solution/45 🤲 Helper domains/55 ☁️ Hosters/☁️🤲 Hoster helper.md>) name
|           | `Subject`     | string    | `Placed@Talker`
| Body      | `ChatID`      | uuid      | [Chat 💬](<../../4 ⚙️ Solution/35 Chats/💬 Chats/💬 Chat.md>) ID
|           | `Placeholder` | string    | [$Placeholder 💾](<../../4 ⚙️ Solution/35 Chats/😃 Talkers/😃💾 Talker data/10 💾 $Placeholder.md>) name
|

<br/>

## Synchronous Response

```yaml
{A:1, B:2}
```