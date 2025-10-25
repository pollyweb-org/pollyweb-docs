# 🤵🪣 Chats

> Stores [Chats 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>)

> Inserted by [`Converse` 📃 script](<../🤵⏩ Broker flows/Converse 💬/.📎 Assets/Converse 📃 script.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Chats.yaml
Table: Chats
Key: Chat
Parents:
    Wallet: { Wallets.Wallet: Chats.Wallet }
    Host: { Domains.Domain: Chats.Host }
```

| Link | Table | Contains
|-|-|-
| Parents   | [`Wallets` 🪣](<🤵🪣 Wallets table.md>) | [Wallets 🧑‍🦰](<../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
|           | [`Domains` 🪣](<🤵🪣 Domains table.md>) | [domains 👥](<../../../40 👥 Domains/👥 Domain.md>)
|

<br/>

## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) result.

```yaml
# GET|Chats|<chat-id>

Chat: <chat-uuid>
Wallet: <wallet-uuid>

# Host info
Host: any-host.dom
Host$: Any Host

# Locator info
Key: ANY-LOCATOR
Parameters: {A:1, B:2}

# For Wallets to sign messages
PrivateKey: <PrivateKey>

# For domains to verify Wallet messages
PublicKey: <PublicKey>
```