# 🪣 Hosts

> Stores [Host 🤗 domains](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

```yaml
# Hosts.yaml
Key: Host
Children:
    Chats: Chats|Host
```


| Link | Table | Contains
|-|-|-
| Children | [`Chats` 🪣](<🤵🪣 Chats.md>)
|

## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET 🗺️ item.md>) result.

```yaml
# GET|Hosts|any-host.dom
Host: any-host.dom
Title: Any Host
```