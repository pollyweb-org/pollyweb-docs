# 🛢 Update Idempotency ♒ pattern

> Part of [Itemizer 🛢 helper domains](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)


The Update Idempotency ♒ pattern ensures that repeated [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) operations with the same data do not trigger more than one event.
* This is particularly useful in scenarios where network issues or retries may lead to multiple identical [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) requests.

## Diagram

![alt text](<🛢 Update Idempotency ⚙️ uml.png>)