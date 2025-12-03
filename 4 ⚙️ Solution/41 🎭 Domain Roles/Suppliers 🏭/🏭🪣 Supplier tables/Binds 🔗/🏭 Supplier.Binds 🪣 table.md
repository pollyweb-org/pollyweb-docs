# 👥 Supplier.Binds 🪣 table

> About
* Part of the [`Supplier` 🏭 domain role](<../../🏭 Supplier/🏭🎭 Supplier role.md>)

<br/>

## Schema

```yaml
Prefix: Supplier
Table: Binds
Item: Bind
```

Extends the [`Vault.Binds` 🪣 table](<../../../Vaults 🗄️/🗄️🪣 Vault tables/Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>) from the [Vault 🗄️ domain](<../../../Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) role.

```yaml
Extends: Vault.Binds
```

The extended [Item 🛢 Children](<../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) are: [`Supplier.Domains`](<../Domains 👥/🏭 Supplier.Domains 🪣 table.md>)

```yaml
Children: Domains
```