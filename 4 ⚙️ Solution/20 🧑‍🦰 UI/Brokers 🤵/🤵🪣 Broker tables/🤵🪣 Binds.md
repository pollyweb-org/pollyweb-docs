# 🪣 Binds

> Stores [Binds 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).


```yaml
# Binds.yaml
Key: Bind
Parents:
    Wallet: Wallets|Wallet
```


| Link | Table | Contains
|-|-|-
| Parent    | [`Wallets` 🪣](<🤵🪣 Wallets.md>) | [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
|


## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET 🗺️ item.md>) result.

```yaml
# GET|Binds@Broker|<bind-id>
Bind: <bind-id>
Vault: any-vault.dom
Wallet: <wallet-uuid>
Schema: any-authority.dom/ANY-CODE
```