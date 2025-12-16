# 🛢 Insert Idempotency ♒ pattern

> Part of [Itemizer 🛢 helper domains](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)

The Insert Idempotency ♒ pattern ensures that repeated insert operations with the same data do not create duplicate records in the database. This is particularly useful in scenarios where network issues or retries may lead to multiple identical insert requests.

## Diagram

![alt text](<🛢 Insert Idempotency ⚙️ uml.png>)