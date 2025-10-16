# 🔃 Syncer tool

> Relates to [Resourcer 🗃️ domain role](<../../41 🎭 Domain Roles/Resourcers 🗃️/🗃️🎭 Resourcer role.md>).

<br/>


1. **What is a Syncer tool?**

    A [Syncer 🔃 tool](<🔃🛠️ Syncer tool.md>)
    * is a command-line tool
    * to sync local files 
    * with a [Resourcer 🗃️ domain](<../../41 🎭 Domain Roles/Resourcers 🗃️/🗃️🎭 Resourcer role.md>).

    ---
    <br/>

1. **What commands are supported on the terminal?**

    |Command 🧑‍💻| Description
    |-|-
    |[⏩ `clone`](<🔃⏩ Syncer flows/10 🔃⏩🗃️ Clone.md>) | Registers [Syncer 🔃 tools](<🔃🛠️ Syncer tool.md>) on [Resourcers 🗃️](<../../41 🎭 Domain Roles/Resourcers 🗃️/🗃️🎭 Resourcer role.md>)
    |[⏩ `sync`](<🔃⏩ Syncer flows/20 🔃⏩🗃️ Sync.md>) | Syncs local files with [Resourcer 🗃️ domains](<../../41 🎭 Domain Roles/Resourcers 🗃️/🗃️🎭 Resourcer role.md>) 
    |[⏩ `chat`](<../../41 🎭 Domain Roles/Resourcers 🗃️/🗃️🅰️ Resourcer methods/🔃🐌🗃️ Chat.md>)| Opens [Chats 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) with [Resourcer 🗃️ domains](<../../41 🎭 Domain Roles/Resourcers 🗃️/🗃️🎭 Resourcer role.md>)
    <!--|`test <env>`| Runs test scripts on an environment<br/>- e.g., `my-hoster test local`-->

    ---
    <br/>


1. **Is it encrypted?**

    Yes. All communication is done over HTTPS.

    ---
    <br/>

1. **Is it authenticated?**

    Yes. 
    * First, users use their [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) to approve the [Clone ⏩](<🔃⏩ Syncer flows/10 🔃⏩🗃️ Clone.md>) with one-time passwords, registering the [Syncer's 🔃](<🔃🛠️ Syncer tool.md>) public key on the [Resourcer 🗃️ domain](<../../41 🎭 Domain Roles/Resourcers 🗃️/🗃️🎭 Resourcer role.md>).

    * Follow-up requests are then signed with the [Syncer's 🔃](<🔃🛠️ Syncer tool.md>) private key.

    ---
    <br/>

1. **How are changes identified?**

    Using SHA-256 hashing.

    ---
    <br/>


