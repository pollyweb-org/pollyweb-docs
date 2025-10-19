# 🪣 Wallets

> Stores [Wallet 🧑‍🦰 apps](<../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

```yaml
# Wallets.yaml
Key: Wallet

Parent:
    Notifier: Notifiers|Notifier

Children:
    Chats: Chats|Wallet
    Binds: Binds|Wallet
    Tokens: Tokens|Wallet
```

| Link | Table | Contains
|-|-|-
| Parent | [`Notifiers` 🪣](<🤵🪣 Notifiers.md>) | [Notifier 📣 domain](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣👥 Notifier domain.md>)
| Children | [`Chats` 🪣](<🤵🪣 Chats.md>) | [Chats 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>)
| | [`Binds` 🪣](<🤵🪣 Binds.md>) | [Binds 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| | [`Tokens` 🪣](<🤵🪣 Tokens.md>) | [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
|

## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) result.

```yaml
# GET|Wallets|<wallet-uuid>
Wallet: <wallet-uuid>
PublicKey: <public-key>
Notifier: any-notifier.dom
```