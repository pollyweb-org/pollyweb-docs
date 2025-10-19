# 🪣 Issuers

> Stores [Issuer 🎴 domains](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).


```yaml
# Issuers.yaml
Key: Issuer
Children: 
    Tokens: Tokens|Issuer
```

| Link | Table | Contains
|-|-|-
| Children | [`Tokens` 🪣](<🤵🪣 Tokens.md>) | [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
|


## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET 🗺️ item.md>) result.

```yaml
# GET|Issuers|any-issuer.dom
Issuer: any-issuer.dom
Title: Any Issuer
```