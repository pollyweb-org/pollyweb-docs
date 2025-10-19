# 🪣 Vaults

> Stores [Vault 🗄️ domains](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) 

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

```yaml
# Vaults.yaml
Key: Vault
Children: 
    Binds: Binds|Vault
```

| Link | Table | Contains
|-|-|-
| Children | [`Binds` 🪣](<🤵🪣 Binds.md>) | [Binds 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
|


## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET 🗺️ item.md>) result.

```yaml
# GET|Vaults|any-vault.dom
Vault: any-vault.dom
Title: Any Vault
```