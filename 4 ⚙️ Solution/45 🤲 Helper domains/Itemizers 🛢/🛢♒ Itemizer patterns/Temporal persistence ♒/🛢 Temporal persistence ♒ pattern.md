# 🛢 Temporal persistence ♒ pattern

> Part of [Itemizer 🛢 helper domains](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)

The Temporal persistence ♒ pattern ensures that data stored in an Itemizer 🛢 remains valid only for a specified time period. 
* When data is inserted or updated, a timer is set for the specified duration.
* After this period, the data is automatically deleted, helping to manage storage and maintain data relevance.
* This pattern is particularly useful for caching scenarios, temporary data storage, or any situation where data should not persist indefinitely.


## Diagram

![alt text](<🛢 Temporal persistence ⚙️ uml.png>)