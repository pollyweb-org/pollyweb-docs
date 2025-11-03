# 🛢 Itemizer helper


## FAQ

1. **What's an Itemizer?**

    An [Itemizer 🛢 helper domain](<🛢🤲 Itemizer helper.md>)
    * is a [Helper 🤲 domain](<../$ Helpers 🤲/🤲👥 Helper domain.md>)
    * that manages [Itemized 🪣 datasets](<../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * on behalf of other [domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>).

    ---
    <br/>

1. **What are the inbound messages supported?**

    |Scope|[Message 📨](<../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | Purpose
    |-|-|-
    |Item   | [🚀 `Delete`](<🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)| Delete an item
    |       | [🚀 `Get`](<🛢🅰️ Itemizer methods/Item Get 👥🚀🛢/🛢 Get 🚀 request.md>) | Get an item
    |       | [🚀 `Save`](<🛢🅰️ Itemizer methods/Item Save 👥🚀🛢/🛢 Save 🚀 request.md>) | Save an item
    |       | [🚀 `Undo`](<🛢🅰️ Itemizer methods/Item Undo 👥🚀🛢/🛢 Undo 🚀 request.md>) | Undo a delete
    |Table  | [🐌 `Build`](<🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>) | Build a table
    |       | [🐌 `Burn`](<🛢🅰️ Itemizer methods/Table Burn 👥🐌🛢/🛢 Burn 🐌 msg.md>) | Destroy a table
    |       | [🚀 `List`](<🛢🅰️ Itemizer methods/Table List 👥🚀🛢/🛢 List 🚀 Request.md>) | List all tables

1. **What are the triggers supported?**
   
    |[Message 📨](<../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | Purpose
    |-|-
    | [🔔 `Triggered`](<🛢🔔 Itemizer events/🛢🔔 Triggered.md>) | Informs on item changes

    ---
    <br/>

1. **How are they mapped to script commands?**

    [Command ⌘](<../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | Purpose
    |-|-
    |[🧲 `GET`](<../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) | Calls [`Get@Itemizer` 🅰️ ](<🛢🅰️ Itemizer methods/Item Get 👥🚀🛢/🛢 Get 🚀 request.md>)
    |[💾 `SAVE`](<../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Calls [`Save@Itemizer` 🅰️ ](<🛢🅰️ Itemizer methods/Item Save 👥🚀🛢/🛢 Save 🚀 request.md>)
    |[🗑️ `DELETE`](<../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) | Calls [`Delete@Itemizer` 🅰️ ](<🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)
    |[↩️ `UNDO`](<../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) | Calls [`Undo@Itemizer` 🅰️ ](<🛢🅰️ Itemizer methods/Item Undo 👥🚀🛢/🛢 Undo 🚀 request.md>)

    ---
    <br/>