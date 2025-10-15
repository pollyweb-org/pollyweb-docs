# 🗃️🎭 Resourcer domain role

1. **What is a Resourcer role?**

    A [domain 👥](<../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) with a [Resourcer 🗃️ role](<🗃️🎭 Resourcer role.md>)
    * is any [domain 👥](<../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) that stores files
    * and syncs them locally via a [Syncer 🔃 tool](<../../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>).

    ---
    <br/>

1. **Why are Resources important?**

    [Resourcers 🗃️](<🗃️🎭 Resourcer role.md>) 
    * allow users to edit configuration files on their workstations 
    * using any offline editor of their choice.

    ---
    <br/>
    
1. **What API messages do Resources expose?**

    | Flow | Message | Details
    |-|-|-
    |[⏩ Clone](<../../../5 ⏩ Flows/77 🔃⏩ Syncer/10 🔃⏩🗃️ Clone.md>)|[`Clone`](<🗃️🅰️ Resourcer methods/🔃🚀🗃️ Clone.md>) | Registers [Syncers 🔃 ](<../../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>) on [Resourcers 🗃️](<🗃️🎭 Resourcer role.md>)
    |[⏩ Sync](<../../../5 ⏩ Flows/77 🔃⏩ Syncer/20 🔃⏩🗃️ Sync.md>)|[`Map`](<🗃️🅰️ Resourcer methods/🔃🚀🗃️ Map.md>) | [Syncers](<../../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>) send a map current files
    ||[`Upload`](<🗃️🅰️ Resourcer methods/🔃🚀🗃️ Upload.md>) | Then upload each file individually
    ||[`Uploaded`](<🗃️🅰️ Resourcer methods/🔃🚀🗃️ Uploaded.md>) | [Resourcers 🗃️](<🗃️🎭 Resourcer role.md>) calculate changes
    ||[`Download`](<🗃️🅰️ Resourcer methods/🔃🚀🗃️ Download.md>) | [Syncers](<../../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>) execute the changes
    |[⏩ Chat](<🗃️🅰️ Resourcer methods/🔃🐌🗃️ Chat.md>)|[`Chat`](<🗃️🅰️ Resourcer methods/🔃🐌🗃️ Chat.md>) | Opens a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) with a [Resourcer 🗃️](<🗃️🎭 Resourcer role.md>)
    

    ---
    <br/>