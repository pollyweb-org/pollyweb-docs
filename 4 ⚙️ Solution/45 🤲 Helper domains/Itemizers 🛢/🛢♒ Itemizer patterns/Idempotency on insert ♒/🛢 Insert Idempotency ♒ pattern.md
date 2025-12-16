# 🛢 Insert Idempotency ♒ pattern

> Part of [Itemizer 🛢 helper domains](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)

The Insert Idempotency ♒ pattern ensures that repeated insert operations with the same data do not create duplicate records in the database. 
* This is particularly useful in scenarios where network issues or retries may lead to multiple identical insert requests.
* By implementing this pattern, the system can safely handle retries without the risk of data duplication, ensuring data integrity and consistency.
* Typically, this is achieved by using a unique identifier for each insert operation, allowing the system to recognize and ignore duplicate requests.

When an insert request is received, the system checks if a record with the same key already exists. 
* If it does exist with the same content, the system ignores the new request.
* If it does not exist, it proceeds with the insertion.
* If it exists but with different content, it returns `BLOCKED`.


## Diagram

![alt text](<🛢 Insert Idempotency ⚙️ uml.png>)