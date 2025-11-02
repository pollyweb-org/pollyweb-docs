# 👥🐌🏭 Order @ Supplier

<!-- #TODO -->

<!-- Docs: -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/482a44e4f22df82cf524f20278d6e1883146de79/python/suppliers/supplier/SUPPLIER.py#L39 --> 
<!-- Test: -->


## Async Message 🐌

```yaml
Header:
    From: any-domain.dom
    To: any-supplier.dom
    Subject: Order@Supplier
Body:
    OrderID: <order-uuid>
    ItemCode: nlweb.dom/PRINTER/ORDER/ITEM
    Items: 
      - {item-1}
      - {item-2}
```

|Object|Property|Type|Description
|-|-|-|-
|Header |`From`|domain| Caller [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
|       |`To`|domain| [Supplier 🏭 domain](<../🏭🎭 Supplier role.md>)
|       |`Subject`  | string | `Order @ Supplier`
|Body   |`OrderID`  | uuid   | ID of the order on the  Caller [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|       | `ItemCode`| string | [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) of the items
||

