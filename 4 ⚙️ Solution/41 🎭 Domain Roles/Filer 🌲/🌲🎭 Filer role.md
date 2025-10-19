# 🌲🎭 Filer domain role

1. **What is a Filer role?**

    A [domain 👥](<../../40 👥 Domains/👥 Domain.md>) with a [Filer 🌲 role](<🌲🎭 Filer role.md>)
    * is any [domain 👥](<../../40 👥 Domains/👥 Domain.md>) that stores files
    * and syncs them locally via a [Syncer 🔃 tool](<../../55 👷 Build domains/Syncers 🔃/🔃🛠️ Syncer tool.md>).

    ---
    <br/>

1. **Why are Filers important?**

    [Filer 🌲](<🌲🎭 Filer role.md>) 
    * allow users to edit configuration files on their workstations 
    * using any offline editor of their choice.

    ---
    <br/>
    
1. **What API messages do Filers expose?**

    | Flow | Message | Details
    |-|-|-
    |[⏩ Clone](<../../55 👷 Build domains/Syncers 🔃/🔃⏩ Syncer flows/10 🔃⏩🌲 Clone.md>)|[`Clone`](<🌲🅰️ Filer methods/🔃🚀🌲 Clone.md>) | Registers [Syncers 🔃 ](<../../55 👷 Build domains/Syncers 🔃/🔃🛠️ Syncer tool.md>) on [Filer 🌲](<🌲🎭 Filer role.md>)
    |[⏩ Sync](<../../55 👷 Build domains/Syncers 🔃/🔃⏩ Syncer flows/20 🔃⏩🌲 Sync.md>)|[`Map`](<🌲🅰️ Filer methods/🔃🚀🌲 Map.md>) | [Syncers](<../../55 👷 Build domains/Syncers 🔃/🔃🛠️ Syncer tool.md>) send a map current files
    ||[`Upload`](<🌲🅰️ Filer methods/🔃🚀🌲 Upload.md>) | Then upload each file individually
    ||[`Uploaded`](<🌲🅰️ Filer methods/🔃🚀🌲 Uploaded.md>) | [Filer 🌲](<🌲🎭 Filer role.md>) calculate changes
    ||[`Download`](<🌲🅰️ Filer methods/🔃🚀🌲 Download.md>) | [Syncers](<../../55 👷 Build domains/Syncers 🔃/🔃🛠️ Syncer tool.md>) execute the changes
    |[⏩ Chat](<🌲🅰️ Filer methods/🔃🐌🌲 Chat.md>)|[`Chat`](<🌲🅰️ Filer methods/🔃🐌🌲 Chat.md>) | Opens a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) with a [Filer 🌲](<🌲🎭 Filer role.md>)
    

    ---
    <br/>