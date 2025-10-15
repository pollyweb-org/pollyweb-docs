# 👥🐌🏭 Order @ Supplier

<!-- #TODO -->

<!-- Docs: -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/482a44e4f22df82cf524f20278d6e1883146de79/python/suppliers/supplier/SUPPLIER.py#L39 --> 
<!-- Test: -->


## Async Message 🐌

```yaml
Header:
    From: any-domain.com
    To: any-supplier.com
    Subject: Order@Supplier
Body:
    OrderID: <order-uuid>
    ItemCode: nlweb.org/PRINTER/ORDER/ITEM
    Items: 
      - {item-1}
      - {item-2}
```

|Object|Property|Type|Description
|-|-|-|-
|Header |`From`     | string | Caller [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) name
|       |`To`       | string | [Supplier 🏭 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>)
|       |`Subject`  | string | `Order @ Supplier`
|Body   |`OrderID`  | uuid   | ID of the order on the  Caller [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>)
|       | `ItemCode`| string | [Schema Code 🧩](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) of the items
||

