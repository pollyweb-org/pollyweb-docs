# 🪣 Chats

> Stores [Chats 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>)

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

```yaml
# Chats.yaml
Key: Chat
Parents:
    Wallet: Wallets|Wallet
```

| Link | Table | Contains
|-|-|-
| Parents   | [`Wallets` 🪣](<🤵🪣 Wallets.md>) | [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
|

## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET 🗺️ item.md>) result.

```yaml
# GET|Chats|<chat-id>
Chat: <chat-id>
Wallet: <wallet-uuid>
Host: any-host.dom
Title: Any Host
```