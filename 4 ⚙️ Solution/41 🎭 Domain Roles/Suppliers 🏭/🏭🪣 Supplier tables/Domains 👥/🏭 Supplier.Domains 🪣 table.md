# 👥 Supplier.Domains 🪣 table

> About
* Part of the [`Supplier` 🏭 domain role](<../../🏭 Supplier/🏭🎭 Supplier role.md>)

<br/>

## Schema

```yaml
Prefix: Supplier
Table: Domains
Item: Domain
```

<br/>

The [Item 🛢 Parents](<../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are `Supplier.Binds`

```yaml
Parents: Binds
```

<br/>

Here's the [Item 🛢 Assert](<../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:
    AllOf: Bind, Domain

    # Token assertions
    Token.Schema: .DOMAIN   # Admin
    Token.Issuer: Domain        # Matching domain
    Token.Starts.IsPast:        # Activate
    Token.Expires.IsFuture:     # Not expired
```

<br/>

## Example

```yaml
Bind: <bind-uuid>       # Wallet bound
Domain: any-domain.dom  # Domain to administer
```

[Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) of [`DOMAIN` 🧩 schema](<../../../../40 👥 Domains/👥🧩 Domain schemas/🧩 DOMAIN.md>).

```yaml
Token: 
    Schema: .DOMAIN
    Starts: 2024-01-01T00:00:00Z
    Expires: 2025-01-01T00:00:00Z
    Issuer: any-domain.dom
    #...
```