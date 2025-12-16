# 🛢 Optimistic concurrency ♒ pattern

The Optimistic concurrency pattern allows multiple [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) commands to run in parallel without locking resources, assuming that conflicts are rare. 
* On [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>), [Itemizers 🛢](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>) check if the key was modified by another [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>). 
* If a conflict is detected, an [`ERROR`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/ERROR 💥/💥 ERROR ⌘ cmd.md>) is returned.

## Diagram

![alt text](<🛢 Optimistic concurrency ⚙️ uml.png>)