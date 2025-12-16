# 🛢 Optimistic concurrency ♒ pattern

> Part of [Itemizer 🛢 helper domains](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)


The Optimistic concurrency pattern allows multiple [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) commands to run in parallel without locking resources, assuming that conflicts are rare. 
* On [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>), [Itemizers 🛢](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>) check if the key was modified by another [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>). 
* If a conflict is detected, it returns `OUTDATED`.
* This pattern is useful in high-concurrency environments where locking would lead to performance bottlenecks.
* Clients must handle the `OUTDATED` response by retrying the operation, possibly after refreshing their data.


## Diagram

![alt text](<🛢 Optimistic concurrency ⚙️ uml.png>)