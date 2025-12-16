# 🛢 Itemizer helper


## FAQ

1. **What's an Itemizer?**

    An [Itemizer 🛢 helper domain](<🛢🤲 Itemizer helper.md>)
    * is a [Helper 🤲 domain](<../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>)
    * that manages [Itemized 🪣 datasets](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * on behalf of other [domains 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>).

    ---
    <br/>

1. **What are the inbound messages supported?**

    |Scope|[Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | Purpose
    |-|-|-
    |Item   | [🚀 `Delete`](<../🛢📨 Itemizer msgs/Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>)| Delete an item
    |       | [🚀 `Get`](<../🛢📨 Itemizer msgs/Item Read 👥🚀🛢/🛢 Read 🚀 call.md>) | Get an item
    |       | [🚀 `Save`](<../🛢📨 Itemizer msgs/Item Save 👥🚀🛢/🛢 Save 🚀 call.md>) | Save an item
    |Table  | [🐌 `Build`](<../🛢📨 Itemizer msgs/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>) | Build a table
    |       | [🐌 `Burn`](<../🛢📨 Itemizer msgs/Table Burn 👥🐌🛢/🛢 Burn 🐌 msg.md>) | Destroy a table
    |       | [🚀 `List`](<../🛢📨 Itemizer msgs/Table List 👥🚀🛢/🛢 List 🚀 call.md>) | List all tables

1. **What are the triggers supported?**
   
    |[Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | Purpose
    |-|-
    | [🔔 `Triggered`](<../../Alarms ⏰/⏰🔔 Alarm events/⏰🔔 Triggered.md>) | Informs on item changes

    ---
    <br/>

1. **How are they mapped to script commands?**

    [Command ⌘](<../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    |[🧲 `READ`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | Calls [`Read@Itemizer` 🅰️ ](<../🛢📨 Itemizer msgs/Item Read 👥🚀🛢/🛢 Read 🚀 call.md>)
    |[💾 `SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Calls [`Save@Itemizer` 🅰️ ](<../🛢📨 Itemizer msgs/Item Save 👥🚀🛢/🛢 Save 🚀 call.md>)
    |[🗑️ `DELETE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) | Calls [`Delete@Itemizer` 🅰️ ](<../🛢📨 Itemizer msgs/Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>)

    ---
    <br/>